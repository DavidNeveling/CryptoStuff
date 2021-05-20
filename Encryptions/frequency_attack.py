from collections import defaultdict

ORDERED_FREQUENCIES = 'etaoinshrdlcumwfgypbvkjxqz'

def calc_freqs(message):
    freqs = defaultdict(lambda: 0)
    for character in message:
        freqs[character] += 1
    return freqs

def ordered_characters_from_freq(freq_dict):
    return ''.join(sorted([(key, freq_dict[key]) for key in freq_dict.keys()],key=lambda t: t[1]))

def attack(encryption):
    character_freqs = calc_freqs(encryption)
    ordered_characters = ordered_characters_from_freq(character_freqs)
    message_guess = ''
    for character in encryption:
        index = ordered_characters.find(character)
        if index >= 26:
            message_guess += ' '
        else:
            message_guess += ORDERED_FREQUENCIES[index]
    return message_guess