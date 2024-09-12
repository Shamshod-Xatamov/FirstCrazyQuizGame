import random



class Quiz:

    quiz_questions = {
            "What is the capital of France?": "Paris",
            "What is 2 + 2?": "4",
            "What is the color of the sky?": "Blue",
            "Which planet is known as the Red Planet?": "Mars",
            "Who wrote 'Romeo and Juliet'?": "Shakespeare"
        }

    def game(self):
            return random.choice(list(self.quiz_questions.keys()))


obj1=Quiz()



