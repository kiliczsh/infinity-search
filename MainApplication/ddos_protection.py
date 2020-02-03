import pymongo
import datetime as dt

from accounts import mongodb_endpoint, mongodb_database, mongodb_collection

# Fixed DDOS protection: Just pauses the Bing API if we get a massive traffic spike in one day that is
# probably not organic
def ddos_safe():
    try:
        client = pymongo.MongoClient(mongodb_endpoint, serverSelectionTimeoutMS=1000)

        db = client[mongodb_database]
        col = db[mongodb_collection]

        date = dt.datetime.now()

        year = date.year
        month = date.month
        day = date.day

        daily_search_frequency = col.find_one({ 'year' : year, 'month' : month, 'day': day })

        if daily_search_frequency is None:
            col.insert_one({'year' : year, 'month' : month, 'day' : day, 'frequency': 0})
            return True

        current_search_amount = daily_search_frequency['frequency']

        if current_search_amount > 5000:
            col.update({'year' : year, 'month' : month, 'day' : day, 'frequency': current_search_amount + 1})
            return False

        col.update({'_id': daily_search_frequency['_id'] } , {'year' : year, 'month' : month, 'day' : day, 'frequency': current_search_amount + 1})
        return True

    except Exception:
        return True

