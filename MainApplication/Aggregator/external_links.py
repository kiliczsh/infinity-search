# Links that go on the sidebar
def get_external_links(query):
    query = query.replace(' ', '+')
    links = [
        # Open Resources:
        ['Internet Archive Results', 'https://archive.org/search.php?query=' + query],
        ['GitHub Results', 'https://github.com/search?q=' + query],
        ['GitLab Results', 'https://gitlab.com/search?search=' + query],
        # Popular Websites
        ['Wikipedia Search Results', 'https://en.wikipedia.org/wiki/' + query],
        ['Invidious Search Results', 'https://www.invidio.us/search?q=' + query],
        ['Youtube Results', 'https://www.youtube.com/results?search_query=' + query],
        ['Unsplash Image Results', 'https://unsplash.com/s/photos/' + query],
        ['Twitter Results', 'https://mobile.twitter.com/search?q=' + query],
        ['Amazon Results', 'https://www.amazon.com/s?k=' + query],
        # Forum Searches
        ['Reddit Search Results', 'https://www.reddit.com/search/?q=' + query],
        ['BoardReader Forum Engine Results', 'http://boardreader.com/s/' + query + '.html'],
        # Technical Searches
        ['Petey Vid Search Results', 'https://www.peteyvid.com/index.php?q=' + query],
        ['Stack Overflow Search Results', 'https://stackoverflow.com/search?q=' + query],
        ['Wolfram Alpha Results', 'https://www.wolframalpha.com/input/?i=' + query],
        # Archive Searches
        ['Project Gutenburg Results', 'https://www.gutenberg.org/ebooks/search/?query=' + query],
        ['Wayback Machine Results', 'https://web.archive.org/web/*/' + query],
        ['Wikimedia Commons Results', 'https://commons.wikimedia.org/wiki/' + query],
        ['SlideShare Search Results', 'https://www.slideshare.net/search/slideshow?searchfrom=header&q=' + query],
        # ['Software Heritage Archive Results', 'https://archive.softwareheritage.org/browse/search/?q=' + query],
        # Other Search Engines
        ['DuckDuckGo Search Engine Results', 'https://duckduckgo.com/?q=' + query],
        ['Gigablast Search Engine Results', 'http://gigablast.com/search?c=main&q=' + query],
        ['Mojeek Search Engine Results', 'https://www.mojeek.com/search?q=' + query],
        ['Yandex Russian Search Engine Results', 'https://yandex.com/search/?text=' + query],
        ['Quant Search Engine Results', 'https://www.qwant.com/?q=' + query],
        # ['360 Chinese Search Engine Results', 'https://www.so.com/s?q=' + query],
        ['Baidu Chinese Search Engine Results',
         'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=' + query],
        # Trend Data
        ['Google Trends Results', 'https://trends.google.com/trends/explore?q=' + query],
    ]

    return links

