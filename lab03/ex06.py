while True:
    val = input("Enter a number or stop to exit: ")
    if val.lower() == 'stop':
        print('Thank you ! Existing the program')
        break
    else:
        cube = int(val)
        epsilon = 0.01
        guess = 0.0
        increment = 0.0001
        num_guesses = 0
        while abs(guess**3 - cube) >= epsilon:
            guess += increment
            num_guesses += 1
            print('num_guesses =', num_guesses)
            if abs(guess**3 - cube) >= epsilon:
                print('Failed on cube root of', cube)
            else:
                print(guess, 'is close to the cube root of', cube)