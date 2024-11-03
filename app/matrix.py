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
        if self.rows != self.cols:
            return False
        return len(self.reflective_closure) == 0
    
    @property
    def symmetry(self):
        return len(self.symetry_closure) == 0
    
    @property
    def reflective_closure(self):        
        positions = []  
        
        for i in range(1,self.rows+1):
            if self.get(i,i) != 1:
                positions.append([i,i])

        return positions
    
    @property
    def symetry_closure(self):
        matriz_transposta = LinearAlgebra.transpose(self)

        positions = []

        for i in range(1,self.rows+1):
            for j in range(1,self.cols+1):
                if self.get(i,j) != matriz_transposta.get(i,j):
                    positions.append([i,j])
                
        return positions
    
    @property
    def asymmetric(self):
        if self.rows != self.cols:
            return False

        return len(self.asymmetric_closure) == 0
    
    @property
    def antisymmetric(self):
        if self.rows != self.cols:
            return False

        return len(self.antisymmetric_closure) == 0
    
    @property
    def asymmetric_closure(self):
        positions = []
        for i in range(1, self.rows + 1):
            if self.get(i, i) != 0:
                positions.append([i, i])
            for j in range(1, self.cols + 1):
                if i != j and self.get(i, j) == self.get(j, i):
                    positions.append([i, j])

        return positions
    
    @property
    def antisymmetric_closure(self):
        if self.rows != self.cols:
            return []

        positions = []
        for i in range(1, self.rows + 1):
            for j in range(i + 1, self.cols + 1):
                if i != j and self.get(i, j) == self.get(j, i):
                    positions.append([i, j])

        return positions

class LinearAlgebra:
    @staticmethod
    def transpose(a):
        """
        Retorna a matriz ou vetor transposto.

        :param a: A matriz ou vetor a ser transposto.
        :return: Uma matriz ou vetor transposto.
        """
        if isinstance(a, Matrix):
            # Se 'a' for uma matriz
            transposed_elements = []
            for j in range(1, a.cols + 1):
                column = []
                for i in range(1, a.rows + 1):
                    column.append(a.get(i, j))
                transposed_elements.extend(column)
            return Matrix(a.cols, a.rows, transposed_elements)
        
        raise ValueError("O parâmetro 'a' deve ser uma matriz ou um vetor.")