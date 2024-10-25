# TODO: asking the questions

# TODO: Checking if the answer was correct

# TODO: checking if we're the end of the quiz

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        current_question = self.question_list[self.question_number]
        if answer == current_question.answer:
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: "
                       f"{current_question.text} (True/False): ")
