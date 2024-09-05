import random

# Generar 1000 números aleatorios entre 1 y 1000 y escribirlos en un archivo
with open("nprimos.txt", "w") as file:
    for _ in range(1000):
        num = random.randint(1, 1000)
        file.write(f"{num}\n")
