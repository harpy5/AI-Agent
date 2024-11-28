from dotenv import load_dotenv
import os
load_dotenv()
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
from netbox_tools import connect_to_server, get_device_info_by_name, get_device_by_role
from pyats_tools import show_interface_info_tor

NETBOX_API_URL = os.getenv('NETBOX_API_URL')
NETBOX_API_TOKEN = os.getenv('NETBOX_API_TOKEN')

get_device_by_role_tool = FunctionTool.from_defaults(fn=get_device_by_role)
tor_interfaces_tool = FunctionTool.from_defaults(fn=show_interface_info_tor)
ConnectToServer_tool = FunctionTool.from_defaults(fn=connect_to_server)
GetdeviceIP_tool = FunctionTool.from_defaults(fn=get_device_info_by_name)

def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    return a * b


multiply_tool = FunctionTool.from_defaults(fn=multiply)


def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b


add_tool = FunctionTool.from_defaults(fn=add)

llm = OpenAI(model="gpt-4o", temperature=0)

agent = ReActAgent.from_tools([multiply_tool, add_tool, GetdeviceIP_tool, tor_interfaces_tool, get_device_by_role_tool], llm=llm, verbose=True)

response = agent.chat("Find the devices with the netinfra-tor and find the status of the interfaces of those devices")

print(response)