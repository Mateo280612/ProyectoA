#Metodo de burbuja
# Un profesor requiere ordenar la lista de sus alumnos de universidad por edades de menor a mayor y nos muestre 
# sus nombres y edades de manera ordenada.
def bubble_sort(diccionario):
    items = list(diccionario.items())  # O(n)
    n = len(items)  # O(1)
    for i in range(n):  # O(n)
        for j in range(0, n-i-1):  # O(n)
            if items[j][1] > items[j+1][1]:  # O(1)
                items[j], items[j+1] = items[j+1], items[j]  # O(1)
    return items  # O(1)

diccionario_edades = {
    "Juan": 30,
    "María": 25,
    "Pedro": 35,
    "Luisa": 28
}

lista_ordenada = bubble_sort(diccionario_edades)  # O(n^2)

for nombre, edad in lista_ordenada:  # O(n)
    print(nombre, ":", edad)  # O(1)
    
#Metodo de Quicksort
def quicksort(diccionario):
    if len(diccionario) <= 1:  # O(1)
        return diccionario  # O(1)
    
    clave_pivote = next(iter(diccionario))  # O(1)
    valor_pivote = diccionario[clave_pivote]  # O(1)
    
    menores = {clave: valor for clave, valor in diccionario.items() if valor < valor_pivote}  # O(n)
    iguales = {clave: valor for clave, valor in diccionario.items() if valor == valor_pivote}  # O(n)
    mayores = {clave: valor for clave, valor in diccionario.items() if valor > valor_pivote}  # O(n)
    
    return {**quicksort(menores), **iguales, **quicksort(mayores)}  # O(n*log(n))

# Ejemplo de diccionario de edades
diccionario_edades = {
    "Juan": 30,
    "María": 25,
    "Pedro": 35,
    "Luisa": 28
}

# Ordenar el diccionario por edades usando Quicksort
diccionario_edades_ordenado = quicksort(diccionario_edades)

# Mostrar los nombres y edades ordenados
for nombre, edad in diccionario_edades_ordenado.items():
    print(f"Nombre: {nombre}, Edad: {edad}")