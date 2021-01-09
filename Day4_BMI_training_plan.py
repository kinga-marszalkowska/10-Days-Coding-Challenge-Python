import random

# description : (min value of bmi, max value of bmi)
bmi_interpretation = {
    "Very severely underweight": (0, 15),
    "Severely underweight":	(15, 16),
    "Underweight":	(16, 18.5),
    "Normal (healthy weight)":	(18.5, 25),
    "Overweight": (25, 30),
    "Obese Class I (Moderately obese)":	(30, 35),
    "Obese Class II (Severely obese)":	(35, 40),
    "Obese Class III (Very severely obese)": (40, 60)
}

exercise_list = ['running', 'swimming', 'yoga', 'walking', 'cycling']


def bmi_calculator():
    weight = -1
    height = -1

    while weight < 0 or weight > 1000:
        weight = int(input("Give weight in kg: "))

    while height < 0 or height > 1000:
        height = int(input("Give height in cm: "))

    bmi = weight / pow(height/100, 2)

    for key in bmi_interpretation.keys():
        if bmi_interpretation[key][0] < bmi < bmi_interpretation[key][1]:
            print("Your bmi is: {bmi} which means you are {description}".format(
                bmi="{:.2f}".format(bmi),
                description=str(key)
            ))
            return str(key), int(bmi)
    return ""


def training_plan(bmi_val, description):
    file = open("training_plan.txt", "a")
    max_time = -1
    while max_time < 10 or max_time > 500:
        max_time = int(input('Max time you can devote to training daily (minutes), more than 10: '))

    file.write("\n Your training plan: ")
    for i in range(1, 8):
        if bmi_val > max_time:
            exercise_time = random.randint(10, max_time)
        else:
            exercise_time = random.randint(int(bmi_interpretation[description][1]), max_time)
        file.write("\n Day {day_no}: activity: {activity}, time: {exercise_time} mins \n".format(
            day_no=str(i),
            activity=random.choice(exercise_list),
            exercise_time=exercise_time,
        ))
    file.close()


bmi_val_desc = bmi_calculator()

training_plan(bmi_val=bmi_val_desc[1], description=bmi_val_desc[0])
