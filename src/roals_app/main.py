from __future__ import annotations

import sys

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMenu, QSystemTrayIcon, QStyle

from roals_app.ui.main_window import MainWindow


def main() -> int:
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    # Main window (hidden by default)
    win = MainWindow()

    # Tray
    tray = QSystemTrayIcon()
    tray.setToolTip("ROALS Desktop (read-only)")

    # Use a guaranteed built-in icon (no file needed)
    icon = app.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon)
    tray.setIcon(icon)

    # Menu
    menu = QMenu()

    act_open = QAction("Open", menu)
    act_open.triggered.connect(win.show)
    menu.addAction(act_open)

    act_quit = QAction("Exit", menu)
    act_quit.triggered.connect(app.quit)
    menu.addSeparator()
    menu.addAction(act_quit)

    tray.setContextMenu(menu)

    # Click on tray -> show window
    tray.activated.connect(lambda reason: win.show() if reason == QSystemTrayIcon.Trigger else None)

    tray.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
