# IPv4 Binary Converter
#Step 1: Read user input and echo back the IP address

ip_address = input("Enter an IPv4 address:")
print("You Entered:", ip_address)


#Step 2: Split the IP address into its four octets
octets = ip_address.split(".")


#Step 3: Convert each octet from decimal to binary
binary_octets = []
for octet in octets:
    binary_octet = format(int(octet), '08b')
    binary_octets.append(binary_octet)


#Step 4: Join the binary octets into a single string
binary_ip = ".".join(binary_octets)
#Step 5: Print the binary representation of the IP address
print("Binary Representation:", binary_ip)