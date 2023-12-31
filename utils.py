def GetEdges(fileName="./labirinti/Trees/tree1.txt"):
    file = open(fileName, "r")
    lines = file.readlines()
    file.close()

    indexOfEdges = lines.index("EDGES:\n")
    indexOfRoot = lines.index("TERMINALS:\n")

    edgesTxtList = lines[indexOfEdges + 1 : indexOfRoot]

    edgesList = [
        tuple(map(int, edgeTxt.strip().split(" "))) for edgeTxt in edgesTxtList
    ]

    return edgesList


def GetTerminals(fileName="./labirinti/Trees/tree1.txt"):
    file = open(fileName, "r")
    lines = file.readlines()
    file.close()

    indexOfTerminals = lines.index("TERMINALS:\n")

    terminalsTxtList = lines[indexOfTerminals + 1]
    terminalsList = [
        int(terminalTxt.strip()) for terminalTxt in terminalsTxtList.split()
    ]

    return terminalsList
