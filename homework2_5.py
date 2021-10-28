import os

cur_path = os.getcwd()

while True:
    user_input = input("say folder or folders name to create or pass to continue or file to create a file ")
    if user_input == "pass":
        pass
    elif user_input == 'file':
        file_add = input("say file name to create or pass for continue ")
        if file_add != 'pass':
            with open(file_add, 'w') as f:
                pass
    else:
        os.makedirs(user_input)
    check = input("finish? ")
    if check == "yes":
        break

while True:
    check = input("wanna delete some folders? if yes tell the name no for pass")

    if os.path.isdir(check):
        list_path = os.listdir(check)
        if list_path:
            print(f"{check} is not empty values {list_path}")
            user_choice = input("tell dir name to enter or pass to ignore")
            if user_choice != "pass":
                new_path = os.path.join(check, user_choice)
                os.chdir(new_path)
        else:
            os.rmdir(check)

    check_file = input("wanna delete some files? if yes tell the name no for pass ")

    if os.path.isfile(check_file):
        os.remove(check_file)

    cd_check = input("wanna change dir no for continue ")
    if cd_check != "no":
        os.chdir(cd_check)

    exit_ = input("exit? no for continue")
    if exit_ != "no":
        break