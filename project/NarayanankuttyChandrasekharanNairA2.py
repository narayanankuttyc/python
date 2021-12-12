from random import randint
from random import choice

# Function for getting name from user
def get_name():
    ask_name = input("A: Welcome to calorie intake assistant, my name is Cal.What is your name ? \n U:")
    while not ask_name.isalpha():
        ask_name = input("A :Invalid Name ! Please enter name again \n ")
    return ask_name

# Function for getting gender from user and validating the input
def get_gender(username):
    ask_gender = (input("A: Great "+username+" What's your gender? Enter M for male or F for female?\n U:")).upper()
    while not (ask_gender.isalpha() and (ask_gender == "M" or ask_gender == "F")):
        ask_gender = (input("A:I am sorry,I cannot understand.What's your gender? Enter M for male or F for female?\n U:")).upper()
    return ask_gender

# Function for validating age,weight,height
def get_number(min,max,prompt):
    ask_num = input(prompt)
    while not (ask_num.isdigit() and (int(ask_num ) > min and int(ask_num) < max)):
        ask_num = input("I am sorry ,I cannot understand."+ prompt)
    return ask_num

# Function for calculating rdci
def calc_rdci (input_height,input_weight,input_age,input_gender,username):
    calculate = 0
    if input_gender == "M" :
        calculate = 10*input_weight + 6.25*input_height - 5*input_age + 5
        print("A: Thank you for your information "+username+ " !\n Considering the details given,your daily recommended "
                                                             "intake is of",calculate,"calories per day\n A: Let’s see how healthy your meals were last week.")
    else:
        calculate = 10*input_weight + 6.25*input_height - 5*input_age - 161
        print("A: Thank you for your information "+username+ " ! \n Considering the details given,your daily recommended "
                                                             "intake is of",calculate,"calories per day \n A: Let’s see how healthy your meals were last week.")
    return calculate

# Function for getting daily meal type from user
def get_mealtype(min,max):
    daily_meals_intake = []
    for day in range (1,8):
        print("A: Day" +str(day)+ ": were your meals very unhealthy (1), unhealthy (2), healthy (3),or very healthy (4)? ")
        daily_meal = input("Enter your corresponding number.\n")
        while not(daily_meal.isdigit() and (int(daily_meal) >= min and int(daily_meal) <=max)):
            daily_meal = input("A: I’m sorry, I cannot understand. Day " + str(day)+": were your meals very unhealthy (1), unhealthy (2),"
                  " healthy (3), or very healthy (4)? Enter the corresponding number.")
        daily_meals_intake.append(daily_meal)

    return daily_meals_intake

# Function for calculating adci
def cal_adci(meal_type,rdci,username):
    total_adci = 0
    category_types = {
        1: 1.5 * rdci,
        2: 1.2 * rdci,
        3: rdci,
        4: 0.8 * rdci
    }
    print(username, "here are your results:")
    for day in range(7):
        dailyadci = category_types[int(meal_type[day])]
        tname,tvalue= add_temptation()  # tname is the temptation name variable and tvalue is temptation name value
        if tvalue:
            total_adci = total_adci + dailyadci + tvalue
            print("A:","{:.2f}".format(dailyadci + tvalue),"calorie intake in day",day + 1,"Also,it looks like this day you’ve been tempted with",tname,"and",tvalue,"calories have been added!")
        else:
            total_adci = total_adci + dailyadci
            print("A:",dailyadci," calorie intake in day",day+1)

    return total_adci

#Function for giving recommendations as per the adci and tempted food intake
def recommendation(total_adci, rdci, username):
    avg_adci = total_adci / 7
    perc_value = (avg_adci / rdci ) * 100
    if perc_value > 100:
        rec_value = perc_value -100
    else:
        rec_value = 100 - perc_value
    print("A:During the last 7 days you had an intake of ","{:.2f}".format(total_adci), "calories, meaning a daily average of ","{:.2f}".format( avg_adci)," calories.")
    if perc_value < 90 :
        print("A:",username," your daily calorie intake is lower than the recommended with",int(rec_value),"%.This way you will\n lose weight, just make sure your meals contain all nutritional value needed. \nIt’s recommended that you do not fall under the healthy weight and that you keep a balanced lifestyle")
    elif perc_value >=90 and perc_value <=110:
        print("A:",username,"your daily calorie intake is close to the recommended one! You have a balanced healthy lifestyle, well done!")
    else:
        print(username,"your daily calorie intake is higher than the recommended with", int(rec_value),"%. This way you will gain weight,and in time health concerns\nmay arise. It’s recommended that you either lower your calorie intake,either exercise more! ")
        print("Goodbye and good luck!")

# Function for adding tempted food with adci
def add_temptation():
    tempt_foods = {"chocolate":250,"chips":550,"ice-cream":207,
    "fast-food":350,"fizzy drink":180,"party cake":257,"popcorn":375}
    tempt_list = list(tempt_foods.keys())
    if randint(0,1):
        tempt_choice=choice(tempt_list)
        return (tempt_choice,tempt_foods[tempt_choice])
    else:
        return (0,0)

# Main Function
def main():
    username = get_name()
    gender = get_gender(username)
    prompt_age = "What is your age in years?\n U:"
    prompt_weight = "What is your current weight in kg?\n U:"
    prompt_height = "What is your height in cm?\n U:"
    age = get_number(18,99,prompt_age)
    weight = get_number(40,200,prompt_weight)
    height = get_number(80,200,prompt_height)
    rdci = calc_rdci(float(height),float(weight),float(age),gender,username)
    meal_type = get_mealtype(1,4)
    adci = cal_adci(meal_type,rdci,username)
    recommendation(adci,rdci,username)


main()