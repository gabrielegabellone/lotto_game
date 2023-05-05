# Lotto Game 
![Coverage Badge](https://github.com/gabrielegabellone/lotto_game/blob/main/reports/coverage-badge.svg)  
Project realized at the end of the TomorrowDevs Programming Basics in Python course.  
The aim is to create an OOP software that simulates the game of the lottery and that is easily extendable as features are added.  
The project was carried out with 3 learning paths, in each of which features are added:
* In the first learning path the software allows the user to generate lottery bills.  
* In the second learning path, an extraction is simulated and on the basis of this, each of the bills generated is checked if it is a winner.
* In the third learning path, the software allows the user to enter the amount of money for the bill.
## How does Lotto game work?
Lotto is a game based on betting numbers between 1 and 90 to be drawn on various "ruote" represented by cities.  
There are different types of bets, depending on how many numbers are predicted, here are those available in the game:
* ambata: predict the extraction of a number; 
* ambo: predict the extraction of two numbers;
* terno: predict the extraction of three numbers; 
* quaterna: predict the extraction of four numbers;
* cinquina: predict the extraction of five numbers.

You can bet up to a maximum of 10 numbers per bill. In the game it is possible to bet on a specific city or on all of them, finally if a bill is a winner an amount is calculated, it depends on: how much money you bet on the bill, the type of bet, how many numbers have been played, how many combinations have been guessed. If you bet on all cities, it is divided by the total number of cities (10).

More info: https://www.sisal.it/lotto/come-si-gioca - https://www.estrazionedellotto.it/prontuario-vincite-lotto
## How to start the program:
Make sure you have Python 3.9 or next.  
Run the lotto_game.py file directly from the command line, no arguments need to be passed:
```
python lotto_game.py
```
### Practical example
Once started, the program initially asks the user to choose how many bills he wants to play and then for each bill he must choose the type of bet, how many numbers he wants to play (the numbers are randomly generated), the city and the amount of money to play:

![enter_bill](https://user-images.githubusercontent.com/115152050/233775882-e1e8d0dd-627f-4f3f-ad97-83a8f56be521.png)

Subsequently an extraction is made, and all the generated bills are checked, if a bill is a winner, it is printed and the gross and net amounts are displayed:

![extraction_and_check_win](https://user-images.githubusercontent.com/115152050/233775938-07169f89-e1f1-47a1-9603-0b84239fa341.png)
## Structure
- lotto_game.py  
represents the entry point;
- lotto  
folder that contains the modules with the classes used in the program;
- tests  
folder that contains the tests, for example the test of the "bill.py" module will be "test_bill.py" and so on.
## Acknowledgments :)
[TomorrowDevs](https://github.com/tomorrowdevs-projects/) - A mentorship program for developer.  
[Isabel Lombardi](https://github.com/isabel-lombardi) - She contributed by reviewing the code and giving me advice and feedback.
