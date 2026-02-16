import os
import pandas as pd
from datetime import datetime

archivo_nombre = "Registro_Ventas.csv"

def generar_resumen():
    if os.path.exists(archivo_nombre):
        try:
            df = pd.read_csv(archivo_nombre, sep=';', decimal=',', encoding="utf-8-sig")
            df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')
            hoy = pd.Timestamp(datetime.now().date())
            ventas_hoy = df[df['Fecha'] == hoy]
            
            if not ventas_hoy.empty:
                print("\n" + "═"*50)
                print(f"📊 PARA EL CIERRE DE CAJA - {datetime.now().strftime('%d/%m/%Y')}")
                print(f"✅ Ventas hoy:          {len(ventas_hoy)}")
                print(f"💰 Total Ventas:        ${ventas_hoy['Total ($)'].sum():.2f}")
                print(f"📈 Ganancia Neta:       ${ventas_hoy['Ganancia ($)'].sum():.2f}")
                print("═"*50)
        except:
            print("Esperando primer registro para el resumen...")

# --- BUCLE PRINCIPAL ---
while True:
    print("\n" + "•"*50)
    print("            CALCULADORA DAVITECH V7.0")
    print("•"*50)

    nombre_repuesto = input("Nombre del repuesto (o escribe 'salir'): ")
    if nombre_repuesto.lower() == 'salir':
        break  # Rompe el bucle y sale del programa

    try:
        tasa_bcv = float(input("1. TASA BCV (Bs/$): ").replace(",", "."))
        costo_bs_inicial = float(input("2. COSTO DEL REPUESTO (Bs): ").replace(",", "."))

        # Lógica de cascada (Mi fórmula secreta)
        usd_base = costo_bs_inicial / tasa_bcv 
        usd_con_iva = usd_base * 0.16
        subtotal_iva = usd_base + usd_con_iva 
        usd_con_ganancia = subtotal_iva * 0.25
        subtotal_ganancia = subtotal_iva + usd_con_ganancia
        monto_riesgo = subtotal_ganancia * 0.05
        precio_final_usd = subtotal_ganancia + monto_riesgo
        precio_final_bs = precio_final_usd * tasa_bcv 

        print("-" * 40)
        print(f">> BASE:            ${usd_base:.2f} <<")
        print(f">> IVA (16%):       ${usd_con_iva:.2f} <<")
        print(f">> GANANCIA (25%):  ${usd_con_ganancia:.2f} <<")
        print(f">> PRECIO FINAL:    ${precio_final_usd:.2f} <<")
        print(f">> PRECIO EN BS:    Bs.{precio_final_bs:.2f} <<")
        print("-" * 40)

        # Guardar datos
        archivo_existe = os.path.isfile(archivo_nombre)
        fecha_hoy = datetime.now().strftime("%d/%m/%Y")
        
        with open(archivo_nombre, "a", encoding="utf-8-sig") as archivo:
            if not archivo_existe:
                archivo.write("Fecha;Repuesto;Tasa BCV;Costo Base ($);IVA ($);Ganancia ($);Total ($)\n")
            
            def to_ex(num): return str(round(num, 2)).replace('.', ',')
            
            datos = (f"{fecha_hoy};{nombre_repuesto};{to_ex(tasa_bcv)};"
                     f"{to_ex(usd_base)};{to_ex(usd_con_iva)};"
                     f"{to_ex(usd_con_ganancia)};{to_ex(precio_final_usd)}\n")
            archivo.write(datos)

        # Mostrar cómo va el día después de cada venta
        generar_resumen()

    except ValueError:
        print("\n❌ ERROR: Por favor introduce números válidos.")

# Fuera del bucle (cuando escribes 'salir')
print("\nSaliendo del sistema...")

input("Presiona ENTER para cerrar definitivamente.")
