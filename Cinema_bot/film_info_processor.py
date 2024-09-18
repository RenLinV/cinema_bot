import requests
import json

#get info about film: poster, name, description, ratings
class film_info():
    def get_by_name(msg, header):
        query = msg.text
        params = {
            "query": query
            }
        response = requests.get(
            "https://api.kinopoisk.dev/v1.4/movie/search",
            headers=header,
            params=params
            ) 
        
        name = str(json.dumps(response.json()["docs"][0]["names"][0]["name"], ensure_ascii=False))
        description = json.dumps(response.json()["docs"][0]["description"], ensure_ascii=False)
        rating_kp = json.dumps(response.json()["docs"][0]["rating"]["kp"], ensure_ascii=False)
        rating_imdb = json.dumps(response.json()["docs"][0]["rating"]["imdb"], ensure_ascii=False)
        
        
        url = json.dumps(response.json()["docs"][0]['poster']['url'], ensure_ascii=False)[1:-1]

        movie_info = f"🍿Название: {name} \n 📃Описание: {description} \n 💎Рейтинг KinoPoisk: {rating_kp} \n ✨Рейтинг IMDB: {rating_imdb}"
        
        return movie_info, url,  json.dumps(response.json()["docs"][0], ensure_ascii=False)