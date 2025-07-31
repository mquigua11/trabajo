a=0
b=1
n=int(input("Cuantos numeros de la serie fibonacci quieres ver?: "))
print("Serie Fibonacci: ")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
