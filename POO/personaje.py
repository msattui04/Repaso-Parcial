class Personaje:
    def __init__(self, nombre, base, id, edad, caracteristica, descendencia):
        self.nombre = nombre
        self.base = base
        self.id = id
        self.edad = edad
        self.caracteristica = caracteristica
        self.descendencia = descendencia
    
    def __str__(self):
        return f"El personaje {self.nombre} tiene {self.edad} años. Tiene descendencia {self.descendencia} y su base queda en {self.base}. Se caracteriza por ser {self.caracteristica}"

personajes = [Personaje("Eddard Stark", ["Norte"], 1, 35, ["honorable"], ["Winterfell"]), Personaje("Jon Snow", ["Norte", "Guardia de la Noche"], 4, 22, ["valiente", "misterioso"], ["Stark"])]

contador = 0
valientes = []

for personaje in personajes:
    if personaje.edad > 30:
        contador += 1

for personaje in personajes:
    if "valiente" in personaje.caracteristica:
        valientes.append(personaje.nombre)

print (contador)
print (valientes)