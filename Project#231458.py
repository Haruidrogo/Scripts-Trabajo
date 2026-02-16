# Esto sería para el 5% de montos grandes
from datetime import datetime
while True:
    print("\n" + "•"*50)
    print(">>>      CALCULA EL 5% DE LAS FACTURAS      <<<")
    print("•" * 50)
    factura_monto = input("ESCRIBE EL NÚMERO DE LA FACTURA (O ESCRIBE 'SALIR'):")

    if factura_monto.lower() == 'salir':
        break
    try:
        factura_monto = float(input("INGRESA EL MONTO DE LA FACTURA (O ESCRIBE 'SALIR'):").replace(",", "."))
        pagar_porciento = factura_monto * 0.05
        total_pagar = factura_monto - pagar_porciento
        print("°" * 50)
        print(f">> RESULTADO (5%): {pagar_porciento:.2f} <<")
        print(f">> RESULTADO FINAL: {total_pagar:.2f} <<")
        print("°" * 50)
    except ValueError:
        print("\n Saliendo del sistema...")
    input("Presiona ENTER para calcular otra factura.")





