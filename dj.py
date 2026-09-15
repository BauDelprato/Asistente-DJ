import random
import webbrowser
import yt_dlp

generos = {
    "rock": [
        "rock clásico",
        "rock internacional",
        "rock argentino",
        "rock alternativo",
        "rock 2000"
    ],
    "pop": [
        "pop internacional",
        "pop 2000",
        "pop 2010",
        "pop actual",
        "pop latino"
    ],
    "reggaeton": [
        "reggaeton clásico",
        "reggaeton 2010",
        "reggaeton actual",
        "reggaeton latino",
        "reggaeton mix"
    ],
    "lofi": [
        "lofi hip hop",
        "lofi para estudiar",
        "lofi chill",
        "lofi beats",
        "lofi instrumental"
    ],
    "electronica": [
        "música electrónica",
        "electro house",
        "deep house",
        "techno",
        "electronic mix"
    ],
    "argentina": [
        "rock argentino",
        "pop argentino",
        "cumbia argentina",
        "trap argentino",
        "música argentina"
    ]
}

def reproducir(cancion):
    webbrowser.open("https://www.youtube.com/results?search_query=" + cancion.replace(" ", "+"))

def crear_playlist(palabra):
    palabra = palabra.lower().strip()

    if palabra not in generos:
        return []

    canciones = generos[palabra].copy()
    random.shuffle(canciones)

    return canciones

def buscar_video(cancion):
    opciones = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        resultado = ydl.extract_info(f"ytsearch1:{cancion}", download=False)

    if "entries" not in resultado or not resultado["entries"]:
        return None

    return resultado["entries"][0]["id"]

def reproducir_playlist(palabra):
    canciones = crear_playlist(palabra)

    if not canciones:
        return False

    videos = []

    for cancion in canciones:
        video_id = buscar_video(cancion)

        if video_id:
            videos.append(video_id)

    if not videos:
        return False

    url = f"https://www.youtube.com/watch?v={videos[0]}&playlist={','.join(videos[1:])}"
    webbrowser.open(url)

    return True