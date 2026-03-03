from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("ROALS Desktop")
        self.resize(600, 300)

        central = QWidget()
        layout = QVBoxLayout(central)

        layout.addWidget(QLabel("ROALS Desktop läuft stabil."))

        self.setCentralWidget(central)
