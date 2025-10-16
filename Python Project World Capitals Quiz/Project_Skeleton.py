import random #Do not update or remove

def main():
    input_filename = "WorldCapitals.txt" #Do not update
    output_filename = "HighScores.txt" #Do not update
    username = "hxu231" #use your username
    print_banner(username)
    capitals = get_world_capitals_dictionary(input_filename)
    total = run_quiz(capitals)
    handle_high_scores(output_filename, username, total)

#To complete
def print_banner(username):
    upper_username = username.upper()
    message= f"World Capitals Quiz For {upper_username}"
    inner_line = f"#  {message}  #"
    border = "#" * len(inner_line)
    print(border)
    print(inner_line)
    print(border)
    print()

#To complete
def get_world_capitals_dictionary(filename):
    result = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            country, capital = line.split(":", 1)
            result[country.strip()] = capital.strip()
    return result

#To complete
def get_player_answer(target_country, cities):
    choice = ""
    while choice not in cities:
        print(f"Choices available: {cities}")
        print()
        choice = input(f"What is the capital city of {target_country}? ").strip()
        if choice not in cities:
            print("You must choose from the city choices available!")
    cities.remove(choice)
    return choice

#To complete
def run_round(world_capitals_dict, countries_tested):
    target_country, cities = get_question_data(world_capitals_dict, countries_tested)
    correct = world_capitals_dict[target_country]
    attempts = 0
    score = 0
    while attempts < 3:
        attempts += 1
        answer = get_player_answer(target_country, cities)
        if answer == correct:
            print("Your answer is correct! Well done!")
            score = 4 - attempts  # 1st+3, 2nd+2, 3rd+1
            break
        elif attempts < 3:
            print("Your answer is incorrect! Please try again!")
            print()
        else:
            print("Your answer is incorrect! Better luck next time!")
    return score

#To complete
def run_quiz(world_capitals_dict):
    countries_tested = []
    total = 0
    round_number = 1
    while round_number <= 6:
        print(f"Round {round_number}:")
        print()
        total += run_round(world_capitals_dict, countries_tested)
        round_number += 1
        print()
    print(f"You have scored {total} out of 18 for the World Capital's Quiz!")
    print()
    return total

#To complete
def read_high_scores(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f.readlines()]
    except FileNotFoundError:
        return [0, 0, 0, 0, 0]
    scores = []
    for line in lines[1:]:
        if ". " in line:
            try:
                score = int(line.split(". ")[1])
                scores.append(score)
            except ValueError:
                continue
    while len(scores) < 5:
        scores.append(0)
    return scores[:5]

#To complete
def update_high_scores(filename, username, high_scores, new_score):
    new_list = list(high_scores)
    inserted = False
    i = 0
    while i < len(new_list) and not inserted:
        if new_score >= new_list[i]:
            new_list.insert(i, new_score)
            inserted = True
        i += 1
    if not inserted:
        new_list.append(new_score)
    new_list = new_list[:5]
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"High Scores for {username}\n")
        for idx, val in enumerate(new_list, start=1):
            f.write(f"{idx}. {val}\n")

#To complete
def handle_high_scores(filename, username, new_score):
    high_scores = read_high_scores(filename)
    if new_score >= min(high_scores):
        update_high_scores(filename, username, high_scores, new_score)

#Do not update or remove
def get_question_data(world_capitals_dict, countries_tested):
    countries = list(world_capitals_dict.keys())
    target_country = countries[random.randrange(0, len(countries))]
    while target_country in countries_tested:
        target_country = countries[random.randrange(0, len(countries))]
    countries_tested.append(target_country)
    countries.remove(target_country)
    cities = [world_capitals_dict[target_country]]
    while len(cities) < 5:
        country = countries[random.randrange(0, len(countries))]
        countries.remove(country)
        cities.append(world_capitals_dict[country])
    random.shuffle(cities)
    return target_country, cities

#Do not update or remove   
main()

