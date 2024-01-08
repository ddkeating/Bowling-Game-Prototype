#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    """Class representing a ten pin bowling game"""

    def __init__(self):
        """Initialize a new list to track each bowl."""
        self.rolls = []

    def rollBall(self, pinsKnocked):
        """
        Record the number of pins knocked down in a roll and appends the value to the list.
        
        Args: 
            pinsKnocked (int): Number of pins knocked down.

        Return:
            Appends number of knocked over pins to the list.
        """
        self.rolls.append(pinsKnocked)

    def score(self):
        """
        Calculate the total score of the game.

        Returns:
            int: Total score of the game.
        """

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
        """
        Checks if is a strike.

        Args: 
            rollIndex (int): Index of the roll in the list.

        Returns:
            bool: True if the roll was a strike, otherwise False.
        """
        return self.rolls[rollIndex] == 10
    
    def isSpare(self, rollIndex):
        """
        Checks if is a spare

        Args:
            rollIndex (int): Index of the roll in the list.

        Returns:
            bool: True if the roll was a spare, other False.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10
    
    def calculateStrikeScore(self, rollIndex):
        """
        Calculate the score for a frame with a strike.

        Args:
            rollIndex (int): Index of the roll in the list.
        
        Returns:
            int: Score of the frame.
        """
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def calculateSpareScore(self, rollIndex):
        """
        Calculate the score for a frame with a spare.

        Args: 
            rollIndex (int): Index of the roll in the list.

        Returns:
            int: Score of the frame.
        """
        return 10 + self.rolls[rollIndex + 2]

    def calculateFrameScore(self, rollIndex):
        """
        Calculate the score for a regular frame.

        Args:
            rollIndex (int): Index of the roll in the list.

        Returns:
            int: Score of the frame.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]