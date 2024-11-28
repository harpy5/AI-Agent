import pynetbox 
import urllib3
import requests
import paramiko
import time
from dotenv import load_dotenv
import os
from pprint import pprint



NETBOX_API_URL = os.getenv('NETBOX_API_URL')
NETBOX_API_TOKEN = os.getenv('NETBOX_API_TOKEN')

def connect_to_server():
    """
    Connects to Netbox server
    """
    try:
        urllib3.disable_warnings()
        session = requests.Session()
        session.verify = False
        session.timeout = None
        # netbox = pynetbox.api(
        #     NETBOX_URL,
        #     ssl_verify=False,
        #     token=NETBOX_AUTH_TOKEN
        # )
        #print(NETBOX_API_URL)
        #print(NETBOX_API_TOKEN)
        netbox = pynetbox.api(NETBOX_API_URL, token=NETBOX_API_TOKEN)
        netbox.http_session = session

        return netbox
    except Exception as err:
        print("Cannot connect to Netbox server {}\n{}".format(NETBOX_API_URL, err))
        return None

def get_device_info_by_name(name:str) ->str:
    """This function takes the name as input and gets the device IP address from the Netbox 
    
    :param name:
    :return: Primary ipv4 address
    """
    netbox=connect_to_server()
    device = netbox.dcim.devices.get(name=name)
    #pprint(dict(device))
    device1=dict(device)
    print(device1['primary_ip4']['address'])
    return device1['primary_ip4']['address']
    #print(device1['display'])

def get_device_by_role(role: str) -> list:
    """This function returns the name of the devices based on the role
    :param: role
    :return: list of devices"""

    netbox=connect_to_server()
    devices= netbox.dcim.devices.filter(role=role)
    device_list = []
    for device in devices:
        device_list.append(device)

    return device_list


