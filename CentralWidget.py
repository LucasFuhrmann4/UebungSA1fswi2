from PyQt6.QtCore import QTimer, QTime, pyqtSlot, Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLCDNumber, QLineEdit, QPushButton, QLabel, QGridLayout, QComboBox


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.combo_box = QComboBox()
        self.combo_box.addItem("Option 1")
        self.combo_box.addItem("Option 2")
        self.combo_box.addItem("Option 3")

        self.combo_box2 = QComboBox()
        self.combo_box2.addItem("neue Box 1")
        self.combo_box2.addItem("neue Box 2")
        self.combo_box2.addItem("neue Box 3")


        # Label, um die Auswahl anzuzeigen
        self.label = QLabel("Bitte wählen Sie eine Option.")
        self.label1 = QLabel("Die Option wurde ausgewählt")

        # Verbindung des Signal 'currentIndexChanged' zu einer Methode
        self.combo_box.currentIndexChanged.connect(self.update_label)
        self.combo_box2.currentIndexChanged.connect(self.update_label1)

        # Layout für das Fenster
        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.combo_box2)
        layout.addWidget(self.label)
        layout.addWidget(self.label1)

        self.setLayout(layout)
        self.setWindowTitle("ComboBox Beispiel")
        self.setGeometry(100, 100, 300, 200)

    def update_label(self):
       # """Aktualisiert das Label basierend auf der Auswahl des Benutzers."""
        selected_option = self.combo_box.currentText()
        self.label.setText(f"Ausgewählte Option: {selected_option}")

    def update_label1(self):
       # """Aktualisiert das Label basierend auf der Auswahl des Benutzers."""
        selected_option = self.combo_box2.currentText()
        self.label1.setText(f"Ausgewählte Option: {selected_option}")