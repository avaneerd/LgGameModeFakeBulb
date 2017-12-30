import os
from lg import Remote

address = Remote.find_tvs(first_only=True)

remote = Remote(address)

remote.set_pairing_key(os.environ['LG_PAIRING_KEY'])

commands = [410, 12, 12, 20, 412]

remote.send_multiple(commands, 1)