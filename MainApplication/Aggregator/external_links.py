# Links that go on the sidebar
def get_external_links(query):
    query = query.replace(' ', '+')
    links = [
        # Open Resources:
        ['Internet Archive Results', 'https://archive.org/search.php?query=' + query, 'https://archive.org/favicon.ico'],
        ['GitHub Results', 'https://github.com/search?q=' + query, 'https://github.com/favicon.ico'],
        ['GitLab Results', 'https://gitlab.com/search?search=' + query, 'https://gitlab.com/favicon.ico'],
        ['DuckDuckGo IA Results', 'https://duck.co/ia?q=' + query, 'https://duckduckhack.com/images/favicons/favicon-32x32.png'],
        # Popular Websites
        ['Wikipedia Search Results', 'https://en.wikipedia.org/wiki/' + query, 'https://en.wikipedia.org/favicon.ico'],
        ['Invidious Search Results', 'https://www.invidio.us/search?q=' + query, 'https://www.invidio.us/favicon.ico'],
        ['Youtube Results', 'https://www.youtube.com/results?search_query=' + query, 'https://www.youtube.com/favicon.ico'],
        ['Unsplash Image Results', 'https://unsplash.com/s/photos/' + query, 'https://unsplash.com/favicon-32x32.png'],
        ['Twitter Results', 'https://twitter.com/search?q=' + query, 'https://twitter.com/favicon.ico'],
        ['Amazon Results', 'https://www.amazon.com/s?k=' + query, 'https://www.amazon.com/favicon.ico'],
        # Forum Searches
        ['Reddit Search Results', 'https://www.reddit.com/search/?q=' + query, 'https://www.reddit.com/favicon.ico'],
        ['BoardReader Forum Engine Results', 'http://boardreader.com/s/' + query + '.html', 'https://boardreader.com/favicon.ico'],
        # Technical Searches
        ['Petey Vid Search Results', 'https://www.peteyvid.com/index.php?q=' + query, 'https://www.peteyvid.com/favicon.ico'],
        ['Stack Overflow Search Results', 'https://stackoverflow.com/search?q=' + query, 'https://cdn.sstatic.net/Sites/stackoverflow/img/favicon.ico'],
        ['Wolfram Alpha Results', 'https://www.wolframalpha.com/input/?i=' + query, 'https://www.wolframalpha.com/favicon.ico'],
        # Archive Searches
        ['Project Gutenburg Results', 'https://www.gutenberg.org/ebooks/search/?query=' + query, 'https://www.gutenberg.org/favicon.ico'],
        ['Wayback Machine Results', 'https://web.archive.org/web/*/' + query, 'https://archive.org/favicon.ico'],
        ['Wikimedia Commons Results', 'https://commons.wikimedia.org/wiki/' + query, 'https://commons.wikimedia.org/favicon.ico'],
        ['SlideShare Search Results', 'https://www.slideshare.net/search/slideshow?searchfrom=header&q=' + query, 'https://www.slideshare.net/favicon.ico'],
        # ['Software Heritage Archive Results', 'https://archive.softwareheritage.org/browse/search/?q=' + query],
        # Other Search Engines
        ['DuckDuckGo Search Engine Results', 'https://duckduckgo.com/?q=' + query, 'https://duckduckgo.com/favicon.ico'],
        ['Gigablast Search Engine Results', 'http://gigablast.com/search?c=main&q=' + query, 'https://gigablast.com/favicon.ico'],
        ['Mojeek Search Engine Results', 'https://www.mojeek.com/search?q=' + query, 'https://www.mojeek.com/favicon.ico'],
        ['Yandex Russian Search Engine Results', 'https://yandex.com/search/?text=' + query, 'https://yandex.com/favicon.ico'],
        ['Quant Search Engine Results', 'https://www.qwant.com/?q=' + query, 'https://www.qwant.com/favicon.ico'],
        # ['360 Chinese Search Engine Results', 'https://www.so.com/s?q=' + query],
        ['Baidu Chinese Search Engine Results',
         'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=' + query, ''],
        # Trend Data
        # ['Google Trends Results', 'https://trends.google.com/trends/explore?q=' + query, 'https://ssl.gstatic.com/trends_nrtr/2051_RC11/favicon.ico'],
    ]

    return links

