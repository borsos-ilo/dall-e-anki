from aqt import mw
from aqt.addons import AddonsDialog
from aqt.qt import QAction
from .settings_dialog import SettingsDialog

def open_settings_dialog():
    dialog = SettingsDialog(mw)
    dialog.exec_()

def on_addon_config():
    mw.addonManager.setConfigAction(__name__, open_settings_dialog)

# Add a menu item to open the settings dialog, if needed
action = QAction("Configure Language Settings", mw)
action.triggered.connect(open_settings_dialog)
mw.form.menuTools.addAction(action)

on_addon_config()
