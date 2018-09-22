class Persona:

	def __init__(self,edad,nombre):
		self.edad=edad
		self.nombre=nombre
		print("Se ha creado a ",self.nombre," de ",self.edad, " años")


	def hablar(self, ** palabras):
		for frase in palabras:
			print(self.nombre," : ",palabras[frase])

ivan = Persona(24,"Ivan")
ivan.hablar(t1="Hola, estoy hablando",t2="Este soy yo")
luis = Persona(20,"luis")
luis.hablar(t1="Hola, Soy Luis",t2="Este soy yo")