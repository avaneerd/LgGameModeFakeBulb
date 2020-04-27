import os
from lg import Remote

address = os.environ['LG_IP_ADDRESS']

remote = Remote(address)

remote.set_pairing_key(os.environ['LG_PAIRING_KEY'])

commands = [410, 13, 13, 20, 412]

remote.send_multiple(commands, 1)