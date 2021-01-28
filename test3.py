
import re

deviceConfig = open("config.txt", "r").read()
customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
customerNames = re.findall (customerNamePattern, deviceConfig)
print(customerNames)


