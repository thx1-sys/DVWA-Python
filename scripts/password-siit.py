# Abre un archivo llamado "numeros.txt" en modo escritura ('w')
with open('password-sitt.txt', 'w') as f:
    # Itera sobre el rango de números del 1000 al 9999
    for i in range(1000, 10000):
        # Escribe cada número seguido de un salto de línea en el archivo
        f.write(str(i) + '\n')
