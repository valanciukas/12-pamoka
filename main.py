from controller import printHighscores
from controller import playGame
printHighscores()
nuo = int(input("Nuo kurio skaiciaus spesim? Kokia intervalo pradzia?"))
iki = int(input("Iki kurio skaiciaus spesim? Kokia intervalo pabaiga?"))
playGame(nuo=nuo, iki=iki)
