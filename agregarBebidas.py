import pytest

# Run pytest agregarBebidas.py to run the tests


def agregar_bebida(entrada):
    # Eliminar espacios en blanco de la entrada
    entrada = entrada.replace(" ", "")
    # Dividir la entrada en una lista utilizando la coma como separador
    entrada = entrada.split(",")
    # El primer elemento de la lista es el nombre de la bebida
    nombre = entrada[0]
    # Los elementos restantes son los tamaños de la bebida
    tamanos = entrada[1:]

    # Verificar que el nombre cumpla con las condiciones
    if not (2 <= len(nombre) <= 15) or not nombre.isalpha():
        raise ValueError("El nombre de la bebida es inválido")

    # Convertir los tamaños a enteros
    tamanos = list(map(int, tamanos))

    # Verificar que los tamaños cumplan con las condiciones
    if (
        len(tamanos) > 5
        or tamanos != sorted(tamanos)
        or any(tamano < 1 or tamano > 48 for tamano in tamanos)
    ):
        raise ValueError("Los tamaños de la bebida son inválidos")

    # Devolver un diccionario con el nombre y los tamaños de la bebida
    return {"nombre": nombre, "tamanos": tamanos}


def test_nombre_alfabetico():
    entrada = "Coca Cola,12,24,48"
    assert agregar_bebida(entrada)["nombre"] == "CocaCola"


def test_nombre_menos_de_2_caracteres():
    entrada = "A,12,24,48"
    with pytest.raises(ValueError):
        agregar_bebida(entrada)


def test_nombre_de_2_a_15_caracteres():
    entrada = "Pepsi,12,24,48"
    assert agregar_bebida(entrada)["nombre"] == "Pepsi"


def test_valor_tamano_en_rango():
    entrada = "Sprite,1,24,48"
    assert agregar_bebida(entrada)["tamanos"] == [1, 24, 48]


def test_valor_tamano_entero():
    entrada = "Fanta,12,24,48"
    assert all(isinstance(tamano, int) for tamano in agregar_bebida(entrada)["tamanos"])


def test_valores_tamano_orden_ascendente():
    entrada = "Pepsi,12,24,48"
    tamanos = agregar_bebida(entrada)["tamanos"]
    assert tamanos == sorted(tamanos)


def test_uno_a_cinco_valores_tamano():
    entrada = "Mirinda,12,24,48"
    tamanos = agregar_bebida(entrada)["tamanos"]
    assert 1 <= len(tamanos) <= 5


def test_nombre_primero_en_entrada():
    entrada = "Coca Cola,12,24,48"
    assert agregar_bebida(entrada)["nombre"] == "CocaCola"


def test_coma_separa_entradas():
    entrada = "Coca Cola,12,24,48"
    assert agregar_bebida(entrada)["tamanos"] == [12, 24, 48]


def test_espacios_en_blanco():
    entrada = "  Coca Cola  ,  12  ,  24  ,  48  "
    assert agregar_bebida(entrada)["nombre"] == "CocaCola"
    assert agregar_bebida(entrada)["tamanos"] == [12, 24, 48]
