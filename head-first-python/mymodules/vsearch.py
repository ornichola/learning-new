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
