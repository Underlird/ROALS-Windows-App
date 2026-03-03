from __future__ import annotations

import sys

from PySide6.QtWidgets import QLabel, QMainWindow

from roals_app.core.config import load_config


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("roals_desktop (read-only)")
        self.setMinimumSize(900, 550)

        config = load_config()

        label = QLabel(
            "roals_desktop (read-only)\n\n"
            f"Python Version: {sys.version.split()[0]}\n"
            f"Python Executable: {sys.executable}\n"
            f"Config Path: {config.config_path}\n"
            f"Data Root: {config.data_root}\n"
            f"Logs Dir: {config.logs_dir}"
        )
        label.setWordWrap(True)
        self.setCentralWidget(label)
