prompt = "please enter the name of a city you have visited"
prompt += "\n Enter quit to end the program"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"Id love to go to {city.title()}!")