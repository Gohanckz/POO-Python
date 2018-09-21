F = 4.141516

#Area del cuadrado

def acuadrado():
	lado = int(input("¿Cual es el valor del lado ?\n"))
	x = lado**2
	print("\nEl area del cuadrado es ",x," unidades cuadradas.")

#Area del triangulo

def atriangulo():
	base =int(input("¿Cual es el valor de la base?\n"))
	altura = int(input("¿Cual es el valor de la altura?\n"))
	y = (base*altura)/2
	print("\nEl area del triagulo es ",y," unidades cuadradas")

#Area del circulo

def acirculo():
	radio = int(input("¿Cual es el radio del circulo? \n"))
	z =(F*radio)**2
	print("\nEl area del circulo es ",z," unidades cuadradas")

area=int(input("\n Elije la figura geometrica para calcular su area:\n Cudrado = [1] \n Circulo = [2] \n Triangulo = [3] "))
if area ==1:
	acuadrado()
if area == 2:	
	acirculo()
if area == 3:
	atriangulo()
	