def readFile(filename):
    file = open(filename, "r")

    return file.read()

def writeFile(filename, data):
    file = open(filename, "w")

    file.write(str(data))

    return readFile(filename)