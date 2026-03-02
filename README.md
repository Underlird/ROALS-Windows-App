# ROALS Windows App

## Run locally on Windows 11

1. Create a virtual environment:
   ```powershell
   py -3.11 -m venv .venv
   ```
2. Activate the environment:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the app:
   ```powershell
   python -m roals_app
   ```

## Notes
- This is a tray-first PySide6 application.
- Task 1 currently provides minimal placeholder windows and menu actions.
