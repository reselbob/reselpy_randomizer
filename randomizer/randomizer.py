import json
import random
import os.path

class Randomizer:

    def json_loader(json_file_spec):
        path  = os.path.join(os.path.dirname(__file__), json_file_spec)
        with open(path) as json_data:
            d = json.load(json_data)
            json_data.close()
            return d;
    secure_random = random.SystemRandom()
    cities = json_loader('data/cities.js')
    first_names = json_loader('data/first_names.js')
    last_names = json_loader('data/last_names.js')
    words = json_loader('data/words.js')
    extensions = ['com', 'net', 'org', 'io', 'tv']
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+'

    @staticmethod
    def get_random_address():
        return Randomizer.secure_random.choice(Randomizer.cities)
    @staticmethod
    def get_random_first_name():
        return Randomizer.secure_random.choice(Randomizer.first_names)
    @staticmethod
    def get_random_last_name():
        return Randomizer.secure_random.choice(Randomizer.last_names)
    @staticmethod
    def get_random_email(first_name, last_name):
        company = Randomizer.get_random_phrase(1)
        ext = Randomizer.secure_random.choice(Randomizer.extensions)
        return '{}.{}@{}.{}'.format(first_name, last_name, company, ext)
    @staticmethod
    def get_random_string(max_length):
        str = ''
        length = random.randint(1, max_length)
        count = 0
        while (count < length):
            s = Randomizer.alphabet[random.randint(0, len(Randomizer.alphabet)-1)]
            if( random.randint(1, 1000) % 2 == 0):
                s = s.upper()
            str = str + s
            count += 1
        return str
    @staticmethod
    def get_random_phrase(number_of_words):
        words = ''
        count = 0
        while (count < number_of_words):
            word = Randomizer.secure_random.choice(Randomizer.words)
            if(count == 0):
                words = word
            else:
                words += ' {}'.format(word);
            count += 1
        return words
    @staticmethod
    def get_random_int(min, max):
        return random.randint(min, max)
    @staticmethod
    def get_random_float(min, max):
        return random.uniform(min, max)


