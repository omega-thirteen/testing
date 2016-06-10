#!/usr/bin/env python


def calc_birthday_prob(n):
    '''
    Calculates the probability of at least two people in a group of size
    n having the same birthday.

    INPUTS: n (integer): number of people in the group
    OUTPUTS: p (float): probability of matching birthday
    '''

    prob = 1
    for x in range(1, n):
        prob *= (365 - x)/365
    return 1 - prob

if __name__ == '__main__':
    for x in range(60):
        print(x, calc_birthday_prob(x))
