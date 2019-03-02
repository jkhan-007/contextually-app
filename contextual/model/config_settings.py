import configparser

from contextual.core import str_to_bool
from contextual.external.data_file import app_dir

JIRA_SEC = 'JIRA'
JIRA_SEC_SERVER = 'server'
JIRA_SEC_USERNAME = 'username'
JIRA_SEC_PASSWORD = 'password'

UPDATES_SEC = 'UPDATES'
UPDATES_CHECK = 'startupCheck'


class ConfigSettings:
    def __init__(self, config_location):
        self.config = configparser.ConfigParser()
        self.config_location = config_location
        if config_location.exists():
            self.config.read(config_location)
        else:
            self._save_config()

    def jira_configured(self):
        js = self.config.has_section(JIRA_SEC)
        if js:
            js_sec = self.config[JIRA_SEC]
            return js_sec.get(JIRA_SEC_SERVER) and js_sec.get(JIRA_SEC_USERNAME) and js_sec.get(JIRA_SEC_PASSWORD)
        else:
            return False

    def save_configuration(self, jira_server, jira_username, jira_password, updates_check):
        self.config[JIRA_SEC] = {
            JIRA_SEC_SERVER: jira_server,
            JIRA_SEC_USERNAME: jira_username,
            JIRA_SEC_PASSWORD: jira_password
        }
        self.config[UPDATES_SEC] = {
            UPDATES_CHECK: updates_check
        }
        self._save_config()

    def load_jira_configuration(self):
        if self.config.has_section(JIRA_SEC):
            js_sec = self.config[JIRA_SEC]
            return js_sec.get(JIRA_SEC_SERVER), js_sec.get(JIRA_SEC_USERNAME), js_sec.get(JIRA_SEC_PASSWORD)
        else:
            return "", "", ""

    def load_updates_configuration(self):
        if self.config.has_section(UPDATES_SEC):
            up_sec = self.config[UPDATES_SEC]
            return str_to_bool(up_sec.get(UPDATES_CHECK))
        else:
            return True

    def _save_config(self):
        with self.config_location.open('w') as fp:
            self.config.write(fp)


def create_or_open():
    config_location = app_dir.joinpath("config.ini")
    return ConfigSettings(config_location)


config_settings = create_or_open()

