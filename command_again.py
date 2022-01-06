def compute_again():
    proceed = int(input("\nВведите 1, что бы повторить программу или 0, что бы выключить программу    "))
    if proceed == 1:
        return True
    elif proceed == 0:
        return False
    else:
        while True:
            proceed_error = int(input("\nВы ввели неправильную команду, повторите действие:"
                                      "\nВведите 1, что бы повторить программу или 0, что бы выключить программу    "))
            if proceed_error == 1:
                return True
            elif proceed_error == 0:
                return False
