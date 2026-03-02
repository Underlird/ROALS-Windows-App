"""Main window for the ROALS tray application."""

from PySide6.QtWidgets import QLabel, QMainWindow


class MainWindow(QMainWindow):
    """Minimal placeholder main window for Task 1."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("ROALS")
        self.resize(420, 220)
        self.setCentralWidget(QLabel("ROALS main window placeholder", self))
