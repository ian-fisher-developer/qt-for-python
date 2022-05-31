import unittest
from fixed_table_model import FixedTableModel
from PySide6.QtCore import Qt


class TestFixedTableModel(unittest.TestCase):

    def setUp(self):
        self.model = FixedTableModel()

    def test_has_three_rows(self):
        self.assertEqual(self.model.rowCount(), 3)

    def test_has_five_columns(self):
        self.assertEqual(self.model.columnCount(), 5)

    def test_first_column_header_displays_A(self):
        actual = self.model.headerData(0, Qt.Horizontal, Qt.DisplayRole)
        self.assertEqual(actual, "A")

    def test_last_column_header_displays_E(self):
        section = self.model.columnCount()-1
        actual = self.model.headerData(section, Qt.Horizontal, Qt.DisplayRole)
        self.assertEqual(actual, "E")

    def test_first_row_header_displays_1(self):
        actual = self.model.headerData(0, Qt.Vertical, Qt.DisplayRole)
        self.assertEqual(actual, "1")

    def test_last_row_header_displays_3(self):
        section = self.model.rowCount()-1
        actual = self.model.headerData(section, Qt.Vertical, Qt.DisplayRole)
        self.assertEqual(actual, "3")

    def test_displays_data_as_column_letter_row_number(self):
        test_cells = [{"row": 0, "col": 0, "display": "A1"},
                      {"row": 2, "col": 0, "display": "A3"},
                      {"row": 0, "col": 4, "display": "E1"},
                      {"row": 2, "col": 4, "display": "E3"}]
        for cell in test_cells:
            index = self.model.index(cell["row"], cell["col"])
            actual = self.model.data(index, Qt.DisplayRole)
            self.assertEqual(actual, cell["display"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
