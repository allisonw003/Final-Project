SpongeBob Superfan Quiz
This is my PyQt6 project for my summer CS class, an interactive SpongeBob-themed multiple-choice quiz. I designed the GUI in Qt Designer, connected it to Python logic, and added my own 
features like input validation, a ranking system, and CSV result saving.

What the App Does.......
Lets the player enter their name, age, and how long they have watched SpongeBob.
Asks multiple choice SpongeBob questions one at a time.
Gives warnings if inputs are missing or invalid, such as letters for age or no answer selected.
Calculates the score and assigns a SpongeBob themed rank.
Saves all results to a CSV file with headers for future viewing.
Shows a "Question X of Y" counter to track your progress!

How to Run..
1)Install Python 3.10 or newer on your system.
2)Install PyQt6 by running:
3)pip install PyQt6
4)Clone this repository and navigate into it:
5)git clone <your-repo-link>
6)cd <repo-name>
7)Run the program:
8)python main.py
9)take quiz 

Files in This Project.....
main.py : This starts the app and then connects the GUI to logic and handles validation and it saves your results.
logic.py : Contains OOP classes like Player, Question, QuizManager, TimedQuizManage and ranking logic, and CSV.
quiz_data.py : This holds the question bank for the quiz
sponge_quiz.ui : GUI layout created in Qt Designer

NOT NEEDED......
gui.py : This is auto generated so im showing you this as an EXAMPLE of what is generated. 
results.csv : Stores quiz your results, name, age, watch time, score, rank, so I am showing you an EXAMPLE up above, its not necessary to download.

MY REFERENCES, LISTED AND SHOWN EXAMPLES IN MY CODE BY NUMBER, AND ALSO SHOWN WHAT I WAS TAUGHT BY THIS...... 
REFERENCES:
REF#1: Medium article by Sumayya Malik
https://medium.com/@sumayya.malik/mastering-python-day-10-multiple-choice-quiz-game-in-python-a2745a6812f7
This inspired my quiz logic structure

REF#2: Stack Overflow QRadioButton post
https://stackoverflow.com/questions/62396153/toggling-a-qradiobutton-in-pyqt5-uncheck-when-a-checked-radio-button-is-clicked
This showed how to reset radio buttons between questions because I had SEVERAL failed attempts. 

REF#3: YouTube PyQt6 tutorial by Alina C
https://www.youtube.com/watch?v=gfV1a3ri1tk
This was just an inspo video 

REF#4: PythonGUIs.com Creating Your First PyQt6 Window
https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/
This explained the main window and event loop basics and the pycharm imports for the GUI and some format 

REF#5: Stack Overflow about self
https://stackoverflow.com/questions/65152659/in-pyqt-why-somes-widgets-needs-the-self-parameter-before-calling-them-while
This clarified how self works for accessing widgets and data across methods and showed me several examples
