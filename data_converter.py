def bytes_to_kilobytes(byte_value):
    """
    Convert bytes to kilobytes.

    Parameters:
    - byte_value (int or float): The size in bytes to convert.

    Returns:
    - float: The size in kilobytes.
    """
    if not isinstance(byte_value, (int, float)):
        raise TypeError("Input must be a number.")
    if byte_value < 0:
        raise ValueError("Bytes cannot be negative.")
    
    return byte_value / 1024
