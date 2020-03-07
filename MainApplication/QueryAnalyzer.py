

search_topics = {
    # Openweather integration
    'weather': 'weather',

    # Calculator
    'calculator': 'calculator',

    # Graph
    'graph': 'graph',
    'graphing': 'graph',
    'graphing calculator': 'graph',

    # Wikivoyage # TODO
    'travel': 'travel',

    # Wiktionary, owlbot as backup
    'define' : 'definition',
    'definition' : 'definition',
    'meaning' : 'definition',
    'etymology' : 'etymology',

    # Maps
    'map' : 'map',

    # Tradingview
    'stock' : 'stock',
    'crypto' : 'crypto',
    'stock news' : 'stock news',
    'investing': 'investing',  # Tradingview widget

    # Stopwatch TODO:
    'stopwatch' : 'stopwatch',

    # Make a custom editor widget # TODO
    'javascript' : 'javascript_editor',
    'html': 'html_editor',
    'html editor': 'html_editor',
    'css': 'html_editor',


    # Integrate the codepen widget # TODO
    'codepen editor': 'codepen_editor',

    # TODO
    '@' : 'social_media',

    # Integrate cheat sheets from online and DDG IA  # TODO
    'git usage' : 'git cheat sheet',
    'git': 'git cheat sheet',

    # Shows something cool (integrated into the webpage) # TODO
    'show me something' : 'something_random',

    # Find a score API # TODO
    'score': 'sports',

}


def weather_search(words):
    # words = words.split()
    city = ''
    word_length = len(words)
    if word_length > 4:
        return False

    if words[0].upper() == 'WEATHER':
        for word in words[0:word_length - 1]:
            city += word + ' '
        return True, city

    if words[word_length - 1].upper() == 'WEATHER':
        for word in words[0:word_length - 1]:
            city += word + ' '
        return True, city

    return False, city


def topic_search(words, topic):
    # words = words.split()
    searched_for = ''
    word_length = len(words)
    if word_length > 4:
        return False

    if words[0].upper() == topic.upper():
        for word in words[0:word_length - 1]:
            searched_for += word + ' '
        return True, searched_for

    if words[word_length - 1].upper() == topic.upper():
        for word in words[0:word_length - 1]:
            searched_for += word + ' '
        return True, searched_for

    return False, searched_for

def topic_search_v2(words):
    searched_for = ''
    word_length = len(words)

    if words[0].lower() in search_topics:
        if word_length == 1:
            return search_topics[words[0].lower()], searched_for

        for word in words[1:]:
            searched_for += word + ' '
        return search_topics[words[0].lower()], searched_for

    if words[word_length - 1].lower() in search_topics:
        if word_length == 1:
            return search_topics[words[word_length - 1].lower()], searched_for

        for word in words[0:word_length - 1]:
            searched_for += word + ' '
        return search_topics[words[word_length - 1].lower()], searched_for

    # if search_topics[words[0].lower()] is not None:
    #     for word in words[0:word_length - 1]:
    #         searched_for += word + ' '
    #     return True, searched_for
    #
    # if search_topics[words[word_length - 1].lower()] is not None:
    #     for word in words[0:word_length - 1]:
    #         searched_for += word + ' '
    #     return True, searched_for

    return '', ''

# weather_search('broken arrow weather')

def calculation_search(query):
    # words = words.split()
    words = query.replace(' ', '')
    calculation = ''
    for word in words:
        is_number = False
        is_math_operation = False
        try:
            num = float(word)
            is_number = True
            calculation += str(num)
        except Exception as e:
            is_number = False

        if word == '(' or word == ')' or word == '^' or word == '*' or word == 'x' or word == '/' or word == '+' or word == '-':
            is_math_operation = True
            calculation += str(word)

        if is_number is False and is_math_operation is False:
            return False, ''

    return True, calculation



def analyze_topic(query):
    # Find similar topics
    # Do spell checks
    # Find other relevant results that are similar
    x = 0


def analyze_query(query):
    words = str(query).split()


    weather = topic_search(words, 'weather')
    if weather[0] is True:
        return "weather", weather[1]

    travel = topic_search(words, 'travel')
    if travel[0] is True:
        return "travel", travel[1]

    travel = topic_search(words, 'map')
    if travel[0] is True:
        return "map", travel[1]

    calculation = calculation_search(query)
    if calculation[0] is True:
        return "calculation", calculation[1]

    return None, None


# This is the main one
def analyze_query_v2(query):
    words = str(query).split()

    if len(words) == 1:
        if words[0].lower() == 'crypto':
            return 'crypto', ''

    if len(words) == 2:
        if words[1].lower() == 'stock':
            return 'stock', words[0]

        if words[0].lower() == 'stock' and words[1].lower() == 'news':
            return 'stock news', ''

    topic = topic_search_v2(words)

    if topic[0] != '':
        return topic

    calculation = calculation_search(query)
    if calculation[0] is True:
        return "calculator", calculation[1]

    return None, None


if __name__ == '__main__':
    analyze_query_v2('(4+3)/3')

