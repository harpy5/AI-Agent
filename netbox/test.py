from netbox_tools import connect_to_server, get_device_info_by_name, get_device_by_role
from pyats_tools import show_interface_info_tor

if __name__ == "__main__":
  print(get_device_by_role("netinfra-tor-pe"))
