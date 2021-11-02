def show_choices():
    print('\n=================================')
    print('choose from an option below')
    print('1.Ejo')
    print('2.Hayder')
    print('3.Majed')
    print('4.Ninos')
    print('5.Thor')
    print('6.Exite')
    print('=================================')

choices = [1,2,3,4,5,6]

def is_choice(value):
    try:
        int_val = int(value)
        if int_val in choices:
            return True
        else:
            return False
    except:
        return False

dic_func = {1:GetPCInfo,2:greeting,3:start_calc,4:start_cal,5:dragons_lair}

def start_app():
    while True:
        show_choices()
        choice = int(input("Please make your choice: "))
        while is_choice(choice) == False:
            choice = int(input(f"Please make your right choice between ({str(choices[0])}-{str(choices[-1])}): "))
        if choice in choices:
            if choice == 1:
                print(dic_func[choice]())
                ask = input('Want to make anothe choice y/n: ').lower()
                if ask == 'n':
                    break
            elif choice == 2:
                user_greeting = input("Enter Your Name: ")
                dic_func[choice](user_greeting)
                ask = input('Want to make anothe choice y/n: ').lower()
                if ask == 'n':
                    break
            elif choice == 3:
                dic_func[choice]()
                ask = input('Want to make anothe choice y/n: ').lower()
                if ask == 'n':
                    break
            elif choice == 4:
                dic_func[choice]()
                ask = input('Want to make anothe choice y/n: ').lower()
                if ask == 'n':
                    break
            elif choice == 5:
                dic_func[choice]()
                ask = input('Want to make anothe choice y/n: ').lower()
                if ask == 'n':
                    break
            elif choice == 6:
                print("======== Thanks The Program Has Been Terminated By The User ========")
                break    
        else:
            print("Please, chose the corect option!!")  
start_app()