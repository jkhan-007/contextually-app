import logging

from contextual.core.core_settings import app_settings
from contextual.model.app_data import Ticket
from contextual.ui.widgets.ticket_page import WebEnginePage


class TicketContentPresenter:
    selected_ticket: Ticket

    def __init__(self, parent_view):
        self.parent_view = parent_view
        self.selected_ticket = None
        self.lbl_title = self.parent_view.lbl_ticket_title
        self.web_engine = self.parent_view.web_engine
        self.web_page = WebEnginePage(self.web_engine)
        self.web_engine.setPage(self.web_page)
        app_settings.app_data.signals.ticket_changed.connect(self.refresh)

    def refresh(self, ticket):
        logging.info("Refreshing data for ticket content")
        jira_server, _, _ = app_settings.load_jira_configuration()
        self.selected_ticket = ticket
        ticket_browse_link = f"{jira_server}/browse/{self.selected_ticket.ticket_number}"
        ticket_title = f"<a href=\"{ticket_browse_link}\">{self.selected_ticket.ticket_number}</a> - {self.selected_ticket.ticket_title}"
        self.lbl_title.setText(ticket_title)
        self.web_engine.setHtml(self.selected_ticket.ticket_description)
