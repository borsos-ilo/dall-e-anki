from aqt import mw
from aqt.qt import *
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QDialogButtonBox

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.resize(500, 400)  # Set the window size to 400x200 pixels

        self.setWindowTitle('Language Settings')
        
        layout = QVBoxLayout(self)
        
        # Language selection
        language_label = QLabel('Select Language:', self)
        layout.addWidget(language_label)
        self.language_combo = QComboBox(self)
        self.language_combo.addItems(["Hungarian", "Polish", "English", "Czech"])
        layout.addWidget(self.language_combo)
        
        # Language level selection
        level_label = QLabel('Select Language Level:', self)
        layout.addWidget(level_label)
        self.level_combo = QComboBox(self)
        self.level_combo.addItems(["A", "B", "C"])
        layout.addWidget(self.level_combo)
        
        # API Key input
        api_key_label = QLabel('API Key:', self)
        layout.addWidget(api_key_label)
        self.api_key_input = QLineEdit(self)
        layout.addWidget(self.api_key_input)
        
        # OK and Cancel buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        self.load_settings()

    def load_settings(self):
        config = mw.addonManager.getConfig(__name__)
        self.language_combo.setCurrentText(config.get('selected_language', 'English'))
        self.level_combo.setCurrentText(config.get('language_level', 'A'))
        self.api_key_input.setText(config.get('api_key', ''))

    def accept(self):
        config = mw.addonManager.getConfig(__name__)
        config['selected_language'] = self.language_combo.currentText()
        config['language_level'] = self.level_combo.currentText()
        config['api_key'] = self.api_key_input.text()
        mw.addonManager.writeConfig(__name__, config)
        super(SettingsDialog, self).accept()
