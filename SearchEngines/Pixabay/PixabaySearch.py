import requests
from accounts import pixabay_api_key


def search_pixabay_images(query):
    query = query.replace(' ', '%20')
    results = requests.get('https://pixabay.com/api/?key='+ pixabay_api_key +'&q=' + query).json()

    images = []

    for hit in results['hits']:
        images.append([hit['pageURL'], hit['webformatURL'], hit['webformatWidth'], hit['webformatHeight'], hit['largeImageURL']])

    for image in images:
        print(image)


def search_pixabay_videos(query):
    query = query.replace(' ', '%20')
    results = requests.get('https://pixabay.com/api/videos/?key='+ pixabay_api_key +'&q=' + query).json()


if __name__ == '__main__':
    search_pixabay_images('code')

