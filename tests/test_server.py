"""Tests for yaam-server MCP tools."""
import json
import os
import shutil
import subprocess
import tempfile
import time

import pytest

SERVER_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "yaam-server.py")


@pytest.fixture
def project():
    tmp = tempfile.mkdtemp()
    yield tmp
    shutil.rmtree(tmp, ignore_errors=True)


def _start_server(project_path):
    proc = subprocess.Popen(
        ["python3", SERVER_SCRIPT, "--project-path", project_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    # initialize
    _send(proc, {"jsonrpc": "2.0", "id": 1, "method": "initialize",
                  "params": {"protocolVersion": "2025-03-26", "capabilities": {},
                             "clientInfo": {"name": "test", "version": "1.0"}}})
    return proc


def _send(proc, msg):
    proc.stdin.write(json.dumps(msg) + "\n")
    proc.stdin.flush()
    time.sleep(0.2)
    return json.loads(proc.stdout.readline())


def _call_tool(proc, name, arguments):
    return _send(proc, {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
                         "params": {"name": name, "arguments": arguments}})


class TestCheckYaamStatus:
    def test_not_initialized(self, project):
        proc = _start_server(project)
        r = _call_tool(proc, "check_yaam_status", {"project_path": project})
        data = json.loads(r["result"]["content"][0]["text"])
        assert data["initialized"] is False
        proc.kill()

    def test_initialized(self, project):
        os.makedirs(os.path.join(project, "contexts"), exist_ok=True)
        proc = _start_server(project)
        r = _call_tool(proc, "check_yaam_status", {"project_path": project})
        data = json.loads(r["result"]["content"][0]["text"])
        assert data["initialized"] is True
        proc.kill()


class TestSetupYaamFramework:
    def test_creates_structure(self, project):
        proc = _start_server(project)
        r = _call_tool(proc, "setup_yaam_framework",
                        {"project_path": project, "project_name": "test", "stack": "generic"})
        data = json.loads(r["result"]["content"][0]["text"])
        assert len(data["created"]) == 9
        assert os.path.isdir(os.path.join(project, "contexts"))
        assert os.path.isfile(os.path.join(project, "AGENT.md"))
        proc.kill()

    def test_double_init_without_force(self, project):
        os.makedirs(os.path.join(project, "contexts"), exist_ok=True)
        proc = _start_server(project)
        r = _call_tool(proc, "setup_yaam_framework",
                        {"project_path": project, "project_name": "test"})
        data = json.loads(r["result"]["content"][0]["text"])
        assert data.get("confirmation_required") is True
        proc.kill()

    def test_double_init_with_force(self, project):
        os.makedirs(os.path.join(project, "contexts"), exist_ok=True)
        proc = _start_server(project)
        r = _call_tool(proc, "setup_yaam_framework",
                        {"project_path": project, "project_name": "test", "force": True})
        data = json.loads(r["result"]["content"][0]["text"])
        assert "created" in data
        proc.kill()

    def test_dry_run(self, project):
        proc = _start_server(project)
        r = _call_tool(proc, "setup_yaam_framework",
                        {"project_path": project, "project_name": "test", "dry_run": True})
        text = r["result"]["content"][0]["text"]
        assert "[DRY RUN]" in text
        assert not os.path.isdir(os.path.join(project, "contexts"))
        proc.kill()


class TestYaamInit:
    def test_with_readme(self, project):
        with open(os.path.join(project, "README.md"), "w") as f:
            f.write("# My App\n\nA Laravel project.\n")
        proc = _start_server(project)
        r = _call_tool(proc, "yaam_init", {"project_path": project})
        data = json.loads(r["result"]["content"][0]["text"])
        assert data["readme_found"] is True
        assert data["detected_name"] == "My App"
        assert data["detected_stack"] == "laravel"
        proc.kill()

    def test_without_readme(self, project):
        proc = _start_server(project)
        r = _call_tool(proc, "yaam_init", {"project_path": project})
        data = json.loads(r["result"]["content"][0]["text"])
        assert data["readme_found"] is False
        proc.kill()


class TestTracerTools:
    def _setup(self, project):
        os.makedirs(os.path.join(project, "contexts"), exist_ok=True)
        with open(os.path.join(project, "contexts", "progress-tracer.md"), "w") as f:
            f.write("# Tracker\n\n## 🎯 Objectifs en cours\n\n\n## ✅ Terminé\n\n\n## 📜 Journal Historique\n\n")

    def test_add_task(self, project):
        self._setup(project)
        proc = _start_server(project)
        r = _call_tool(proc, "add_tracer_task",
                        {"project_path": project, "task": "Implement login"})
        data = json.loads(r["result"]["content"][0]["text"])
        assert data["message"] == "Task added."
        content = open(os.path.join(project, "contexts", "progress-tracer.md")).read()
        assert "- [ ] Implement login" in content
        proc.kill()

    def test_complete_task(self, project):
        self._setup(project)
        with open(os.path.join(project, "contexts", "progress-tracer.md"), "a") as f:
            f.write("- [ ] Fix bug\n")
        proc = _start_server(project)
        r = _call_tool(proc, "complete_tracer_task",
                        {"project_path": project, "task": "Fix bug"})
        data = json.loads(r["result"]["content"][0]["text"])
        assert data["message"] == "Task completed."
        content = open(os.path.join(project, "contexts", "progress-tracer.md")).read()
        assert "- [x] Fix bug" in content
        proc.kill()

    def test_log_note(self, project):
        self._setup(project)
        proc = _start_server(project)
        r = _call_tool(proc, "log_progress_note",
                        {"project_path": project, "note": "Started work"})
        data = json.loads(r["result"]["content"][0]["text"])
        assert data["message"] == "Note logged."
        content = open(os.path.join(project, "contexts", "progress-tracer.md")).read()
        assert "Started work" in content
        proc.kill()

    def test_get_status(self, project):
        self._setup(project)
        proc = _start_server(project)
        r = _call_tool(proc, "get_project_status",
                        {"project_path": project})
        assert len(r["result"]["content"][0]["text"]) > 50
        proc.kill()

    def test_add_duplicate_task(self, project):
        self._setup(project)
        content = open(os.path.join(project, "contexts", "progress-tracer.md")).read()
        content += "- [ ] Duplicate task\n"
        open(os.path.join(project, "contexts", "progress-tracer.md"), "w").write(content)
        proc = _start_server(project)
        r = _call_tool(proc, "add_tracer_task",
                        {"project_path": project, "task": "Duplicate task"})
        data = json.loads(r["result"]["content"][0]["text"])
        assert data["message"] == "Task already exists."
        proc.kill()


class TestErrors:
    def test_unknown_tool(self, project):
        proc = _start_server(project)
        r = _call_tool(proc, "nonexistent", {"project_path": project})
        assert r["result"].get("isError") is True
        proc.kill()

    def test_setup_missing_templates(self, project):
        """Should handle missing templates gracefully."""
        proc = _start_server(project)
        r = _call_tool(proc, "setup_yaam_framework",
                        {"project_path": project, "project_name": "test"})
        data = json.loads(r["result"]["content"][0]["text"])
        assert "created" in data
        proc.kill()
