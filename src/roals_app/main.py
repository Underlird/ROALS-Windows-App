import sys

from PySide6.QtWidgets import QApplication

from roals_app.ui.main_window import MainWindow


def main() -> int:
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # wichtig für Tray-only später

    win = MainWindow()
    win.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
