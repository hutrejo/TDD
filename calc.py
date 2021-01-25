import ipaddress

 

def calculator(RED,MASK):

    global PEIP

    global CEIP

    c = "0.0.0.1"

    d = "0.0.0.1"

    resta = ipaddress.IPv4Address(c)

    resta2= ipaddress.IPv4Address(d)

    net = ipaddress.IPv4Network(RED+ '/' + MASK, False)

    print (( ipaddress.IPv4Address(net.network_address + int(resta) )))

    print (( ipaddress.IPv4Address(net.network_address + int(resta) + int(resta2))))

 

calculator("10.0.0.0", "255.255.255.252")

 

###########BUG FIX

#try:

#             calculator("dasada", "255..255.255.252")

#except ipaddress.AddressValueError:

#             print("datos incorrectos")

