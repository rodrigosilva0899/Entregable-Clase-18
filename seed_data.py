from MVT.models import Familiar

Familiar(nombre="Tomas", direccion="Libertador 4200", numero_dni=41300100, nacimiento=str("1993-04-14")).save()
Familiar(nombre="Nicolas", direccion="Libertador 4300", numero_dni=42000399, nacimiento=str("1998-05-17")).save()
Familiar(nombre="Santiago", direccion="Libertador 4400", numero_dni=20393844, nacimiento=str("1968-06-29")).save()

print("Se cargo con éxito los usuarios de pruebas")