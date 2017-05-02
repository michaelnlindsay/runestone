
import random

def fill_random(guess):
    """
    fill_random(list) -> list
    
    replaces all occurences of _ with a radmon lower case letter
    or space
    """
    letters = 'abcdefghijklmonpqrstuvwxyz '
    for i in range(len(guess)):
        if (guess[i] == None):
            guess[i] = letters[random.randrange(0, len(letters))]
    return guess

def score_string(guess, target):
    score = 0
    for i in range(len(guess)):
        if guess[i] == target[i]:
            score += 1
        else:
            guess[i] = None

    return score

def start_monkeys():
    target_string = 'methinks it is like a weasel'
    best_result = ['_'] * len(target_string)
    best_score = -1
    for i in range(1000):
        guess = fill_random(best_result)
        score = score_string(guess,target_string)
        if score > best_score:
            best_result = guess
            best_score = score
            print(best_result, best_score, i)
            if best_score == len(target_string):
                print('Monkeys Win!')
                break


start_monkeys()