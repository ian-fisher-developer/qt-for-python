import sys
from PySide6.QtWidgets import QApplication, QTableView
from fixed_table_model import FixedTableModel


if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = FixedTableModel()
    table = QTableView()
    table.setModel(model)
    table.resizeColumnsToContents()
    table.show()
    sys.exit(app.exec())
