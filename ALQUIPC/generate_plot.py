# generate_plot.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# --- DATOS SIMULADOS/OBTENIDOS ---
# (En un escenario real, estos datos vendrían del reporte de pytest o un log)
# Supongamos que obtuvimos estos resultados de la tabla anterior:
results = {
    'Estado': ['PASS'] * 14 # O actualizar si hubo fallos, ej: ['PASS']*13 + ['FAIL']
}
df_results = pd.DataFrame(results)

# Contar ocurrencias de cada estado
status_counts = df_results['Estado'].value_counts()

# --- GENERAR GRÁFICO ---
plt.figure(figsize=(6, 6)) # Tamaño de la figura
sns.set_style("whitegrid") # Estilo del gráfico

# Gráfico de Barras
# plt.bar(status_counts.index, status_counts.values, color=['green', 'red']) # Simple
# O un gráfico de pastel
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel", len(status_counts)))
plt.title('Resultado Ejecución Pruebas Automatizadas ALQUIPC')
plt.ylabel('') # Ocultar etiqueta Y en gráfico de pastel

# Guardar el gráfico en un archivo
plt.savefig('test_results_pie_chart.png')

print("Gráfico 'test_results_pie_chart.png' generado exitosamente.")
# plt.show() # Descomentar si quieres que se muestre la ventana del gráfico