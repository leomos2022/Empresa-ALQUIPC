# La Empresa ALQUIPC desea que se le realice el programa de Facturación de sus servicios prestados

# alquipc_logic.py

TARIFA_DIARIA_POR_EQUIPO = 35000
MINIMO_EQUIPOS = 2
INCREMENTO_FUERA_CIUDAD_PCT = 0.05  # 5%
DESCUENTO_EN_ESTABLECIMIENTO_PCT = 0.05 # 5%
DESCUENTO_DIA_ADICIONAL_PCT = 0.02 # 2%

def validar_entradas(num_equipos, dias_iniciales):
    """Valida las entradas básicas según las reglas."""
    if not isinstance(num_equipos, int) or not isinstance(dias_iniciales, int):
        raise TypeError("Número de equipos y días deben ser enteros.")
    if num_equipos < MINIMO_EQUIPOS:
        raise ValueError(f"Se requiere un mínimo de {MINIMO_EQUIPOS} equipos.")
    if dias_iniciales <= 0:
        raise ValueError("El número de días iniciales debe ser positivo.")
    # Podrían añadirse más validaciones (ej. días adicionales >= 0)
    return True

def calcular_costo_alquiler(num_equipos, dias_iniciales, dias_adicionales=0, opcion_alquiler="Dentro Ciudad"):
    """
    Calcula el costo total del alquiler según las reglas de ALQUIPC.

    Args:
        num_equipos (int): Número de equipos a alquilar.
        dias_iniciales (int): Número de días iniciales.
        dias_adicionales (int): Número de días adicionales (default 0).
        opcion_alquiler (str): "Dentro Ciudad", "Fuera Ciudad", "Dentro Establecimiento".

    Returns:
        float: El costo total calculado.
        str: Descripción del ajuste aplicado (incremento/descuento).
        float: Porcentaje de ajuste aplicado (0 si no aplica).
    """
    try:
        validar_entradas(num_equipos, dias_iniciales)
        if not isinstance(dias_adicionales, int) or dias_adicionales < 0:
            raise ValueError("Los días adicionales deben ser un entero no negativo.")
    except (TypeError, ValueError) as e:
        # En una app real, manejaríamos esto más elegantemente.
        # Para las pruebas, podemos dejar que la excepción se propague o retornar None/Error.
        print(f"Error de validación: {e}")
        # O podríamos retornar un valor indicativo de error, ej:
        # return None, "Error de validación", 0.0
        # Por simplicidad aquí, dejamos que la excepción detenga el flujo si ocurre en pruebas.
        raise # Vuelve a lanzar la excepción para que pytest la capture si es necesario probarla

    total_dias = dias_iniciales + dias_adicionales
    costo_base = num_equipos * total_dias * TARIFA_DIARIA_POR_EQUIPO

    costo_final = costo_base
    ajuste_desc = "Sin ajuste"
    ajuste_pct = 0.0

    # 1. Ajuste por opción de alquiler
    if opcion_alquiler == "Fuera Ciudad":
        incremento = costo_base * INCREMENTO_FUERA_CIUDAD_PCT
        costo_final += incremento
        ajuste_desc = "Incremento Domicilio"
        ajuste_pct = INCREMENTO_FUERA_CIUDAD_PCT
    elif opcion_alquiler == "Dentro Establecimiento":
        descuento_est = costo_base * DESCUENTO_EN_ESTABLECIMIENTO_PCT
        costo_final -= descuento_est
        ajuste_desc = "Descuento Establecimiento"
        ajuste_pct = -DESCUENTO_EN_ESTABLECIMIENTO_PCT # Negativo para descuento

    # 2. Descuento por días adicionales (Aplicado sobre el costo ya ajustado por ubicación?)
    #    La especificación no es 100% clara aquí. Asumiremos que se aplica sobre el costo *antes* del descuento adicional.
    #    Interpretación: 2% por cada día adicional sobre el costo base de esos días adicionales? O sobre el total?
    #    Vamos a implementar una interpretación simple: 2% por día adicional sobre el costo total *antes* de este descuento.
    #    ¡ESTO ES ALGO QUE SE IDENTIFICARÍA COMO AMBIGÜEDAD EN EL ANÁLISIS DE REQUISITOS!
    if dias_adicionales > 0:
        # Interpretación: Descuento aplicable al costo *antes* de este paso
        costo_antes_desc_adic = costo_final
        # Calcular descuento total por días adicionales
        descuento_total_adic_pct = dias_adicionales * DESCUENTO_DIA_ADICIONAL_PCT
        descuento_adic_valor = costo_antes_desc_adic * descuento_total_adic_pct

        # Aplicar descuento
        costo_final -= descuento_adic_valor

        # Actualizar descripción (podría combinarse si ya había otro ajuste)
        # Para simplificar, solo mostraremos el último ajuste significativo o el % total.
        # Aquí es mejor devolver el desglose completo en una estructura más compleja,
        # pero para este ejemplo, devolveremos el costo final y asumimos que
        # la descripción del ajuste principal (ubicación) es suficiente + el total.
        # O podríamos añadir al string:
        if ajuste_desc != "Sin ajuste":
             ajuste_desc += f" y Descuento Adicional"
        else:
             ajuste_desc = "Descuento Días Adicionales"
        # El % de ajuste se vuelve más complejo de representar como un solo número aquí.
        # Quizás mejor retornar un desglose: (costo_final, desc_ubicacion_pct, desc_adic_pct_total)
        # Por simplicidad en este taller básico, nos quedamos con la 1ra implementación.
        # -> REVERTIR A DEVOLVER SOLO EL COSTO FINAL PARA SIMPLIFICAR PRUEBAS <-
        # (Refactorización basada en complejidad de pruebas)

    # Versión simplificada que devuelve solo el costo para facilitar las pruebas unitarias iniciales:
    costo_final_simplificado = costo_base
    if opcion_alquiler == "Fuera Ciudad":
        costo_final_simplificado += costo_base * INCREMENTO_FUERA_CIUDAD_PCT
    elif opcion_alquiler == "Dentro Establecimiento":
        costo_final_simplificado -= costo_base * DESCUENTO_EN_ESTABLECIMIENTO_PCT

    if dias_adicionales > 0:
        # Aplicar descuento sobre el costo ya ajustado por ubicación
        descuento_total_adic_pct = dias_adicionales * DESCUENTO_DIA_ADICIONAL_PCT
        costo_final_simplificado -= costo_final_simplificado * descuento_total_adic_pct

    # Devolvemos solo el costo final para este ejemplo
    return round(costo_final_simplificado, 2) # Redondeo a 2 decimales por ser dinero


def generar_resumen_email(num_equipos, dias_iniciales, dias_adicionales, opcion_alquiler, costo_total):
    """Genera el texto del resumen para el email (simulado)."""
    resumen = f"--- Resumen Alquiler ALQUIPC ---\n"
    resumen += f"Opción Alquiler: {opcion_alquiler}\n"
    resumen += f"Equipos Alquilados: {num_equipos}\n"
    resumen += f"Días Iniciales: {dias_iniciales}\n"
    resumen += f"Días Adicionales: {dias_adicionales}\n"
    # Incluir detalles de descuento/incremento requeriría que calcular_costo_alquiler los devuelva
    # O volver a calcularlos aquí (menos eficiente)
    # Por simplicidad basada en el refactor anterior:
    resumen += f"Descuentos/Incrementos: Aplicados según opción y días adic.\n"
    resumen += f"VALOR TOTAL A CANCELAR: ${costo_total:,.2f}\n" # Formato de moneda
    resumen += f"---------------------------------\n"
    # Simula que no hay opción de imprimir
    resumen += "(Información generada para envío por email. ALQUIPC apoya el reciclaje de papel.)"
    return resumen