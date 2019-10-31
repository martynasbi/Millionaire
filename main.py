import random
import json

def read_questions(questionaire):
    with open(questionaire, encoding='utf-8') as f:
        question_lines = f.read().splitlines()
    questions = [json.loads(question) for question in question_lines]
    return questions

def to_start(start):
    beginning = 0
    while True:
        if start == beginning:
            answer = input("\nAr norite pradėti žaidimą: TAIP / NE\n").upper()
        else:
            answer = input("\nAr norite kartoti žaidimą: TAIP / NE\n").upper()
        if "T" in answer:
            start_game()
        elif "N" in answer:
            print ("\nIki. Lauksime Jūsų sugrįžtant!\n")
            exit()
        else:
            continue

def introduction():
    
    print("********************************************************************************************************************************************")
    print("Sveiki atvykę į žaidimą \"Kas laimės milijoną?\"!\n\nŽaidimo metu Jums bus pateikta 10 klausimų ir 4 atsakymų variantai.")
    print("\nĮveikę pirmus 4 klausimus, Jūs užsitikrinsite 25 000 Eur laimėjimą, o įveikę pirmus 7 klausimus, užsitikrinsite net 180 000 Eur laimėjimą!")
    print(f"\nIš viso Jūs turite 3 bandymus. Išnaudojus visus bandymus, žaidimas bus baigtas.")
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

    question = (random.choice(questionaire))
    questionaire.remove(question)
    provided_question = QUESTION_NUMBERS[question_number]
    print(str(provided_question) + ". " + question["question"])
    random_answers = random.sample(question["answers"], len(question["answers"]))
    print("\nAtsakymų variantai:")

    for letter, answer in zip(ANSWER_LETTERS, random_answers):
        print(f"{letter}. {answer}")
    print()

    while True:
        while True:
            if tries_left == 0:
                print("Jūs išnaudojote visus bandymus.\n")
                if win_amount >= 180000:
                    win_amount = 180000
                    print("************************************")
                    print(f"Jūs laimėjote {win_amount} Eur. Sveikiname!")
                    print("************************************")
                    to_start(1)
                elif win_amount >= 25000:
                    win_amount = 25000
                    print("************************************")
                    print(f"Jūs laimėjote {win_amount} Eur. Sveikiname!")
                    print("************************************")
                    to_start(1)
                else:
                    print("*****************************************")
                    print("Deja šį kartą Jūs nieko nelaimėjote.\n\nAčiū už dalyvavimą, bandykite kitą kartą!")
                    print("*****************************************")
                    to_start(1)
            answer_letter = input("Kai norėsite stabdyti žaidimą, pasirinkite: S.\nPasirinkite atsakymo variantą: A, B, C ar D.\n").upper()
            if answer_letter in ANSWER_LETTERS:
                answer = random_answers[ord(answer_letter)-65]
                print("Jūs pasirinkote atsakymą:",answer)
                break
            elif answer_letter == "S":
                if win_amount == 0:
                    print("*************************************************************************************************")
                    print(f"Jūs nusprendėte nebetęsti žaidimo. Deja šį kartą Jūs nieko nelaimėjote. Bandykite sekantį kartą.")
                    print("*************************************************************************************************")
                    to_start(1)
                else:
                    print("*********************************************************************************")
                    print(f"Jūs nusprendėte nebetęsti žaidimo. Jūs laimėjote {win_amount} Eur. Sveikiname!")
                    print("*********************************************************************************")
                    to_start(1)
            else:
                print("Nėra tokio pasirinkimo.\n")
        if question["answer"] == answer:
            print("\nJūsų answer yra teisingas!")
            win_amount += WIN_AMOUNTS[correct_answers]
            if win_amount < 1000000:
                print("******************************************")
                print(f"Sveikiname, Jūs pasiekėte {win_amount} Eur ribą!")
                print("******************************************\n")
                return questionaire, win_amount, tries_left, correct_answers+1, question_number+1
            else:
                print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$Sveikiname, Jūs laimėjote milijoną!$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                to_start(1)
        else:
            tries_left -= 1
            if tries_left > 1:
                print(f"\nDeja, Jūsų atsakymas yra neteisingas.\n-------------------------------------\nJums liko {tries_left} bandymai.\n")
            elif tries_left == 1:
                print("\nDeja, Jūsų atsakymas yra neteisingas.\n-------------------------------------\nJums liko paskutinis bandymas.\n")
            else:
                print(f"\nDeja, Jūsų atsakymas yra neteisingas.\n")
    return questionaire, win_amount, tries_left, question_number, correct_answers

if __name__ == "__main__":
    introduction()
    to_start(0)
    start_game()
