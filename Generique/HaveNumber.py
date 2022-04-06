def haveNum(message: str = "Nombre(str) = ") -> str:
    """
    Permet d'obtenir un str qui est un nombre.
    :param message: intitulé de question
    :return:
    """
    val = ""
    while not (val.isnumeric()):
        val = input(message)
    return val


def haveInteger(message: str = "Nombre(int) = ") -> int:
    """
    Permet d'obtenir un nombre entier.
    :param message: intitulé de question
    :return:
    """
    val, notInteger = "", True
    while notInteger:
        val = haveNum(message)
        if val.isnumeric():
            notInteger = float(int(val)) != float(val)
    return int(val)


def haveFloatant(message: str = "Nombre(float) = ") -> float:
    """
    Permet d'obtenir un nombre decimal.
    :param message: intitulé de question
    :return:
    """
    while 1:
        try:
            val: float = float(input(message))
        except ValueError:
            continue
        else:
            return val
