def translator(text):
    vowels = 'aeiouAEIOU'
    qu_index = text.find("qu")
    if text[0] in vowels or text.startswith('xr') or text.startswith('yt'):
            return text + 'ay'
    if qu_index > 0:
        return text[qu_index + 2:] + text[:qu_index + 2] + "ay"
        
    if text.startswith('y'):
        return text[1:] + text[0] + "ay"
        
    for id, letter in enumerate(text):
        if text[id:].startswith('qu'):
            text = text[id+1:] + text[:id+1]
        if letter in vowels or letter == 'y':
            return text[id:] + text[:id] + 'ay'
            
def translate(text):
    # Split the text into words
    words = text.split()
    
    # Translate each word and join them back together
    translated_words = [translator(word) for word in words]

    # Join the translated words back into a sentence
    return ' '.join(translated_words)

    # tranlsation = text.split()
    # for word in tranlsation:
    #     qu_index = word.find("qu")
    #     if word[0] in vowels or word.startswith('xr') or word.startswith('yt'):
    #             return word + 'ay'
    #     if qu_index > 0:
    #         return word[qu_index + 2:] + word[:qu_index + 2] + "ay"
            
    #     if word.startswith('y'):
    #         return word[1:] + word[0] + "ay"
            
    #     for id, letter in enumerate(word):
    #         if word[id:].startswith('qu'):
    #             word = word[id+1:] + word[:id+1]
    #         if letter in vowels or letter == 'y':
    #             word = word[id:] + word[:id] + 'ay' 
    # return text
