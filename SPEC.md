# SPEC — ROALS Windows App (v1.0)

## Purpose
A small, always-on Windows 11 tray app (PySide6) that monitors and manually triggers the local ROALS runner on a single laptop (Yoga 7).
The app is an interface/control layer only and must not contain business logic.

## Target platform
- Windows 11
- Single user, single device
- Python 3.11+

## In-scope (v1.0)
1. Tray-first application
   - Tray icon visible after start
   - Context menu:
     - Open (show main window)
     - Show logs (open minimal log viewer)
     - Run now (trigger runner)
     - Exit

2. Status polling (read-only)
   - QTimer polling reads these local files (paths configurable later, default relative paths):
     - `last_status.txt` (one of: OK / DEGRADED / FAILED)
     - `run_log.json` (small JSON with last run metadata)
     - `run_console.log` (text log tail)
   - Tray tooltip shows current `last_status.txt` + timestamp of last update
   - Stale detection:
     - if `last_status.txt` mtime older than 26h -> show status as STALE

3. Minimal main window
   - Displays:
     - current status (OK/DEGRADED/FAILED/STALE)
     - last run time
     - last run duration (if available)
     - last exit code / overall status (if available)
   - Buttons:
     - Run now
     - Open logs
     - Quit

4. Minimal log viewer
   - Shows:
     - last N lines (e.g. 300) of `run_console.log`
     - optional: basic fields from `run_log.json` if present
   - Must not crash on missing/invalid files (show a clear message instead)

5. Local run instructions
   - `requirements.txt` includes PySide6 (and only minimal extras if truly required)
   - `README.md` includes exact Windows steps (venv, pip install, run)

## Out of scope (explicitly NOT in v1.0)
- No Home Assistant integration
- No network calls, no API clients, no telemetry upload
- No database
- No auto-updater
- No plugin system
- No scheduler implementation (runner scheduling stays outside; app only triggers)
- No complex dashboards, charts, analytics, or data transformations

## Definition of Done (v1.0)
- App launches on Windows 11 and shows tray icon
- Menu actions work (Open, Show logs, Run now, Exit)
- Polling updates status and handles missing files gracefully
- Main window and log viewer open without errors
- README instructions allow a clean local run in a venv
