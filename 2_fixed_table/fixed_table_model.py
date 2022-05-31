"""A simple Qt-for-Python table model with fixed data."""

from string import ascii_uppercase
from PySide6.QtCore import (QAbstractTableModel, QModelIndex, Qt)


class FixedTableModel(QAbstractTableModel):
    """A fixed 3 rows by 5 columns table model.

    The model displays row headers as numbers, column headers as letters, and
    the data as A1, B1, etc."""

    # Exercise Notes:
    # - This Python implementation should look very familiar to C++ developers
    # - Note the lack of QString or QVariant, Qt-for-Python uses native types

    def __init__(self, parent=None):
        super().__init__(parent)

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return 3

    def columnCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return 5

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role != Qt.DisplayRole:
            return None

        col_label = self.headerData(index.column(), Qt.Horizontal)
        row_label = self.headerData(index.row(), Qt.Vertical)
        return col_label + row_label

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return ascii_uppercase[section]

        return str(section+1)
