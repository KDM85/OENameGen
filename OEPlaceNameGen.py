import random


def GetPlaceName() -> str:
    """
    Returns a random Anglo-Saxon place name as a string

    Parameters:
    None

    Returns:
    pName1[random.randint(0, len(pName1) - 1)]
        + pName2[random.randint(0, len(pName2) - 1)] (str):
    Random place name as a string
    """
    pName1 = [
        "Anne",
        "Ansetl",
        "Æppel",
        "Æsc",
        "Bagga",
        "Beofor",
        "Blæc",
        "Bliþa",
        "Brad",
        "Bucc",
        "Cocc",
        "Craƿe",
        "Ea",
        "East",
        "Fearn",
        "Fugol",
        "Geoc",
        "Heg",
        "Hamel",
        "Hara",
        "Heorht",
        "Hoh",
        "Hryðer",
        "Hƿit",
        "Lang",
        "Leac",
        "Lind",
        "Neþer",
        "Norþ",
        "Preost",
        "Rum",
        "Ryge",
        "Sand",
        "Scir",
        "Suþ",
        "Þorn",
        "Upp",
        "Ƿacu",
        "Ƿer",
        "Ƿest",
        "Ƿilig",
        "Ƿin",
    ]
    pName2 = [
        "burh",
        "burna",
        "dæl",
        "denu",
        "dun",
        "ea",
        "eg",
        "feld",
        "ford",
        "halh",
        "ham",
        "leah",
        "tun",
        "ƿell",
        "ƿic",
        "ƿorþ",
        "ƿudu",
    ]
    return (
        pName1[random.randint(0, len(pName1) - 1)]
        + pName2[random.randint(0, len(pName2) - 1)]
    )
