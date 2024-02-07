unconfirmed_users = ['bruh', 'antohberhfs', 'dbjtg', 'dbfjyt',]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Currently verifying {current_user}.")
    confirmed_users.append(current_user)

for confirmed_user in confirmed_users:
    print("\nthis user has been verified:")
    print(f"{confirmed_user}")