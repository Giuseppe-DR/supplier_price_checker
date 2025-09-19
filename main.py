import sys
from PyQt6.QtWidgets import QApplication
from gui.main_gui import SimpleWindow
from PyQt6.QtGui import QIcon

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon2.ico"))
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec())
