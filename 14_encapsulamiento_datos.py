class Persona:

	def __init__(self,edad,nombre):
		self.edad = edad
		self.nombre = nombre
		print("Se ha creado a ",self.nombre," de ",self.edad," años.")

	def hablar(self, *palabras):
		for frase in palabras:
			print(self.nombre," : ",frase)

#utilizamos herencia para crear una clase deportista

class Deportista(Persona):

	#Sobreescritura de metodos

	def __init__(self,edad,nombre,deporte):
		self.edad = edad
		self.nombre = nombre
		self.__deporte = deporte
		print("Se ha creado a ",self.nombre," de ",self.edad," años.")

	def practicarDeporte(self):
		print(self.nombre," : voy a practicar");

	#Método publico que accede a la variable encapsulada 
	def verMideporte(self):
		return self.__deporte;

luis = Persona(30,"Luis")
luis.hablar("Hola, estoy hablando","Este soy yo")
ivan = Deportista(24,"Ivan","Taekwondo")
ivan.hablar("Hola, estoy hablando","Este soy yo")
ivan.practicarDeporte()
	#se llama al metodo el cual accede a la variable encapsulada.
print("Ivan practica ",ivan.verMideporte())