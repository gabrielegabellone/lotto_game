# Lotto Game
Project divided into 3 learning paths, based on the lottery game.

In the first learning path the software allow the user to generate lottery bills.
## How does Lotto game work?
Lotto is a game based on betting numbers between 1 and 90 to be drawn on various "ruote" represented by cities. More info: https://www.sisal.it/lotto/come-si-gioca
### To start the program:
Run the main.py file directly from the command line, no arguments need to be passed:
```
python main.py
```
Once started, the program initially asks the user to choose how many bills he wants to play and then for each bill he must choose the type of bet, how many numbers he wants to play (the numbers are randomly generated) and the city.
## Contents of the "lotto" and "tests" folders
The “lotto” folder contains the modules with the classes used in the program:
* game.py  
Contains the Game class and therefore information on the lottery game, such as the minimum and maximum number of bills that can be generated

* bill.py  
Contains the Bill class and therefore also the methods that assist in the generation of the bill.

* bet_type.py  
Contains the Bet_type class and therefore information on the types of bets available in the game.

* city.py  
Contains the City class and therefore information about the available cities.

For each of these modules there is a test inside the "tests" folder, for example the test of the "game.py" module will be "test_game.py" and so on.
