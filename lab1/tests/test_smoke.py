from __future__ import annotations

import subprocess
import sys


def test_import_package() -> None:
    import pad_rag  # noqa: F401


def test_cli_version() -> None:
    completed = subprocess.run(
        [sys.executable, "-m", "pad_rag.cli", "--version"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "pad-rag 0.1.0" in completed.stdout


def test_cli_status_reports_not_implemented() -> None:
    completed = subprocess.run(
        [sys.executable, "-m", "pad_rag.cli", "status"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "not implemented yet" in completed.stdout.lower()
