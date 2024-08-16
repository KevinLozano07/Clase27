opciones = {
    "izquierda": "Te haz topado con un dragon!",
    "derecha": "Te haz topado con un tesoro!",
    "delante": "Haz caido en un pozo!",
}

Frase = """
Te topaste con tres caminos distintos.
Uno que guia hacia la derecha, otro 
hacia la izquierday otro que te guia 
hacia delante.

¿Cual camino deberias tomar?

""" 

decision = input(Frase).lower()

print("-" * 30)

print("")
print("Tomaste el camino que te guia hacia:", decision)
print("")

if decision in opciones:
    print("Vaya!", opciones[decision])
    print("")
else:
    print("Esta no es una decision valida")
    print("")
    print("") 