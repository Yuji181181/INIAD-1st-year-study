def minmax(opponent_hand):

    hands = ["G", "C", "P"]
    scores = {"G": 0, "C": 0, "P": 0}

    if opponent_hand == "G":
        scores["P"] = 6  # グーに対してパーで勝ち
        scores["G"] = 1  # グーに対してグーで引き分け
    elif opponent_hand == "C":
        scores["G"] = 6 # チョキに対してグーで勝ち
        scores["C"] = 1 # チョキに対してチョキで引き分け
    elif opponent_hand == "P":
        scores["C"] = 6 # パーに対してチョキで勝ち
        scores["P"] = 1 # パーに対してパーで引き分け


    best_hand = max(scores, key=scores.get)
    best_score = scores[best_hand]


    return best_hand, best_score


# 全ての相手の手に対して最適な手を計算
opponent_hands = ["G", "C", "P"]
for opponent_hand in opponent_hands:
    my_hand, score = minmax(opponent_hand)
    print(f"相手の手が {opponent_hand} の時、最適な手は {my_hand} で、得点は {score} です。")