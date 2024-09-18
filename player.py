# The Player class represents each instance of a player
# and contains the information/attributes each player object will posess
class Player:

  # Initializes a player object with all its listed attributes
  def __init__(self):
    self.__firstname = ""
    self.__lastname =""
    self.__position = ""
    self.__nationality = ""
    self.__games = 0
    self.__height = 0
    self.__weight = 0
    self.__value = 0
    self.__rank = 0
    self.__age = 0
    self.__goals = 0
    self.__assists = 0
    self.__passrating = 0
    self.__finishing = 0
    self.__stamina = 0
    self.__ballcontrol = 0
    self.__slide = 0


  # sets and gets a player object's name

  def get_firstname(self):
    return self.__firstname

  def set_firstname(self,firstname):
    self.__firstname = firstname 

  # sets and gets a player object's last name
  def get_lastname(self):
    return self.__lastname

  def set_lastname(self,lastname):
    self.__lastname = lastname

  # sets and gets a player object's position
  def get_position(self):
    return self.__position
    
  def set_position(self,position):
    self.__position = position 
    
  # set and gets a player object's nationality
  def get_nationality(self):
    return self.__nationality
    
  def set_nationality(self,nationality):
    self.__nationality = nationality 

  # Enoc
  # set and gets a player object's games
  def get_games(self):
    return self.__games
    
  def set_games(self,games):
    self.__games = games 

  # set and gets a player object's height
  def get_height(self):
    return self.__height
    
  def set_height(self,height):
    self.__height = height 

  # set and gets a player object's weight
  def get_weight(self):
    return self.__weight
    
  def set_weight(self,weight):
    self.__weight = weight 

  # set and gets a player object's value
  def get_value(self):
    return self.__value

  def set_value(self,value):
    self.__value = value 

  # set and gets a player object's rank
  def get_rank(self):
    return self.__rank
    
  def set_rank(self,rank):
    self.__rank = rank 

  # Adrien
  # set and gets a player object's age
  def get_age(self):
    return self.__age
    
  def set_age(self,age):
    self.__age = age 

  # set and gets a player obect's goals
  def get_goals(self):
    return self.__goals
    
  def set_goals(self,goals):
    self.__goals = goals 

  # set and gets a player object's assists rating
  def get_assists(self):
    return self.__assists
    
  def set_assists(self,assists):
    self.__assists = assists 

  # set and gets a player object's pass rating
  def get_passrating(self):
    return self.__passrating
    
  def set_passrating(self,passrating):
    self.__passrating = passrating 

  # set and gets a player object's finishing rating
  def get_finishing(self):
    return self.__finishing
    
  def set_finishing(self,finishing):
    self.__finishing = finishing 

  # set and gets a player object's stamina rating
  def get_stamina(self):
    return self.__stamina
    
  def set_stamina(self,stamina):
    self.__stamina = stamina 

  # set and gets a player object's ball control rating
  def get_ballcontrol(self):
    return self.__ballcontrol
    
  def set_ballcontrol(self,ballcontrol):
    self.__ballcontrol = ballcontrol 

  # set and gets a player object's slide rating
  def get_slide(self):
    return self.__slide
    
  def set_slide(self,slide):
    self.__slide = slide 

  # print information
  def __str__(self):
    line = "Name: " + self.__firstname + " " + self.__lastname + "\nPosition: " + self.__position + "\nNationality: " + self.__nationality + "\nGames: " + self.__games + "\nHeight(m): " + self.__height + "\nWeight(kg): " + self.__weight + "\nMarket Value(millions): " + self.__value + "\nRank: " + self.__rank + "\nAge: " + self.__age + "\nGoals: " + self.__goals + "\nAssists: " + self.__assists + "\nPass: " + self.__passrating + "\nFinish: " + self.__finishing + "\nStamina: " + self.__stamina + "\nBall Control: " + self.__ballcontrol + "\nSlide: " + self.__slide
    return line

   # Accepts a number from 0 to 14 (one for each ceteogry)
   # and returns the value associated with that category for this specific player instance
  def get_category_value(self, number):
    if number == 0:
       return self.__position
    elif number == 1:
      return self.__nationality
    elif number == 2:
      return self.__games
    elif number == 3:
      return self.__height
    elif number == 4:
      return self.__weight
    elif number == 5:
      return self.__value
    elif number == 6:
      return self.__rank
    elif number == 7:
      return self.__age
    elif number == 8:
      return self.__goals
    elif number == 9:
      return self.__assists
    elif number == 10:
      return self.__passrating
    elif number == 11:
      return self.__finishing
    elif number == 12:
      return self.__stamina
    elif number == 13:
      return self.__ballcontrol
    elif number == 14:
      return self.__slide
