def agregar_bebida(entrada):
    entrada = entrada.replace(" ", "")
    entrada = entrada.split(",")
    nombre = entrada[0]
    tamanos = entrada[1:]

    if not (2 <= len(nombre) <= 15) or not nombre.isalpha():
        raise ValueError("El nombre de la bebida es inválido")

    tamanos = list(map(int, tamanos))

    if (
        len(tamanos) > 5
        or tamanos != sorted(tamanos)
        or any(tamano < 1 or tamano > 48 for tamano in tamanos)
    ):
        raise ValueError("Los tamaños de la bebida son inválidos")

    return {"nombre": nombre, "tamanos": tamanos}
