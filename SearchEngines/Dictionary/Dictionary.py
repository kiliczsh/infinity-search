import requests


def search_word(word):
    try:
        definition = requests.get('https://owlbot.info/api/v4/dictionary/' + word.lower(),
                                  headers={'Authorization': 'Token ' + '4ace25e2f5a04b106f15b11d737365118a722a2a'},
                                  timeout=1).json()
        if definition['definitions'][0] is not None:
            definition = definition['definitions'][0]

            word_type = definition['type']
            define = definition['definition']
            example = definition['example']
            image_url = definition['image_url']

            if word_type is None:
                word_type = ''

            if define is None:
                define = ''

            if example is None:
                example = ''

            if image_url is None:
                image_url = ''

            return [[word, word_type, define, example, image_url]]

    except Exception:
        return []


if __name__ == '__main__':
    search_word('owl')
