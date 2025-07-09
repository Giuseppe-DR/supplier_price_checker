from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QLabel, QFileDialog, QMessageBox, QComboBox
)
from db.sqlite_utils import search_items_by_name, insert_items
from utils.cedi_input_file import insert_cedi_file


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📦 Supplier Price Manager")
        self.resize(950, 600)

        layout = QVBoxLayout()
        self.supplier_file_types = {
            "CEDI": "PDF Files (*.pdf)",
            "Surgelati Rossi": "Excel Files (*.xlsx)",
            "Distribuzione Italiana": "CSV Files (*.csv)",
            "Cash & Carry Luigi": "CSV Files (*.csv)"
        }

        # ===================== File Loader Area ==========================
        file_layout = QHBoxLayout()

        self.file_label = QLabel("No file selected")
        self.supplier_dropdown = QComboBox()
        self.supplier_dropdown.addItems(["CEDI", "SupplierB", "SupplierC", "SupplierD"])

        self.browse_button = QPushButton("📂 Choose CSV File")
        self.browse_button.clicked.connect(self.choose_file)

        self.load_button = QPushButton("🚀 Load & Insert Items")
        self.load_button.clicked.connect(self.load_and_insert_items)

        file_layout.addWidget(self.browse_button)
        file_layout.addWidget(QLabel("Supplier:"))
        file_layout.addWidget(self.supplier_dropdown)
        file_layout.addWidget(self.load_button)

        # ===================== Search Area ==========================
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by article code or description...")
        self.search_button = QPushButton("🔍 Search")
        self.search_button.clicked.connect(self.search_items)
        search_layout.addWidget(QLabel("🔎"))
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        # ===================== Table ==========================
        self.table = QTableWidget()
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels([
            "Fornitore", "Codice Articolo", "Codice Fornitore","Ean", "Descrizione", "Price (€)", "Netto", "Ivato", "Confezioni"
        ])
        self.table.setSortingEnabled(True)

        # Assemble all parts
        layout.addLayout(file_layout)
        layout.addLayout(search_layout)
        layout.addWidget(self.table)
        self.setLayout(layout)

        self.csv_path = None

    def load_and_insert_items(self):
        if not self.csv_path:
            QMessageBox.warning(self, "Missing File", "Please choose a file.")
            return

        supplier = self.supplier_dropdown.currentText()

        try:
            if supplier == "CEDI":
                items = insert_cedi_file(self.csv_path, supplier)

            insert_items(items)
            QMessageBox.information(self, "Success", f"✅ Inserted {len(items)} items for {supplier}.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"❌ Failed to insert: {e}")

    def search_items(self):
        query = self.search_input.text()
        results = search_items_by_name(query)
        self.table.setRowCount(len(results))
        for row, item in enumerate(results):
            self.table.setItem(row, 0, QTableWidgetItem(item.supplier))
            self.table.setItem(row, 1, QTableWidgetItem(item.articleCode))
            self.table.setItem(row, 2, QTableWidgetItem(item.supplierCode))
            self.table.setItem(row, 3, QTableWidgetItem(item.ean) or "")
            self.table.setItem(row, 4, QTableWidgetItem(item.description))
            self.table.setItem(row, 5, QTableWidgetItem(str(item.quantity)))
            self.table.setItem(row, 6, QTableWidgetItem(f"{item.price:.4f}") or 0.0)
            self.table.setItem(row, 7, QTableWidgetItem(f"{item.netto:.4f}") or 0.0)
            self.table.setItem(row, 8, QTableWidgetItem(f"{item.ivato:.4f}") or 0.0)


    def choose_file(self):
        supplier = self.supplier_dropdown.currentText()
        file_filter = self.supplier_file_types.get(supplier, "All Files (*)")

        file_path, _ = QFileDialog.getOpenFileName(self, f"Select file for {supplier}", "", file_filter)
        if file_path:
            self.csv_path = file_path
            self.file_label.setText(file_path)
