#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    def __init__(self):
        self.rolls = []

    def rollBall(self, pinsKnocked):
        self.rolls.append(pinsKnocked)

    def score(self):
        
        result = 0
        rollIndex = 0

        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.calculateStrikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.calculateSpareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.calculateFrameScore(rollIndex)
                rollIndex += 2
        return result

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10
    
    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10
    
    def calculateStrikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def calculateSpareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 2]

    def calculateFrameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]