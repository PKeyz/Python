alphabet = ['Amore', 'Bella', 'Ciao', 'Dolce', 'Elegante', 'Fragile', 'Grazie', 'Hai', 'Innamorato', 'Joviale', 'Kiss',
            'Luna', 'Mamma', 'Natura', 'Oceano', 'Pasta', 'Quando', 'Ragazzo', 'Sole', 'Terra', 'Uva', 'Vino','Wine', 'Xylophone', 'Yogurt',
            'Zucchero']

name = 'Max'
nato_names = [word for letter in name for word in alphabet if word[0].lower() == letter.lower()]
print(nato_names)
"""
split name into letters
get first letter from capital_letters that is equal to letter in name
get index of that letter from capital_letters
get word in alphabet equal to index of letter in capital_letters


"""
# name_full = [ alphabet[capital_letters[letter]] for letter in name]
# print(name_full)
#
#
# # List Comprehension range
# range_doubled = [ num * 2 for num in range(1,5)]
# print(range_doubled)


#conditional list comprehension
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

capital_names = [name.upper() for name in names if len(name) > 4]
print(capital_names)
