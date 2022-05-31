def a_add(a,b):
    """
    Add two numbers
    """
    try:
        return int(a) + int(b)
    except:
        return "Error: Please check the inputs"


def a_sub(a,b):
    """
    Subtract two numbers
    """
    try:
        return int(a) - int(b)
    except:
        return "Error: Please check the inputs"

