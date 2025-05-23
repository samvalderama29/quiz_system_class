import os

class QuestionLoader:
    def __init__(self, questions_file):
        self.questions_file = questions_file

    def load_questions(self):
        if not os.path.exists(self.questions_file):
            print("Quiz file not found")
            return[]

        with open(self.questions_file, "r") as quiz_file:
            question_blocks = quiz_file.read().split("-----\n")

        quiz_questions = []

        for question_block in question_blocks:
            lines_in_block = question_block.strip().splitlines()
            if len(lines_in_block) < 6:
                continue

            file_question = {
                "file_question": lines_in_block[0][len("Question: "):],
                "option_a": lines_in_block[1][3:],
                "option_b": lines_in_block[2][3:],
                "option_c": lines_in_block[3][3:],
                "option_d": lines_in_block[4][3:],
                "correct_answer": lines_in_block[5][-1].lower()
            }
            quiz_questions.append(file_question)
        return quiz_questions