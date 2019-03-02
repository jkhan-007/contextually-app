from contextual.core.jira_interactor import JiraInteractor
from contextual.model.app_data import app_data
from contextual.model.config_settings import config_settings


class MainPresenter:
    def __init__(self, view):
        self.view = view
        self.jira_interactor = JiraInteractor()
        self.initial_load = True

    def after_load(self):
        if not self.initial_load:
            return

        self.initial_load = False
        if not config_settings.jira_configured():
            self.view.show_jira_configuration_dialog()
        else:
            self.refresh_all_tickets()

        self.check_updates()

    def check_updates(self):
        if config_settings.load_updates_configuration():
            self.view.updater.check()

    def refresh_all_tickets(self):
        args = {
            "exclude_status": "Done",
            "on_success": self.on_all_tickets_loaded,
            "on_failure": self.on_all_tickets_failed
        }
        self.view.show_progress_dialog("Refreshing all tickets")
        self.jira_interactor.fetch_all_tickets(**args)

    def on_all_tickets_loaded(self, result):
        print("All tickets loaded...Showing in List view")
        self.view.hide_progress_dialog()
        tickets = result.get('tickets')
        app_data.add_visible_tickets(tickets)

    def on_all_tickets_failed(self, result):
        print("Error fetching All tickets")
        self.view.hide_progress_dialog()
