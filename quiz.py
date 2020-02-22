from quiz_class import Question

question_prompts = [
    "2+2 is equal to?\n a)21\n b)5\n c)4\n",
    "What color of logo has Intel?\n a)Yellow\n b)Blue\n c)Red\n",
    "Which game is most popular?\n a)Minecraft\n b)Witcher\n c)Diablo\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct.")


run_test(questions)