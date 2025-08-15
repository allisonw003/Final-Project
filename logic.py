from typing import List
import csv

#player class represents each quiz taker
class Player:
    """Holds one quiz player and score."""
    def __init__(self, name: str, age: int, years_watched: str):
# to save the player's name, age, and how long they’ve watched SpongeBob
        self.name = name
        self.age = age
        self.years_watched = years_watched
        self.score: int = 0

    def add_point(self) -> None:
        """Add 1 point."""
        self.score += 1

    def get_result_row(self) -> List[str]:
        """Return CSV row for this player."""
# formats the results into a row that can be saved in the CSV
        rank = get_rank(self.score)  # Call the standalone function instead of static method
        return [self.name, str(self.age), self.years_watched, str(self.score), rank]
# i want to return like a list like: ["Alli", "21", "2+ years", "12", "VICTORY SCREEECHHH!"]

# Question class stores one quiz question, the answer options, and the correct answer
class Question:
    """One multiple-choice question."""
    def __init__(self, text: str, choices: List[str], correct: str):
        self.text = text
        self.choices = choices
        self.correct = correct
        self.answer = correct

    def check_answer(self, user_choice: str) -> bool:
        """True if selected answer matches correct."""
        # Returns True if the user’s selected answer matches the correct one
        return user_choice == self.correct

# This class manages the quiz flow and keeps track of current question and moving forward
class QuizManager:
    """Controls quiz flow and index."""
    def __init__(self, questions: List['Question']):
        self.questions: List[Question] = questions  # Store the full list of questions
        self.current_index: int = 0  # Start at the first question

    def get_current_question(self) -> 'Question':
        """Return current question."""
        return self.questions[self.current_index]

    def move_to_next(self) -> None:
        """Advance to next question."""
        self.current_index += 1

    def has_more(self) -> bool:
        """Whether more questions remain."""
# Check if there are more questions left
        return self.current_index < len(self.questions)

    def reset(self) -> None:
        """Restart quiz at beginning."""
# Reset the quiz so it starts from the beginning again
        self.current_index = 0

def get_rank(score: int) -> str:
    """Rank string based on score."""
    if score >= 13:
        return "You are a Goofy Goober!!!!"
    elif score >= 9:
        return "VICTORY SCREEECHHH!"
    elif score >= 5:
        return "Still in Boating School"
    elif score >= 1:
        return "You are a load of barnacles"
    else:
        return "Plankton? Is that you?"

def save_to_csv(row: List[str], filename: str = "quiz_results.csv") -> None:
    """Append one row to CSV."""
    try:
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)
    except OSError as e:
        print("Error saving quiz result:", e)

class TimedQuizManager(QuizManager):
    """Simple subclass to demonstrate inheritance."""
    pass
