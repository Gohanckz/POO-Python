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

	def practicarDeporte(self):
		print(self.nombre," : voy a practicar");

luis = Persona(30,"Luis")
luis.hablar("Hola, estoy hablando","Este soy yo")
ivan = Deportista(24,"Ivan")
ivan.hablar("Hola, estoy hablando","Este soy yo")
ivan.practicarDeporte()