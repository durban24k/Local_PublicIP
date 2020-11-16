import socket
from requests import get

hostname=socket.gethostname()
local_ip=socket.gethostbyname(hostname)
ip_v4_public_ip=get('https://api.ipify.org').text
ip_v6_public_ip=get('https://api64.ipify.org').text

print(f'Hostname: {hostname}')
print(f'Local IP: {local_ip}')
print(f'IPv4 Public IP: {ip_v4_public_ip}')
print(f'IPv6 Public IP: {ip_v6_public_ip}')