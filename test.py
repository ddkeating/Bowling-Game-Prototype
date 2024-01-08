#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):
    """Test cases for the bowling game class."""

    def setUp(self):
        """Setup the BowlingGame instance for each test."""
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        """Test a game where no pins are knocked down."""
        self.rollMany(0, 20)
        assert self.game.score() == 0

    def testAllOnes(self):
        """Test a game with all rolls being 1."""
        self.rollMany(1, 20)
        assert self.game.score() == 20

    def testOneSpare(self):
        """Test a game with only one spare."""
        self.game.rollBall(5)
        self.game.rollBall(5)
        self.game.rollBall(3)
        self.rollMany(0, 17)
        assert self.game.score() == 16

    def testOneStrike(self):
        """Test a game with one strike."""
        self.game.rollBall(10)
        self.game.rollBall(4)
        self.game.rollBall(3)
        self.rollMany(0, 17)
        assert self.game.score() == 24

    def testTwoStrikes(self):
        """Test a game with two strikes."""
        self.game.rollBall(10)
        self.game.rollBall(10)
        self.game.rollBall(5)
        self.game.rollBall(3)
        self.rollMany(0, 14)
        assert self.game.score() == 51

    def testPerfectGame(self):
        """Test a perfect game (all strikes)"""
        self.rollMany(10, 12)
        assert self.game.score() == 300

    def rollMany(self, pins, rolls):
        """
        Helper function to roll multiple times

        Args: 
            pins (int): Number of pins knocked down in each roll.
            rolls (int): Number of rolls to perform.
        """
        for i in range(rolls):
            self.game.rollBall(pins)