# Links that go on the sidebar
def get_external_links(query):
    query = query.replace(' ', '+')

    links = [
        # Open Resources:
        ['Internet Archive Results', 'https://archive.org/search.php?query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/archive.ico'],
        ['Wikipedia Results', 'https://en.wikipedia.org/wiki/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikipedia.ico'],
        ['Youtube Results', 'https://www.youtube.com/results?search_query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/youtube.ico'],

        ['GitHub Results', 'https://github.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/github.ico'],
        ['GitLab Results', 'https://gitlab.com/search?search=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/gitlab.png'],

        # Popular Websites
        ['Unsplash Image Results', 'https://unsplash.com/s/photos/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/unsplash.png'],
        ['Wikimedia Commons Results', 'https://commons.wikimedia.org/wiki/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikimedia.ico'],

        ['Amazon Results', 'https://www.amazon.com/s?k=' + query + '&tag=infinitysea0b-20',
         'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/amazon.ico'],

        # ['Invidious Results', 'https://www.invidio.us/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/invidious.ico'],
        # Forum Searches

        ['Twitter Results', 'https://twitter.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/twitter.ico'],
        ['Reddit Results', 'https://www.reddit.com/search/?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/reddit.ico'],
        ['BoardReader Results', 'https://boardreader.com/s/' + query + '.html', 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/boardreader.ico'],
        # Technical Searches
        ['Petey Vid Results', 'https://www.peteyvid.com/index.php?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/peteyvid.ico'],
        ['Stack Overflow Results', 'https://stackoverflow.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/stackoverflow.ico'],
        ['Wolfram Alpha Results', 'https://www.wolframalpha.com/input/?i=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wolfram.ico'],
        # Archive Searches
        ['Project Gutenburg Results', 'https://www.gutenberg.org/ebooks/search/?query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/gutenberg.ico'],
        ['Wayback Machine Results', 'https://web.archive.org/web/*/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/archive.ico'],
        # ['SlideShare Results', 'https://www.slideshare.net/search/slideshow?searchfrom=header&q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/slideshare.ico'],
        # Other Search Engines
        ['DuckDuckGo Results', 'https://duckduckgo.com/?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/duckduckgo.ico'],
        ['Mojeek Results', 'https://www.mojeek.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/mojeek.ico'],
        ['Yandex Results', 'https://yandex.com/search/?text=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/yandex.ico'],
        ['Qwant Results', 'https://www.qwant.com/?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/qwant.ico'],
        ['Cliqz Results', 'https://beta.cliqz.com/search?q=' + query + '#channel=infinitysearch', 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/cliqz.ico'],
        # ['DuckDuckGo IA Results', 'https://duck.co/ia?q=' + query,
        #  'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/duckduckhack.png'],

        # ['360 Chinese Search Engine Results', 'https://www.so.com/s?q=' + query],
        # ['Baidu Results',
         # 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/baidu.ico'],
    ]

    return links

def get_external_links_german(query):
    query = query.replace(' ', '+')

    links = [
        # Open Resources:
        ['Internet Archive Ergebnisse', 'https://archive.org/search.php?query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/archive.ico'],
        ['GitHub Ergebnisse', 'https://github.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/github.ico'],
        ['GitLab Ergebnisse', 'https://gitlab.com/search?search=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/gitlab.png'],
        ['DuckDuckGo IA Ergebnisse', 'https://duck.co/ia?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/duckduckhack.png'],
        # Popular Websites
        ['Wikipedia Ergebnisse', 'https://de.wikipedia.org/wiki/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikipedia.ico'],
        ['Invidious Ergebnisse', 'https://www.invidio.us/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/invidious.ico'],
        ['Youtube Ergebnisse', 'https://www.youtube.com/results?search_query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/youtube.ico'],
        ['Unsplash Ergebnisse', 'https://unsplash.com/s/photos/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/unsplash.png'],
        ['Twitter Ergebnisse', 'https://twitter.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/twitter.ico'],
        # ['Amazon Results', 'https://www.amazon.com/s?k=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/amazon.ico'],
        # With affiliate link
        ['Amazon Ergebnisse', 'https://www.amazon.com/gp/search?ie=UTF8&tag=infinitysearc-20&linkCode=ur2&linkId=2477f1f1396323c01402d67e62bdbd5c&camp=1789&creative=9325&index=aps&keywords=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/amazon.ico'],
        # Forum Searches
        ['Reddit Ergebnisse', 'https://www.reddit.com/search/?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/reddit.ico'],
        ['BoardReader Ergebnisse', 'https://boardreader.com/s/' + query + '.html', 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/boardreader.ico'],
        # Technical Searches
        ['Petey Vid Ergebnisse', 'https://www.peteyvid.com/index.php?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/peteyvid.ico'],
        ['Stack Overflow Ergebnisse', 'https://stackoverflow.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/stackoverflow.ico'],
        ['Wolfram Alpha Ergebnisse', 'https://www.wolframalpha.com/input/?i=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wolfram.ico'],
        # Archive Searches
        ['Project Gutenburg Ergebnisse', 'https://www.gutenberg.org/ebooks/search/?query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/gutenberg.ico'],
        ['Wayback Machine Ergebnisse', 'https://web.archive.org/web/*/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/archive.ico'],
        ['Wikimedia Commons Ergebnisse', 'https://commons.wikimedia.org/wiki/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikimedia.ico'],
        ['SlideShare Ergebnisse', 'https://www.slideshare.net/search/slideshow?searchfrom=header&q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/slideshare.ico'],
        # ['Software Heritage Archive Results', 'https://archive.softwareheritage.org/browse/search/?q=' + query],
        # Other Search Engines
        ['DuckDuckGo Ergebnisse', 'https://duckduckgo.com/?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/duckduckgo.ico'],
        ['Mojeek Ergebnisse', 'https://www.mojeek.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/mojeek.ico'],
        ['Yandex Ergebnisse', 'https://yandex.com/search/?text=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/yandex.ico'],
        ['Qwant Ergebnisse', 'https://www.qwant.com/?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/qwant.ico'],
        ['Cliqz Ergebnisse', 'https://beta.cliqz.com/search?q=' + query + '#channel=infinitysearch', 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/cliqz.ico'],
        # ['360 Chinese Search Engine Results', 'https://www.so.com/s?q=' + query],
        ['Baidu Ergebnisse',
         'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/baidu.ico'],
    ]

    return links

def get_external_links_spanish(query):
    query = query.replace(' ', '+')

    links = [
        # Open Resources:
        ['Resultados de Internet Archive', 'https://archive.org/search.php?query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/archive.ico'],
        ['Resultados de GitHub', 'https://github.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/github.ico'],
        ['Resultados de GitLab', 'https://gitlab.com/search?search=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/gitlab.png'],
        ['Resultados de DuckDuckGo IA', 'https://duck.co/ia?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/duckduckhack.png'],
        # Popular Websites
        ['Resultados de Wikipedia', 'https://es.wikipedia.org/wiki/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikipedia.ico'],
        ['Resultados de Invidious', 'https://www.invidio.us/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/invidious.ico'],
        ['Resultados de Youtube', 'https://www.youtube.com/results?search_query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/youtube.ico'],
        ['Resultados de Unsplash', 'https://unsplash.com/s/photos/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/unsplash.png'],
        ['Resultados de Twitter', 'https://twitter.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/twitter.ico'],
        # ['Amazon Results', 'https://www.amazon.com/s?k=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/amazon.ico'],
        # With affiliate link
        ['Resultados de Amazon', 'https://www.amazon.com/gp/search?ie=UTF8&tag=infinitysearc-20&linkCode=ur2&linkId=2477f1f1396323c01402d67e62bdbd5c&camp=1789&creative=9325&index=aps&keywords=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/amazon.ico'],
        # Forum Searches
        ['Resultados de Reddit', 'https://www.reddit.com/search/?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/reddit.ico'],
        ['Resultados de BoardReader', 'https://boardreader.com/s/' + query + '.html', 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/boardreader.ico'],
        # Technical Searches
        ['Resultados de Petey Vid', 'https://www.peteyvid.com/index.php?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/peteyvid.ico'],
        ['Resultados de Stack Overflow', 'https://stackoverflow.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/stackoverflow.ico'],
        ['Resultados de Wolfram Alpha', 'https://www.wolframalpha.com/input/?i=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wolfram.ico'],
        # Archive Searches
        ['Resultados de Project Gutenburg', 'https://www.gutenberg.org/ebooks/search/?query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/gutenberg.ico'],
        ['Resultados de Wayback Machine', 'https://web.archive.org/web/*/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/archive.ico'],
        ['Resultados de Wikimedia Commons', 'https://commons.wikimedia.org/wiki/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikimedia.ico'],
        ['Resultados de SlideShare', 'https://www.slideshare.net/search/slideshow?searchfrom=header&q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/slideshare.ico'],
        # ['Software Heritage Archive Results', 'https://archive.softwareheritage.org/browse/search/?q=' + query],
        # Other Search Engines
        ['Resultados de DuckDuckGo', 'https://duckduckgo.com/?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/duckduckgo.ico'],
        ['Resultados de Mojeek', 'https://www.mojeek.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/mojeek.ico'],
        ['Resultados de Yandex', 'https://yandex.com/search/?text=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/yandex.ico'],
        ['Resultados de Qwant', 'https://www.qwant.com/?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/qwant.ico'],
        ['Resultados de Cliqz', 'https://beta.cliqz.com/search?q=' + query + '#channel=infinitysearch', 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/cliqz.ico'],
        # ['360 Chinese Search Engine Results', 'https://www.so.com/s?q=' + query],
        ['Resultados de Baidu',
         'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/baidu.ico'],
    ]

    return links


def get_image_links(query):
    query = query.replace(' ', '+')
    links = [
        # Image engines
        ['DuckDuckGo Image Results', 'https://duckduckgo.com/?iar=images&iax=images&ia=images&q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/duckduckgo.ico'],
        ['Bing Image Results', 'https://www.bing.com/images/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/bing.ico'],
        ['Google Image Results', 'https://www.google.com/search?hl=en&tbm=isch&source=hp&q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/google.ico'],
        ['Pixabay Results', 'https://pixabay.com/images/search/' + query + '/', 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/pixabay.ico'],
        ['Unsplash Results', 'https://unsplash.com/s/photos/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/unsplash.png'],
        ['Flickr Results', 'https://www.flickr.com/search/?text=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/flickr.ico'],
        ['Pexels Results', 'https://www.pexels.com/search/' + query + '/', 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/pexels.ico'],
        ['Creative Commons Results', 'https://search.creativecommons.org/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/creativecommons.ico'],
        ['Wikimedia Commons Results', 'https://commons.wikimedia.org/wiki/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikimedia.ico'],
        ['Pinterest Results', 'https://www.pinterest.com/search/pins/?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/pinterest.ico'],
        ['Internet Archive Image Results', 'https://archive.org/details/image?and[]=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/archive.ico'],
        ['Picsearch Image Results', 'https://www.picsearch.com/index.cgi?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/picsearch.ico'],
        ['Nasa Image Results', 'https://images.nasa.gov/search-results?yearStart=1920&yearEnd=2020&media=image&q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/nasa.ico'],
        ['Tineye Reverse Image Search', 'https://tineye.com/', 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/tineye.ico'],
    ]

    return links


def get_video_links(query):
    query = query.replace(' ', '+')
    links = [
        ['Invidious Search Results', 'https://www.invidio.us/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/invidious.ico'],
        ['Youtube Results', 'https://www.youtube.com/results?search_query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/youtube.ico'],
        ['Vimeo Results', 'https://vimeo.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/vimeo.png'],
        ['Daily Motion Results', 'https://www.dailymotion.com/search/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/dailymotion.ico'],
        ['Internet Archive Movie Results', 'https://archive.org/details/movies?and[]=' + query,'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/archive.ico'],
        ['DTube Results', 'https://d.tube/#!/s/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/dtube.ico'],
        ['Bitchute Results','https://search.bitchute.com/renderer?use=bitchute-json&name=Search&login=bcadmin&key=7ea2d72b62aa4f762cc5a348ef6642b8&query=' + query,'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/bitchute.ico'],
        ['Petey Vid Search Results', 'https://www.peteyvid.com/index.php?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/peteyvid.ico'],
        ['Twitch Results', 'https://www.twitch.tv/search?term=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/twitch.ico'],
        ['LiveLeak Results', 'https://www.liveleak.com/browse?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/liveleak.ico'],
        ['Ted Talk Results', 'https://www.ted.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/ted.ico'],
        ['Veoh Results', 'https://www.veoh.com/find/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/veoh.ico'],
        ['Metacafe Results', 'https://www.metacafe.com/videos_about/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/metacafe.ico'],
        ['Vlare Results', 'https://vlare.tv/search/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/vlare.ico'],
        ['Lbry Results', 'https://lbry.tv/$/search?q=' + query,'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/lbry.ico'],
    ]
    return links


def get_news_links(query):
    query = query.replace(' ', '+')
    links = [
        ['Reuters Results', 'https://www.reuters.com/search/news?blob=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/reuters.ico'],
        ['New York Times Results', 'https://www.nytimes.com/search?query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/nyt.ico'],
        ['Fox Results', 'https://www.foxnews.com/search-results/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/fox.ico'],
        ['CNN Results', 'https://www.cnn.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/cnn.ico'],
        ['Washington Post Results','https://www.washingtonpost.com/newssearch/?datefilter=All%20Since%202005&sort=Relevance&query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/washingtonpost.ico'],
        ['Business Insider Results', 'https://www.businessinsider.com/s?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/businessinsider.ico'],
        ['BBC News Results', 'https://www.bbc.co.uk/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/bbc.ico'],
        ['RT Results', 'https://www.rt.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/rt.ico'],
        ['Sputnik News Results', 'https://sputniknews.com/search/?query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/sputnik.ico'],
        ['NDTV Results', 'https://www.ndtv.com/search?searchtext=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/ndtv.ico']
    ]
    return links


def get_book_links(query):
    query = query.replace(' ', '+')


    links = []

    return links


def get_shopping_links(query):
    query = query.replace(' ', '+')

    links = [
        # ['Amazon Results','https://www.amazon.com/gp/search?ie=UTF8&tag=infinitysearc-20&linkCode=ur2&linkId=2477f1f1396323c01402d67e62bdbd5c&camp=1789&creative=9325&index=aps&keywords=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/amazon.ico'],
        ['Jet Results', 'https://jet.com/search?term=' + query,'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/jet.ico'],
        # ['Ebay Results', 'https://www.ebay.com/sch/i.html?_nkw=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/ebay.ico'],
        ['Ebay Results', 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575565606&toolid=10001&campid=5338647778&customid=&mpre=https%3A%2F%2Fwww.ebay.com%2Fsch%2Fi.html%3F_nkw%3D' + query,'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/ebay.ico'],
        ['Overstock Results', 'https://www.overstock.com/'+ query +',/k,/results.html?SearchType=Header', 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/overstock.ico'],
        ['BestBuy Results', 'https://www.bestbuy.com/site/searchpage.jsp?st=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/bestbuy.ico'],
        ['Barnes and Noble Results', 'https://www.barnesandnoble.com/s/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/barnesandnoble.ico'],
        ['Etsy Results', 'https://www.etsy.com/search?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/etsy.ico'],
    ]

    return links

def get_map_links(query):
    query = query.replace(' ', '+')

    links = [
        ['Open Street Map Results', 'https://www.openstreetmap.org/search?query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/openstreetmap.ico'],
        ['Google Maps Results', 'https://www.google.com/maps/search/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/googlemaps.ico'],
        ['Mapquest Results', 'https://www.mapquest.com/search/results?query=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/mapquest.ico'],
        ['Bing Maps Results', 'https://www.bing.com/maps?q=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/bing.ico'],
        ['Here We Go Results', 'https://wego.here.com/search/' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wego.ico'],
        ['Wayz Results', 'https://www.waze.com/livemap/', 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wayz.ico'],
        ['Qwant Map Results','https://www.qwant.com/maps/', 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/qwant.ico']
    ]

    return links


def get_music_links(query):
    query = query.replace(' ', '+')

    links = []

    return links


def get_wiki_links(query):
    query = query.replace(' ', '+')

    links = [
        ['Wikipedia', 'https://wikipedia.org/w/index.php?search=' + query , 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikipedia.ico',],
        ['Wikibooks', 'https://wikibooks.org/w/index.php?search=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikibooks.ico'],
        ['Wikiquote', 'https://wikiquote.org/w/index.php?search=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikiquote.ico'],
        ['Wikivoyage', 'https://wikivoyage.org/w/index.php?search=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikivoyage.ico'],
        ['Wikisource', 'https://wikivoyage.org/w/index.php?search=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikisource.ico'],
        ['Wikimedia Commons', 'https://commons.wikimedia.org/w/index.php?search=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikimedia.ico'],
        ['Wikinews', 'https://wikinews.org/w/index.php?search=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikinews.ico'],
        ['Wikiversity', 'https://wikiversity.org/w/index.php?search=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikiversity.ico'],
        ['Wikidata', 'https://www.wikidata.org/w/index.php?search=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikidata.ico'],
        ['Wikimedia Meta', 'https://meta.wikimedia.org/w/index.php?search=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikimedia.ico'],
        ['Wiktionary', 'https://wiktionary.org/w/index.php?search=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wiktionary.ico'],
        ['Wikispecies', 'https://species.wikimedia.org/w/index.php?search=' + query, 'https://infinity-search-saved-favicons.s3.amazonaws.com/external_link_favicons/wikispecies.ico'],
    ]

    return links


