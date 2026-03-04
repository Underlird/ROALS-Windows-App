import json
import os
import time
from datetime import datetime, timedelta
from pathlib import Path

# ROALS Import (Pfade aus deiner Config laden)
try:
    from roals_config import load_config, get
except ImportError:
    # Fallback für Standalone-Tests
    def get(cfg, key): return None

class StatusReader:
    def __init__(self, config_path=None):
        self.config = load_config() if config_path is None else load_config(config_path)
        self.log_dir = Path(get(self.config, "paths.log_root") or "logs")
        self.run_log_path = self.log_dir / "quality" / "latest_run_log.json"

    def _safe_read_json(self, file_path, retries=3, delay=0.5):
        """Liest JSON mit Retry-Logik (Schutz vor Dateisperren)"""
        for i in range(retries):
            try:
                if not os.path.exists(file_path):
                    return None
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (IOError, json.JSONDecodeError):
                if i < retries - 1:
                    time.sleep(delay)
                else:
                    return None
        return None

    def get_latest_status(self):
        """
        Analysiert den letzten Run und gibt Status + Details zurück.
        Status: OK (Green), WARN (Yellow), ERROR (Red), STALE (Grey/Blink)
        """
        data = self._safe_read_json(self.run_log_path)
        
        if not data:
            return {"status": "UNKNOWN", "message": "Kein Log gefunden"}

        # Zeit-Check (Forensik)
        ended_at_str = data.get("meta", {}).get("ended_at")
        is_stale = False
        if ended_at_str:
            try:
                # ISO-Zeit parsen (Berücksichtigt dein Zeitformat aus dem Runner)
                ended_at = datetime.fromisoformat(ended_at_str.replace('Z', '+00:00'))
                if datetime.now(ended_at.tzinfo) - ended_at > timedelta(hours=26):
                    is_stale = True
            except ValueError:
                pass

        overall_status = data.get("meta", {}).get("overall_status", "UNKNOWN")
        
        if is_stale:
            return {"status": "STALE", "message": "Letzter Run > 26h her", "data": data}
        
        return {
            "status": overall_status,
            "message": f"Run vom {ended_at_str[:16]}",
            "data": data
        }

# Test-Modus: Kann direkt ausgeführt werden
if __name__ == "__main__":
    reader = StatusReader()
    print(f"🔍 Prüfe Log: {reader.run_log_path}")
    print(f"📊 Ergebnis: {reader.get_latest_status()}")
