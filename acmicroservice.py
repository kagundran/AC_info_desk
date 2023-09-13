import time
import requests
from requests import Session
import api_key

# class to access API
class Villagers:
    """ Gets the information from the villagers """
    def __init__(self, token):
        self._apiurl = 'https://api.nookipedia.com/villagers'
        self._headers = headers = {'X-API-KEY': api_key.API_KEY, 'Accept-Version': '1.0.0'}
        self._session = Session()
        self._session.headers.update(headers=headers)
        self._response_api = requests.get(self._apiurl, headers=headers)
        self.data = self._response_api.json()              # array containing dictionaries


while True:
    time.sleep(1)
    villagers = Villagers(api_key.API_KEY)  # creates a Villager Class to access JSON API info
    villager_personality_species = []

    # open file and read start-microservice.txt
    file = open("start-microservice.txt", "r", encoding="utf-8")
    time.sleep(5)
    file_read = file.read()

    # if read file line is "run"
    if file_read == "run":

        # creates a ac-list.txt file that has the list of villagers based off personality type
        file_list = open("ac-list.txt", "r")
        file_read_list = file_list.read().split(",")
        file_list.close()

        # determines what type of species to filter by
        villager_species = open("ac-species-filter.txt", "r")
        villager_read_species = villager_species.read()
        villager_species.close()

        species_filtered = []
        count = 0
        for object in villagers.data:
            if villager_read_species in object["species"]:
                species_filtered.append(villagers.data[count]["name"])
            count += 1

        for value in file_read_list:                # original list of personality type villagers
            if value in species_filtered:
                villager_personality_species.append(value)

        if len(villager_personality_species) == 0:
            file = open("start-microservice.txt", "w")
            no_species = "No species found!"
            file.write(no_species)
            file.close()
        else:
            file = open("start-microservice.txt", "w")
            file.write(str(villager_personality_species))
            file.close()
