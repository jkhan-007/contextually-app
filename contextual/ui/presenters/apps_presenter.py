import logging
import subprocess

from PyQt5.QtCore import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from contextual.model.app_data import app_data


class AppsPresenter:
    def __init__(self, parent_view):
        self.parent_view = parent_view
        self.list_apps = self.parent_view.list_apps
        self.model = QStandardItemModel()
        self.list_apps.setModel(self.model)
        self.ticket = None
        self.parent_view.btn_add_application.clicked.connect(self.add_application)
        self.list_apps.doubleClicked.connect(self.on_clicked)
        app_data.signals.ticket_changed.connect(self.refresh)
        app_data.signals.app_changed.connect(self.refresh_apps)

    def refresh_apps(self):
        self.model.clear()
        for app in app_data.get_apps():
            logging.info(f"Adding {app.get('path')}")
            i = QStandardItem(app.get('path'))
            self.model.appendRow(i)

    def refresh(self, ticket):
        logging.info(f"Refreshing Apps for ticket {ticket.ticket_number} - Workspace {ticket.workspace_dir}")
        self.ticket = ticket
        self.model.clear()
        for app in app_data.get_apps():
            logging.info(f"Adding {app.get('path')}")
            i = QStandardItem(app.get('path'))
            self.model.appendRow(i)

    def add_application(self):
        application_name, file_types = self.parent_view.open_file(
            "Select Application",
            "/Applications"
        )
        app_data.add_app(application_name)

    def on_clicked(self, index: QModelIndex):
        app_path = index.data()
        workspace_dir = self.ticket.workspace_dir
        cmd = f"open -a '{app_path}' '{workspace_dir}'"
        subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
