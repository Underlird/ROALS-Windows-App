from __future__ import annotations

from PySide6.QtWidgets import QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("ROALS Desktop (Read-only)")
        self.setMinimumSize(900, 550)

        label = QLabel(
            "ROALS Desktop – Read-only UI\n\n"
            "Nächster Schritt: Status/Logs anzeigen, Runner triggern, Registry Browser (read-only)."
        )
        label.setWordWrap(True)
        self.setCentralWidget(label)
