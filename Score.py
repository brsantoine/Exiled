
class Score:
    def __init__(self, win = 0, time = 0, playerName = "Unknown"):
        
        self.win = win
        self.time = time
        self.playerName = playerName
        
    def getFileString(self):

        return str(self.win) + " ; " + str(self.time) + " ; " + self.playerName

    def getPrintStrings(self):

        if self.win == 0:
            winText = "Defeat"
        else:
            winText = "Victory"

        hours = self.time // 3600
        mins = self.time // 60 - (hours * 60)
        secs = self.time % 60

        hoursText = ""

        if hours < 9:
            hoursText += "0"

        hoursText += str(hours)

        minsText = ""

        if mins < 9:
            minsText += "0"

        minsText += str(mins)

        secsText = ""

        if secs < 9:
            secsText += "0"

        secsText += str(secs)

        return [winText, hoursText + ":" + minsText + ":" + secsText, self.playerName]

    def getFromString(self, scoreString):

        scoreList = scoreString.split(" ; ")
        self.win = int(scoreList[0])
        self.time = int(scoreList[1])
        self.playerName = scoreList[2]