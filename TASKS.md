# TASKS — ROALS Windows App (v1.0)

## Task 0 — Repo scaffold (structure only)
Create required folders and placeholder files:
- src/roals_app/main.py
- src/roals_app/ui/main_window.py
- src/roals_app/ui/log_viewer.py
- src/roals_app/core/status_reader.py
- src/roals_app/core/runner_trigger.py
- src/roals_app/assets/ (icons later)
- tests/ (optional placeholder)

Do not implement full functionality yet. Keep imports clean.

## Task 1 — Minimal PySide6 tray app
Implement:
- QApplication startup
- QSystemTrayIcon with menu:
  - Open
  - Show logs
  - Run now (stub)
  - Exit
- Minimal main window (placeholder)
- Ensure it runs on Windows 11 via `python -m roals_app` or equivalent entry.

## Task 2 — Status polling (read-only)
Implement QTimer polling:
- read `last_status.txt` and compute status (OK/DEGRADED/FAILED/STALE)
- stale rule: > 26h -> STALE
- update tray tooltip + main window labels
- handle missing/invalid files without crashing

## Task 3 — Log viewer (minimal)
Implement log viewer window:
- show last N lines from `run_console.log` (default N=300)
- basic parse of `run_log.json` (if present) and show key fields
- robust error handling (missing/corrupt files)

## Task 4 — Runner trigger (manual only)
Implement "Run now":
- trigger a local command (configurable constant for now), e.g. `roals_runner.py`
- run in a non-blocking way (QProcess preferred)
- capture exit code; do not parse or transform run data

## Task 5 — README + requirements finalized
- requirements.txt: PySide6 pinned (plus only necessary deps)
- README: venv instructions + run instructions + troubleshooting

## Task 6 — Optional packaging (only if requested)
- PyInstaller build instructions
- single-file exe
- app icon integration (later, only after icons exist)

## Guardrails
- Implement only the current task.
- No refactors across tasks unless required to fix a bug.
- No feature additions not explicitly listed.
