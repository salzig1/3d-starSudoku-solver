import unittest

from sudokuSolver import sudoku


class SudokuTest(unittest.TestCase):
    def test_sudoku1(self):
        # Sudoku: https://www.anypuzzle.com/puzzles/logic/3D%20Sudoku/Sudoku%203D%20Star%20puzzle.pdf
        # Lösung: https://www.anypuzzle.com/puzzles/logic/3D%20Sudoku/3D%20Sudoku%20Star%20solution.pdf
        board = [[3, 0, 0, 0, 0, 2, 0, 0, 8, 0, 0, 0, 0, 0, 3, 0],
                 [0, 0, 0, 6, 8, 0, 0, 1, 7, 0, 0, 0, 0, 4, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 5, 3, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 5, 0, 1, 0, 0, 0, 0, 2, 0, 0],
                 [0, 0, 0, 0, 8, 2, 4, 0, 0, 0, 0, 0, 0, 6, 0, 0],
                 [8, 0, 0, 6, 0, 3, 0, 0, 2, 6, 3, 0, 0, 7, 0, 0]]
        solution = [[3, 7, 1, 8, 4, 2, 6, 5, 8, 1, 2, 4, 6, 5, 3, 7],
                 [5, 2, 4, 6, 8, 3, 7, 1, 7, 6, 3, 5, 1, 4, 2, 8],
                 [2, 5, 7, 1, 6, 8, 3, 4, 7, 4, 8, 5, 3, 1, 6, 2],
                 [7, 4, 2, 3, 6, 8, 5, 1, 1, 5, 7, 8, 3, 2, 6, 4],
                 [5, 3, 2, 7, 8, 2, 4, 6, 4, 7, 1, 8, 1, 6, 5, 3],
                 [8, 1, 4, 6, 5, 3, 1, 7, 2, 6, 3, 5, 4, 7, 8, 2]]
        solvedBoard = sudoku.solve(board)
        self.assertEqual(solvedBoard, solution)


    def test_sudoku2(self):
        # Sudoku + Lösung: https://www.raetselfactory.ch/tredoku.htm
        board = [[0, 0, 0, 0, 0, 5, 1, 0, 0, 0, 0, 2, 0, 0, 3, 0],
                 [7, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 4, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 6],
                 [0, 0, 2, 6, 7, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [3, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 2, 0],
                 [4, 0, 0, 0, 0, 2, 0, 0, 0, 3, 1, 0, 1, 8, 5, 0]]
        solution = [[3, 4, 6, 8, 2, 5, 1, 7, 6, 7, 5, 2, 8, 1, 3, 4],
                 [7, 1, 2, 5, 6, 4, 3, 8, 8, 3, 1, 4, 5, 2, 6, 7],
                 [1, 7, 5, 4, 6, 2, 3, 8, 8, 4, 7, 2, 5, 3, 1, 6],
                 [3, 1, 2, 6, 7, 5, 4, 8, 8, 6, 7, 5, 2, 4, 3, 1],
                 [3, 5, 8, 1, 7, 1, 4, 5, 2, 8, 6, 7, 4, 6, 2, 3],
                 [4, 7, 6, 2, 6, 2, 8, 3, 5, 3, 1, 4, 1, 8, 5, 7]]
        solvedBoard = sudoku.solve(board)
        self.assertEqual(solvedBoard, solution)


    def test_sudoku3(self):
        # Sudoku: http://www.clarity-media.co.uk/puzzleblog/3d-sudoku-snowflake-star
        board = [[7, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 6, 1, 4, 7, 0, 2, 0, 0, 0, 0, 0, 8, 1],
                 [8, 0, 0, 0, 0, 0, 0, 0, 3, 5, 0, 0, 0, 0, 6, 7],
                 [0, 0, 0, 0, 0, 0, 0, 4, 5, 0, 7, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 4, 6, 0, 8, 0, 5, 6, 0, 0, 1],
                 [0, 2, 0, 0, 0, 0, 0, 7, 3, 0, 0, 0, 0, 0, 0, 0]]
        solution = [[7, 3, 4, 1, 5, 6, 2, 8, 1, 8, 7, 3, 2, 4, 6, 5],
                 [5, 8, 2, 6, 1, 4, 7, 3, 2, 6, 5, 4, 7, 3, 8, 1],
                 [8, 6, 3, 4, 1, 7, 5, 2, 3, 5, 1, 8, 4, 2, 6, 7],
                 [2, 7, 5, 8, 6, 3, 1, 4, 5, 1, 7, 2, 4, 8, 6, 3],
                 [5, 4, 7, 3, 2, 1, 4, 6, 7, 8, 2, 5, 6, 3, 8, 1],
                 [1, 2, 8, 6, 8, 5, 3, 7, 3, 6, 4, 1, 7, 4, 2, 5]]
        solvedBoard = sudoku.solve(board)
        self.assertEqual(solvedBoard, solution)


if __name__ == '__main__':
    unittest.main()