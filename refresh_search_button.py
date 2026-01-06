# -*- coding: utf-8 -*-
"""
Anki Add-on: Refresh Search Button
Adds a refresh button next to the search bar to re-run the current search.
"""
from aqt.qt import *
from aqt import gui_hooks

def add_refresh_button(browser):
    """Add a refresh button next to the search bar"""
    
    # Create refresh button (flat style, no border)
    refresh_button = QPushButton("🔄")
    refresh_button.setToolTip("Refresh search results")
    refresh_button.setFlat(True)
    refresh_button.setMaximumWidth(30)
    
    # Connect to search function
    refresh_button.clicked.connect(lambda: refresh_search(browser))
    
    # Add button to the grid layout (row 0, next column after existing widgets)
    layout = browser.form.gridLayout
    layout.addWidget(refresh_button, 0, layout.columnCount())

def refresh_search(browser):
    """Re-run the current search"""
    # searchEdit is a QComboBox, use currentText() instead of text()
    current_search = browser.form.searchEdit.currentText()
    browser.search_for(current_search)

# Register the hook to add button when browser opens
gui_hooks.browser_will_show.append(add_refresh_button)
