import sys
import os
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

def load_stylesheet(app):
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(BASE_DIR, "resources", "style.qss"), "r") as f:
            app.setStyleSheet(f.read())
    except:
        print("Style not loaded")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_stylesheet(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())