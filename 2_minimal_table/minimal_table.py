import sys
from PySide6.QtWidgets import QApplication, QTableView
from minimal_table_model import MinimalTableModel


if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = MinimalTableModel()
    table = QTableView()
    table.setModel(model)
    table.show()
    sys.exit(app.exec())
