def get_formatted_name(first_name, last_name):
    full_name = (f"{first_name.title()} {last_name.title()}")
    return full_name.title()

while True:
    print("please enter your name")
    print("(press q at any time to quit)")
    
    f_name = input("What is your first name?")
    if f_name == 'q':
        break

    l_name = input("what is your last name?")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}.")
