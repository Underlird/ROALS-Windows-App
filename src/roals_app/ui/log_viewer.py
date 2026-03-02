"""Log viewer window for the ROALS tray application."""

from PySide6.QtWidgets import QLabel, QDialog, QVBoxLayout


class LogViewer(QDialog):
    """Minimal placeholder log viewer for Task 1."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("ROALS Logs")
        self.resize(520, 320)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Log viewer placeholder", self))
