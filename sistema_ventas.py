cliente = input("Ingrese el nombre del cliente: ")
cantidad_libros = int(input("Ingrese la cantidad de libros comprados: "))
precio_unitario = float(input("Ingrese el precio unitario del libro: "))

subtotal_bruto = cantidad_libros * precio_unitario

descuento_aplicado = 0.0
if subtotal_bruto > 80000:
    descuento_aplicado = subtotal_bruto * 0.15

subtotal_con_descuento = subtotal_bruto - descuento_aplicado
iva_19 = subtotal_con_descuento * 0.19
total_final = subtotal_con_descuento + iva_19

print("\n" + "="*40)
print("        DETALLE DE LA COMPRA - LIBRERÍA        ")
print("="*40)
print(f"Cliente: {cliente}")
print(f"Cantidad de libros: {cantidad_libros}")
print(f"Precio Unitario: ${precio_unitario:,.0f}")
print("-"*40)
print(f"Subtotal Bruto: ${subtotal_bruto:,.0f}")
print(f"Descuento Aplicado (15%): -${descuento_aplicado:,.0f}")
print(f"IVA (19%): ${iva_19:,.0f}")
print("-"*40)
print(f"TOTAL FINAL A PAGAR: ${total_final:,.0f}")
print("="*40)