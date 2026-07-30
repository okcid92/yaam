#!/usr/bin/env python3
"""Yaam MCP Server — Vibe Coding context management framework."""

from __future__ import annotations

import argparse
import logging
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolResult,
    ListToolsResult,
    TextContent,
    Tool,
)

log: logging.Logger

TOOLS: list[Tool] = [
    Tool(
        name="check_yaam_status",
        description="Check if Yaam framework is initialized in the project",
        input_schema={
            "type": "object",
            "properties": {
                "project_path": {"type": "string", "description": "Path to the project root"},
            },
            "required": ["project_path"],
        },
    ),
    Tool(
        name="setup_yaam_framework",
        description="Generate the full Yaam directory tree in the project",
        input_schema={
            "type": "object",
            "properties": {
                "project_path": {"type": "string", "description": "Path to the project root"},
                "project_name": {"type": "string", "description": "Name of the project"},
                "stack": {"type": "string", "description": "Tech stack (generic, nextjs, laravel, etc.)"},
                "dry_run": {"type": "boolean", "description": "Preview without writing files"},
            },
            "required": ["project_path", "project_name"],
        },
    ),
    Tool(
        name="get_project_status",
        description="Read the project's progress-tracer.md roadmap",
        input_schema={
            "type": "object",
            "properties": {
                "project_path": {"type": "string", "description": "Path to the project root"},
            },
            "required": ["project_path"],
        },
    ),
    Tool(
        name="add_tracer_task",
        description="Add an unchecked task to progress-tracer.md",
        input_schema={
            "type": "object",
            "properties": {
                "project_path": {"type": "string", "description": "Path to the project root"},
                "task": {"type": "string", "description": "Task description"},
            },
            "required": ["project_path", "task"],
        },
    ),
    Tool(
        name="complete_tracer_task",
        description="Mark a task as completed in progress-tracer.md",
        input_schema={
            "type": "object",
            "properties": {
                "project_path": {"type": "string", "description": "Path to the project root"},
                "task": {"type": "string", "description": "Exact task description to check off"},
            },
            "required": ["project_path", "task"],
        },
    ),
    Tool(
        name="log_progress_note",
        description="Add a timestamped journal entry to progress-tracer.md",
        input_schema={
            "type": "object",
            "properties": {
                "project_path": {"type": "string", "description": "Path to the project root"},
                "note": {"type": "string", "description": "Journal note content"},
            },
            "required": ["project_path", "note"],
        },
    ),
    Tool(
        name="yaam_init",
        description="Scan a project's README.md and detect name, stack, description for setup",
        input_schema={
            "type": "object",
            "properties": {
                "project_path": {"type": "string", "description": "Path to the project root"},
            },
            "required": ["project_path"],
        },
    ),
]


def _find_templates_dir() -> Path:
    script = Path(__file__).resolve()
    candidates = [
        script.parent / "templates",
        script.parent.parent / "templates",
        Path.cwd() / "templates",
    ]
    for p in candidates:
        if p.is_dir():
            return p
    return candidates[0]


def _read_template(*parts: str) -> str:
    templates_dir = _find_templates_dir()
    path = templates_dir.joinpath(*parts)
    if not path.exists():
        return f"# {parts[-1]}\n\nTemplate not found.\n"
    return path.read_text(encoding="utf-8")


def _progress_tracer_path(project_path: str) -> Path:
    return Path(project_path) / "contexts" / "progress-tracer.md"


# Tool implementations

async def _check_yaam_status(project_path: str) -> str:
    root = Path(project_path)
    contexts = root / "contexts"
    if not contexts.is_dir():
        return json_dumps({"initialized": False, "message": "Yaam framework not found. Run setup_yaam_framework."})
    files = sorted(f.name for f in contexts.iterdir() if f.suffix == ".md")
    return json_dumps({"initialized": True, "project": root.name, "context_files": files})


async def _setup_yaam_framework(project_path: str, project_name: str, stack: str = "generic", dry_run: bool = False) -> str:
    root = Path(project_path)
    base_structure = {
        "contexts": [
            "ai-workflow-rules.md",
            "architecture-context.md",
            "code-standards.md",
            "progress-tracer.md",
            "project-overview.md",
            "ui-context.md",
        ],
        "features-specs": ["TEMPLATE.md"],
        "issues": ["TEMPLATE.md"],
    }
    agent_content = _read_template("AGENT.md")

    if dry_run:
        lines = [f"[DRY RUN] Would create: {root.name}/"]
        for dir_name, files in base_structure.items():
            lines.append(f"  {dir_name}/")
            for f in files:
                lines.append(f"    {f}")
            lines.append(f"  AGENT.md")
        return "\n".join(lines)

    created = []
    for dir_name, files in base_structure.items():
        target_dir = root / dir_name
        target_dir.mkdir(parents=True, exist_ok=True)
        for fname in files:
            content = _read_template(dir_name, fname)
            (target_dir / fname).write_text(content, encoding="utf-8")
            created.append(f"{dir_name}/{fname}")

    agent_path = root / "AGENT.md"
    agent_path.write_text(agent_content, encoding="utf-8")
    created.append("AGENT.md")

    return json_dumps({"created": created, "project": project_name, "stack": stack})


async def _get_project_status(project_path: str) -> str:
    path = _progress_tracer_path(project_path)
    if not path.exists():
        return json_dumps({"error": "progress-tracer.md not found. Run setup_yaam_framework first."})
    content = path.read_text(encoding="utf-8")
    return content


async def _add_tracer_task(project_path: str, task: str) -> str:
    path = _progress_tracer_path(project_path)
    if not path.exists():
        return json_dumps({"error": "progress-tracer.md not found. Run setup_yaam_framework first."})
    content = path.read_text(encoding="utf-8")
    marker = "## 🎯 Objectifs en cours"
    new_entry = f"- [ ] {task}"
    if new_entry in content:
        return json_dumps({"message": "Task already exists.", "task": task})
    if marker in content:
        content = content.replace(marker, f"{marker}\n{new_entry}", 1)
    else:
        content += f"\n{new_entry}\n"
    path.write_text(content, encoding="utf-8")
    return json_dumps({"message": "Task added.", "task": task})


async def _complete_tracer_task(project_path: str, task: str) -> str:
    path = _progress_tracer_path(project_path)
    if not path.exists():
        return json_dumps({"error": "progress-tracer.md not found."})
    content = path.read_text(encoding="utf-8")
    pattern = f"- [ ] {task}"
    if pattern not in content:
        return json_dumps({"error": "Task not found.", "task": task})
    content = content.replace(pattern, f"- [x] {task}", 1)
    path.write_text(content, encoding="utf-8")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    log_entry = f"- **{now} UTC** — Tâche terminée : {task}"
    history_marker = "## 📜 Journal Historique"
    if history_marker in content:
        content = content.replace(history_marker, f"{history_marker}\n{log_entry}", 1)
        path.write_text(content, encoding="utf-8")

    return json_dumps({"message": "Task completed.", "task": task})


async def _log_progress_note(project_path: str, note: str) -> str:
    path = _progress_tracer_path(project_path)
    if not path.exists():
        return json_dumps({"error": "progress-tracer.md not found."})
    content = path.read_text(encoding="utf-8")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    entry = f"- **{now} UTC** — {note}"
    history_marker = "## 📜 Journal Historique"
    if history_marker in content:
        content = content.replace(history_marker, f"{history_marker}\n{entry}", 1)
    else:
        content += f"\n{entry}\n"
    path.write_text(content, encoding="utf-8")
    return json_dumps({"message": "Note logged.", "note": note})


# README scanning heuristics

STACK_KEYWORDS: dict[str, list[str]] = {
    "laravel":   ["laravel", "eloquent", "artisan", "php artisan", "blade"],
    "nextjs":    ["next.js", "nextjs", "next js"],
    "react":     ["react", "jsx", "tsx", "vite"],
    "django":    ["django", "python manage.py", "wsgi.py", "asgi.py"],
    "fastapi":   ["fastapi", "uvicorn"],
    "flask":     ["flask", "werkzeug"],
    "rails":     ["ruby on rails", "rails", "activerecord"],
    "symfony":   ["symfony", "doctrine", "twig"],
    "spring":    ["spring boot", "spring framework"],
    "express":   ["express.js", "expressjs"],
    "svelte":    ["svelte", "sveltekit"],
    "vue":       ["vue.js", "vuejs", "nuxt"],
    "react-native": ["react native", "expo"],
}


def _detect_stack(readme_text: str) -> str:
    text = readme_text.lower()
    scores: dict[str, int] = {}
    for stack, keywords in STACK_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in text)
        if score > 0:
            scores[stack] = score
    if not scores:
        return "generic"
    return max(scores, key=scores.get)


def _detect_name(project_path: str, readme_text: str) -> str:
    m = re.search(r'^#\s+(.+)$', readme_text, re.MULTILINE)
    if m:
        return m.group(1).strip().lstrip('#').strip()
    return Path(project_path).resolve().name


def _detect_description(readme_text: str) -> str:
    lines = readme_text.strip().splitlines()
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('#') and not stripped.startswith('>') and not stripped.startswith('---'):
            return stripped[:200]
    return ""


async def _yaam_init(project_path: str) -> str:
    root = Path(project_path)
    if not root.is_dir():
        return json_dumps({"error": f"Directory not found: {project_path}"})

    readme_path = root / "README.md"
    if not readme_path.exists():
        return json_dumps({
            "readme_found": False,
            "detected_name": root.resolve().name,
            "detected_stack": "generic",
            "detected_description": "",
            "message": "No README.md found. Using defaults.",
        })

    text = readme_path.read_text(encoding="utf-8")
    result = {
        "readme_found": True,
        "detected_name": _detect_name(project_path, text),
        "detected_stack": _detect_stack(text),
        "detected_description": _detect_description(text),
    }
    return json_dumps(result)


# JSON helper (avoid extra dependency)

def json_dumps(obj) -> str:
    import json
    return json.dumps(obj, ensure_ascii=False, indent=2)


# Main entrypoint

def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Yaam MCP Server")
    p.add_argument("--project-path", default=".", help="Default project root path")
    p.add_argument("--verbose", action="store_true", help="Enable debug logging")
    p.add_argument("--dry-run", action="store_true", help="Simulate operations without writing")
    p.add_argument("--init", action="store_true", help="Run yaam-init scan and exit (standalone mode)")
    return p


def setup_logging(verbose: bool) -> logging.Logger:
    level = logging.DEBUG if verbose else logging.INFO
    fmt = "%(asctime)s [%(levelname)s] %(message)s"
    logging.basicConfig(stream=sys.stderr, level=level, format=fmt)
    return logging.getLogger("yaam-server")


async def main() -> None:
    global log
    args = build_arg_parser().parse_args()
    log = setup_logging(args.verbose)

    if args.init:
        log.debug("Standalone init mode for %s", args.project_path)
        result = await _yaam_init(args.project_path)
        print(result)
        return

    log.debug("Starting yaam-server (project-path=%s, dry-run=%s)", args.project_path, args.dry_run)

    async def list_tools(ctx, params=None) -> ListToolsResult:
        log.debug("list_tools called")
        return ListToolsResult(tools=TOOLS)

    async def call_tool(ctx, params) -> CallToolResult:
        name = params.name
        arguments = params.arguments or {}
        log.debug("call_tool: %s %s", name, arguments)
        project_path = arguments.get("project_path", args.project_path)

        try:
            if name == "check_yaam_status":
                result = await _check_yaam_status(project_path)
            elif name == "setup_yaam_framework":
                result = await _setup_yaam_framework(
                    project_path=project_path,
                    project_name=arguments.get("project_name", "untitled"),
                    stack=arguments.get("stack", "generic"),
                    dry_run=arguments.get("dry_run", args.dry_run),
                )
            elif name == "get_project_status":
                result = await _get_project_status(project_path)
            elif name == "add_tracer_task":
                result = await _add_tracer_task(project_path, arguments["task"])
            elif name == "complete_tracer_task":
                result = await _complete_tracer_task(project_path, arguments["task"])
            elif name == "log_progress_note":
                result = await _log_progress_note(project_path, arguments["note"])
            elif name == "yaam_init":
                result = await _yaam_init(project_path)
            else:
                return CallToolResult(content=[TextContent(type="text", text=f"Unknown tool: {name}")], is_error=True)

            return CallToolResult(content=[TextContent(type="text", text=result)], is_error=False)
        except Exception as e:
            log.exception("Error executing %s", name)
            return CallToolResult(content=[TextContent(type="text", text=str(e))], is_error=True)

    server = Server(
        "yaam-server",
        on_list_tools=list_tools,
        on_call_tool=call_tool,
        version="1.0.0",
    )

    async with stdio_server() as (read_stream, write_stream):
        log.info("yaam-server ready (MCP stdio)")
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import anyio
    anyio.run(main)
