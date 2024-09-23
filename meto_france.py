import requests
import helpers.json_helpers

url = r"https://public-api.meteofrance.fr/public/DPPaquetObs/v1/liste-stations"



print(helpers.json_helpers.fetch_secret('liste_stations_api_key'))