# Used for network-related operations but not used in this exemple
import socket
import time
import random

def create_firewall_rules():
  """Defines a set of firewall rules. You can customize these rules as needed.
  Returns a dictionary where keys are IP addresses or ports, and values are booleans indicating allowed traffic."""
  # Creates a dictionary to store firewall rules.
  firewall_rules = {
    "192.168.1.100": True,  # Allow traffic from IP 192.168.1.100
    "80": True,             # Allow traffic on port 80 (HTTP)
    "443": True             # Allow traffic on port 443 (HTTPS)
  }
  return firewall_rules


def check_firewall(ip_address, port):
  """Checks if traffic is allowed based on firewall rules.
  Args:
    ip_address: The IP address of the incoming traffic.
    port: The port number of the incoming traffic.
  Returns:
    True if traffic is allowed, False otherwise."""
  firewall_rules = create_firewall_rules()
  # This part checks if the ip_address exists as a key in the firewall_rules dictionary.
  # If the IP address is found as a key, this part evaluates to True. Otherwise, it's False.
  # Assuming the first condition is True (the IP address is a key), this part accesses the value associated with that IP address in the dictionary.
  # Since firewall rules are represented as boolean values (True for allowed, False for blocked), this part essentially checks if the value for that IP address is True.
  if ip_address in firewall_rules and firewall_rules[ip_address]:
    return True
  if str(port) in firewall_rules and firewall_rules[str(port)]:
    return True
  return False

def simulate_network_traffic():
  """Simulates network traffic and applies firewall rules."""
  while True:
    # Generate a random IP address and port to simulate incoming traffic
    ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))
    port = random.randint(1, 65535)

    if check_firewall(ip_address, port):
      print(f"Allowing traffic from {ip_address} on port {port}")
    else:
      print(f"Blocking traffic from {ip_address} on port {port}")
    time.sleep(1)  # Make a delay between traffic checks

if __name__ == "__main__":
  simulate_network_traffic()
