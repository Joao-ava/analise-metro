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

print(matriz)
print("Reflexiva: ", matriz.reflective)
print("linha, coluna: ", matriz.reflective_closure)
print("Simetrica: ", matriz.symmetry)
print("linha, coluna: ", matriz.symetry_closure)
print("Assimetrica: ", matriz.asymmetric)
print("linha, coluna: ", matriz.asymmetric_closure)
print("Antissimetrica", matriz.antisymmetric)
print("linha, coluna: ", matriz.antisymmetric_closure)
print("Transitiva: ", matriz.transitive)

print("Matriz de Ordem", matriz.order)
print("Matriz de equivalência", matriz.equivalence)

print("Maximais:", matriz2.maximal_elements)
print("Minimais:", matriz2.minimal_elements)

print("linha, coluna: ", matriz.transitive_closure)

print("-" * 20)

# # Definindo outra matriz
# matriz3 = Matrix(3, 3, [
#     0, 1, -1,
#     -1, 0, 0,
#     1, 0, 0
# ])

# print(matriz3)
# print("Maximais:", matriz3.maximal_elements)
# print("Minimais:", matriz3.minimal_elements)
# print(matriz3.asymmetric)
# print(matriz3.antisymmetric)
# print(matriz3.asymmetric_closure)
# print(matriz3.antisymmetric_closure)
