"""PyQt6 GUI for the SpongeBob quiz: collects player info, runs the quiz, saves results."""
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QRadioButton
from gui import Ui_MainWindow
from quiz_data import get_questions
from typing import Optional
from logic import Player, QuizManager, get_rank  # use my OOP classes here

import sys
import csv
import os

# my the main window class for the quiz application
class QuizApp(QMainWindow):
    """Main window for the quiz: screens, validation, navigation, and CSV saving."""
    def __init__(self) -> None:
        """Set up the UI and initialize quiz state."""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # to connect the Start button to the start_quiz function
        self.ui.startButton.clicked.connect(self.start_quiz)
        # to connect the Next button to the next_question function
        self.ui.nextButton.clicked.connect(self.next_question)

        # my quiz variables (use OOP manager + player instead of raw list + index)
        self.quiz_manager: QuizManager = QuizManager(get_questions())
        self.player: Optional[Player] = None
        self.score: int = 0

        # hide the quiz section and show the player info input section at the beginning
        self.ui.groupBox.hide()
        self.ui.playerGroupBox.show()

        # prep the first question text/counter quietly (keeps your original behavior)
        # this will no-op visually until Start is pressed because the quiz box is hidden
        self.update_question_counter()
        self.load_question()

    def start_quiz(self) -> None:
        """Collect player info, validate it, then start the quiz."""
        # Collecting my players info through their input so theyre going to type type select
        name = self.ui.nameInput.text().strip()
        age_text = self.ui.ageInput.text().strip()
        watch_time = self.ui.watchCombo.currentText()

        # Validate that name and age are not empty
        # error handling!!!!
        if not name or not age_text:
            QMessageBox.warning(self, "Input Error", "Please enter your name and age!")
            return

        # Validate that age is a positive integer, not zero and not a number
        try:
            age = int(age_text)
            if age < 1 or age > 120:
                QMessageBox.warning(self, "Input Error", "Please enter a valid age (1–120)!")
                return
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Your age must be a number!")
            return

        if len(name) < 2:
            QMessageBox.warning(self, "Input Error", "Please enter your full name.")
            return

        # build the Player object and reset quiz state
        self.player = Player(name, age, watch_time)
        self.score = 0
        self.quiz_manager.reset()

        # Hide the input form and show the quiz section
        self.ui.playerGroupBox.hide()
        self.ui.groupBox.show()

        # load the first question!!!!
        self.update_question_counter()
        self.load_question()

    def load_question(self) -> None:
        """Load the current question into the UI."""
        # if somehow there are no questions, bail gracefully
        if not self.quiz_manager.questions:
            QMessageBox.critical(self, "Error", "No questions found.")
            return

        # Load the current question based on the index
        q = self.quiz_manager.get_current_question()
        self.ui.questionLabel.setText(q.text)

        # Set each radio button with one of the answer choices
        self.ui.radioButton1.setText(q.choices[0])
        self.ui.radioButton2.setText(q.choices[1])
        self.ui.radioButton3.setText(q.choices[2])
        self.ui.radioButton4.setText(q.choices[3])

        # https://stackoverflow.com/questions/62396153/toggling-a-qradiobutton-in-pyqt5-uncheck-when-a-checked-radio-button-is-clicked
        # BOTTOM (2)
        # Reset the radio buttons (so none are selected)
        for button in self.findChildren(QRadioButton):
            button.setAutoExclusive(False)   # temporarily allowing unchecking
            button.setChecked(False)         # uncheck all the radiobuttons
            button.setAutoExclusive(True)    # restoring exclusivity (only one checked at a time)

        # update the "Question X of Y" label
        self.update_question_counter()

    def update_question_counter(self) -> None:
        """Update the top label to show 'Question X of Y'."""
        total: int = len(self.quiz_manager.questions)
        # clamp when at last screen so it never shows > total
        current: int = min(self.quiz_manager.current_index + 1, total if total > 0 else 1)
        # IMPORTANT: make sure your Designer label objectName is questionNumberLabel
        self.ui.questionNumberLabel.setText(f"Question {current} of {total}")

    def next_question(self) -> None:
        """Read selected answer, score it, and go to next question or show results."""
        # Determine which radio button the user selected
        selected_answer = ""
        if self.ui.radioButton1.isChecked():
            selected_answer = self.ui.radioButton1.text()
        elif self.ui.radioButton2.isChecked():
            selected_answer = self.ui.radioButton2.text()
        elif self.ui.radioButton3.isChecked():
            selected_answer = self.ui.radioButton3.text()
        elif self.ui.radioButton4.isChecked():
            selected_answer = self.ui.radioButton4.text()

        # If no answer selected, show a warning
        if not selected_answer:
            QMessageBox.warning(self, "Selection Error", "Please select an answer before continuing!")
            return

        # Compare selected answer with the correct answer
        correct_answer = self.quiz_manager.get_current_question().answer
        if selected_answer == correct_answer:
            self.score += 1

        # move forward
        self.quiz_manager.move_to_next()

        # If no more questions show results
        if not self.quiz_manager.has_more():
            self.show_results()
        else:
            self.load_question()

    def _ensure_csv_headers(self, path: str) -> None:
        """Create the CSV with headers once if file does not exist or is empty."""
        try:
            need_headers = (not os.path.exists(path)) or (os.path.getsize(path) == 0)
            if need_headers:
                with open(path, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Name", "Age", "YearsWatched", "Score", "Rank"])
        except OSError:
            # If we can't create the file, show error when saving results later
            pass

    def show_results(self) -> None:
        """Hide quiz, show popup with results, and append to CSV with error handling."""
        # Hide the quiz box now that quiz is over
        self.ui.groupBox.hide()

        # use shared rank logic
        rank = get_rank(self.score)

        # guard for player being None (shouldn't happen if start_quiz ran)
        pname = self.player.name if self.player else ""
        page = str(self.player.age) if self.player else ""
        ptime = self.player.years_watched if self.player else ""

        # their result message to show in a popup
        msg = (f"Name: {pname}\n"
               f"Age: {page}\n"
               f"Time Watching SpongeBob: {ptime}\n"
               f"Score: {self.score}/15\n"
               f"Ranking: {rank}")
        # Show results
        QMessageBox.information(self, "Quiz Results", msg)

        # Save the result to a CSV file (with headers + exception handling)
        csv_path = "results.csv"
        self._ensure_csv_headers(csv_path)
        try:
            with open(csv_path, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([pname, page, ptime, self.score, rank])
        except OSError as e:
            QMessageBox.critical(self, "Save Error", f"Could not save results: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizApp()
    window.resize(400, 400)
    window.show()
    sys.exit(app.exec())

#######111111
#some inspiratioon for how to format from the follwoing link {list of questions}
#https://medium.com/@sumayya.malik/mastering-python-day-10-multiple-choice-quiz-game-in-python-a2745a6812f7
# Day 10
# Multiple-Choice Quiz Game in Python

# import random
#
# # Define a list of questions, options, and correct answers as a dictionary
# quiz_data = [
#     {
#         "question": "Which planet is known as the Red Planet?",
#         "options": ["a) Venus", "b) Mercury", "c) Earth", "d) Mars"],
#         "correct_answer": "d"
#     },
#     {
#         "question": "Who developed the theory of relativity?",
#         "options": ["a) Isaac Newton", "b) Albert Einstein", "c) Galileo Galilei", "d) Marie Curie"],
#         "correct_answer": "b"
#     },
#     {
#         "question": "What is the largest ocean on Earth?",
#         "options": ["a) Pacific Ocean", "b) Indian Ocean", "c) Southern Ocean", "d) Atlantic Ocean"],
#         "correct_answer": "a"
#     },
#     {
#         "question": "What is the fastest land animal on Earth?",
#         "options": ["a) Cheetah", "b) Lion", "c) Elephant", "d) Giraffe"],
#         "correct_answer": "a"
#     },
#     {
#         "question": "Who is the author of the Harry Potter book series?",
#         "options": ["a) J.R.R. Tolkien", "b) C.S. Lewis", "c) J.K. Rowling", "d) George R.R. Martin"],
#         "correct_answer": "c"
#     }
# ]
#
# # Create a list of indices from 0 to the length of quiz_data - 1
# indices = list(range(len(quiz_data)))
#
# # Shuffle the indices to get a random order
# random.shuffle(indices)
#
# # Initialize a variable to keep track of the score
# score = 0
#
# # Iterate through the questions and ask the user
# for i in indices:
#     current_question = quiz_data[i]
#
#     print(f"Question: {current_question['question']}")
#     for option in current_question['options']:
#         print(option)
#
#     user_answer = input("Your answer (a/b/c/d): ").strip().lower()
# I USED AS REFERENCE MAP
#     # Check if the user's answer is correct
#     if user_answer == current_question['correct_answer']:
#         print("Correct!\n")
#         score += 1
#     else:
#         print(f"Wrong! The correct answer is: {current_question['correct_answer'].upper()}\n")
#
# # Display the final score
# print(f"You scored {score} out of {len(quiz_data)} questions.")
#
# if score == len(quiz_data):
#     print("Congratulations! You are the quiz champion!")

##############222222222
# from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QButtonGroup
# import sys
#
#
# class MainWindow(QWidget):
#
#     def __init__(self):
#
#         super().__init__()
#
#         # Radio buttons
#         self.group = QButtonGroup()
#
#         self.b1 = QRadioButton()
#         self.group.addButton(self.b1)
#         self.b1.clicked.connect(lambda: self.radioButtonClicked())
#
#         self.b2 = QRadioButton()
#         self.group.addButton(self.b2)
#         self.b2.clicked.connect(lambda: self.radioButtonClicked())
#
#         # Layout
#         self.layout = QHBoxLayout()
#         self.layout.addWidget(self.b1)
#         self.layout.addWidget(self.b2)
#         self.setLayout(self.layout)
#
#
#     def radioButtonClicked(self):
#         if self.sender().isChecked():
#             self.sender().setAutoExclusive(False)
#             self.sender().setChecked(False) # This is not working, as it fires on the first click
#             self.sender().setAutoExclusive(True)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     app.exec_()

#########3333333
# https://www.youtube.com/watch?v=gfV1a3ri1tk by alina c


#pyuic6 sponge_quiz.ui -o gui.py
