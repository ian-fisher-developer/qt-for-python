import unittest
from minimal_table_model import MinimalTableModel
from PySide6.QtCore import Qt


class TestFixedTableModel(unittest.TestCase):

    def setUp(self):
        self.model = MinimalTableModel()

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


if __name__ == '__main__':
    unittest.main(verbosity=2)
