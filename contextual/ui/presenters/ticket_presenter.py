from contextual.core.jira_interactor import JiraInteractor
from contextual.model.app_data import app_data, Ticket


# @todo: May not be used - Deprecated
class JiraTicketPresenter:
    def __init__(self, view, parent_view):
        self.view = view
        self.parent_view = parent_view
        self.view.initialize()
        self.view.btn_ok.pressed.connect(self.accept)
        self.view.btn_cancel.pressed.connect(self.cancel)
        self.jira_interactor = JiraInteractor()

    def accept(self):
        jira_ticket = self.view.txt_jira_ticket.text()
        print(f"Loading {jira_ticket}")
        kwargs = {
            'ticket_number': jira_ticket,
            'on_success': self.on_success,
            'on_failure': self.on_failure
        }
        self.parent_view.status_bar.showMessage("Getting ticket details for ...")
        self.jira_interactor.fetch_ticket_details(**kwargs)

    def on_success(self, result):
        print("Save JIRA Ticket in app data")
        print("Add Ticket to ListView")
        self.parent_view.status_bar.showMessage("Ready", 5000)
        ticket_number = result.get('ticket_number')

        ticket = Ticket(
            ticket_number=ticket_number,
            ticket_title=result.get('ticket_title'),
            ticket_description=result.get('ticket_description'),
            ticket_comments=result.get('ticket_comments')
        )
        app_data.upsert_ticket(ticket_number, ticket)
        self.view.accept()

    def on_failure(self, result):
        self.view.reject()

    def cancel(self):
        self.view.reject()
