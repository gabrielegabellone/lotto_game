# Lotto Game
Project divided into 3 learning paths, based on the lottery game.

In the first learning path the software allow the user to generate lottery bills.  
In the second learning path, an extraction is simulated and on the basis of this, each of the bills generated is checked if it is a winner.
## How does Lotto game work?
Lotto is a game based on betting numbers between 1 and 90 to be drawn on various "ruote" represented by cities. More info: https://www.sisal.it/lotto/come-si-gioca
### To start the program:
Make sure you have Python 3.9 or next.  
Run the lotto_game.py file directly from the command line, no arguments need to be passed:
```
python lotto_game.py
```
Once started, the program initially asks the user to choose how many bills he wants to play and then for each bill he must choose the type of bet, how many numbers he wants to play (the numbers are randomly generated) and the city. Here is an example:

![Inserimento](https://user-images.githubusercontent.com/115152050/232223106-648f9888-83e6-4cba-9166-e918ddae548b.png)

Subsequently an extraction is made, and all the generated bills are checked, the winning ones are printed:

![Estrazione](https://user-images.githubusercontent.com/115152050/232223736-edc3b57f-ad8d-4842-a55c-2d90c9149c98.png)
## Contents of the "lotto" and "tests" folders
The “lotto” folder contains the modules with the classes used in the program and for each of these modules there is a test inside the "tests" folder, for example the test of the "bill.py" module will be "test_bill.py" and so on.
