import random

notas = [random.randint(0, 10) for _ in range(100)]

numCeros = notas.count(0)
print("En mi lista tengo", numCeros, "ceros.")

notas = [nota for nota in notas if nota != 0]

print(len(notas), notas)
