# Utilizada para almacenar multiples valores "valores de cualquier tipo de dato"
# son mutables = alteradas
# [1, 2, 3, 4]
# ["pedro", "maria", "rosa"]

vocales = ["a" , "e", "i", "o", "u"]
print(vocales[3])


# al final de la lista [append]
vocales.append("s")
print(vocales)


# insertar indice especifico
vocales.insert(0, "Insert.")
print(vocales)


# remover un elemento [remove]
vocales.remove("e")
print(vocales)


# encontrar un elemento [in]
# "elemento" in lista
print("z" in vocales)


# retorna el indice de un elemento .index(elemento)
# lista .index(elemento)
print(vocales.index("u"))


# Cambiar el valor de un elemento
# <Lista> [<indice>] = <nuevo valor>
edad = [1, 2, 3, 4]
print(edad)
edad[3]= 5
print(edad)

# Metodos de las listas
# <lista>.metodo(<parametro)
"""
.count = cuantas veces se repite un elemento          
.reverse = reversa los elementos de la lista
.extend = extender una lista, agregando los elementos de otra lista
.sort = ordena la lista en asc - desc
.pop = remover o retorna
"""

