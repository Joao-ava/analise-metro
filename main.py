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