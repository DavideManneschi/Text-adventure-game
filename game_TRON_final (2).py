import random
import sys
import time
import random


def enter_virtual_world():
    credentials = {

        "username": ["flynn"],

        "password": ["encom"]

    }

    print("ACCESSING ENCOM REMOTE TERMINAL...")
    time.sleep(1)

    for i in range(2, 0, -1):
        print(i, "..........")
        time.sleep(.7)

    whoami = input("Do you have an ENCOM account?[yes/no]")

    while True:

        if whoami == "yes" :
            user_name = input("username>")
            password = input("password>")

            if user_name in credentials["username"] and password in credentials["password"]:


                enter_grid = input(f"hello {user_name}\n"
                              f"Press [1]--->for the GRID\n"
                              f"press[2]--->Shut Down\n"
                              f"Insert your choice>")

                if enter_grid == "1":

                    print("Entering the GRID.....")

                    for i in range(10, 0, -1):
                        print("ETA ", i, ".....")


                        time.sleep(0.5)
                    break



                elif enter_grid == "2":
                    sys.exit(0)


            else:
                main = input("*****WARNING*****\n"
                            "invalid credential, try again,press any key to try again\n"
                             "or press [0] to return to the option selection.\n"
                             "*****************"
                             "\n"
                             "Insert your choice>")
                if main == "0":
                    enter_virtual_world()

                    print("\n")

                    break

















        elif whoami == "no":

            while True:

                new_userame = input("select new username>")
                new_password = input("select new password>")
                password_confirmation = input("confirm new password>")
                if new_password == password_confirmation:

                    credentials["username"].append(new_userame)
                    credentials["password"].append(new_password)
                    print("the database has been updated with your data", credentials)

                    break

                else:
                    print("the two passwords do not match,\n"
                          "please insert credentials again!\n"
                          "")

            enter_grid = input(f"Welcome User {new_userame}, your password is {new_password}\n"
                               f"----------------------------------------------------------------\n"
                               f"The GRID  is a research platform  utilized by  ENCOM founder,\n"
                               f"Kevin Flynn to conduct research at unparallelled speeds.\n"
                               f"The time in the GRID is measured in cycles which are a fraction of the normal time...\n"
                               f"----WARNING----\n"
                               f"INSIDE THE GRID YOU WLL FACE MANY CHALLENGES\n"
                               f"AND FIGHT POSSIBLE ENEMIES, BEWARE!\n"
                               f"-----------------------------------\n"
                               f"-----------------------------------\n"
                               f"Press [1]--->for the GRID\n"
                               f"press[2]--->Shut Down\n"
                               f"Insert your choice>")

            if enter_grid == "1":

                print("Entering the GRID.....")

                for i in range(10, 0, -1):
                    print("ETA ", i, ".....")

                    time.sleep(0.5)
                break



            elif enter_grid == "2":
                sys.exit(0)


        elif whoami!= "yes" or "no":

            print("invalid selection!!")
            enter_virtual_world()
        break









def game_selection():



    serial_number = random.randint(0, 1000)

    actions_options = ["disk_wars", "motorbike_race"]

    while True:

        memory_disk = []
        print(f"User you are now in the GRID...\n"
          "You have been assigned a memory disc\n"
          f"with the serial number {serial_number}\n"
          f"you will append your new skills, abilities and memories\n"
          f"to  your memory_disk{memory_disk}")

        print("what do you want to do in the grid?", actions_options)
        actions_grid = input(f"press [0] to select {actions_options[0]}\n"
                         f"press [1] to select {actions_options[1]}\n"
                         "choice>")

        if actions_grid == "0":
            return disk_wars()


        elif actions_grid == "1":
            return motorbike()

        elif actions_grid!="0"or "1":
            print("invalid selection!")
            game_selection()
        break



def disk_wars():
    opponents_disk_war = [["Opponent_1", "difficulty:10"], ["Opponent_2", "difficulty:50"], ["TRON", "difficulty:90"]]

    list_moves = [["tron", "clu", "quorra"], ["creative", "diskwar", "programs"],
                  ["userslive", "cludies", "encomisthebest"]]

    counter = 0

    begin = input("\n"
                  "You are entering DISK WARS!!\n"
                  "****************INSTRUCTIONS***************\n"
                  "to become the champion of DISK WARS \n"
                  "you need to win three fights,\n"
                  "each fight is incrementally more difficult\n"
                  "to win you need to WRITE THE SAME WORD OF YOUR OPPONENT  for three times\n"
                  "********************************************\n"
                  "\n"
                  "press[1] if ready\n"
                  "press[0] if you want to exit the grid\n"
                  "\n"
                  "choice>")

    if begin == "1":

        while True:
            for i, j in zip(opponents_disk_war, list_moves):
                for z in range(1):
                    random_word = random.choice(j)
                    print("*****", z, " round about to begin*****\n"
                                      "you are facing", (i),
                          "\n"
                          "\n")

                    time.sleep(2)
                    print("opponent word selection::", random_word)

                    user_input = input("insert the word::")

                    if user_input == random_word:
                        counter += 1

            if counter == 3:

                print("\n"
                      "YOU ARE THE DISK WAR CHAMPION!!!\n"
                      "CONGRATULATIONS USER!!!")

                while True:

                    decision = input("what do you eant to do now?[exit_grid==>[0]]\n"
                                     "[end_of_line_club==>[1]]\n"
                                     "[motorbike_race==>[2]]\n"
                                     "your choice>")

                    if decision == "0":
                        print("Exiting the GRID.....")

                        for i in range(10, 0, -1):
                            print("ETA ", i, ".....")

                            time.sleep(0.5)
                        sys.exit(0)




                    elif decision == "1":

                        fail()

                    elif decision == "2":

                        motorbike()
                        break


                    else:
                        print("Sorry invalid input")

                break

            else:

                print("you mistaken  some words,\n"
                      " please try again!\n"
                      "\n"
                 )
    elif begin=="0":
        sys.exit(0)


def motorbike():
    counter = 0
    round_counter = 0
    list_moves = ({

        "opponents_moves": [["w", "s", "s"], ["a", "w", "s"], ["s", "s", "a"]],

        "player_moves": [["s", "w", "w"], ["d", "s", "w"], ["w", "w", "d"]],

    })

    begin = input("\n"
                  
                  "You are entering  MOTORBIKE RACE!!\n"
                  
                  "****************INSTRUCTIONS***************\n"
                  "to survive MOTORBIKE RACE  \n"
                  "you need to drive your motorbike,\n"
                  "using the keywords --w--,--a--,--s--,--d--\n"
                  "to win you need to avoid the other motorbike by selecting\n"
                  "the opposite key 3 times:\n"
                  "i.e.\n"
                  "OPPONENT MOVE==>w\n"
                  "YOUR MOVE==>s\n"
                  "\n"
                  "OPPONENT MOVE==>a\n"
                  "YOUR MOVE==>d\n"
                  "*******************************************\n"
                  "\n"
                  "press[1] if ready\n"
                  "press[0] if you want to exit the grid\n"
                  "\n"
                  "choice>")

    if begin == "1":

        while True:

            for z, i in zip(list_moves["opponents_moves"], list_moves["player_moves"]):
                for x, y in zip(z, i):
                    for ii in range(1):

                        time.sleep(2)
                        print("opponent word selection::", x)

                        user_input = input("insert the opposite key::")

                        if user_input == y:
                            counter += 1
                            if counter == 3:
                                print("CONGRATULATIONS,\n"
                                      "YOU SURVIVED THE MOTORBIKE RACE!!")



                                while True:

                                    decision = input("what do you want to do now?\n"
                                                     "\n"
                                                     "[exit_grid==>[0]]\n"
                                                     "[end_of_line_club==>[1]]\n"
                                                     "[disk_wars==>[2]]\n"
                                                     "your choice>")

                                    if decision == "0":
                                        print("Exiting the GRID.....")

                                        for i in range(10, 0, -1):
                                            print("Exiting the grid in -- ", i, ".....")

                                            time.sleep(0.5)
                                        sys.exit(0)




                                    elif decision == "1":

                                        fail()

                                        break



                                    elif decision == "2":

                                        disk_wars()
                                        break




                                    else:

                                        print("\n"
                                              "Sorry invalid input"
                                              "\n")

                                break

                            break



                        else:

                            print("\n"
                                  "ouch!,you crashed!!, try again "
                                  "\n")

                        break
                    break


                pass



            pass

    elif begin=="0":
        sys.exit()




def fail():
    for i in range(6):

        if i == 0:

            time.sleep(1)

            print("****** END OF LINE CLUB******\n")
        else:
            print("..........")
            time.sleep(1)

    print("\n")
    time.sleep(1)

    print("Castor: Hello my friend! what a sparkling day you have been having!\n"
          "In the GRID no ones talks about anything else besides the rumors about the return of THE SON OF THE CREATOR!\n"
          "Are those rumors true??\n")

    time.sleep(1)

    print("Clu: That is none  of your business Castor, remember,\n"
          "you work for me, i own you after  i let you live with  what happened with the ISO's...  \n")

    time.sleep(1)

    print("CASTOR: Of course, Of course, i would never even think to disrespect you... my Leader... \n")

    time.sleep(1)

    print("Clu: If you see him you know what to do...\n")

    time.sleep(1)

    print("Castor: Considered it done\n")

    for i in range(3):
        print("..........")

        time.sleep(1)

    print("USER IS ENTERING THE END OF LINE CLUB\n")

    time.sleep(.1)

    print("User: Castor,... i am looking for zuus...  ")

    time.sleep(.1)

    print("Castor:Indeed, many are...  ")

    time.sleep(.1)

    print("User: Where i can find him?, will you help me?  ")

    time.sleep(.1)

    print("Castor: you know, once i fought for the Users, hide the ISO's from CLU persecution\n"
          "but today, i  conspire with CLU for the end of the USERS...AHAHAHAH...\n"
          "GUARDS!!...KILL HIM!!")

    for i in range(3):
        print("..........")

        time.sleep(.1)

    decision_user = input("Quorra: User, you have to make a decision,\n"
                          "what should we do??[[fight]/[run]/[cheat_code]]\n"
                          "your choice>")

    if decision_user == "fight":

        action=input("you are fighting the guards...\n"
              "choose your attack[punch/kick/throw]\n"
              "your choice>")

        if action=="kick":
            print("you tried to kick the guard,but  the guard parries and arrests you!! ")

            sys.exit()
        elif action=="punch":

            print("you punch  the guard,but the guard has an helmet and you break your hand!! ")
            sys.exit()


        elif action=="throw":

            print("you throw the guard away,you are free to escape!")
            sys.exit()





    elif decision_user == "run":
        print("you ran away, but your are caught by the guards!! you are dead meat")

    elif decision_user == "cheat_code":

        print("\n"
              "you used cheat codes, you decided to nuke the whole GRID!")


        decision_to_go = input("do you want to exit the GRID before nuking it?[y/n]")

        if decision_to_go == "y":

            print("Exiting the GRID.....")

            for i in range(10, 0, -1):
                print("Exiting the grid in -- ", i,)

                time.sleep(0.5)

            print("The grid is nuked!")
            sys.exit(0)

        else:

            print("You are dead!")

            sys.exit(0)


if __name__ == "__main__":
    enter_virtual_world()
    game_selection()

