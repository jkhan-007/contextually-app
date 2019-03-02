import os

from PyQt5.QtWidgets import QFileDialog

from contextual.core import truncate
from contextual.core.git_interactor import git_info
from contextual.model.app_data import Ticket
from contextual.model.app_data import app_data


class GitStatsPresenter:
    def __init__(self, parent_view):
        self.parent_view = parent_view
        self.parent_view.btn_workspace.clicked.connect(self.select_directory)
        self.selected_ticket = None
        app_data.signals.ticket_changed.connect(self.refresh)

    def select_directory(self):
        directory = self.parent_view.open_directory(
            "Select Folder",
            os.path.expandvars("~"),
            QFileDialog.ShowDirsOnly
        )
        if directory:
            app_data.add_workspace(self.selected_ticket.ticket_number, directory)

    def refresh(self, ticket: Ticket):
        print(f"Refreshing GitStats for Ticket: {ticket.ticket_number} - Dir: {ticket.workspace_dir}")
        self.selected_ticket = ticket
        self.update_view(ticket.workspace_dir)

    def update_view(self, directory):
        if directory:
            viewable_directory = truncate(directory)
            directory_label = f"<a href=\"file://{directory}\">{viewable_directory}</a>"
            self.parent_view.lbl_workspace_dir.setText(directory_label)
            branch, no_changes = git_info(directory)
            self.parent_view.lbl_branch_status.setText(f"{branch} (Pending Changes {no_changes})")
        else:
            self.parent_view.lbl_workspace_dir.setText("select workspace directory 👉")
            self.parent_view.lbl_branch_status.setText("(branch) (pending changes)")
