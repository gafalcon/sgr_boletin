import folium
import requests

URL_SERVIDOR = "http://192.188.159.28:81"
URL_SERVIDOR = "http://127.0.0.1:3000"
def consultar_evento(id_evento):
    res = requests.get(URL_SERVIDOR+"/evento/{}".format(id_evento))
    return res.json()

def consultar_temperatura(lat, lon):
    res = requests.get(URL_SERVIDOR+"/temperatura?lat={}&lon={}".format(lat, lon))
    return res.json()

def consultar_ids():
    """Retorna lista con ids de todos los eventos registrados en la base de datos"""
    res = requests.get(URL_SERVIDOR+"/evento")
    return res.json()

def consultar_todos():
    """
    Retorna una lista de listas con la informacion de todos los eventos registrados en la base de datos
    """
    res = requests.get(URL_SERVIDOR+"/all")
    return res.json()


def leer_folium_map(filename):
    """
    Lee archivo html con el codigo de un mapa creado utilizando folium.
    Retorna las diferentes secciones necesarias para poder insertar el mapa en la plantilla html
    """
    with open(filename, "r") as html_file:
        line = ""
        # Extraer stilo del mapa
        while line.find("<style>") == -1:
            line = html_file.readline()
        style = line
        while line.strip() != "</style>":
            line = html_file.readline()
            style += line
        # Extraer div del mapa
        div = ""
        while div.find("</div>") == -1:
            div = html_file.readline()
        # Extraer script del mapa
        script = ""
        while script.find("<script>") == -1:
            script = html_file.readline()
        script += html_file.read()
    return style, div, script


def leer_html_file(html_file):
    """Devuelve un str con todo el contenido del archivo"""
    with open(html_file, "r") as f:
        contenido = f.read()
    return contenido

def crear_infograma(map_file, infograma_file):
    """
    Crea boletin html a partir de plantilla
    map_file: archivo html con un mapa generado
    infograma_file: archivo html donde crear boletin
    """
    style, map_div, script = leer_folium_map(map_file)

    template = leer_html_file("plantilla.html")
    titulo = leer_html_file("titulo.html")
    detalles = leer_html_file("detalles.html")
    clima = leer_html_file("clima.html")
    recomendaciones = leer_html_file("recomendaciones.html")

    template = template.format(estilo_mapa=style,
                               seccion1=titulo,
                               seccion2=map_div,
                               script_mapa=script,
                               seccion3=detalles,
                               seccion4=clima,
                               seccion5="",
                               seccion6=recomendaciones,
                               )

    with open(infograma_file, "w") as f:
        f.write(template)

def nuevo_evento(id_evento):
    # TODO implementar
    return ""



m = folium.Map(
    location=[-0.107, -77.54],
    height=400,
    zoom_start=8
)
m.save("mapa.html")

crear_infograma("mapa.html", "infograma.html")
