# Checking usernames

current_users = ['steve', 'admin', 'cyrill', 'jane', 'sergio', 'TOM']
new_users = ['steve', 'cyrill', 'amanda', 'arnold', 'tom']

if current_users:
    current_users = [user.lower() for user in current_users]
else:
    print("List of current users is empty")
    
if new_users:
    for new_user in new_users:
        if new_user in current_users:
            print(f"{new_user.title()} - You need to take another name")
        else:
            print(f"{new_user.title()} - This name is availiable!")
else:
    print("List of new users is empty")