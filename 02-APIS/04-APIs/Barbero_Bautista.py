import requests
import pandas as pd
from weasyprint import HTML

# Obtener datos de la API ReqRes
response = requests.get("https://reqres.in/api/users")
data = response.json()["data"]

# Procesar los datos
df = pd.DataFrame(data)

# Generar tabla HTML
html_table = df.to_html()

# Generar archivo PDF
HTML(string=html_table).write_pdf("usuarios.pdf")