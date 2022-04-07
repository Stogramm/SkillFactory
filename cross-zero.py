play_area = list(range(1,10))

def draw_board(play_area):
    print ("-" * 13)
    for i in range(3):
        print ("|", play_area[0+i*3], "|", play_area[1+i*3], "|", play_area[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("In which cell will we add " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Incorrect. You need to enter a number?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(play_area[player_answer-1]) not in "XO"):
                play_area[player_answer-1] = player_token
                valid = True
            else:
                print ("This cell is already occupied")
        else:
            print ("Incorrect. Enter a number from 1 to 9")

def check_win(play_area):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if play_area[each[0]] == play_area[each[1]] == play_area[each[2]]:
            return play_area[each[0]]
    return False

def main(play_area):
    counter = 0
    win = False
    while not win:
        draw_board(play_area)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(play_area)
            if tmp:
                print (tmp, "Victory!!!")
                win = True
                break
        if counter == 9:
            print ("Draw!")
            break
    draw_board(play_area)

main(play_area)