#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:49:02 2020

@author: aireesrondain
"""

# -*- coding: utf-8 -*-


pinoy_kakanin = {}    # create an empty dictionary

pinoy_kakanin['biko'] = 'It is made of coconut milk, brown sugar, and glutinous rice. It is usually topped with latik.'
pinoy_kakanin['bibingka'] = 'It is usually eaten for breakfast, especially during the Christmas season. It is traditionally cooked in clay pots lined with leaves.'
pinoy_kakanin['suman'] = 'It is made from glutinous rice cooked in coconut milk, often wrapped in banana leaves, coconut leaves, or buli or buri palmleav es for steaming. It is usually eaten sprinkled with sugar or laden with latik.'
pinoy_kakanin['palitaw'] = 'From litaw, the Tagalog word for "float" or "rise", is a small, flat, sweet rice cake made from galapong-washed, soaked, and ground malagkit'
pinoy_kakanin['turon'] = 'A Pinoy snack made of thinly sliced bananas (preferably saging na saba), dusted with brown sugar, rolled in a spring roll wrapper and fried.'
pinoy_kakanin['puto bumbong'] = 'is a type of street food also traditionally served during the Christmas season.'
pinoy_kakanin['sapin-sapin'] = 'colorful layers of glutinous rice and coconut dessert made from rice flour, coconut milk, sugar, water, flavoring and coloring. It is usually sprinkled with latik or toasted desiccated coconut flakes.'
pinoy_kakanin['puto'] = 'are Filipino steamed rice cakes, eaten as is or as an accompaniment to a number of savoury dishes (most notably, dinuguan).'
pinoy_kakanin['kutsinta'] = 'It is made from a mixture of tapioca or rice flour, brown sugar and lye, enhanced with yellow food coloring or annatto extract, and steamed in small ramekins.'
pinoy_kakanin['maja blanca'] = 'made with coconut milk, sweet corn kernels, and toasted coconut.'


def kakanin_game(score):   # question and answer portion and scoring
    for meaning in pinoy_kakanin.values():
        print("\nQuestion: %s" % meaning)
        answer = input("Answer: ")
        if answer in pinoy_kakanin:
            score = score + 1
        else:
            score = score + 0
    return(score)


print("\n<<< Let's test your Pinoy Kakanin Level>>>")
name = input("\nWhat is your name? ")

print("\nHi " + name.title() + ". Game ka na ba?")

score = 0.  # initialize variable
dsize = len(pinoy_kakanin)   # get the size of the dictionary

final_score = int(kakanin_game(score))  # converts to integer

print("\n", name.title() + ',' + " you scored ", final_score, " out of", dsize)

percentage = final_score/dsize * 100  # converting to percentage score

print("Your grade is: %0.2f" % percentage, "%")  # round to 2 decimal places
if percentage >= 70:  # passing grade
    print(">>> Congratulations, you're a Certified Pinoy Kakainin Expert <<<")
else:
    print(">>> Sorry, kain pa more! <<<")
