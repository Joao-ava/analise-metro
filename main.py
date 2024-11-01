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

print(matriz.symetry_closure)

matriz2 = Matrix(3, 3, [
    0, 2, -2,
    -2, 0, 3,
    2, -3, 0
])

#print(matriz2.asymmetric)      

#print(matriz2.antisymmetric) 
