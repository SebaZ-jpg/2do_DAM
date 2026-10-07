for pedido in [30, 100, 200]:
    if pedido < 50:
        descuento = 5.95
    elif pedido < 150:
        descuento = 2.95
    else:
        descuento = 0

    total = pedido + descuento

    print(f"Pedido: {pedido:.2f}€ | Envio: {descuento}% | Total: {total:.2f}€")
