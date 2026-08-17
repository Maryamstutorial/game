
# 🎮 Rock Paper Scissors Game

A simple **Rock Paper Scissors** game built with Python. You play against the computer, and the game keeps track of both the player's and computer's scores.

## 📌 Features

* 🪨 Rock, 📄 Paper, and ✂️ Scissors gameplay
* 🎲 Computer makes a random choice
* 🏆 Displays the winner after each round
* 📊 Keeps track of player and computer scores
* ❌ Handles invalid input
* 🔄 Allows the player to play multiple rounds

## 🛠️ Requirements

You need:

* Python 3.x

The game uses Python's built-in `random` module, so no external libraries are required.

## 🚀 How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the Python file:

```bash
python game.py
```

> Replace `game.py` with the actual name of your Python file if it is different.

## 🎯 How to Play

When the game starts, enter one of the following choices:

* `rock`
* `paper`
* `scissors`

The computer will randomly select one of the three choices.

### 🏆 Winning Rules

| Player Choice | Beats       |
| ------------- | ----------- |
| 🪨 Rock       | ✂️ Scissors |
| 📄 Paper      | 🪨 Rock     |
| ✂️ Scissors   | 📄 Paper    |

If both the player and computer choose the same option, the round is a **tie**.

## 💻 Example

```text
enter your choice: rock
computer choice scissors
YOU WIN!!

enter your choice: paper
computer choice scissors
COMPUTER WIN!!
```

## 📊 Score

The game keeps track of the score:

```text
Score -> You: 1 | Computer: 1
```

The player's score increases when the player wins, while the computer's score increases when the computer wins.

## ❌ Invalid Input

If you enter something other than `rock`, `paper`, or `scissors`, the game displays:

```text
INVALID
```

The game then asks you to enter a valid choice again.

## 🔄 Play Again

After a round, you can choose whether you want to continue playing:

```text
Play again? (yes/no):
```

Enter `yes` to continue or anything other than `yes` to stop the game.

## 📚 Concepts Used

This project demonstrates several basic Python programming concepts:

* Variables
* Lists
* `while` loops
* `if`, `elif`, and `else` statements
* User input with `input()`
* String methods such as `.lower()`
* Random selection using `random.choice()`
* Comparison operators
* Logical operators
* F-strings
* `continue` and `break`

## 🔮 Future Improvements

Possible improvements for the game include:

* Add a best-of-3 or best-of-5 mode
* Add colored terminal output
* Add a game history
* Add a reset-score option
* Add a graphical user interface (GUI)
* Add more choices, such as **Rock Paper Scissors Lizard Spock**

## 👨‍💻 Author

Created as a Python practice project to learn programming fundamentals, loops, conditions, user input, and the `random` module.



