#Class to determine the different connection parameters needed.
class Connection:
    def __init__(self, channel, domain, system_id):
        self.channel = channel
        self.core_services_url = 'https://<url>.' + channel + '.' + domain
        self.system_id = system_id

# Sets connections for the different environments
class Connections:
    SBX1 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    SLS1 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    SLS2 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    STG1 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    STG3 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    QA10 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    QA5 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    QA5.core_services_url = "<url>"
    PRD1 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    PRD3 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")

    all_connections = []
    all_connections.append(SBX1)
    all_connections.append(SLS1)
    all_connections.append(SLS2)
    all_connections.append(STG1)
    all_connections.append(STG3)
    all_connections.append(PRD1)
    all_connections.append(PRD3)
    all_connections.append(QA10)
    all_connections.append(QA5)

    # Sets connection based off of env variable in main.py
    def get_connection(self, channel):
        matched_connection = list(
            filter(
                lambda x: x.channel == channel,
                self.all_connections))

        if len(matched_connection) == 0:
            raise ValueError(
                "Please provide the valid Env (PRD1/PRD3/SBX1/SLS1/SLS2/STG1/STG3/QA)")

        return matched_connection[0]
