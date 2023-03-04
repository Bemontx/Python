# coleccion de datos = clave: valor,claves unicas e-inmutables
# diccionarios son mutables
# datos de cualquier tipo
# {"a": 1, "b": 2, "c": 3}  
# con la clave podemos acceder al valor 
# <diccionario> {<clave>: <valor>}


usuarios = {
    "Pedro": 12,
    "Maria": 32,
    "Lola": 43,
    "Fernando": 33
}

print(usuarios["Lola"])
print(usuarios["Pedro"])
print(usuarios.get("Lola"))

# Añadir y modificar
# <diccionario>[<clave>] = <nuevo_valor>
usuarios["Luis"] = 21
print(usuarios)
print(usuarios.get("Luis"))
print()

# Actualizar valor
# <diccionario>[<clave] = <nuevo_valor>
print(usuarios)
usuarios["luis"] = 18
print(usuarios)
print()

# Remover 
# del <diccionario>[<clave>]
print(usuarios)
del usuarios["luis"]
print(usuarios)
print()

# Revisar esxitencia = retorna valor booleano
# <elemento> in <diccionarion>
print("Lola" in usuarios)
print("Frank" in usuarios)


