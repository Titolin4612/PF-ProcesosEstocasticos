import lyricsgenius
import os
import re
import unidecode
import nltk
import time

# Descarga el recurso necesario para tokenización
try:
    nltk.download('punkt_tab', quiet=True)
except Exception as e:
    print(f"Error al descargar punkt_tab: {e}")
    print("Usando split simple como respaldo para tokenización.")

# Configura el cliente de Genius con tu token
genius = lyricsgenius.Genius('p_MfEW38jKau61VXTOu3t9LrFAk5t3bhwWG_Vn5R0SONubN6Ly5jTob2IvGjOubT', timeout=15)  # Reemplaza con tu token de Genius

# Lista de canciones y artistas 1
'''
canciones = [
    {"titulo": "TQG", "artista": "Karol G"},
    {"titulo": "Gatúbela", "artista": "Karol G"},
    {"titulo": "Provenza", "artista": "Karol G"},
    {"titulo": "Bichota", "artista": "Karol G"},
    {"titulo": "200 Copas", "artista": "Karol G"},
    {"titulo": "Don Juan", "artista": "J Balvin"},
    {"titulo": "In Da Ghetto", "artista": "J Balvin"},
    {"titulo": "Mi Gente", "artista": "J Balvin"},
    {"titulo": "Ginza", "artista": "J Balvin"},
    {"titulo": "Safari", "artista": "J Balvin"},
    {"titulo": "Felices los 4", "artista": "Maluma"},
    {"titulo": "Hawái", "artista": "Maluma"},
    {"titulo": "Sobrio", "artista": "Maluma"},
    {"titulo": "Corazón", "artista": "Maluma"},
    {"titulo": "Normal", "artista": "Feid"},
    {"titulo": "Feliz Cumpleaños Ferxxo", "artista": "Feid"},
    {"titulo": "Hey Mor", "artista": "Feid"},
    {"titulo": "De Moda", "artista": "Feid"},
    {"titulo": "Si Te Preguntan", "artista": "Feid"},
    {"titulo": "La Inocente", "artista": "Mike Bahía"},
    {"titulo": "La Noche", "artista": "Mike Bahía"},
    {"titulo": "Traicionera", "artista": "Sebastián Yatra"},
    {"titulo": "Robarte un Beso", "artista": "Sebastián Yatra"},
    {"titulo": "Una Lady Como Tú", "artista": "Manuel Turizo"},
    {"titulo": "El Merengue", "artista": "Manuel Turizo"},
    {"titulo": "Despídase", "artista": "Manuel Turizo"},
    {"titulo": "La Bachata", "artista": "Manuel Turizo"},
    {"titulo": "Lo Que Siento", "artista": "Greeicy"},
    {"titulo": "No Te Vayas", "artista": "Piso 21"},
    {"titulo": "De Donde Vengo Yo", "artista": "ChocQuibTown"},
    {"titulo": "La Cura", "artista": "Kevin Flórez"},
    {"titulo": "Ella No Es Tuya", "artista": "Karol G"},
    {"titulo": "Machika", "artista": "J Balvin"},
    {"titulo": "Perra", "artista": "J Balvin"},
    {"titulo": "Runaway", "artista": "J Balvin"},
    {"titulo": "Sensualidad", "artista": "J Balvin"},
    {"titulo": "Sigo Extrañándote", "artista": "J Balvin"},
    {"titulo": "Ay Vamos", "artista": "J Balvin"},
    {"titulo": "La Canción", "artista": "J Balvin"},
    {"titulo": "Qué Más Pues?", "artista": "J Balvin"},
    {"titulo": "No Me Conoce", "artista": "J Balvin"},
    {"titulo": "La Rompe Corazones", "artista": "J Balvin"},
    {"titulo": "Colores", "artista": "J Balvin"},
    {"titulo": "Siempre Te Voy a Querer", "artista": "J Balvin"},
    {"titulo": "Bobo", "artista": "J Balvin"},
    {"titulo": "La Temperatura", "artista": "J Balvin"}
    
]

canciones += [
    {"titulo": "La Eterna", "artista": "Alcolirykoz"},
    {"titulo": "Esmeraldas", "artista": "Crudo Means Raw"},
    {"titulo": "La Jungla", "artista": "Flaco Flow y Melanina"},
    {"titulo": "Jaula de Oro", "artista": "Laberinto ELC"},
    {"titulo": "El Original", "artista": "Rocca"},
    {"titulo": "Somos Pacífico", "artista": "ChocQuibTown"},
    {"titulo": "Tengo un Trato", "artista": "La Mala Rodríguez"},
    {"titulo": "Con los Ojos de Engañá", "artista": "La Mala Rodríguez"},
    {"titulo": "Especias y Especies", "artista": "La Mala Rodríguez"},
    {"titulo": "Favorito", "artista": "Camilo"},
    {"titulo": "Tattoo (Remix)", "artista": "Rauw Alejandro"},
    {"titulo": "Relación (Remix)", "artista": "Sech"},
    {"titulo": "Caramelo", "artista": "Ozuna"},
    {"titulo": "Fantasías", "artista": "Rauw Alejandro"},
    {"titulo": "Ignorantes", "artista": "Bad Bunny"},
    {"titulo": "Rayando el Sol", "artista": "Maná"},
    {"titulo": "Ojalá", "artista": "Silvio Rodríguez"},
    {"titulo": "La Flaca", "artista": "Jarabe de Palo"},
    {"titulo": "Lucha de Gigantes", "artista": "Nacha Pop"},
    {"titulo": "Clavado en un Bar", "artista": "Maná"},
    {"titulo": "Me Cuesta Tanto Olvidarte", "artista": "Mecano"},
    {"titulo": "Persiana Americana", "artista": "Soda Stereo"},
    {"titulo": "De Música Ligera", "artista": "Soda Stereo"},
    {"titulo": "La Ingrata", "artista": "Café Tacvba"},
    {"titulo": "Eres", "artista": "Café Tacvba"},
    {"titulo": "El Sol No Regresa", "artista": "La Quinta Estación"},
    {"titulo": "Te Dejo Madrid", "artista": "Shakira"},
    {"titulo": "Ciega, Sordomuda", "artista": "Shakira"},
    {"titulo": "Antología", "artista": "Shakira"},
    {"titulo": "Tu Mirada", "artista": "Reik"}
]'''
# Lista de canciones y artistas 2
canciones = [
    {"titulo": "La herida", "artista": "Héroes del Silencio"},
    {"titulo": "Nuestros nombres", "artista": "Héroes del Silencio"},
    {"titulo": "Sin documentos", "artista": "Los Rodríguez"},
    {"titulo": "Resistiré", "artista": "Barón Rojo"},
    {"titulo": "La balsa", "artista": "Los Gatos"},
    {"titulo": "Trátame suavemente", "artista": "Soda Stereo"},
    {"titulo": "Ji ji ji", "artista": "Patricio Rey y sus Redonditos de Ricota"},
    {"titulo": "Muchacha (ojos de papel)", "artista": "Luis Alberto Spinetta"},
    {"titulo": "Persiana americana", "artista": "Soda Stereo"},
    {"titulo": "El amor después del amor", "artista": "Fito Páez"},
    {"titulo": "Eiti Leda", "artista": "Serú Girán"},
    {"titulo": "Imágenes paganas", "artista": "Virus"},
    {"titulo": "Seguir viviendo sin tu amor", "artista": "Luis Alberto Spinetta"},
    {"titulo": "Himno de mi corazón", "artista": "Los Abuelos de la Nada"},
    {"titulo": "Matador", "artista": "Los Fabulosos Cadillacs"},
    {"titulo": "Cerca de la revolución", "artista": "Charly García"},
    {"titulo": "Flaca", "artista": "Andrés Calamaro"},
    {"titulo": "Juntos a la par", "artista": "Pappo"},
    {"titulo": "11 y 6", "artista": "Fito Páez"},
    {"titulo": "La ciudad de la furia", "artista": "Soda Stereo"},
    {"titulo": "Será", "artista": "Las Pelotas"},
    {"titulo": "Seminare", "artista": "Serú Girán"},
    {"titulo": "Rezo por vos", "artista": "Charly García y Luis Alberto Spinetta"},
    {"titulo": "Costumbres argentinas", "artista": "Los Abuelos de la Nada"},
    {"titulo": "Spaghetti del rock", "artista": "Divididos"},
    {"titulo": "Mañana en el Abasto", "artista": "Sumo"},
    {"titulo": "Entre dos tierras", "artista": "Héroes del Silencio"},
    {"titulo": "Estás dormida", "artista": "Caifanes"},
    {"titulo": "De música ligera", "artista": "Soda Stereo"},
    {"titulo": "Estrechez de corazón", "artista": "Los Prisioneros"},
    {"titulo": "Mala vida", "artista": "Mano Negra"},
    {"titulo": "El extraño de pelo largo", "artista": "Los Enanitos Verdes"},
    {"titulo": "Yo no quiero volverme tan loco", "artista": "Charly García"},
    {"titulo": "Ay qué dolor", "artista": "La Derecha"},
    {"titulo": "Quisiera ser alcohol", "artista": "Caifanes"},
    {"titulo": "Cuéntame tu vida", "artista": "Caifanes"},
    {"titulo": "Bar Tacuba", "artista": "Café Tacvba"},
    {"titulo": "Tengo el poder", "artista": "Manuel Carrasco"},
    {"titulo": "Caída libre", "artista": "Leiva y Robe"},
    {"titulo": "Sola y feliz", "artista": "Tiburona"}
]
canciones += [
    # Canciones añadidas (ejemplos de rock/pop en español con letras extensas):
    {"titulo": "El lado oscuro", "artista": "Jarabe de Palo"},
    {"titulo": "La flaca", "artista": "Jarabe de Palo"},
    {"titulo": "Corazón espinado", "artista": "Santana ft. Maná"},
    {"titulo": "Rayando el sol", "artista": "Maná"},
    {"titulo": "Vivir sin aire", "artista": "Maná"},
    {"titulo": "En algún lugar", "artista": "Duncan Dhu"},
    {"titulo": "Lobo-hombre en París", "artista": "La Unión"},
    {"titulo": "La chispa adecuada", "artista": "Heroes del Silencio"},
    {"titulo": "Maldito duende", "artista": "Héroes del Silencio"},
    {"titulo": "El ataque de las chicas cocodrilo", "artista": "Hombres G"},
    {"titulo": "Marta tiene un marcapasos", "artista": "Hombres G"},
    {"titulo": "Cuando zarpa el amor", "artista": "Los Enanitos Verdes"},
    {"titulo": "Lamento boliviano", "artista": "Enanitos Verdes"},
    {"titulo": "Mariposa tecknicolor", "artista": "Fito Páez"},
    {"titulo": "Tumbas de la gloria", "artista": "Los Rodríguez"},
    {"titulo": "Para no olvidar", "artista": "Los Rodríguez"},
    {"titulo": "A las nueve", "artista": "No Te Va Gustar"},
    {"titulo": "El espejo", "artista": "Los Tres"},
    {"titulo": "La sangre en el cuerpo", "artista": "La Vela Puerca"},
    {"titulo": "El baile de los que sobran", "artista": "Los Prisioneros"},
    {"titulo": "We are sudamerican rockers", "artista": "Los Prisioneros"},
    {"titulo": "La voz de los '80", "artista": "Los Prisioneros"},
    {"titulo": "Cuando pase el temblor", "artista": "Soda Stereo"},
    {"titulo": "Zoom", "artista": "Soda Stereo"},
    {"titulo": "En la ciudad de la furia", "artista": "Soda Stereo"},
    {"titulo": "Canción animal", "artista": "Soda Stereo"},
    {"titulo": "Un misil en mi placard", "artista": "Soda Stereo"},
    {"titulo": "Prófugos", "artista": "Soda Stereo"},
    {"titulo": "Juegos de seducción", "artista": "Los Fabulosos Cadillacs"},
    {"titulo": "Vasos vacíos", "artista": "Los Fabulosos Cadillacs"},
    {"titulo": "Calaveras y diablitos", "artista": "Los Fabulosos Cadillacs"},
    {"titulo": "Padre Nuestro", "artista": "Los Fabulosos Cadillacs"},
    {"titulo": "Mal bicho", "artista": "Los Fabulosos Cadillacs"},
    {"titulo": "Yo no me sentaría en tu mesa", "artista": "Los Fabulosos Cadillacs"},
    {"titulo": "El genio del dub", "artista": "Los Fabulosos Cadillacs"},
    {"titulo": "Carnaval toda la vida", "artista": "Los Fabulosos Cadillacs"},
    {"titulo": "Mi enfermedad", "artista": "Fabiana Cantilo"},
    {"titulo": "Avanti Morocha", "artista": "Caballeros de la Quema"},
    {"titulo": "Sasha, Sissi y el círculo de baba", "artista": "Fito Páez"},
    {"titulo": "Al lado del camino", "artista": "Fito Páez"},
    {"titulo": "Tumbas de la gloria", "artista": "Fito Páez"},
    {"titulo": "Brillante sobre el mic", "artista": "Fito Páez"},
    {"titulo": "11 y 6", "artista": "Fito Páez"},
    {"titulo": "Dos días en la vida", "artista": "Fito Páez"},
    {"titulo": "Mariposa tecknicolor", "artista": "Fito Páez"},
    {"titulo": "Polaroid de locura ordinaria", "artista": "Fito Páez"},
    {"titulo": "Tres agujas", "artista": "Fito Páez"},
    {"titulo": "Un vestido y un amor", "artista": "Fito Páez"},
    {"titulo": "El amor después del amor", "artista": "Fito Páez"},
    {"titulo": "A rodar mi vida", "artista": "Fito Páez"},
    {"titulo": "Dale alegría a mi corazón", "artista": "Fito Páez"},
    {"titulo": "Detrás del muro de los lamentos", "artista": "Charly García"},
    {"titulo": "No voy en tren", "artista": "Charly García"},
    {"titulo": "Inconsciente colectivo", "artista": "Charly García"},
    {"titulo": "Chipi chipi", "artista": "Charly García"},
    {"titulo": "Los dinosaurios", "artista": "Charly García"},
    {"titulo": "Raros peinados nuevos", "artista": "Charly García"},
    {"titulo": "No me dejan salir", "artista": "Charly García"},
    {"titulo": "Fanky", "artista": "Charly García"},
    {"titulo": "Promesas sobre el bidet", "artista": "Charly García"},
    {"titulo": "Cerca de la revolución", "artista": "Charly García"},
    {"titulo": "Yo no quiero volverme tan loco", "artista": "Charly García"},
    {"titulo": "Rezo por vos", "artista": "Charly García y Luis Alberto Spinetta"},
    {"titulo": "El tiempo está después", "artista": "Divididos"},
    {"titulo": "Spaghetti del rock", "artista": "Divididos"},
    {"titulo": "Ala delta", "artista": "Divididos"},
    {"titulo": "Nene de antes", "artista": "Divididos"},
    {"titulo": "Qué ves?", "artista": "Divididos"},
    {"titulo": "La razón que te demora", "artista": "La Renga"},
    {"titulo": "El final es en donde partí", "artista": "La Renga"},
    {"titulo": "El viento que todo empuja", "artista": "La Renga"},
    {"titulo": "Hablando de la libertad", "artista": "La Renga"},
    {"titulo": "Tripa y corazón", "artista": "La Renga"},
    {"titulo": "Luciendo mi saquito blusero", "artista": "La Renga"},
    {"titulo": "El camino desolado", "artista": "La Renga"},
    {"titulo": "La nave del olvido", "artista": "La Renga"},
    {"titulo": "Paja brava", "artista": "La Renga"},
    {"titulo": "El juicio del ganso", "artista": "Patricio Rey y sus Redonditos de Ricota"},
    {"titulo": "Un poco de amor francés", "artista": "Patricio Rey y sus Redonditos de Ricota"},
    {"titulo": "Juguetes perdidos", "artista": "Patricio Rey y sus Redonditos de Ricota"},
    {"titulo": "Blues de la artillería", "artista": "Patricio Rey y sus Redonditos de Ricota"},
    {"titulo": "Motorpsico", "artista": "Patricio Rey y sus Redonditos de Ricota"},
    {"titulo": "Mi perro dinamita", "artista": "Patricio Rey y sus Redonditos de Ricota"},
    {"titulo": "La parábola de los hermanos eternos", "artista": "Invisible"},
    {"titulo": "El anillo del capitán Beto", "artista": "Invisible"},
    {"titulo": "Durazno sangrando", "artista": "Invisible"},
    {"titulo": "Sui Generis", "artista": "Sui Generis"},
    {"titulo": "Canción para mi muerte", "artista": "Sui Generis"},
    {"titulo": "Rasguña las piedras", "artista": "Sui Generis"},
    {"titulo": "Confesiones de invierno", "artista": "Sui Generis"},
    {"titulo": "Aprendizaje", "artista": "Sui Generis"},
    {"titulo": "Necesito", "artista": "Sui Generis"},
    {"titulo": "Tango en segunda", "artista": "Sumo"},
    {"titulo": "Mejor no hablar de ciertas cosas", "artista": "Sumo"},
    {"titulo": "Nextweek", "artista": "Sumo"},
    {"titulo": "Lo quiero ya", "artista": "Sumo"},
    {"titulo": "La rubia tarada", "artista": "Sumo"},
    {"titulo": "No tan distintos", "artista": "Sumo"},
    {"titulo": "Criminal mambo", "artista": "Los Auténticos Decadentes"},
    {"titulo": "La guitarra", "artista": "Los Auténticos Decadentes"},
    {"titulo": "El murguero", "artista": "Los Auténticos Decadentes"},
    {"titulo": "Veneno", "artista": "La Renga"},
    {"titulo": "Despedazado por mil partes", "artista": "La Renga"},
    {"titulo": "En el baldío", "artista": "La Renga"},
    {"titulo": "El terco", "artista": "Attaque 77"},
    {"titulo": "Hacelo por mí", "artista": "Attaque 77"},
    {"titulo": "Dulce condena", "artista": "Attaque 77"},
    {"titulo": "Ojos de cielo", "artista": "Attaque 77"},
    {"titulo": "Arrancacorazones", "artista": "Attaque 77"},
    {"titulo": "Siempre es lo mismo", "artista": "Los Violadores"},
    {"titulo": "Represión", "artista": "Los Violadores"},
    {"titulo": "Uno, dos, ultraviolento", "artista": "Los Violadores"},
    {"titulo": "Comunicándome", "artista": "Massacre"},
    {"titulo": "Animal", "artista": "Massacre"},
    {"titulo": "Mundo agradable", "artista": "Massacre"},
    {"titulo": "Quiero estar contigo", "artista": "Massacre"},
    {"titulo": "Moscas verdes para el charlatan", "artista": "Massacre"},
    {"titulo": "Como Ali", "artista": "Massacre"},
    {"titulo": "Amor descartable", "artista": "Massacre"},
    {"titulo": "Mensaje de voz", "artista": "Massacre"},
    {"titulo": "No nos podrán parar", "artista": "Massacre"},
    {"titulo": "Descontrol", "artista": "Massacre"},

]

# Crea una carpeta para guardar las letras
output_dir = r"C:\Users\LENOVO\OneDrive - UPB\Archivos Materias\Tercer Semestre\Procesos Estocasticos\Proyecto Final PE\Proyecto Final\letras"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Función para limpiar el nombre del archivo
def limpiar_nombre(titulo):
    return "".join(c for c in titulo if c.isalnum() or c in (' ', '_')).replace(' ', '_')

# Función para normalizar el texto con cuidado
def normalizar_texto(texto):
    try:
        # Eliminar las primeras dos líneas (colaboradores y título)
        lineas = texto.split('\n')
        if len(lineas) > 2:
            texto = '\n'.join(lineas[2:])  # Preserva el resto del contenido
        else:
            texto = '\n'.join(lineas)  # Usa todo si es muy corto

        # Eliminar metadatos entre corchetes (e.g., [Verse 1], [Outro])
        texto = re.sub(r'\[.*?\]', '', texto, flags=re.DOTALL)

        # Eliminar líneas con solo números o metadatos residuales (e.g., "1", "Embed")
        lineas = [linea for linea in texto.split('\n') if linea.strip() and not linea.strip().isdigit() and 'Embed' not in linea]
        texto = '\n'.join(lineas)

        # Convertir a minúsculas
        texto = texto.lower()

        # Eliminar acentos
        texto = unidecode.unidecode(texto)

        # Eliminar puntuación y caracteres especiales, preservando palabras
        texto = re.sub(r'[^\w\s]', ' ', texto)

        # Normalizar espacios (eliminar múltiples espacios y líneas vacías)
        texto = re.sub(r'\s+', ' ', texto).strip()

        # Dividir en palabras para contar (sin tokenización compleja para evitar cortes)
        palabras = texto.split()

        # Verificar si tiene al menos 200 palabras
        if len(palabras) < 200:
            print(f"Descartada: La letra tiene {len(palabras)} palabras, menos de 200.")
            return None

        # Unir palabras en una sola línea
        texto = ' '.join(palabras)

        return texto
    except Exception as e:
        print(f"Error en normalización: {e}")
        return None

# Descarga las letras, normalízalas y guárdalas en archivos .txt
descartadas = []
for cancion in canciones:
    try:
        print(f"Buscando '{cancion['titulo']}' por {cancion['artista']}...")
        # Busca la canción en Genius
        song = genius.search_song(cancion["titulo"], cancion["artista"])
        if song:
            # Normaliza el texto
            letra_normalizada = normalizar_texto(song.lyrics)
            if letra_normalizada is None:
                descartadas.append(f"{cancion['titulo']} por {cancion['artista']}")
                print(f"'{cancion['titulo']}' descartada (menos de 200 palabras o error en normalización).")
                continue
            
            # Limpia el título para usarlo como nombre de archivo
            nombre_archivo = limpiar_nombre(f"{cancion['titulo']}_{cancion['artista']}")
            ruta_archivo = os.path.join(output_dir, f"{nombre_archivo}.txt")
            
            # Guarda la letra normalizada en un archivo .txt
            with open(ruta_archivo, 'w', encoding='utf-8') as f:
                f.write(letra_normalizada)
            print(f"Letra normalizada de '{cancion['titulo']}' guardada en {ruta_archivo} ({len(letra_normalizada.split())} palabras)")
        else:
            descartadas.append(f"{cancion['titulo']} por {cancion['artista']}")
            print(f"No se encontró la letra de '{cancion['titulo']}' por {cancion['artista']}")
        # Pausa para evitar límites de la API
        time.sleep(1)
    except Exception as e:
        descartadas.append(f"{cancion['titulo']} por {cancion['artista']}")
        print(f"Error al descargar o normalizar '{cancion['titulo']}': {e}")
        continue

print("\nDescarga y normalización completadas.")
if descartadas:
    print("\nCanciones descartadas (menos de 200 palabras o no encontradas):")
    for cancion in descartadas:
        print(f"- {cancion}")