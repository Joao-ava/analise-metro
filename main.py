from app.matrix import Matrix
 

matriz = Matrix(6,6,[ 
    1,1,0,0,0,0,
    1,1,1,0,0,1,
    0,0,1,0,0,0,
    0,0,0,1,0,1,
    0,0,0,1,1,1,
    0,1,0,0,1,1,
])

#print(matriz.reflective)

#print(matriz.symmetry)

#print(matriz.reflective_closure)

#print(matriz.symetry_closure)

matriz2 = Matrix(3, 3, [
    0, 1, 1,
    -1, 0, 0,
    0, 0, 0
])

print("f ou t: ", matriz2.asymmetric)      
print("f ou t: ", matriz2.antisymmetric) 
print("linha, coluna: ", matriz2.asymmetric_closure)  
print("linha, coluna: ", matriz2.antisymmetric_closure())

print("-" * 20)

# Definindo outra matriz
matriz3 = Matrix(3, 3, [
    0, 1, -1,
    -1, 0, 0,
    1, 0, 0
])

print("Maximais:", matriz3.maximal_elements)      
print("Minimais:", matriz3.minimal_elements)
print(matriz3.asymmetric)      
print(matriz3.antisymmetric) 
print(matriz3.asymmetric_closure)
print(matriz3.antisymmetric_closure()) 