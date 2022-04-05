def haveNum(message: str = "Nombre(str) = ") -> str:
    """Permet d'obtenir un str qui est un nombre."""
    val = ""
    while not (val.isnumeric()):
        val = input(message)
    return val


def haveInteger(message: str = "Nombre(int) = ") -> int:
    """Permet d'obtenir un nombre entier."""
    val, notInteger = "", True
    while notInteger:
        val = haveNum(message)
        if val.isnumeric():
            notInteger = float(int(val)) != float(val)
    return int(val)


def haveFloatant(message: str = "Nombre(float) = ") -> float:
    """Permet d'obtenir un nombre decimal."""
    val = haveNum(message)
    return float(val)
