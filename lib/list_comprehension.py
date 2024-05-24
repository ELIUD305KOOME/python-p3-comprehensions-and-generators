#!/usr/bin/env python3

def return_evens(num_list):
    if num_list == []:
        return []
    else:
        even_nums = [num for num in num_list if num % 2 == 0]
        return even_nums

def make_exclamation(sentence_list):
    if not sentence_list:
        return []
    else:
        exclamated_sentences = [sentence + "!" for sentence in sentence_list]
        return exclamated_sentences




