# Práctoca 6, Calculadora
# Jesús Preciado

# 4 Opreación básicas (+ - * /)

# Variable Global

r = 0
# n1 = 0
# n2 = 0

def suma(n1,n2):
    print("Suma de 2 numeros")
    print("La suma de " + str(n1) + " + " + str(n2) + " es igual a: ")
    r=n1+n2
    print("La suma es: " + str(r))
    
def resta(n1,n2):
    print("Resta de 2 numeros ")
    print("La Resta de: " + str(n1) + " - " + str(n2) + " es igual a: ")
    r=n1-n2
    print("" + str(r))
    
    
# Arranque
    
suma(1,2)
resta(1,2)
