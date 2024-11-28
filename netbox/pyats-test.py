#from pyats.topology import loader
from genie import testbed
from pprint import pprint

#testbed = loader.load('testbed.yaml')

testbed= testbed.load('testbed.yaml')

iosxr1 = testbed.devices["sandbox-iosxr-1.cisco.com"]

iosxr1.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)

show_interface = iosxr1.parse('show interfaces description')

pprint(show_interface)
#print(show_interface['interface']['MgmtEth0/RP0/CPU0/0']['ip_address'])
"""interface_list = []
for interface in show_interface['interface']:
    print(f"{interface} -- {show_interface['interface'][interface]['ip_address']} -- {show_interface['interface'][interface]['interface_status']}")
    interface_list.append(f"{interface} -- {show_interface['interface'][interface]['ip_address']} -- {show_interface['interface'][interface]['interface_status']}")

print(interface_list)
#print(show_interface)
"""

iosxr1.disconnect()
