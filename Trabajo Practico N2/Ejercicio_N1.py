def mayor_estricto(a, b, c):
    if a > b:
        if a > c:
            if b != a and c != a:  
                return a
    if b > a:
        if b > c:
            if a != b and c != b:  
                return b
    if c > a:
        if c > b:
            if a != c and b != c:  
                return c
    return None  

a = float(input("Ingrese el primer numero : "))
b = float(input("Ingrese el segundo numero : "))
c = float(input("Ingrese el tercer numero: "))

max = mayor_estricto(a, b, c)

if max is not None:
    print(f"El mayor estricto es: {max}")
else:
    print("No existe un mayor estricto.")
