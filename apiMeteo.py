import requests
api_key = "276374eb47f924837d68a9aeca0d0e22"
def get_weather(api_key):
    # URL de l'API pour obtenir la météo actuelle à Paris (France)
    #url = "http://api.openweathermap.org/data/2.5/weather?q=Paris,fr&units=metric&appid=" + api_key
    #url= "https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid="+ api_key
    url = f"http://api.openweathermap.org/data/2.5/forecast?q=Paris,fr&units=metric&appid={api_key}"

    
    # Faire la requête à l'API
    response = requests.get(url)
    print(response)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        data = response.json()
 # Afficher les informations sur la ville
        city_info = data["city"]
        print(f"Ville: {city_info['name']}")
        print(f"Population: {city_info['population']}")
        
        # Afficher les informations de météo pour les premières prévisions disponibles
        for forecast in data["list"][:5]:  # Limiter à 5 pour simplifier l'exemple
            print(f"\nDate et heure: {forecast['dt_txt']}")
            print(f"Température: {forecast['main']['temp']} °C")
            print(f"Humidité: {forecast['main']['humidity']} %")
            print(f"Météo: {forecast['weather'][0]['main']} - {forecast['weather'][0]['description']}")
            print(f"Vitesse du vent: {forecast['wind']['speed']} km/h")
            print(f"Couverture nuageuse: {forecast['clouds']['all']} %")
    else:
        print(f"Erreur lors de la récupération des données: {response.status_code}")

# Remplacez 'YOUR_API_KEY' par votre clé API personnelle
get_weather(api_key)
