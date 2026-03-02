# ROALS Windows App — Codex Working Agreement (AGENTS.md)

This repository contains ONLY the ROALS Windows desktop app for a single device (Yoga 7, Windows 11).
It is a tray-based PySide6 application used to observe and control local ROALS runner scripts.
No Home Assistant integration. No cloud services. No network features.

## Non-negotiables
- Windows 11 only. Single-user, single-machine (Yoga 7).
- PySide6 UI. Tray-first app. Runs continuously.
- Read-only by default. Any write actions must be explicit user actions (menu click).
- No business logic in the UI. UI is a thin presentation/control layer only.
- No modifications to external systems. No HA, no MQTT, no APIs.
- Keep dependencies minimal. Prefer stdlib. Avoid heavy frameworks.
- Code must be deterministic, stable, and boring.

## Repository layout (required)
Use a src layout:
- src/roals_app/...
Entry point: src/roals_app/main.py

## Coding standards
- Python 3.11+
- Type hints required for public functions.
- Small modules, clear names.
- Defensive error handling (file not found, JSON errors, permission errors).
- Logging via stdlib `logging` (rotating later, not now).
- No hidden background threads unless necessary; prefer QTimer polling.

## UI rules (v1.0)
- Tray icon with context menu:
  - Open (show main window)
  - Show logs (opens a minimal viewer)
  - Run now (triggers runner)
  - Exit
- Main window is minimal (status + last run + buttons). No complex dashboards.

## Scope control
- Implement only what is asked in the current task.
- Do not add extra features “because it’s useful”.
- If requirements are unclear, STOP and ask a question instead of guessing.

## Output expectations
- Every change must be testable on Windows 11.
- Provide a short README run section for local execution in a venv.
- If packaging is requested, use PyInstaller with a single-file build (later tasks only).
