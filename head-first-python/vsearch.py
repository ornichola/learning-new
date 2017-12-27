def search4vowels(phrase:str) -> set:
    """Выводит гласные, найденные в указанной фразе."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str) -> set:
    """
    Выводит множество символов, найденных в указанной фразе,
    по переданному паттерну.
    """
    return set(letters).intersection(set(phrase))

print(search4letters('hitch-hiker', 'aeiou'))
print(search4letters('galaxy', 'xyz'))
print(search4letters('life, the universe, and everything', 'o'))
