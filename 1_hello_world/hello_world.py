import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel


def greeting():
    return "Hello Qt for Python!"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel(greeting(), alignment=Qt.AlignCenter)
    label.show()
    sys.exit(app.exec())
