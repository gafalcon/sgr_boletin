
with open("template.html", "r") as template:
    template = template.read()

print(template)


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
    with open(html_file, "r") as f:
        contenido = f.read()
    return contenido

def crear_infograma(map_file, infograma_file):
    style, map_div, script = get_map(map_file)

    template = leer_html_file("template.html")
    titulo = leer_html_file("titulo.html")
    detalles = leer_html_file("detalles.html")
    clima = leer_html_file("clima.html")
    recomendaciones = leer_html_file("recomendaciones.html")

    template = template.format(stilo_mapa=style,
                               mapa=map_div,
                               script_mapa=script,
                               titulo=titulo,
                               detalles=detalles,
                               recomendaciones=recomendaciones,
                               clima=clima
                               )

    with open(infograma_file, "w") as f:
        f.write(template)
    return template
