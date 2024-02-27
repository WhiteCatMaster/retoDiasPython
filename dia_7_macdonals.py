# Programar una maquina de macdonals
def donde_comer():
    respuesta_aceptada = False
    print("donde desea tomar el pedido")
    while respuesta_aceptada == False:
        sitio_comida = input("Aqui(1)/ Para llevar(0)")
        if sitio_comida == "1":
            respuesta_aceptada = True
            return "aqui"
        elif sitio_comida == "0":
            respuesta_aceptada = True
            return "llevar"
        else:
            print("opcion no vigente, acuerdese de poner bien la respuesta")

def elegir_pedido(posible_catalogo):
    print(f"elija entre nuestras opciones {posible_catalogo.keys()}")
    eleccion_clase = input("")
    falla = True
    for clase in posible_catalogo.keys():
        if eleccion_clase == clase:
            print(f"elige producto entre {posible_catalogo[clase]}")
            producto_elegido = input("")
            for producto in posible_catalogo[clase]:
                if producto_elegido == producto:
                    print("producto añadido a la cesta correctamente")
                    falla = False
                    return producto
    if falla != False:
        print("ha ocurrido un error vuelve a intentarlo")

def pago():
    operacion_aceptada = False
    while operacion_aceptada != True:
        print("¿desea realizar el pago con tarjeta(1) o en efectivo(0)?")
        forma_pago = input("")
        if forma_pago == "1":
            print("tarjeta aceptada, tenga un buen dia")
            operacion_aceptada = True
        elif forma_pago == "0":
            print("dineron aceptado tenga un buen dia")
            operacion_aceptada = True
        else:
            print("forma de pago no encontrada, intentelo de nuevo")

def main(p_catalogo):
    donde_comer()
    lista_pedido = []
    acabar = False
    while acabar == False:
        lista_pedido.append(elegir_pedido(p_catalogo))
        acabado = input("has acabado (si/no)")
        if acabado == "si":
            acabar = True
    print(f"tu pedido es {lista_pedido}")
    pago()

if __name__ == "__main__":
    catalogo = {"hamburguesas": ["Big Mac", "Mini Mac", "Cathee Burguer", "vegetariana", "pollo"],
            "patatas": ["normales", "grandes", "con bacon", "supreme"],
            "bebidas": ["agua", "cerveza", "pepsi", "sprite", "fanta"],
            "acompañantes": ["mac-nuggets", "helado", "ensalada"]}
    main(catalogo)