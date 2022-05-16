def media():
    x1, price1, x2, price2 = 126, 200, 79, 100

    mean = (x1 * price1 + x2 * price2) / (x1 + x2)

    print(mean)


def media_stdev_varcoef():
    x1 = 5
    sallary_list1 = [2536, 2137, 2448, 2121, 2622]
    mean_sallary1 = sum(sallary_list1) / x1

    numerator = 0

    for sallary in sallary_list1:
        dif = sallary - mean_sallary1
        numerator += (abs(dif)) ** 2

    stddev1 = (numerator / x1) ** 0.5
    varcoef1 = stddev1 / mean_sallary1

    x2 = 6
    mean_sallary2 = 2550
    stddev2 = 250
    varcoef2 = stddev2 / mean_sallary2

    print(f"Medias Salarios Buenos Aires({mean_sallary1}) y Córdoba({mean_sallary2})")
    print(f"Desvio Estándar Salarios Buenos Aires({stddev1}) y Córdoba({stddev2})")
    print(f"Coeficiente de Variación Buenos aires({varcoef1}) y Córdoba({varcoef2}) ")


def Condicional(n):
    def difference(n):
        if n < 17:
            return 17 - n
        else:
            return 2 * abs(n - 17)

    print(difference(n))


def near_thousand(n):
    return True if n >= 100 and n <= 1000 else False


def suma_tres(n1, n2, n3):
    sum = n1 + n2 + n3

    if n1 == n2 and n2 == n3:
        return 3 * sum
    else:
        return sum


def cuenta_cuatro(num_list):
    return num_list.count(4)


def check(n, n_list):
    if n in n_list:
        return True
    else:
        n_list.append(n)
        return n_list


def concat_string(string_list):
    return ''.join(string_list)


def stop_248(num_list):
    new_num_list = []

    for num in num_list:
        if num % 2 == 0 and num != 248:
            new_num_list.append(num)
    return new_num_list

def repetidos(num_list):

   check = False

   for num in num_list:
        if num_list.count(num) >= 2:
            check = True

   return check


def primos(num):
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):
        if num%n==0:
            return False
    return True


def unicos(input_list):
    resultado = []

    for i in range(len(input_list)):
        if input_list[i+1:].count(input_list[i]) == 0:
            resultado.append(input_list[i])
    return resultado


def lista_de_unicos(input_list):
    input_list.sort()
    resultado = []

    for i in range(len(input_list)):
        if input_list[i+1:].count(input_list[i]) == 0:
            resultado.append(input_list[i])
    return resultado


def cuadrados():
    square_list = []

    for i in range(1, 31, 1):
        square_list.append(i ** 2)

    return square_list


def impares(n):
  return [i for i in range(0, n, 1) if i%2 != 0]


if __name__ == '__main__':
    # Ejercicio1
    print("Ejercicio 1:")
    media()
    # Ejercicio2: Ninguna de las anteriores
    # Ejercicio3: La Moda sirve para variables Categoricas y Cuantitativas
    # Ejercicio4: La mediana puede cambiar si se modifica el orden de las observaciones.
    # Ejercicio5: Boxplot -> Mediana y Cuartiles
    # Ejercicio6: Si por error de carga se incluye un dato con valor 100000 en una muestra con rango de 1 a 10, entonces el desvío estándar, se  modifica fuertemente
    # Ejercicio7:
    print("Ejercicio 7:")
    media_stdev_varcoef()
    # Ejercicio8 En una distribución en la que hay valores extremos en la cola izquierda: La mediana es mayor que la media y menor que la moda.
    # Ejercicio9
    print("Ejercicio 9:")
    Condicional(19)
    # Ejercicio10
    print("Ejercicio 10")
    n = 200
    print(f"if {n} near thousand {near_thousand(n)}")
    # Ejercicio11
    print("Ejercicio 11")
    print(suma_tres(4, 4, 4))
    # Ejercicio12
    print("Ejercicio 12")
    print(cuenta_cuatro([4, 2, 4, 5, 6, 7, 8, 10, 4]))
    print("Ejercicio 13")
    print(check(4, [3, 2, 5]))
    print("Ejercicio 14")
    print(concat_string(["dsadasd", "Hello", "World"]))
    print("Ejercicio 15")
    print(stop_248([1,2,4,248,9,10]))
    print("Ejercicio 16")
    print(repetidos([1, 2, 3, 4, 2]))
    print("Ejercicio 17")
    print(primos(11))
    print("Ejercicio 18")
    print(unicos([1, 3, 4 ,2, 4, 5, 3, 12]))
    print("Ejercicio 19")
    print(lista_de_unicos([1, 3, 4 ,2, 4, 5, 3, 12]))
    print("Ejercicio 20")
    print(cuadrados())
    print("Ejercicio 21")
    print(impares(21))