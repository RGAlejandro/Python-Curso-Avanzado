mi_set = set([1,2,3,4,(1,2,3),1,1,1,1]) #Los sets permiten tuples ya que son inmutables. Lo que se repita se elimina
print(mi_set)

otro_set = {1,2,3}
print(otro_set)
print(2 in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)
s1.remove(4)
print(s1)

s1.discard(6)
s1.pop()#Elimina un elemente aleatorio

s1.clear() #Vacia el set entero