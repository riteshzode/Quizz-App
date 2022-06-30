import html


class QuizBrain:

    def __init__(self, ques_bank_list):
        self.question_number = 0
        self.score = 0
        self.question_list = ques_bank_list
        self.current_question = None


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):

        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(self.current_question.text)} {self.current_question.answer}: "

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            return True
        else:
            return False


    def score_update(self, user_answer_check):
        if user_answer_check:
            self.score += 1
        else:
            pass
