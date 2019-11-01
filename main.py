import random
import json

def language_data(data_from_txt):
    with open(data_from_txt, encoding='utf-8') as json_file:
        data = json.load(json_file)
    if LT_EN() == "EN":
        txt_data_lang = data["EN"]
        return txt_data_lang
    else:
        txt_data_lang = data["LT"]
        return txt_data_lang

def LT_EN():
    while True:
        language = input("Please choose language:\n1. Type \"EN\" for English language\n2. Type \"LT\" for Lithuanian language ").upper()
        if "E" in language:
            print("\nYou have chosen English language.")
            choice = "EN"
            return choice
        elif "L" in language:
            print("\nJūs pasirinkote Lietuvių kalbą.")
            choice = "LT"
            return choice
        else:
            print("Wrong choice.")

language_choice = language_data("LT-EN.txt")

def read_questions(questionaire):
    with open(questionaire, encoding='utf-8') as f:
        question_lines = f.read().splitlines()
    questions = [json.loads(question) for question in question_lines]
    return questions

def to_start(start):
    beginning = 0
    while True:
        if start == beginning:
            answer = input(language_choice["begin"]).upper()
        else:
            answer = input(language_choice["replay"]).upper()
        if language_choice["yes"] in answer:
            start_game()
        elif language_choice["no"] in answer:
            print (language_choice["farewell"])
            exit()
        else:
            continue

def introduction():
    
    print("********************************************************************************************************************************************")
    print(language_choice["introduction1"])
    print(language_choice["introduction2"])
    print(language_choice["introduction3"])
    print("********************************************************************************************************************************************")

def start_game():
    
    tries_left = 3
    win_amount = 0
    correct_answers = 0
    question_number = 0
    
    questionaire_easy = read_questions("easy_questions.txt")
    questionaire_medium = read_questions("medium_questions.txt")
    questionaire_hard = read_questions("hard_questions.txt")
    
    for question in questionaire_easy.copy():
        questionaire_easy, win_amount, tries_left, question_number, correct_answers = provide_question(
            questionaire_easy, win_amount, tries_left, question_number, correct_answers)
    for question in questionaire_medium.copy():
        questionaire_medium, win_amount, tries_left, question_number, correct_answers = provide_question(
            questionaire_medium, win_amount, tries_left, question_number, correct_answers)
    for question in questionaire_hard.copy():
        questionaire_hard, win_amount, tries_left, question_number, correct_answers = provide_question(
            questionaire_hard, win_amount, tries_left, question_number, correct_answers)

def provide_question(questionaire, win_amount, tries_left, question_number, correct_answers):
    
    WIN_AMOUNTS = [1000, 3000, 6000, 15000, 30000, 50000, 75000, 130000, 250000, 440000]
    QUESTION_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ANSWER_LETTERS = ["A", "B", "C", "D"]

    question = random.choice(questionaire)
    questionaire.remove(question)
    provided_question = QUESTION_NUMBERS[question_number]
    print(str(provided_question) + ". " + question["question"])

    random_answers = random.sample(question["answers"], len(question["answers"]))
    print(language_choice["answers"])

    for letter, answer in zip(ANSWER_LETTERS, random_answers):
        print(f"{letter}. {answer}")
    print()

    while True:
        while True:
            if tries_left == 0:
                print(language_choice["out_of_tries"])
                if win_amount >= 180000:
                    win_amount = 180000
                    print("************************************")
                    print(language_choice["win_amount"].format(win_amount))
                    print("************************************")
                    to_start(1)
                elif win_amount >= 25000:
                    win_amount = 25000
                    print("************************************")
                    print(language_choice["win_amount"].format(win_amount))
                    print("************************************")
                    to_start(1)
                else:
                    print("*****************************************")
                    print(language_choice["no_win"])
                    print("*****************************************")
                    to_start(1)
            answer_letter = input(language_choice["choices"]).upper()
            if answer_letter in ANSWER_LETTERS:
                answer = random_answers[ord(answer_letter)-65]
                print(language_choice["answer"],answer)
                break
            elif answer_letter == "S":
                if win_amount == 0:
                    print("*************************************************************************************************")
                    print(language_choice["stop_lose"])
                    print("*************************************************************************************************")
                    to_start(1)
                else:
                    print("*********************************************************************************")
                    print(language_choice["stop_win"].format(win_amount))
                    print("*********************************************************************************")
                    to_start(1)
            else:
                print(language_choice["wrong_choice"])
        if question["answer"] == answer:
            print(language_choice["correct"])
            win_amount += WIN_AMOUNTS[correct_answers]
            if win_amount < 1000000:
                print("******************************************")
                print(language_choice["reach_goal"].format(win_amount))
                print("******************************************\n")
                return questionaire, win_amount, tries_left, correct_answers+1, question_number+1
            else:
                print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print(language_choice["millionaire"])
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                to_start(1)
        else:
            tries_left -= 1
            if tries_left > 1:
                print(language_choice["tries_left"].format(tries_left))
            elif tries_left == 1:
                print(language_choice["last_try"])
            else:
                print(language_choice["incorrect"])
    return questionaire, win_amount, tries_left, question_number, correct_answers

if __name__ == "__main__":
    introduction()
    to_start(0)
    start_game()
