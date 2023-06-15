# I saw a livestream of a guy mapping a vector in C and I wanted to do the same thing he did in Python, however
# I wanted to create another list so that They can be stored

def mapwords(phrase):
    return [word for word
            in phrase.split()
            if phrase.isalpha
            # Not calling the isalpha() because it needs
            # parameters that we don't need to fulfill
            ]


lista = "Essa é a minha frase"
word_list = list(
    map(
        mapwords, [lista]
    )
) # [0]

print(word_list)
