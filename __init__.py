# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *

def show_config_dialog():
    config = mw.addonManager.getConfig(__name__)
    dialog = QDialog(mw)

    layout = QVBoxLayout(dialog)
    label = QLabel("This is a settings window for your add-on!", dialog)
    layout.addWidget(label)

    dialog.setLayout(layout)
    dialog.exec_()

# This registers the config dialog function as the one to be called
# when the user clicks the "Config" button in Anki's add-on list.
mw.addonManager.setConfigAction(__name__, show_config_dialog)



# # We're going to add a menu item below. First we want to create a function to
# # be called when the menu item is activated.

# def testFunction() -> None:
#     # get the number of cards in the current collection, which is stored in
#     # the main window
#     cardCount = mw.col.cardCount()
#     # show a message box
#     showInfo("Card count: %d" % cardCount)

# # create a new menu item, "test"
# action = QAction("test", mw)
# # set it to call testFunction when it's clicked
# qconnect(action.triggered, testFunction)
# # and add it to the tools menu
# mw.form.menuTools.addAction(action)
