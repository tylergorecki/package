def ret_last_n(word:str, n:int):
    '''returns last n letters of a string'''
    if len(word) <= n: return "length of word must be greater than n"

    return word[-n:]
