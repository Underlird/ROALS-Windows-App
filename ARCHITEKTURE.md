# ARCHITECTURE — ROALS Windows App (v1.0)

## Architectural role
The ROALS Windows App is a thin interface layer.
It observes and manually triggers the local ROALS runner.
It does not contain business logic, data transformation, or analysis logic.

Truth and Meaning layers live outside this repository.

## Layer model

- Runner Layer (external)
  - roals_runner.py (separate project)
  - writes:
    - last_status.txt
    - run_log.json
    - run_console.log

- Desktop App (this repo)
  - reads runner output files
  - shows status
  - allows manual trigger
  - never mutates runner data files

## High-level structure

src/
└── roals_app/
    ├── main.py              (application entry point)
    ├── ui/
    │   ├── main_window.py   (status window)
    │   └── log_viewer.py    (log window)
    ├── core/
    │   ├── status_reader.py (file polling + stale logic)
    │   └── runner_trigger.py (QProcess wrapper)
    └── assets/
        └── icons/

## Execution model

- QApplication starts
- Tray icon created first (tray-first design)
- QTimer polling (default interval configurable, e.g. 60s)
- No background threads in v1.0
- Runner trigger uses QProcess (non-blocking)
- File reads must be defensive (file not found, JSON errors)

## Data flow

last_status.txt → status_reader → UI labels + tray tooltip  
run_log.json → status_reader → UI fields  
run_console.log → log_viewer (tail only)

No database.
No caching layer.
No transformation logic.

## Failure handling philosophy

- Missing files → show "NOT INITIALIZED"
- Invalid JSON → show "CORRUPT"
- Old mtime (>26h) → STALE
- UI must never crash because of file content.

## Design principles

- Deterministic behavior
- Minimal dependencies
- Explicit control
- Boring, stable, predictable
- No hidden automation
