#Class to determine the different connection parameters needed.
class Connection:
    def __init__(self, channel, domain, system_id):
        self.channel = channel
        self.core_services_url = 'https://<url>.' + channel + '.' + domain
        self.system_id = system_id

# Sets connections for the different environments
class Connections:
    ENV1 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    ENV2 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    ENV3 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    ENV4 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    ENV5 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    ENV6 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    ENV7 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    ENV7.core_services_url = "<url>"
    ENV8 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")
    ENV9 = Connection(
        "env",
        "<endpoint>",
        "<system_id>")

    all_connections = []
    all_connections.append(ENV1)
    all_connections.append(ENV2)
    all_connections.append(ENV3)
    all_connections.append(ENV4)
    all_connections.append(ENV5)
    all_connections.append(ENV6)
    all_connections.append(ENV7)
    all_connections.append(ENV8)
    all_connections.append(ENV9)

    # Sets connection based off of env variable in main.py
    def get_connection(self, channel):
        matched_connection = list(
            filter(
                lambda x: x.channel == channel,
                self.all_connections))

        if len(matched_connection) == 0:
            raise ValueError(
                "Please provide the valid Env (ENV1/ENV2/ENV3/ENV4/ENV5/ENV6/ENV7/ENV8/ENV9)")

        return matched_connection[0]
