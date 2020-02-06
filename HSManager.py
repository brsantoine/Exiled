from Score import *

class HSManager:
    def __init__(self):

        self.scoreList = []

        self.update()

    def getStrings(self):

        self.update()

        stringsList = []
        for score in self.scoreList:
            stringsList.append(score.getPrintStrings())

        return stringsList

    def addScore(self, score):

        self.update

        newList = []

        winnersList = []
        loosersList = []

        for scoreElem in self.scoreList:
            if scoreElem.win == 0:
                loosersList.append((scoreElem.time, scoreElem.playerName))
            else:
                winnersList.append((scoreElem.time, scoreElem.playerName))

        winnersCount = len(winnersList)
        loosersCount = len(loosersList)

        if score.win == 0:
            loosersList.append((score.time, score.playerName))
            loosersCount += 1
        else:
            winnersList.append((score.time, score.playerName))
            winnersCount += 1

        winnersList = sorted(winnersList, key=lambda scoreTuple: scoreTuple[0])
        loosersList = sorted(loosersList, key=lambda scoreTuple: scoreTuple[0])

        i = 1

        while i <= 10 and i <= (winnersCount + loosersCount):
            if i - 1 < winnersCount:
                newList.append(Score(1, winnersList[i - 1][0], winnersList[i - 1][1]))
            else:
                newList.append(Score(0, loosersList[i - winnersCount - 1][0], loosersList[i - winnersCount - 1][1]))
            i += 1

        file = open('highScores.score', 'w')

        for newScoreElem in newList:
            file.write(newScoreElem.getFileString() + '\n')
        file.write('#')
        file.close()

    def update(self):
        self.scoreList = []
        
        try:
            file = open('highScores.score')
            file.close()
        except FileNotFoundError as ex:
            file = open('highScores.score', 'w+')
            file.write('#')
            file.close()

        file = open('highScores.score')

        readingScores = True

        while readingScores:

            line = file.readline().replace('\n', '')

            if not line:
                readingScores = False
            else:
                if line[0] == '#':
                    readingScores = False
                else:
                    newScore = Score()
                    newScore.getFromString(line)
                    self.scoreList.append(newScore)
                    
        file.close()