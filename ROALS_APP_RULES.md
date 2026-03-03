Die Desktop-App ist READ ONLY gegenüber ROALS-Daten (Truth/Derived/Reports).
Die App darf bestehende ROALS-Dateien niemals ändern oder überschreiben.
Die App darf nur neue Dateien unter logs/ oder roals_ops/ erzeugen (optional).
Keine Änderungen an der Scriptfabrik (scriptfactory/) und an bestehenden Pipeline-Skripten.
Konfiguration wird nur gelesen (config.json / roals_config.py / Registry-Dateien).
Runner wird nur als separater Prozess gestartet (kein Import der Pipeline-Logik in die App).
Abhängigkeiten minimal: PySide6 + Python Standard Library.
