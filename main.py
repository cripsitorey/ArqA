def convertir(n):
    potencias = [128, 64, 32, 16, 8, 4, 2, 1]
    resultado = ""
    
    numero_temp = n

    for p in potencias:
        if numero_temp >= p:
            resultado = resultado + "1"
            numero_temp = numero_temp - p
        else:
            resultado = resultado + "0"
    
    return resultado

print("--- Conversor Decimal a Binario ---")
print("Escribe 'q' para salir")

while True:
    
    entrada = input("\nDame un numero de 0 a 99: ")
    
    if entrada == 'q':
        print("Adios.")
        break
        
    try:
        num = int(entrada)
        
        if num >= 0 and num <= 99:
            binario = convertir(num)
            print("El binario es:", binario)
        else:
            print("Error: El numero debe ser entre 0 y 99.")
            
    except:
        print("Error: Debes poner un numero valido.")