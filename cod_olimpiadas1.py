def suma(a,b):
  x=a+b
  return x

def resta(a,b):
  x= a - b
  return x

print("Dame el priemr numero:")
a=int(input())
print("Dame el segundo numero:")
b= int(input())
print("La suma da", suma(a,b), "y la resta da", resta(a,b))



def multiplicacion(a,b):
  x= a*b
  return x
  
def division(a,b):
  x= a/b
  return x

print("Dame tu primer numero")
a= int(input())
print("Dame tu segundo numero")
b= int(input())
print("el resultado de la multiplicacion es:", multiplicacion(a,b))
print("el resultado de tu division es:", division(a,b))
