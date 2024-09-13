def calcular_vuelto(total_compra, dinero_recibido):
    if dinero_recibido < total_compra:
        return 
    vuelto = dinero_recibido - total_compra
    print(f"El vuelto es: ${vuelto}")

    billetes = [500, 100, 50, 20, 10, 5, 1]
    cantidad_billetes = {}
    for billete in billetes:
        cantidad = vuelto // billete  
        if cantidad > 0:
            cantidad_billetes[billete] = cantidad
        vuelto = vuelto % billete  
    for billete, cantidad in cantidad_billetes.items():
        print(f"{cantidad} billete de ${billete}")
    
    return cantidad_billetes
if __name__ == "__main__":
    total_compra = int(input("Ingrese el total de la compra: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))
    resultado = calcular_vuelto(total_compra, dinero_recibido)
    if isinstance(resultado, str):
        print(resultado)
