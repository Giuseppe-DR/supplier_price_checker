from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QLabel
)
from PyQt6.QtCore import Qt
from db.sqlite_utils import search_items_by_name


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📦 Supplier Price Finder")
        self.resize(900, 500)

        layout = QVBoxLayout()

        # 🔍 Search section
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by description or article code...")
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_items)
        search_layout.addWidget(QLabel("🔍"))
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        # 🧾 Table setup
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "Supplier", "Article Code", "Supplier Code", "Description", "Price (€)"
        ])
        self.table.setSortingEnabled(True)

        # 🔗 Layout assembly
        layout.addLayout(search_layout)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def search_items(self):
        query = self.search_input.text()
        results = search_items_by_name(query)

        self.table.setRowCount(len(results))

        for row, item in enumerate(results):
            self.table.setItem(row, 0, QTableWidgetItem(item.supplier))
            self.table.setItem(row, 1, QTableWidgetItem(item.articleCode))
            self.table.setItem(row, 2, QTableWidgetItem(item.supplierCode))
            self.table.setItem(row, 3, QTableWidgetItem(item.description))
            self.table.setItem(row, 4, QTableWidgetItem(f"{item.price:.4f}"))
