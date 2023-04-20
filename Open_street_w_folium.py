from flask import Flask
from flask import Flask, render_template
from folium import Map, Marker, TileLayer
import folium

app = Flask(__name__)

@app.route('/')
def mapa():
    # Crear mapa centrado en una ubicación concreta
    mapa = folium.Map(location=[-25.23695541510235, -57.567547239571], zoom_start=22)

    TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', 
              attr='Esri', 
              name='Esri World Imagery',
              overlay=True).add_to(mapa)

    # Añadir marcador a la ubicación
    folium.Marker(
        location=[-25.23695541510235, -57.567547239571], 
        popup="Mi marcador"
    ).add_to(mapa)

    # Renderizar mapa en HTML
    html_mapa = mapa._repr_html_()

    # Devolver HTML con el mapa
    return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Mapa de prueba</title>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {folium.Map().get_root().header.render()}
        </head>
        <body>
            <div>{html_mapa}</div>
        </body>
        </html>
    """

if __name__ == '__main__':
    app.run()
