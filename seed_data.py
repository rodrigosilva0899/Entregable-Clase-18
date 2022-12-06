from MVT.models import Familiar

Familiar(nombre="Santiago", direccion="Libertador 4000", numero_dni=18400500, fecha_nacimiento='20/08/1968').save()
Familiar(nombre="Silvina", direccion="Libertador 4100", numero_dni=27200500, fecha_nacimiento='26/04/1970').save()
Familiar(nombre="Tomas", direccion="Libertador 4200", numero_dni=41300100, fecha_nacimiento='29/10/1996').save()
Familiar(nombre="Nicolas", direccion="Soldado de la Independencia 100", numero_dni=37200400, fecha_nacimiento='06/03/1991').save()

print("Se cargo con éxito los usuarios de pruebas")