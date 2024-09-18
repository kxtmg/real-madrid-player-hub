from traceback import print_list
from playerStats import PlayerStats
from player import Player

class Interface:
    # Main interface that the user will be able to interact with 
    # to gather information about certain players or statistics about a player's performance
    @staticmethod
    def playerInfoCommandLine():
        print("**********************")
        print("[0] - Exit program")
        print("[1] - See entire team")
        print("[2] - Search by name")
        print("[3] - Search by category")
        print("[4] - Search by rating")
        print("**********************")

        player = PlayerStats()
        playerCategory = Player()
        player.readPlayer("ReadMadrid.txt")

        # Prompt user for input
        option = int(input("Please Select an Option 1: "))

        # Used for option 3 and 4
        category = -1

        while (option != 0):

            # Option 1 will show a list of the current roster and their first and last names
            if option == 1:
                player.print_list()

            # Option 2 will allow the user to select a specific player from the roster and 
            # input his name, this will print a player and all of their statistics
            elif option == 2:
                name = input("Enter player's last name:  ")
                print(player.search_name(name))

            # Show each player and their value in a category

            # Option 3 will list of possible categories. 
            # An input prompt will appear and ask for a category number. 
            # All player names and relevant statistic to that category will be displayed. 
            # The category number must be >= 0 and <= 14.
            elif option == 3:
                print(" [0] - Position \n [1] - Nationality \n [2] - Games Played \n [3] - Height \n [4] - Weight \n [5] - Market Value \n [6] - Rank \n [7] - Age \n [8] - Goals \n [9] - Assists \n [10] - Pass Rating \n [11] - Finishing Rating \n [12] - Stamina Rating \n [13] - Ballcontrol Rating \n [14] - Slide Tackle Rating \n")
                category = input("Enter a category: ")
                choice = input("Enter the specifics: ")
                #num = int(input("Enter value: "))
                #assert int(category) >= 0
                #assert int(category) <= 14
                print(player.search_category(category, choice))
                #print(player.search_category(category))
                print("skip")

            # Option 4 will list of possible categories with ratings. 
            # An input prompt will appear and ask for a category number. 
            # Another input prompt will appear for the desired rating value,
            # where 0 <= rating value <= 100 and category number must be one of the options listed
            # Only shows ratings. Enter a rating. Only players of that rating value will be shown.
            elif option == 4:
                print(" [6] - Rank \n [10] - Passing \n [11] - Finishing \n [12] - Stamina \n [13] - Ball Control \n [14] - Slide Tackle \n")
                category = int(input("Enter a Category: "))
                #while (category != 6 or category != 10 or category != 11 or category != 12 or category != 13 or category != 14):
                #    category = int(input("Enter a Category (inital category number failed): "))
                ratingvalue = int(input("Enter a rating value [< 0 and < 100] : "))
                assert int(ratingvalue) >= 0
                assert int(ratingvalue) <= 100
                player.search_rating(category, ratingvalue)

            option = int(input("Please Select an Option 2: "))

        print("Program Terminated")

if __name__ == "__main__":
    Interface.playerInfoCommandLine()