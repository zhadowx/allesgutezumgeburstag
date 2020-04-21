def search_for_vowels(word:str) -> set:
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word)) 

print(search_for_vowels('Sky'))
help(search_for_vowels)