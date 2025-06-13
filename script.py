import json

photos_data = []
photo_id_counter = 1
num_albums = 50
photos_per_album = 2

# Lista de algumas cores para variar as imagens
colors = ["92c952", "771796", "2433fe", "f66b97", "501fe1", "e0a0a0", "a1a1a1", "c1c1c1", "d1d1d1", "e1e1e1"]

for album_id in range(1, num_albums + 1):
    for i in range(photos_per_album):
        # Usar um índice de cor para variar a imagem
        color_index = (photo_id_counter - 1) % len(colors)
        color = colors[color_index]

        photos_data.append({
            "albumId": album_id,
            "id": photo_id_counter,
            "title": f"Foto {photo_id_counter} do álbum {album_id}",
            "url": f"https://via.placeholder.com/600/{color}",
            "thumbnailUrl": f"https://via.placeholder.com/150/{color}"
        })
        photo_id_counter += 1

# Carregar o db.json existente (se houver) e adicionar as fotos
try:
    with open('db.json', 'r') as f:
        db = json.load(f)
except FileNotFoundError:
    db = {} # Se o arquivo não existir, cria um dicionário vazio

db["photos"] = photos_data # Adiciona ou sobrescreve a chave "photos"

with open('db.json', 'w') as f:
    json.dump(db, f, indent=2)

print(f"Geradas {len(photos_data)} fotos e salvas em db.json")