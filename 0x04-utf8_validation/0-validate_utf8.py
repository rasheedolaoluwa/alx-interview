#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Returns True if data is a valid UTF-8 encoding, else False.
    """
    # Variable for counting the number of bytes in a UTF-8 character
    number_bytes = 0

    # Masks for checking if a byte is valid (Starts with 10)
    mask1 = 1 << 7
    mask2 = 1 << 6

    for i in data:
        mask_n_byte = 1 << 7

        if number_bytes == 0:
            # Count the number of bytes the UTF-8 character will have
            while mask_n_byte & i:
                number_bytes += 1
                mask_n_byte = mask_n_byte >> 1

            # If number of bytes did not increase, it has 1 byte
            if number_bytes == 0:
                continue

            # A character in UTF-8 can be 1 to 4 bytes long
            # But 1-byte characters start with 0, so number_bytes
            # should never be 1
            if number_bytes == 1 or number_bytes > 4:
                return False
        else:
            # Every byte that is not the first byte of a character
            # should start with 10
            if not (i & mask1 and not (i & mask2)):
                return False

        # Decrease the count of bytes for the current character
        number_bytes -= 1

    # All characters were verified correctly with their proper byte count
    return number_bytes == 0
