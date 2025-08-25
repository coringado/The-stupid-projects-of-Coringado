import requests
import time

#dados do site e jogo
api_key = "AB9AF60A7E9B00BD7B5081B22CAEDBCF"
user_id = "76561199014807820"
app_id = 250900

#requisição
while True:
    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={user_id}&include_appinfo=1&format=json"
    response = requests.get(url)
    data = response.json()
    
    jogos = data["response"].get("games",[])
    game = False
    
    for jogo in jogos:
        if jogo["appid"] == app_id:
            horas_jogadas = jogo["playtime_forever"] / 60
            print(f"{horas_jogadas:.2f} horas jogadas")
            game = True
    if not game:
        print("jogo não encontrado")
        break
    time.sleep(20)