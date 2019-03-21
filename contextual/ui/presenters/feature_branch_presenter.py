from contextual.core.core_settings import app_settings
from contextual.core.git_interactor import create_feature_branch
from contextual.model.app_data import Ticket


class FeatureBranchPresenter:
    selected_ticket: Ticket

    def __init__(self, view, parent_view):
        self.view = view
        self.parent_view = parent_view
        self.selected_ticket = None
        self.view.btn_create_branch.pressed.connect(self.on_create_branch)
        self.view.btn_cancel_create_branch.pressed.connect(self.view.reject)

    def load_dialog(self, selected_ticket):
        self.selected_ticket = selected_ticket
        self.view.txt_main_branch.setText("develop")
        self.view.txt_feature_branch.setText(f"{self.selected_ticket.ticket_number}-")
        self.view.show()

    def on_create_branch(self):
        if not self.selected_ticket:
            return

        old_branch = self.view.txt_main_branch.text()
        new_branch = self.view.txt_feature_branch.text()
        workspace_dir = self.selected_ticket.workspace_dir
        try:
            create_feature_branch(workspace_dir, old_branch, new_branch)
            app_settings.app_data.update_branch(workspace_dir)
            self.view.accept()
        except IndexError as e:
            self.view.lbl_error.setText(f"ERROR: {e}")
