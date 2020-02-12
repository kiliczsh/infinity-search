from accounts import mapbox_api_key
import requests


def get_location(query):
    query.replace(' ', '%20')
    location_info = {'text': '', 'place_name': '', 'longitude': 0, 'latitude': '0'}
    try:
        location = requests.get('https://api.mapbox.com/geocoding/v5/mapbox.places/' + query + '.json?access_token=' + mapbox_api_key)
        location_data = location.json()

        features = location_data['features']
        print(features)

        if len(features) == 0:
            return []

        features = features[0]
        location_info['text'] = features['text']
        location_info['place_name'] = features['place_name']
        location_info['latitude'] = features['center'][0]
        location_info['longitude'] = features['center'][1]

        return location_info

    except Exception:
        return location_info
