A.	Clear instructions for how to programmatically REQUEST data from the microservice you implemented. 
Include an example call.

The microservice is continuously running during the same time as the main file. In order to use the microservice,
the start-microservice.txt file has the word "run" written in it to indicate the microservice to start. This occurs
when the user enters a certain animal crossing villager species into the CLI. By doing this 3 files are created.
ac-list.txt which contains the list of already filtered villagers based off the personality, this is the data 
being used to filter the villagers more
start-microservice.txt which prompts the microservice to start with the word "run"
ac-species-filter.txt which contains the species needed to be filtered by the microservice.

After filtering by personality type, the user is prompted if they want to filter the villager list more:

    ** YOU'VE SELECTED:
    (3) Filter by Personality Type
    Enter Personality Type: Snooty
    
    Result:
    [Alli,Amelia,Ankha,Annalise,Astrid,Azalea,Baabara,Becky,Bitty,Blaire,Blanche,Bree,Broffina,Carmen,
    Cashmere,Claudia,Cleo,Cupcake,Diana,Elise,Eloise,Francine,Freya,Friga,Gigi,Gloria,Greta,Gwen,Jane,
    Judy,Julia,Kitty,Lulu,Madam Rosa,Maelle,Mallary,Mathilda,Mint,Miranda,Monique,Naomi,Olivia,Opal,Pancetti,
    Pecan,Petri,Petunia,Portia,Purrl,Queenie,Rhoda,Robin,Snooty,Soleil,Sue E,Tasha,Tiara,Tiffany,Timbra,Tipper,
    Valise,Velma,Violet,Vivian,Whitney,Willow,Yuka]

    Would you like to filter this group of selected villagers more by species?
    Enter (1) for YES or (0) for NO: 1

If 1 is entered:

    ac-list.txt file contains:
        Alli,Amelia,Ankha,Annalise,Astrid,Azalea,Baabara,Becky,Bitty,Blaire,Blanche,Bree,Broffina,Carmen,
        Cashmere,Claudia,Cleo,Cupcake,Diana,Elise,Eloise,Francine,Freya,Friga,Gigi,Gloria,Greta,Gwen,Jane,
        Judy,Julia,Kitty,Lulu,Madam Rosa,Maelle,Mallary,Mathilda,Mint,Miranda,Monique,Naomi,Olivia,Opal,Pancetti,
        Pecan,Petri,Petunia,Portia,Purrl,Queenie,Rhoda,Robin,Snooty,Soleil,Sue E,Tasha,Tiara,Tiffany,Timbra,Tipper,
        Valise,Velma,Violet,Vivian,Whitney,Willow,Yuka,

Then user is prompted with: 

    Enter Species Type: Cat

Once entered:

    ac-species-filter.txt contains:
        Cat

    start-microservice.txt contains:
        run

Recquest data from the microservice by reading the txt files.

Code:

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
            FILTER HERE

acmicroservice.py is then prompted to filter because of start-microservice.txt "run"

B.	Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.

Recieve data from reading the txt files.
Code:

    # sleep for 30 seconds
    time.sleep(20)
    print()

    # OPENS DATA CREATED BY MICROSERVICE
    # creates an ac-list.txt file that has the list of villagers based off personality type
    # file = open("new-ac-list.txt", "r")
    file = open("start-microservice.txt", "r")
    time.sleep(10)
    file = file.read()

    print(file)


After the microservice is filtering, start-microservice.txt is rewritten to be the list of Snooty Cats.

    start-microservice.txt contains
        ['Ankha', 'Kitty', 'Monique', 'Olivia', 'Purrl']

The main program is delayed and then opens the start-microservice.txt to read the files and print them.


C. UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your partner 
(and your grader) will understand.!

User gets prompted if they want to filter > yes creates a txt file for data > user prompted what species, species entered >
txt file contains species and txt file contains run > microservice starts and filters > replaces run txt file with new data >
program delay > program read and open file > program print