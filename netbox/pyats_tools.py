from genie import testbed
from pprint import pprint

testbed= testbed.load('testbed.yaml')

def show_interface_info_tor(name:str) -> list:
    """This function takes the device name as input and returns the info about the interfaces such as interface names, ip address, status of interfaces
    
    param: name
    return: list of Interfaces
    """

    iosxr1 = testbed.devices[name]
    iosxr1.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)

    show_interface = iosxr1.parse('show ip interface brief')

    #print(show_interface['interface']['MgmtEth0/RP0/CPU0/0']['ip_address'])
    interface_list = []
    for interface in show_interface['interface']:
        #print(f"{interface} -- {show_interface['interface'][interface]['ip_address']} -- {show_interface['interface'][interface]['interface_status']}")
        interface_list.append(f"{interface} -- {show_interface['interface'][interface]['ip_address']} -- {show_interface['interface'][interface]['interface_status']}")

    iosxr1.disconnect()
    #print(show_interface)
    return interface_list
    
