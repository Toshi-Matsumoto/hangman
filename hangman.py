#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#完全なゲームのコード

#ハングマン
import random

def hangman():
    wrong = 0
    stages = ["", 
              "____________         ",
              "|                    ", 
              "|           |        ", 
              "|           0        ", 
              "|          L|j       ", 
              "|          / L       "
             ]
    words_list = ["dog", "cat", "bird", "tiger", "lion"]
    random_num = random.randint(0, len(words_list)-1)
    cor_word = words_list[random_num]
    rletters = list(cor_word)
    board = ["_"] * len(cor_word)
    win = False
    print("ハングマンへようこそ！")
#ゲームのループ処理    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を入力してね : "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

#勝った時の処理
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
#負けた時の処理

    if not win:
        print("\n".join(stages[0:wrong +1]))
        print("あなたの負け！正解は{}.".format(cor_word))
        
        
hangman()

