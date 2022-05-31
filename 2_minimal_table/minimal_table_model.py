from string import ascii_uppercase
from PySide6.QtCore import (QAbstractTableModel, QModelIndex, Qt)


class MinimalTableModel(QAbstractTableModel):

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

    #def data(self, index, role=Qt.DisplayRole):
    #    if not index.isValid():
    #        return None

    #    if role == Qt.DisplayRole:
    #        return "1A"

    #    return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return ascii_uppercase[section]

        return str(section+1)
