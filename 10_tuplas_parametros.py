class Persona:

	def __init__(self,edad,nombre):
		self.edad=edad
		self.nombre=nombre
		print("Se ha creado a ",self.nombre," de ",self.edad, " años")


	def hablar(self, * palabras):
		for frase in palabras:
			print(self.nombre," : ",frase)

ivan = Persona(24,"Ivan")
ivan.hablar("Hola, estoy hablando","Este soy yo")
luis = Persona(20,"luis")
luis.hablar("Hola, Soy Luis","Este soy yo")