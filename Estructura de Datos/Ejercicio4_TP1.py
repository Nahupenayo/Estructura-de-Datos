def descuentos():
    print("Descuentos por tipo de moneda:")
    print("1. Dolares: 5% de descuento")
    print("2. Yenes: 15% de descuento")
    print("3. Guaranies: 20% de descuento")
    print("4. Pesos: 10% de descuento")
    print("5. Otras monedas: 10% de incremento")

def calcular_precio(cantidad, moneda):
    precio_unitario = 1000  
    descuentos = {
        "Dolares": 0.05,
        "Yenes": 0.15,
        "Guaranies": 0.20,
        "Pesos": 0.10
    }
    incremento = 0.10  
    total = precio_unitario * cantidad

    if moneda in descuentos:
        descuento = descuentos[moneda]
        total_con_descuento = total * (1 - descuento)
        return total_con_descuento, f"{int(descuento * 100)}% de descuento"
    else:
        total_con_incremento = total * (1 + incremento)
        return total_con_incremento, f"10% de incremento"

def generar_recibo(nombre_comprador, empresa, cantidad, moneda, precio_total, detalle_descuento):
    print("\n=== RECIBO ===")
    print(f"Comprador: {nombre_comprador}")
    print(f"Empresa: {empresa}")
    print(f"Producto: Zapallo")
    print(f"Cantidad: {cantidad}")
    print(f"Moneda: {moneda.capitalize()}")
    print(f"Descuento/Incremento: {detalle_descuento}")
    print(f"Precio total: ${precio_total:.2f} pesos")
    print("-------------------")

def main():
    nombre_empresa = "ZAPALLOS NAHUEL"
    
    descuentos()
    nombre_comprador = input("\nIngrese su nombre: ")
    cantidad = int(input("Cuantos zapallos va a comprar? "))
    moneda = input("Ingrese el tipo de moneda: ").lower()
    precio_total, detalle_descuento = calcular_precio(cantidad, moneda)
    
    generar_recibo(nombre_comprador, nombre_empresa, cantidad, moneda, precio_total, detalle_descuento)
if __name__ == "__main__":
    main()
