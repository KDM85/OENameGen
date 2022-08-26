import random


def GetName(strGender):
    """
    Returns a random Anglo-Saxon name as a string

    Parameters:
    strGender (str): Gender of the name to be generated ("M" or "F")

    Returns:
    name1 + name2F | name1 + name2F (str): Random male or female name as a string
    """
    name1List = [
        "Ælf",
        "Æsc",
        "Æðel",
        "Beadu",
        "Beald",
        "Beorht",
        "Beorn",
        "Bil",
        "Brun",
        "Cene",
        "Ceol",
        "Coen",
        "Cuþ",
        "Cyne",
        "Deor",
        "Dunn",
        "Ead",
        "Eald",
        "Ealh",
        "Eard",
        "Earn",
        "Ecg",
        "Eo",
        "Eofor",
        "Eorcen",
        "Eormen",
        "Deor",
        "Fara",
        "Folc",
        "Frea",
        "Friþ",
        "Gar",
        "Glæd",
        "God",
        "Ham",
        "Hæst",
        "Heah",
        "Heoro",
        "Here",
        "Hilde",
        "Hlud",
        "Hring",
        "Hroð",
        "Land",
        "Leode",
        "Leof",
        "Mæð",
        "Milde",
        "Oht",
        "Os",
        "Rægn",
        "Ric",
        "Sæ",
        "Stiþ",
        "Sƿið",
        "Þeode",
        "Uht",
        "Ƿað",
        "Ƿan",
        "Ƿeald",
        "Ƿeard",
        "Ƿealh",
        "Ƿil",
        "Ƿulf",
        "Ƿynn",
    ]
    name2ListMale = [
        "beald",
        "beorht",
        "beorn",
        "bord",
        "dæg",
        "friþ",
        "gang",
        "gar",
        "heah",
        "heard",
        "helm",
        "here",
        "hun",
        "lac",
        "laf",
        "mær",
        "mund",
        "noð",
        "ræd",
        "ric",
        "sige",
        "stan",
        "ƿeald",
        "ƿeard",
        "ƿig",
        "ƿine",
        "ƿulf",
    ]
    name2ListFemale = [
        "burga",
        "flæd",
        "gifu",
        "gyð",
        "hild",
        "lind",
        "run",
        "sƿið",
        "þryð",
    ]
    singleSyllable = 0
    if strGender.upper() == "M":
        singleSyllable = random.randint(0, 10)
        name1 = name1List[random.randint(0, len(name1List) - 1)]
        if singleSyllable == 0:
            # 1/10 chance of monothemetic male name
            name2M = ""
        else:
            name2M = name2ListMale[random.randint(0, len(name2ListMale) - 1)]
        return name1 + name2M
    elif strGender.upper() == "F":
        name1 = name1List[random.randint(0, len(name1List) - 1)]
        name2F = name2ListFemale[random.randint(0, len(name2ListFemale) - 1)]
        return name1 + name2F
