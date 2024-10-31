class Matrix:
    def __init__(self, linha, coluna, matrizelementos):
        self.rows = linha
        self.cols = coluna
        self.matrix = []
        for i in range(linha):
            linha_da_matriz = []
            for j in range(coluna):
                elemento = matrizelementos[i * coluna + j]
                linha_da_matriz.append(elemento)

            self.matrix.append(linha_da_matriz)

    def get(self, i, j):
        return self.matrix[i - 1][j - 1]

    def set(self, i, j, value):
        if i < 1 or i > self.rows:
            raise Exception('Essa matriz não possui a linha ' + str(i))
        if j < 1 or j > self.cols:
            raise Exception('Essa matriz não possui a coluna ' + str(j))

        self.matrix[i-1][j-1] = value

    @property
    def elements(self):
        elements = []
        for row in self.matrix:
            for item in row:
                elements.append(item)
        return elements

    def __str__(self):
        max_elements_size = max([len(str(item)) for item in self.elements])
        content = ''
        content += ('-' * max_elements_size * self.cols) + '---' * self.cols
        content += '\n'
        for row in self.matrix:
            content += '|'
            content += ' | '.join([f'{item:<{max_elements_size}}' for item in row])
            content += '|\n'

        content += ('-' * max_elements_size * self.cols) + '---' * self.cols
        return content

    @property
    def reflective(self):
        return False
