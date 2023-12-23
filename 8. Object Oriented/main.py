from devices import Firewall

# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()

# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

# Create a switches instance
switches28 = Firewall("switches28")
# Verify a CRC
switches28.calculate_crc("dummy data")