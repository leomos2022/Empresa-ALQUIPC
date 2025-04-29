# test_alquipc.py

import pytest # Importar pytest
from alquipc_logic import ( # Importar funciones y constantes del módulo a probar
    calcular_costo_alquiler,
    generar_resumen_email,
    validar_entradas,
    MINIMO_EQUIPOS,
    TARIFA_DIARIA_POR_EQUIPO
)

# --- Pruebas para validar_entradas ---

def test_validar_entradas_correctas():
    """Verifica que entradas válidas pasan la validación."""
    assert validar_entradas(num_equipos=3, dias_iniciales=5) == True

def test_validar_entradas_menos_equipos_falla():
    """Verifica que falla si se alquilan menos equipos del mínimo."""
    with pytest.raises(ValueError, match=f"Se requiere un mínimo de {MINIMO_EQUIPOS} equipos"):
        validar_entradas(num_equipos=1, dias_iniciales=5)

def test_validar_entradas_dias_cero_falla():
    """Verifica que falla si los días iniciales son cero."""
    with pytest.raises(ValueError, match="El número de días iniciales debe ser positivo"):
        validar_entradas(num_equipos=2, dias_iniciales=0)

def test_validar_entradas_dias_negativos_falla():
    """Verifica que falla si los días iniciales son negativos."""
    with pytest.raises(ValueError, match="El número de días iniciales debe ser positivo"):
        validar_entradas(num_equipos=2, dias_iniciales=-3)

def test_validar_entradas_tipo_incorrecto_falla():
    """Verifica que falla si las entradas no son enteros."""
    with pytest.raises(TypeError):
        validar_entradas(num_equipos="dos", dias_iniciales=5)
    with pytest.raises(TypeError):
        validar_entradas(num_equipos=2, dias_iniciales=5.5)

# --- Pruebas para calcular_costo_alquiler ---

# Casos base (Dentro Ciudad, sin días adicionales)
def test_costo_dentro_ciudad_base():
    equipos = 2
    dias = 3
    costo_esperado = equipos * dias * TARIFA_DIARIA_POR_EQUIPO
    assert calcular_costo_alquiler(equipos, dias, opcion_alquiler="Dentro Ciudad") == costo_esperado

# Casos con incremento (Fuera Ciudad)
def test_costo_fuera_ciudad():
    equipos = 3
    dias = 4
    costo_base = equipos * dias * TARIFA_DIARIA_POR_EQUIPO
    costo_esperado = costo_base * (1 + 0.05)
    assert calcular_costo_alquiler(equipos, dias, opcion_alquiler="Fuera Ciudad") == round(costo_esperado, 2)

# Casos con descuento (Dentro Establecimiento)
def test_costo_dentro_establecimiento():
    equipos = 4
    dias = 2
    costo_base = equipos * dias * TARIFA_DIARIA_POR_EQUIPO
    costo_esperado = costo_base * (1 - 0.05)
    assert calcular_costo_alquiler(equipos, dias, opcion_alquiler="Dentro Establecimiento") == round(costo_esperado, 2)

# Casos con días adicionales (Asumiendo Dentro Ciudad para aislar efecto adicional)
def test_costo_dias_adicionales():
    equipos = 2
    dias_ini = 3
    dias_adic = 2
    total_dias = dias_ini + dias_adic
    costo_base = equipos * total_dias * TARIFA_DIARIA_POR_EQUIPO
    # Descuento: 2% por cada día adicional, aplicado sobre costo base
    descuento_pct_total = dias_adic * 0.02
    costo_esperado = costo_base * (1 - descuento_pct_total)
    assert calcular_costo_alquiler(equipos, dias_ini, dias_adic, opcion_alquiler="Dentro Ciudad") == round(costo_esperado, 2)

# Caso complejo: Fuera Ciudad + Días Adicionales
def test_costo_fuera_ciudad_con_dias_adicionales():
    equipos = 3
    dias_ini = 2
    dias_adic = 1
    total_dias = dias_ini + dias_adic
    costo_base = equipos * total_dias * TARIFA_DIARIA_POR_EQUIPO
    # 1. Incremento por ubicación
    costo_con_incremento = costo_base * (1 + 0.05)
    # 2. Descuento por días adicionales (aplicado sobre el costo ya incrementado)
    descuento_pct_total = dias_adic * 0.02
    costo_esperado = costo_con_incremento * (1 - descuento_pct_total)
    assert calcular_costo_alquiler(equipos, dias_ini, dias_adic, opcion_alquiler="Fuera Ciudad") == round(costo_esperado, 2)

# Caso complejo: Dentro Establecimiento + Días Adicionales
def test_costo_dentro_establecimiento_con_dias_adicionales():
    equipos = 5
    dias_ini = 4
    dias_adic = 3
    total_dias = dias_ini + dias_adic
    costo_base = equipos * total_dias * TARIFA_DIARIA_POR_EQUIPO
    # 1. Descuento por ubicación
    costo_con_descuento_est = costo_base * (1 - 0.05)
    # 2. Descuento por días adicionales (aplicado sobre el costo ya descontado)
    descuento_pct_total = dias_adic * 0.02
    costo_esperado = costo_con_descuento_est * (1 - descuento_pct_total)
    assert calcular_costo_alquiler(equipos, dias_ini, dias_adic, opcion_alquiler="Dentro Establecimiento") == round(costo_esperado, 2)

# Prueba para entradas inválidas que deben ser capturadas por la función
def test_costo_entradas_invalidas_menos_equipos():
     with pytest.raises(ValueError):
        calcular_costo_alquiler(num_equipos=1, dias_iniciales=5)

def test_costo_entradas_invalidas_dias_adicionales_negativos():
    with pytest.raises(ValueError):
        calcular_costo_alquiler(num_equipos=2, dias_iniciales=5, dias_adicionales=-1)

# --- Pruebas para generar_resumen_email ---

def test_generar_resumen_formato_basico():
    resumen = generar_resumen_email(2, 3, 1, "Fuera Ciudad", 317520.00)
    assert "--- Resumen Alquiler ALQUIPC ---" in resumen
    assert "Opción Alquiler: Fuera Ciudad" in resumen
    assert "Equipos Alquilados: 2" in resumen
    assert "Días Iniciales: 3" in resumen
    assert "Días Adicionales: 1" in resumen
    # Verificar formato de moneda y texto final
    assert "VALOR TOTAL A CANCELAR: $317,520.00" in resumen
    assert "(Información generada para envío por email. ALQUIPC apoya el reciclaje de papel.)" in resumen
    # Verificar que NO contiene "Imprimir"
    assert "Imprimir" not in resumen