import unittest
from app.matrix import Matrix


class TestMatrix(unittest.TestCase):
    def test_create(self):
        elements = [
            1, 0, 0,
            2, 1, 0,
            3, 2, 1,
            4, 3, 2
        ]
        matrix = Matrix(4, 3, elements)
        self.assertEqual(matrix.rows, 4)
        self.assertEqual(matrix.cols, 3)
        self.assertSequenceEqual(matrix.elements, elements)

    def test_get(self):
        elements = [
            4, 5, 6,
            2, 1, 0,
            3, 2, 1
        ]
        matrix = Matrix(3, 3, elements)
        self.assertEqual(matrix.get(1, 1), 4)
        self.assertEqual(matrix.get(1, 2), 5)
        self.assertEqual(matrix.get(1, 3), 6)

        self.assertEqual(matrix.get(2, 1), 2)
        self.assertEqual(matrix.get(2, 2), 1)
        self.assertEqual(matrix.get(2, 3), 0)

        self.assertEqual(matrix.get(3, 1), 3)
        self.assertEqual(matrix.get(3, 2), 2)
        self.assertEqual(matrix.get(3, 3), 1)

        
        elements = [
            4, 5, 6,
            3, 2, 1
        ]
        matrix = Matrix(2, 3, elements)
        self.assertEqual(matrix.get(1, 1), 4)
        self.assertEqual(matrix.get(1, 2), 5)
        self.assertEqual(matrix.get(1, 3), 6)

        self.assertEqual(matrix.get(2, 1), 3)
        self.assertEqual(matrix.get(2, 2), 2)
        self.assertEqual(matrix.get(2, 3), 1)

    def test_set(self):
        elements = [
            1, 0, 0,
            2, 1, 0,
            3, 2, 1
        ]
        matrix = Matrix(3, 3, elements)
        self.assertEqual(matrix.get(1, 1), 1)
        matrix.set(1, 1, 2)
        self.assertEqual(matrix.get(1, 1), 2)

    def test_diagonal(self):
        matrix = Matrix(2, 3, [
            1, 0, 0,
            2, 1, 0
        ])
        self.assertEqual(matrix.reflective, False)

        matrix = Matrix(2, 3, [
            1, 0, 0,
            2, 1, 0,
            3, 2, 1
        ])
        self.assertEqual(matrix.reflective, True)

        matrix = Matrix(2, 3, [
            1, 0, 0,
            2, 0, 0,
            3, 2, 1
        ])
        self.assertEqual(matrix.reflective, False)

        matrix = Matrix(2, 3, [
            0, 1, 1,
            2, 0, 1,
            3, 2, 0
        ])
        self.assertEqual(matrix.reflective, False)


if __name__ == '__main__':
    unittest.main()
