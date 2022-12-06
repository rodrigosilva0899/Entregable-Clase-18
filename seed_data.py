from MVT.models import Familiar

Familiar(nombre="Tomas", direccion="Libertador 4200", numero_dni=41300100).save()
Familiar(nombre="Nicolas", direccion="Libertador 4300", numero_dni=42000399).save()
Familiar(nombre="Santiago", direccion="Libertador 4400", numero_dni=20393844).save()

print("Se cargo con éxito los usuarios de pruebas")