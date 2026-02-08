# IPv4 Binary Converter

def convert_ipv4_to_binary(ip_address):
    """
    Converts an IPv4 address from decimal dot-notation to binary representation.

    Args:
        ip_address (str): The IPv4 address in decimal dot-notation (e.g., "192.168.1.1").

    Returns:
        str: The binary representation of the IPv4 address, or an error message if invalid.
    """
    octets = ip_address.split(".")

    if len(octets) != 4:
        return "Error: Invalid IPv4 address format. Must have exactly 4 octets."

    binary_octets = []
    for octet_str in octets:
        try:
            octet = int(octet_str)
            if not (0 <= octet <= 255):
                return f"Error: Octet '{octet_str}' is out of valid range (0-255)."
            binary_octets.append(format(octet, '08b'))
        except ValueError:
            return f"Error: Octet '{octet_str}' is not a valid integer."

    return ".".join(binary_octets)

def main():
    """
    Main function to handle user interaction for IPv4 to binary conversion.
    Allows multiple conversions until the user decides to exit.
    """
    print("IPv4 Decimal to Binary Converter")
    print("Enter 'exit' or 'quit' to stop the program.")

    while True:
        ip_address_input = input("\nEnter an IPv4 address: ").strip()

        if ip_address_input.lower() in ("exit", "quit"):
            print("Exiting converter. Goodbye!")
            break

        if not ip_address_input:
            print("Error: No input provided. Please enter an IPv4 address.")
            continue

        binary_representation = convert_ipv4_to_binary(ip_address_input)
        print(f"You Entered: {ip_address_input}")
        print(f"Binary Representation: {binary_representation}")

if __name__ == "__main__":
    main()
