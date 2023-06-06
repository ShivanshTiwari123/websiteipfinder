import socket

def get_ip_address(url):
    ip_address = socket.gethostbyname(url)
    return ip_address

# Example usage
print(get_ip_address("enter the website link"))



