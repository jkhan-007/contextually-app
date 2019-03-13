import logging
import sys
import traceback

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices, QCloseEvent, QIcon
from PyQt5.QtWidgets import qApp, QApplication, QDesktopWidget, QFileDialog, QMainWindow, QToolBar

import contextual
from contextual.ui.configuration_dialog import ConfigurationDialog
from contextual.ui.generated.base_window import Ui_MainWindow
from contextual.ui.menus import file_menu
from contextual.ui.presenters.apps_presenter import AppsPresenter
from contextual.ui.presenters.git_stats_presenter import GitStatsPresenter
from contextual.ui.presenters.main_presenter import MainPresenter
from contextual.ui.presenters.ticket_content_presenter import TicketContentPresenter
from contextual.ui.presenters.ticket_state_presenter import TicketStatePresenter
from contextual.ui.presenters.tickets_list_presenter import TicketsListPresenter
from contextual.ui.progress_dialog import ProgressDialog
from contextual.ui.toolbar import tool_bar_items
from contextual.ui.updater_dialog import Updater


class MainWindow(QMainWindow, Ui_MainWindow):
    releases_page: QUrl = QUrl('https://github.com/jkhan-007/contextually-app/releases/latest')

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.resize(1024, 768)
        self.setWindowTitle('Contextual - Focused workflow for developers')
        self.setWindowIcon(QIcon(":/images/contextually.png"))

        self.btn_workspace.setIcon(QIcon(":/images/folder-48.png"))

        # Add Components on Main Window
        self.updater = Updater(self)
        self.menu_bar = self.menuBar()
        self.tool_bar = QToolBar()
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Ready', 5000)

        # Custom Dialogs
        self.configuration_dialog = ConfigurationDialog(self)
        self.progress_dialog = ProgressDialog(self)

        # Initialise Components
        file_menu(self)
        tool_bar_items(self)

        # Initialise Presenters
        self.presenter = MainPresenter(self)
        self.tickets_list_presenter = TicketsListPresenter(self.tickets_list_widget, self)
        self.ticket_content_presenter = TicketContentPresenter(self)
        self.git_stats_presenter = GitStatsPresenter(self)
        self.apps_presenter = AppsPresenter(self)
        self.ticket_state_presenter = TicketStatePresenter(self)

        # Initialise Sub-Systems
        sys.excepthook = MainWindow.log_uncaught_exceptions

    @staticmethod
    def log_uncaught_exceptions(cls, exc, tb) -> None:
        logging.critical(''.join(traceback.format_tb(tb)))
        logging.critical('{0}: {1}'.format(cls, exc))

    # Main Window events
    def resizeEvent(self, event):
        self.presenter.after_load()

    def closeEvent(self, event: QCloseEvent):
        logging.info("Received close event")
        event.accept()
        self.presenter.shutdown()
        try:
            qApp.exit(0)
        except:
            pass

    # End Main Window events

    def check_updates(self):
        self.updater.check()

    def update_available(self, latest, current):
        update_available = True if latest > current else False
        logging.info(f"Update Available ({latest} > {current}) ? ({update_available}) Enable Toolbar Icon")
        if update_available:
            toolbar_actions = self.tool_bar.actions()
            updates_action = next(act for act in toolbar_actions if act.text() == 'Update Available')
            if updates_action:
                updates_action.setIcon(QIcon(":/images/download-48.png"))
                updates_action.setEnabled(True)

    def open_releases_page(self) -> None:
        QDesktopServices.openUrl(self.releases_page)

    def refresh_all_tickets(self):
        self.presenter.refresh_all_tickets()

    def show_progress_dialog(self, message):
        self.progress_dialog.show_dialog(message)

    def hide_progress_dialog(self):
        self.progress_dialog.hide_dialog()

    def update_progress_dialog(self, percent_completed, message):
        self.progress_dialog.update_status(percent_completed, message)

    def show_jira_configuration_dialog(self):
        self.configuration_dialog.show_dialog()

    def open_directory(self, dialog_title, dialog_location, flags):
        return QFileDialog.getExistingDirectory(
            self,
            dialog_title,
            dialog_location,
            flags
        )

    def open_file(self, dialog_title, dialog_location):
        return QFileDialog.getOpenFileName(
            self,
            dialog_title,
            dialog_location
        )


def configure_theme(application):
    from contextual.ui.themes.light_theme import LightTheme
    application.setStyle(LightTheme())
    application.style().load_stylesheet()


def main():
    application = QApplication(sys.argv)
    application.setApplicationVersion(contextual.__version__)
    application.setApplicationName(contextual.__appname__)
    application.setDesktopFileName(contextual.__desktopid__)

    window = MainWindow()
    configure_theme(application)

    desktop = QDesktopWidget().availableGeometry()
    width = (desktop.width() - window.width()) / 2
    height = (desktop.height() - window.height()) / 2
    window.show()
    window.move(width, height)
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
