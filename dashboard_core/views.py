from django.shortcuts import render

from pymongo import MongoClient
from event_dashboard.settings import MONGODB_COLLECTION, MONGODB_DB, MONGODB_URL


# Create your views here.
def get_action_view(request):
    """
    Count Caliper events per Action.
    """
    client = MongoClient(MONGODB_URL)
    db = client[MONGODB_DB]
    event_collection = db[MONGODB_COLLECTION]

    aggregated_count = event_collection.aggregate([{"$group": {"_id": "$event.action", "count": {"$sum": 1}}}])
    aggregated_action = []

    for i in aggregated_count:
        column = {
            'Action': i['_id'].split('/')[-1].split('#')[-1],
            'Count': i['count']
        }

        aggregated_action.append(column)

    context = {
        'aggregated_action': aggregated_action
    }

    client.close()

    return render(request, 'test.html', context)


def get_event_view(request):
    """
    Count Caliper events per Event type.
    """
    client = MongoClient(MONGODB_URL)
    db = client[MONGODB_DB]
    event_collection = db[MONGODB_COLLECTION]

    aggregated_count = event_collection.aggregate([{"$group": {"_id": "$event.type", "count": {"$sum": 1}}}])
    aggregated_event = []

    for i in aggregated_count:
        column = {
            'Event': i['_id'].split('/')[-1],
            'Count': i['count']
        }

        aggregated_event.append(column)

    context = {
        'aggregated_event': aggregated_event
    }

    client.close()

    return render(request, 'event.html', context)


def get_date_view(request):

    context = {}

    return render(request, 'date.html', context)
