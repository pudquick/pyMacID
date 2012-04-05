# Get the Computer Name from System Preferences -> Sharing
from SystemConfiguration import SCDynamicStoreCopyComputerName
try:
    computer_name = SCDynamicStoreCopyComputerName(None, None)[0].encode('utf-8')
except:
    computer_name = None

# Get the Bonjour .local name
from socket import gethostname
try:
    bonjour_name = gethostname()
except:
    bonjour_name = None

# Get detailed hardware information
from subprocess import Popen, PIPE
from plistlib import readPlistFromString

system_profiler_xml = Popen(["/usr/sbin/system_profiler", "-xml", "SPHardwareDataType", "SPNetworkDataType"], stdout= PIPE).communicate()[0]
cpu_info, net_info = readPlistFromString(system_profiler_xml)

# System serial number
mac_serial = cpu_info._items[0].serial_number

# Machine model
mac_model = cpu_info._items[0].machine_model

# Interface names (in ifconfig), excluding localhost
net_interface_names = [interface.interface for interface in net_info._items]

# Interface names (in System Preferences -> Network)
net_interface_snames = [interface._name for interface in net_info._items]

# IPv4 addresses
net_interface_ipv4s = [interface.IPv4.Addresses[0] for interface in net_info._items]

