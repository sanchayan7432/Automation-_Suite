from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


def create_button(text, callback, icon_path=None):
    btn = QPushButton(f"  {text}")
    btn.setCursor(Qt.CursorShape.PointingHandCursor)

    btn.setMinimumHeight(55)   # 🔥 increase height
    btn.setStyleSheet("text-align: left; padding-left: 12px;")

    if icon_path:
        btn.setIcon(QIcon(icon_path))

    btn.clicked.connect(callback)
    return btn