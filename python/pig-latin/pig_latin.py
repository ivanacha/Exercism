def translator(word):
    vowels = 'aeiouAEIOU'
    qu_index = word.find("qu")
    
    # Rule 1: Word starts with a vowel or 'xr' or 'yt'
    if word[0] in vowels or word.startswith('xr') or word.startswith('yt'):
        return word + 'ay'
    
    # Rule 3: Word starts with consonant(s) followed by 'qu'
    if qu_index > 0:
        return word[qu_index + 2:] + word[:qu_index + 2] + "ay"
    
    # Rule 4: Word starts with 'y'
    if word.startswith('y'):
        return word[1:] + word[0] + "ay"
    
    # Rule 2: Word starts with consonant(s)
    for id, letter in enumerate(word):
        if word[id:].startswith('qu'):
            word = word[id+1:] + word[:id+1]
        if letter in vowels or letter == 'y':
            return word[id:] + word[:id] + 'ay'
    
    return word + 'ay'
            
def translate(text):
    # Split the text into words
    words = text.split()
    
    # Translate each word and join them back together
    translated_words = [translator(word) for word in words]

    # Join the translated words back into a sentence
    return ' '.join(translated_words)
