from abc import ABCMeta,abstractmethod
class Persona:
	__metaclass__=ABCMeta


	def __init__(self,edad,nombre):
		self.edad = edad
		self.nombre = nombre
		print("Se ha creado a ",self.nombre," de ",self.edad," años.")

	@abstractmethod
	def hablar(self): pass
		

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

	def verMiDeporte(self):
		return self.__deporte;

	def hablar(self,*palabras):
		for frase in palabras:
			print(self.nombre,":",frase)

ivan = Deportista(24,"Ivan","Taekwondo")
ivan.hablar("Hola, estoy hablando","Este soy yo")
ivan.practicarDeporte()
print("Ivan practica ",ivan.verMiDeporte())