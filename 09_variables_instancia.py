class Persona:
	def __init__(self,edad,nombre):
		self.edad=edad
		self.nombre=nombre
		print("Se ha creado a ",self.nombre," de ",self.edad, " años")


	def hablar(self,palabras):
		print(self.nombre," : ",palabras)

ivan = Persona(24,"Ivan")
ivan.hablar("Hola, estoy hablando")
luis = Persona(20,"luis")
luis.hablar("Hola, Soy Luis")