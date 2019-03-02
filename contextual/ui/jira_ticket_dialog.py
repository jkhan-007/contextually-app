from PyQt5.QtWidgets import (QDialog)

from contextual.ui.generated.jira_ticket_dialog import Ui_JiraTicketDialog
from contextual.ui.presenters.ticket_presenter import JiraTicketPresenter


class JiraTicketDialog(QDialog, Ui_JiraTicketDialog):

    def __init__(self, parent=None):
        super(JiraTicketDialog, self).__init__(parent)
        self.presenter = JiraTicketPresenter(self, parent)

    def initialize(self):
        self.setupUi(self)
        self.setFixedSize(self.size())
        # @todo: Add validator
        # https://snorfalorpagus.net/blog/2014/08/09/validating-user-input-in-pyqt4-using-qvalidator/

    def show_dialog(self):
        self.show()
