import os

FILE = "dice_score.txt"

def save(result):
    with open(FILE, "a") as f:
        f.write(result + "\n")

def get():
    scores = {"Player": 0, "Computer": 0, "Draw": 0}

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for line in f:
                r = line.strip()
                if r in scores:
                    scores[r] += 1

    return scores