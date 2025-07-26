from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)

from db.sqlite_utils import insert_items
from utils import db_to_excel
from utils.cedi_input_file import insert_cedi_file


class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertitore PDF -> Excel")
        self.resize(400, 200)

        layout = QVBoxLayout()

        self.pdf_path = None
        self.excel_path = None

        self.file_label = QLabel("Nessun PDF selezionato")
        self.excel_pathTxt = QLabel("Percorso Excel non selezionato")

        self.choose_pdf_btn = QPushButton("📂 Scegli PDF")
        self.choose_pdf_btn.clicked.connect(self.choose_pdf)

        self.choose_save_btn = QPushButton("💾 Scegli dove salvare Excel")
        self.choose_save_btn.clicked.connect(self.choose_save_path)

        self.convert_btn = QPushButton("🚀 Converti PDF in Excel")
        self.convert_btn.clicked.connect(self.load_and_insert_items)

        layout.addWidget(self.file_label)
        layout.addWidget(self.choose_pdf_btn)
        layout.addWidget(self.excel_pathTxt)
        layout.addWidget(self.choose_save_btn)
        layout.addWidget(self.convert_btn)

        self.setLayout(layout)


    def choose_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleziona PDF", "", "PDF Files (*.pdf)")
        if file_path:
            self.pdf_path = file_path
            self.file_label.setText(file_path)

    def choose_save_path(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder to Save Excel")
        if folder:
            try:
                self.excel_path = folder
                self.excel_pathTxt.setText(folder)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"❌ Failed to insert: {e}")

    def load_and_insert_items(self):
        if not self.pdf_path:
            QMessageBox.warning(self, "Missing File", "Please choose a file.")
            return
        try:
            items = insert_cedi_file(self.pdf_path)
            insert_items(items)
            db_to_excel("data/items.db", "items", self.excel_path + "/CEDIconvertito.xlsx")

            QMessageBox.information(self, "Success", f"✅ Inserted {len(items)} items.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"❌ Failed to insert: {e}")