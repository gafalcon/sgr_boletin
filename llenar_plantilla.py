

def get_map(filename):
    with open(filename, "r") as html_file:
        line = ""
        while line.find("<style>") == -1:
            line = html_file.readline()
        style = line
        while line.strip() != "</style>":
            line = html_file.readline()
            style += line
        div = ""
        while div.find("</div>") == -1:
            div = html_file.readline()
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
    style, map_div, script = get_map(map_file)

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

m = folium.Map(
    location=[-0.107, -77.54],
    height=400,
    zoom_start=8
)
m.save("mapa.html")

crear_infograma("mapa.html", "infograma.html")
