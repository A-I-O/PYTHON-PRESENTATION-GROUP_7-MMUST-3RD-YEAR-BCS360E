class Get_score:
    def Event(self, scorekeeper_input):
        if scorekeeper_input == 'H':
            return 'D'
        elif scorekeeper_input == 'C':
            return 'C'
        elif scorekeeper_input == 'CO':
            return 5
        else:
            return -2


user_input = []

print("..........RECORD Score as:\n\t\t\033[32m H for HOMERUN\n \t\t C for CATCH\n\t\t CO for COMPLETE\n\t\t M for "
      "MISS \nTYPE 'GAME HALTED' WHEN TEAM FAILS TO CONCLUDE GAME ")

for i in range(1, 8):
    print("\033[1;40m\t\t\033[36m_______\tROUND ", i, "_______")
    Scorekeeper_Input = str(input("\t\033[33;1mEnter the Score:\n")).upper()

    if Scorekeeper_Input == 'H':
        #      for p in range(len(user_input)):
        if user_input == []:
            for r in range(len(user_input)):
                user_input.append(2 * (user_input[-1]))
        else:
            user_input.append(2 * (user_input[-1]))

    elif Scorekeeper_Input == 'C':
        k = 2
        user_input = user_input[:len(user_input) - k]
    elif user_input == [-2, -2, -2, -2, -2, -2, ]:
        user_input.clear()
        # user_input.append(-2)

    if Scorekeeper_Input == 'H' or Scorekeeper_Input == 'CO' or Scorekeeper_Input == 'M' or Scorekeeper_Input == 'C':
        event = Get_score().Event(Scorekeeper_Input)
        user_input.append(event)
        print("\033[32mSCOREBOARD= ", user_input)

    if Scorekeeper_Input == 'GAME HALTED':
        print('\033[31mTEAM FAILED TO CONCLUDE GAME, PRELIMINARY SCORES ARE AS FOLLOWS:')
        #      event = Get_score().Event(User_Event_Input)
        #      user_input.append(event)
        print("\033[32mSCOREBOARD= ", user_input)
        break
    if Scorekeeper_Input != 'H' and Scorekeeper_Input != 'CO' and Scorekeeper_Input != 'M' and Scorekeeper_Input != 'C'\
            and Scorekeeper_Input != 'GAME HALTED':
        k = 0
        while k < 1:
            print("\033[31mYou entered an incorrect score. Please enter score AGAIN ")
            print("\t\t\033[36m_______\tROUND ", i, "_______")
            Scorekeeper_Input = str(input("\t\033[33mEnter the Score:\n")).upper()

            event = Get_score().Event(Scorekeeper_Input)
            user_input.append(event)
            k += 1
        print("\033[32mSCOREBOARD= ", user_input)
