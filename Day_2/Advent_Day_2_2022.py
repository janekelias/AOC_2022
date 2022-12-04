# open and read .txt file
with open("input_2.txt") as file_object:
    cheat_list = file_object.read()
# split by line \n for each round of game
    round_list = cheat_list.split("\n")
    print(round_list) # check
    opponent_sign = []
    player_sign = []
    for round_tactic in round_list:
        # separate by whitespace to create list of opponents and players signs
        a,b = round_tactic.split()
        opponent_sign.append(a)
        player_sign.append(b)

    print(opponent_sign) # check
    print(player_sign)
    print("\n\n\n")
    psign_list = []
    osign_list = []
    # determine sign in player store in new list
    for psign in player_sign:
        if psign == "X":
            cur_p_sign = "ROCK"
        elif psign == "Y":
            cur_p_sign = "PAPER"
        elif psign == "Z":
            cur_p_sign = "SCISSORS"
        psign_list.append(cur_p_sign)
    print(psign_list)
    # determine sign in opponent store in new list
    for osign in opponent_sign:
            if osign == "A":
                cur_o_sign = "ROCK"
            elif osign == "B":
                cur_o_sign = "PAPER"
            elif osign == "C":
                cur_o_sign = "SCISSORS"
            osign_list.append(cur_o_sign)
    print(osign_list)

    print(len(round_list))
    ind = 0
    result_list = []

    while ind <= 2499:
        if osign_list[ind] == "ROCK" and psign_list[ind] == "ROCK":
            result = "DRAW"
        elif osign_list[ind] == "ROCK" and psign_list[ind] == "PAPER":
            result = "WIN"
        elif osign_list[ind] == "ROCK" and psign_list[ind] == "SCISSORS":
            result = "LOSE"
        elif osign_list[ind] == "PAPER" and psign_list[ind] == "ROCK":
            result = "LOSE"
        elif osign_list[ind] == "PAPER" and psign_list[ind] == "PAPER":
            result = "DRAW"
        elif osign_list[ind] == "PAPER" and psign_list[ind] == "SCISSORS":
            result = "WIN"
        elif osign_list[ind] == "SCISSORS" and psign_list[ind] == "ROCK":
            result = "WIN"
        elif osign_list[ind] == "SCISSORS" and psign_list[ind] == "PAPER":
            result = "LOSE"
        elif osign_list[ind] == "SCISSORS" and psign_list[ind] == "SCISSORS":
            result = "DRAW"
        result_list.append(result)
        ind = ind + 1
    print("\n")
    print(result_list)
    resolut_points = 0
    for resolut in result_list:
        if resolut == "DRAW":
            resolut_points = resolut_points + 3
        elif resolut == "LOSE":
            resolut_points = resolut_points
        elif resolut == "WIN":
            resolut_points = resolut_points + 6
    print("\nResolution points are: ")
    print(resolut_points)
    sign_points = 0
    for psigp in psign_list:
        if psigp == "ROCK":
            sign_points = sign_points + 1
        elif psigp == "PAPER":
            sign_points = sign_points + 2
        elif psigp == "SCISSORS":
            sign_points = sign_points + 3
    print("\n point values for signs only is: ")
    print(sign_points)

    print("\nTogether the final point value is:")
    print(resolut_points + sign_points)

