# SENA AA2 - Taller Pruebas de Software ALQUIPC (Adaptación Python/Pytest)

## 1. Contexto del Proyecto

Este repositorio contiene la adaptación del taller práctico "Prueba de Software I" correspondiente a la Actividad de Aprendizaje 2 (AA2) del programa de formación **"Aplicación de la calidad del software en el proceso de desarrollo"** del SENA (Colombia).

La actividad original proponía realizar pruebas manuales sobre un archivo ejecutable (`.exe`) que simulaba el software de facturación de la empresa ALQUIPC. Debido a la **incompatibilidad de ejecutar archivos `.exe` en mi entorno macOS**, este taller fue adaptado para cumplir los objetivos de aprendizaje mediante:

1.  **Implementación de la lógica de negocio** de ALQUIPC en **Python**.
2.  Desarrollo de **pruebas automatizadas (unitarias y de integración)** utilizando el framework **`pytest`**.
3.  Ejecución y análisis de resultados de pruebas en **Visual Studio Code**.
4.  **Visualización** de los resultados de las pruebas.

El objetivo principal sigue siendo aplicar y demostrar conocimientos sobre calidad de software, estándares de medición y técnicas de prueba, pero a través de un enfoque de pruebas automatizadas.

## 2. Descripción del Proyecto

El código en este repositorio implementa las reglas de negocio especificadas para el sistema de facturación de alquiler de equipos de cómputo de **ALQUIPC**. Incluye:

*   Un módulo Python (`alquipc_logic.py`) con funciones para:
    *   Validar las entradas (mínimo de equipos, días positivos).
    *   Calcular el costo total del alquiler aplicando tarifas, incrementos por ubicación (+5% fuera ciudad), descuentos por ubicación (-5% en establecimiento) y descuentos por días adicionales (2% por día).
    *   Generar un resumen de la facturación (simulando la salida para email, sin opción de impresión).
*   Una suite de pruebas automatizadas (`test_alquipc.py`) utilizando `pytest` para verificar:
    *   El correcto funcionamiento de las validaciones.
    *   La exactitud de los cálculos de costos bajo diferentes escenarios.
    *   El formato y contenido del resumen generado.
*   Un script (`generate_plot.py`) para visualizar el resumen de los resultados de las pruebas usando `matplotlib` y `seaborn`.

## 3. Requisitos Originales (Resumen ALQUIPC)

*   Servicio: Alquiler de portátiles por días.
*   Tarifa: $35.000 por día por equipo.
*   Mínimo: 2 equipos por alquiler.
*   Opciones de Alquiler:
    *   Dentro de la ciudad (base).
    *   Fuera de la ciudad (+5% incremento por domicilio).
    *   Dentro del establecimiento (-5% descuento).
*   Días Adicionales: Descuento del 2% por cada día adicional (interpretación aplicada: sobre costo total ajustado por ubicación).
*   Salida: Resumen de datos (Opción, #Equipos, #Días, #Días Adic., Desc/Incr, Total) para enviar por email, **sin opción de impresión**.
*   Id-Cliente: Debe ser asignado (aunque su implementación no fue el foco principal de la *lógica* de cálculo probada aquí).

## 4. Tecnologías Utilizadas

*   **Lenguaje:** Python 3.x
*   **Framework de Pruebas:** pytest
*   **Librerías Adicionales:**
    *   pandas (para manejo de datos, usado en script de gráficos)
    *   matplotlib (para generación de gráficos)
    *   seaborn (para estética de gráficos)
*   **Entorno de Desarrollo:** Visual Studio Code
*   **Sistema Operativo (Desarrollo/Prueba):** macOS

## 5. Estructura del Proyecto
## 6. Configuración del Entorno

Para ejecutar este proyecto localmente, sigue estos pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL-del-repositorio>
    cd <nombre-del-directorio-clonado>
    ```

2.  **Verificar instalación de Python 3:**
    Asegúrate de tener Python 3 instalado. Puedes verificarlo con:
    ```bash
    python3 --version
    ```

3.  **(Recomendado) Crear y activar un entorno virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En macOS/Linux
    # o venv\Scripts\activate   # En Windows
    ```

4.  **Instalar las dependencias:**
    ```bash
    pip3 install pytest pandas matplotlib seaborn
    ```
    *(Opcionalmente, podrías crear un archivo `requirements.txt` con estas dependencias y luego instalar con `pip3 install -r requirements.txt`)*

## 7. Uso

### Ejecución de Pruebas

Para ejecutar la suite de pruebas automatizadas, navega hasta el directorio raíz del proyecto en tu terminal (asegúrate de que el entorno virtual esté activado si creaste uno) y ejecuta:

```bash
pytest -v
pytest descubrirá y ejecutará todas las pruebas en test_alquipc.py.
La opción -v mostrará un resultado detallado para cada prueba (PASS o FAIL).
Generación de Gráfico de Resultados
Para generar el gráfico de pastel que resume los resultados de las pruebas (basado en los datos codificados en el script), ejecuta:
python3 generate_plot.py
Esto creará (o sobrescribirá) el archivo test_results_pie_chart.png en el directorio actual.
8. Resultados de las Pruebas
Al ejecutar la suite de pruebas (pytest -v) en la versión actual del código:
Total Pruebas Ejecutadas: 14
Pruebas Exitosas (PASS): 14
Pruebas Fallidas (FAIL): 0
Esto indica que la implementación actual de la lógica en alquipc_logic.py cumple con todos los casos de prueba definidos en test_alquipc.py.
Visualización:
![alt text](test_results_pie_chart.png)
(El gráfico muestra un 100% de pruebas exitosas)
9. Contexto Original del Taller
Este trabajo se realizó como parte de la Actividad de Aprendizaje 2 (AA2) del programa de formación "Aplicación de la calidad del software en el proceso de desarrollo" del Servicio Nacional de Aprendizaje (SENA), Colombia.
10. Autor
[Tu Nombre Completo Aquí]
11. Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo LICENSE (si decides añadir uno) para más detalles.
