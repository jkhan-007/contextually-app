import pkg_resources
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


def tool_bar_items(self):
    """Create a tool bar for the main window."""
    self.addToolBar(Qt.TopToolBarArea, self.tool_bar)
    self.tool_bar.setMovable(False)

    configure_icon = pkg_resources.resource_filename('contextual.images', 'configure-48.png')
    tool_bar_configure_action = QAction(QIcon(configure_icon), 'Settings', self)
    tool_bar_configure_action.triggered.connect(self.configuration_dialog.show_dialog)

    self.tool_bar.addAction(tool_bar_configure_action)

    refresh_icon = pkg_resources.resource_filename('contextual.images', 'refresh-48.png')
    tool_bar_refresh_all_tickets = QAction(QIcon(refresh_icon), 'Refresh All Tickets', self)
    tool_bar_refresh_all_tickets.triggered.connect(self.refresh_all_tickets)

    self.tool_bar.addAction(tool_bar_refresh_all_tickets)

    spacer = QWidget()
    spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.tool_bar.addWidget(spacer)

    update_icon = pkg_resources.resource_filename('contextual.images', 'download-48.png')
    tool_bar_update_available = QAction(QIcon(update_icon), 'Update Available', self)
    tool_bar_update_available.setEnabled(False)
    tool_bar_update_available.triggered.connect(self.open_releases_page)

    self.tool_bar.addAction(tool_bar_update_available)
