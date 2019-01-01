import subprocess

def title():
    print("""\x1b[1;35;41m                                     TTTTTTTTTTTTTTTTTTTTTTT  iiii                                                             
                                     T:::::::::::::::::::::T i::::i                                                           
                                     T:::::::::::::::::::::T  iiii                                                            
                                     T:::::TT:::::::TT:::::T                                                                  
                                     TTTTTT  T:::::T  TTTTTTiiiiiii     cccccccccccccccc         
                                             T:::::T        i:::::i   cc:::::::::::::::c               
                                             T:::::T         i::::i  c:::::::::::::::::c             
                                             T:::::T         i::::i c:::::::cccccc:::::c             
                                             T:::::T         i::::i c::::::c     ccccccc             
                                             T:::::T         i::::i c:::::c                           
                                             T:::::T         i::::i c:::::c                            
                                             T:::::T         i::::i c::::::c     ccccccc                        
                                           TT:::::::TT      i::::::ic:::::::cccccc:::::c                     
                                           T:::::::::T      i::::::i c:::::::::::::::::c             
                                           T:::::::::T      i::::::i  cc:::::::::::::::c             
                                           TTTTTTTTTTT      iiiiiiii    cccccccccccccccc\n""")           


    print("""\x1b[1;32;41m            TTTTTTTTTTTTTTTTTTTTTTT
            T:::::::::::::::::::::T
            T:::::::::::::::::::::T
            T:::::TT:::::::TT:::::T
            TTTTTT  T:::::T  TTTTTTaaaaaaaaaaaaa      cccccccccccccccc
                    T:::::T        a::::::::::::a   cc:::::::::::::::c
                    T:::::T        aaaaaaaaa:::::a c:::::::::::::::::c
                    T:::::T                 a::::ac:::::::cccccc:::::c
                    T:::::T          aaaaaaa:::::ac::::::c     ccccccc
                    T:::::T        aa::::::::::::ac:::::c
                    T:::::T       a::::aaaa::::::ac:::::c
                    T:::::T      a::::a    a:::::ac::::::c     ccccccc
                  TT:::::::TT    a::::a    a:::::ac:::::::cccccc:::::c
                  T:::::::::T    a:::::aaaa::::::a c:::::::::::::::::c
                  T:::::::::T     a::::::::::aa:::a cc:::::::::::::::c
                  TTTTTTTTTTT      aaaaaaaaaa  aaaa   cccccccccccccccc\n""")


    print("""\x1b[1;34;41m                                                         TTTTTTTTTTTTTTTTTTTTTTT
                                                         T:::::::::::::::::::::T
                                                         T:::::::::::::::::::::T
                                                         T:::::TT:::::::TT:::::T
                                                         TTTTTT  T:::::T  TTTTTTooooooooooo       eeeeeeeeeeee
                                                                 T:::::T      oo:::::::::::oo   ee::::::::::::ee
                                                                 T:::::T     o::::o     o::::oe:::::::::::::::::e
                                                                 T:::::T     o::::o     o::::oe::::::eeeeeeeeeee
                                                                 T:::::T     o::::o     o::::oe:::::::e
                                                               TT:::::::TT   o:::::ooooo:::::oe::::::::e
                                                               T:::::::::T   o:::::::::::::::o e::::::::eeeeeeee
                                                               T:::::::::T    oo:::::::::::oo   ee:::::::::::::e
                                                               TTTTTTTTTTT      ooooooooooo       eeeeeeeeeeeeee\n""")

def game():
    subprocess.call("clear",shell=True)
    title()
    print(""" 1.One player\n 2.Two player\n 3.back\n""")
    selection=int(input("Enter choice:"))
    if selection==2:
        subprocess.call("clear",shell=True)
        main()
    elif selection==3:
        mainMenu()
    else:
        print("Invalid choice. Press enter 1-3!")

def credit():
    subprocess.call("clear",shell=True)
    print("""\x1b[1;33;41m Created by:                 dBBBBBb  dBBBP     dBBBBb      dBBBBb  dBBBP 
                             dB'               dBP dBP                   
                             dBBBP' dBBP      dBP dBP     dBBBB   dBBP    
                             dBP    dBP       dBP dBP     dB' BB  dBP      
                             dBP    dBBBBP    dBP dBP     dBBBBBB dBBBBP\n Peti\n Norbi\n Geri\n""")
    print("1.back")
    selection=int(input("Enter choice:"))                            
    if selection==1:
        mainMenu()
    else:
        print("Invalid choice. Press enter 1!")
    
def win1_score():
    win1=0
    win1+=1
    return win1

def tie_score():
    tie=0
    tie+=1
    return tie

def win2_score():
    win2=0
    win2+=1
    return win2  

def exitgame():
    subprocess.call("clear",shell=True)
    print("Good bye!")
    exit()

def mainMenu():
    subprocess.call("clear",shell=True)
    title()
    print(""" 1.Start\n 2.Credit\n 3.Quit\n""")
    selection=int(input("Enter choice:"))
    if selection==1:
        game()
    elif selection==2:
        credit()
    elif selection==3:
        exitgame()
    else:
        print("Invalid choice. Press enter 1-3!")

def board(map):
    print("|----------|----------|----------|")
    print("|          |          |          |")
    print("|    "+map[1]+"     |    "+map[2]+"     |    "+map[3]+"     |")
    print("|          |          |          |")
    print("|----------|----------|----------|")
    print("|          |          |          |")
    print("|    "+map[4]+"     |    "+map[5]+"     |    "+map[6]+"     |")
    print("|          |          |          |")
    print("|----------|----------|----------|")
    print("|          |          |          |")
    print("|    "+map[7]+"     |    "+map[8]+"     |    "+map[9]+"    |")
    print("|          |          |          |")
    print("|----------|----------|----------|")

def winning_condition(map,state):
    if map[1] == "x" and map[2] == "x" and map[3] == "x" or map[4] == "x" and map[5] == "x" and map[6] == "x" or map[7] == "x" and map[8] == "x" and map[9] == "x" or map[1] == "x" and map[4] == "x" and map[7] == "x" or map[2] == "x" and map[5]  == "x" and map[8] == "x" or map[3] == "x" and map[6] == "x" and map[9] == "x" or map[1] == "x" and map[5] == "x" and map[9] == "x" or map[7] == "x" and map[5] == "x" and map[3] == "x":
        print ("\x1b[1;33;41m Player 1 won:  " + str(win1_score()))
        state == False
        return state
    elif map[1] == "o" and map[2] == "o" and map[3] == "o" or map[4] == "o" and map[5] == "o" and map[6] == "o" or map[7] == "o" and map[8] == "o" and map[9] == "o" or map[1] == "o" and map[4] == "o" and map[7] == "o" or map[2] == "o" and map[5]  == "o" and map[8] == "o" or map[3] == "o" and map[6] == "o" and map[9] == "o" or map[1] == "o" and map[5] == "o" and map[9] == "o" or map[7] == "o" and map[5] == "o" and map[3] == "o":
        print ("\x1b[1;33;41m Player 2 won:  " + str(win2_score()))
        state == False
        return state
    elif " " not in map:
        print("\x1b[1;33;41m Draw:" + str(tie_score()))
        state == False
        return state

def choice(map, counter):
    try:
        cho = int(input("Enter a number: "))
    except ValueError:
        cho = input('press q to return to main menu')
        if cho == 'q':
            mainMenu()
        else:
            subprocess.call("clear",shell=True)
            print('Invalid input')
            board(map)
            choice(map,counter)
    else:
        if counter % 2 == 1:
            if map[cho] != "x":
                map[cho] = "o" 
            else:
                choice(map,counter)
        else:
            if map[cho] != "o":
                map[cho] = "x"
            else:
                choice(map,counter)          
    
    subprocess.call("clear",shell=True)
    board(map)      

def main():   
    map = ["1"," "," "," "," "," "," "," "," "," "]
    i = 0
    counter = 0
    run = True
    while run == True:
        board(map)
        choice(map,counter)
        subprocess.call("clear",shell=True)
        if winning_condition(map,run) == True:
            break
        i += 1
        counter +=1
    restart = input("Press r to restart ") 
    if restart == "r":
        main()
    else:
        print("Invalid input")
mainMenu()
main()