#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        self.rollMany(0, 20)
        assert self.game.score() == 0

    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score() == 20

    def testOneSpare(self):
        self.game.rollBall(5)
        self.game.rollBall(5)
        self.game.rollBall(3)
        self.rollMany(0, 17)
        assert self.game.score() == 16

    def testOneStrike(self):
        self.game.rollBall(10)
        self.game.rollBall(4)
        self.game.rollBall(3)
        self.rollMany(0, 17)
        assert self.game.score() == 24

    def testTwoStrikes(self):
        self.game.rollBall(10)
        self.game.rollBall(10)
        self.game.rollBall(5)
        self.game.rollBall(3)
        self.rollMany(0, 14)
        assert self.game.score() == 51

    def testPerfectGame(self):
        self.rollMany(10, 12)
        assert self.game.score() == 300

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.rollBall(pins)