"""Application entry point for the ROALS Windows tray app."""

from __future__ import annotations

import sys

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMenu, QMessageBox, QStyle, QSystemTrayIcon

from roals_app.ui.log_viewer import LogViewer
from roals_app.ui.main_window import MainWindow


class TrayApp:
    """Minimal tray-first application scaffold for Task 1."""

    def __init__(self, app: QApplication) -> None:
        self._app = app
        self._main_window = MainWindow()
        self._log_viewer = LogViewer()

        tray_icon = self._app.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon)
        self._tray = QSystemTrayIcon(QIcon(tray_icon), self._app)
        self._tray.setToolTip("ROALS")

        menu = QMenu()

        open_action = QAction("Open", menu)
        open_action.triggered.connect(self._show_main_window)
        menu.addAction(open_action)

        show_logs_action = QAction("Show logs", menu)
        show_logs_action.triggered.connect(self._show_log_viewer)
        menu.addAction(show_logs_action)

        run_now_action = QAction("Run now", menu)
        run_now_action.triggered.connect(self._show_not_implemented)
        menu.addAction(run_now_action)

        menu.addSeparator()

        exit_action = QAction("Exit", menu)
        exit_action.triggered.connect(self._app.quit)
        menu.addAction(exit_action)

        self._tray.setContextMenu(menu)
        self._tray.show()

    def _show_main_window(self) -> None:
        self._main_window.show()
        self._main_window.raise_()
        self._main_window.activateWindow()

    def _show_log_viewer(self) -> None:
        self._log_viewer.show()
        self._log_viewer.raise_()
        self._log_viewer.activateWindow()

    def _show_not_implemented(self) -> None:
        QMessageBox.information(self._main_window, "Run now", "Not implemented")


def main() -> int:
    """Start the Task 1 tray application."""
    app = QApplication(sys.argv)

    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "ROALS", "System tray is not available on this system.")
        return 1

    app.setQuitOnLastWindowClosed(False)
    _ = TrayApp(app)

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
