from data import data
import random
# Funkce na vygenerování 2 random účtů pro porovnání
def account_generator(all_accounts):
    data_length = len(all_accounts)
    random_number = random.randint(0, data_length - 1)

    return all_accounts[random_number]


# funkce pro vypsání 2 random vygenerovanýcn účtů pro usera
def printing_options(acc1, acc2):
    print(f"porovnejte A: {acc1['name']}, {acc1['description']}, {acc1['country']}")
    print(f"porovnejte B: {acc2['name']}, {acc2['description']}, {acc2['country']}")


def game():
    # vygeneruje accounty
    account_1 = account_generator(data)
    account_2 = account_generator(data)
    while account_1 == account_2:   # zajistí že vygeneruje jiný account_2 než je account_1
        account_2 = account_generator(data)

    correct_answer = ""
    score = 0
    lets_continue = True

    # dokud odpovídá správně hraje dál
    while lets_continue:
        # # pro testovací účely. pak smazat
        # print(f"Tesovací výpis - účet 1: {account_1['follower_count']}")
        # print(f"Tesovací výpis - účet 2: {account_2['follower_count']}")
        
        printing_options(account_1, account_2)

        user_answer = input("Kdo má více sledujícíh na instagramu? Napište Anebo B. ")

        if account_1["follower_count"] > account_2["follower_count"]:
            correct_answer = "A"
        else:
            correct_answer = "B"
        
        account_1 = account_2 # zajistí že se v dalším kole account_2 přesune do accountu_1

        if correct_answer == user_answer:
            score += 1
            print(f"Spravně! Vaše skore je {score}")
            account_2 = account_generator(data)
            while account_1 == account_2:   # zajistí že vygeneruje jiný account_2 než je account_1
                account_2 = account_generator(data)
        else:
            print(f"To je špatně. Vaše konečné skore je {score}")
            lets_continue = False        
game()