import sys
from PyQt6.QtWidgets import QApplication
from gui.main_gui import SimpleWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec())
