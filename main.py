from connections import *
from core_calls import *
import sys

env = '<env>' #sys.argv[1]

connection = Connections()
connection = connection.get_connection(env)
core_services_url = connection.core_services_url
system_id = connection.system_id

user = ''
password = ''


core_calls = CoreCalls(core_services_url, system_id, user, password)

core_calls.execute_validation()

