import os
from aqt import mw, gui_hooks
from aqt.addons import AddonsDialog
from aqt.qt import QAction, QPushButton, QIcon
from aqt.editor import EditorMode, Editor
from PyQt5.QtWidgets import QHBoxLayout
from .settings_dialog import SettingsDialog
from aqt.gui_hooks import editor_did_init_buttons


ADDON_NAME='dall-e-anki'

def open_settings_dialog():
    dialog = SettingsDialog(mw)
    dialog.exec_()

def on_addon_config():
    mw.addonManager.setConfigAction(__name__, open_settings_dialog)

def on_editor_did_init_buttons(buttons, editor):
    # Create a new button
    icon_path = os.path.join(os.path.dirname(__file__), "picture.svg")
    btn = editor.addButton(
        icon=icon_path,
        tip=ADDON_NAME,
        cmd = "do_nothing",
        func= lambda e=editor: on_my_button_clicked(),
        keys=None,
        disables=False
    )
    buttons.append(btn)
    return buttons

    # Dummy function for the button
def on_my_button_clicked():
    pass  # Do nothing for now


# Add a menu item to open the settings dialog, if needed
action = QAction("Configure Language Settings", mw)
action.triggered.connect(open_settings_dialog)
mw.form.menuTools.addAction(action)

on_addon_config()

editor_did_init_buttons.append(on_editor_did_init_buttons)
