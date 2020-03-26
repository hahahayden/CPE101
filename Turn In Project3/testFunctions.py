#Project3- Tic-Tac-Toe Simulator
#Name: Hayden Tam
#Instructor: S. Einakian
# Section: 05


import unittest
from tictactoeFuncs import *

class TestCases(unittest.TestCase):
  
   def test_checkRows(self):
        
        self.assertEqual(checkRows(["X", "X", "X"," ", " ", " ", " ", " ", " "]),(True,"X"))
        self.assertEqual(checkRows(["O", "O", "O"," ", " ", " ", " ", " ", " "]),(True,"O"))
        self.assertEqual(checkRows([" ", " ", " ","X", "X", "X", " ", " ", " "]),(True,"X"))
   def test_checkCols(self):
        self.assertEqual(checkCol(["X"," "," ","X", " ", " ","X"," ", " "]), (True,"X"))
        self.assertEqual(checkCol([" ","O"," "," ", "O", " "," ","O", " "]), (True,"O"))
        self.assertEqual(checkCol([" "," ","O"," ", " ", "O"," "," ", "O"]), (True,"O"))

   def test_checkDiag(self):
        self.assertEqual(checkDiag(["X","O","X","O", "X", "X","O","X", "X"]),(True,"X"))
        self.assertEqual(checkDiag(["X","X","O","O", "O", "X","O","X", "O"]),(True,"O"))

   def test_boardFull(self):
        self.assertEqual(boardFull(["X","X","O","O", "O", "X","O","X", "O"]),True)
        self.assertEqual(boardFull(["X","X","O","O", " ", "X","O","X", "O"]),False)
  
   def test_turnCount(self):
        self.assertEqual(turnCount("X",2,3), 4)   
        self.assertEqual(turnCount("X",2,5), 6)
   
   
   def test_createBoard(self):
        self. assertEqual(createBoard(),[" ", " ", " ", " ", " ", " ", " ", " ", " "] )
   def test_checkWin(self):
        self.assertEqual(checkWin(["X","X","O","O", "O", "X","O","X", "O"]), True) 
        self.assertEqual(checkWin(["X","X","X","O", "O", "X","O","X", "O"]), True) 

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()


