# -*- coding: utf-8 -*-
"""
Anki Add-on: Refresh Search Button
Adds a refresh button next to the search bar to re-run the current search.
Allows user-configurable shortcuts via the Config button.
"""
from aqt.qt import *
from aqt import gui_hooks, mw

def get_config_shortcut():
    """Retrieve the shortcut from config.json, default to F5 if missing"""
    config = mw.addonManager.getConfig(__name__)
    if config and "refresh_shortcut" in config:
        return config["refresh_shortcut"]
    return "F5"

def add_refresh_button(browser):
    """Add a refresh button next to the search bar and setup shortcut"""
    
    # 1. Get user-defined shortcut
    shortcut_seq = get_config_shortcut()

    # 2. Create Refresh Button
    refresh_button = QPushButton("🔄")
    refresh_button.setToolTip(f"Refresh search results ({shortcut_seq})")
    refresh_button.setFlat(True)
    refresh_button.setMaximumWidth(30)
    
    # Connect button click
    refresh_button.clicked.connect(lambda: refresh_search(browser))
    
    # Add button to layout
    layout = browser.form.gridLayout
    layout.addWidget(refresh_button, 0, layout.columnCount())

    # 3. Create Shortcut
    refresh_shortcut = QShortcut(QKeySequence(shortcut_seq), browser)
    refresh_shortcut.activated.connect(lambda: refresh_search(browser))
    
    # Save reference to prevent garbage collection
    browser.refresh_search_shortcut = refresh_shortcut

def refresh_search(browser):
    """Re-run the current search"""
    current_search = browser.form.searchEdit.currentText()
    browser.search_for(current_search)

# Register the hook
gui_hooks.browser_will_show.append(add_refresh_button)
