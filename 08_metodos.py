class Persona:
	#self accede al resto de los metodos y atributos dentro de la clase
	def __init__(self):
		self.edad = 18
		self.nombre = "Ivan"
		print("Se ha creado a ",self.nombre," de ",self.edad)

	def hablar(self,palabras):
		print(self.nombre," : ",palabras)

#Persona()
Persona().hablar("Hola, estoy hablando")