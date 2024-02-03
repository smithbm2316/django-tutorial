from nanoid import generate

def nanoid():
    """Generate a nanoid with our custom alphabet

    Returns:
        a new nanoid
    """
    return generate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz', 12)
