from player import Player

# The PlayerStats class contains all the functionalities of a player object
class PlayerStats:

    # Initalizes an array of player objects
    def __init__(self):
        self.__player_list = []

    # Prints list of all player names
    def print_list(self):
        for player in self.__player_list:
          print(player.get_firstname() + " " + player.get_lastname() + "\n")

    # The given player name is searched for in the list of players, returns null if the name is not found
    def search_name(self, lastname):
        for player in self.__player_list:
            if player.get_lastname() == lastname:
                return player  # returns object
        return None  # returns null if player is not found

    def search_category(self, category, input):
        for player in self.__player_list:
            match category:
                case "Position":
                    if player.get_position() == input:
                        print(player)
                case "Nationality":
                    if player.get_nationality() == input:
                        print(player)
                case "Games Played":
                    if int(player.get_games()) == int(input):
                        print(player)
                case "Height": 
                    if int(player.get_height()) == int(input):
                        print(player)
                case "Weight":
                    if int(player.get_weight()) == int(input):
                        print(player)
                case "Market Value":
                    if int(player.get_value()) == int(input):
                        print(player)
                case "Rank":
                    if int(player.get_rank()) == int(input):
                        print(player)
                case "Age":
                    if int(player.get_age()) == int(input):
                        print(player)

    def search_rating(self, category, value):
        for player in self.__player_list:
            match category:
                case 6:
                    if int(player.get_rank()) >= value:
                        print(player)
                case 10:
                    if player.get_passrating() >= value:
                        print(player)
                case 11:
                    if player.get_finishing() >= value:
                        print(player)
                case 12:
                    if player.get_stamina() >= value:
                        print(player)
    

    #
    #def search_category(self, categnumb):
    #  for player in self.__player_list:
    #    print(player.get_name() + ": " + player.get_category_value(categnumb))   
    #

    # The given rating category will print all players with that 
    # rating category greater than or equal to given value
    ############################################################
    # def search_ratings(self, categnumb, rating):
    #    for player in self.__player_list:
    #        categvalue = player.search_category(categnumb)
    #       if categvalue >= rating:
    #            print(player.get_name() + " " + categvalue)
    ############################################################

    # The readPlayer class opens and reads the RealMadrid.txt file to set respective information of players
    def readPlayer(self, RealMadrid):
        # Opens the RealMadrid file for reading
        with open("RealMadrid.txt", "r") as file:
            for line in file:
                line = line.strip("\n")  # Removes new line character
                info = line.split()  # Splits the line of string each time there is a space

                # Creates an instance of a player object
                player = Player()

                # Sets respective information about player based on index from .txt file
                player.set_firstname(info[0])
                player.set_lastname(info[1])
                player.set_position(info[2])
                player.set_nationality(info[3])
                player.set_games(info[4])
                player.set_height(info[5])
                player.set_weight(info[6])
                player.set_value(info[7])
                player.set_rank(info[8])
                player.set_age(info[9])
                player.set_goals(info[10])
                player.set_assists(info[11])
                player.set_passrating(info[12])
                player.set_finishing(info[13])
                player.set_stamina(info[14])
                player.set_ballcontrol(info[15])
                player.set_slide(info[16])
               
                self.__player_list.append(player)
