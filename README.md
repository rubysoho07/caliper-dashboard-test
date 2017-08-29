# Caliper Dashboard Test

Tester dashboard website for dashboard of IMS Caliper data. This project uses Django and Google Chart Library.

## Prerequisites

* Python 2.x (This project uses django-mongodb-engine now, but it doesn't work on Python 3.x and latest version of Django.)
* Caliper datastore (e.g. OpenLRW ([GitHub](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW)))
* MongoDB

## How to Build the Environment for Development

1. Build virtual environment with `virtualenv`
```
$ pip install virtualenv
$ virtualenv caliper-dashboard-env
$ cd caliper-dashboard-env
$ source ./activate
```

2. Install packages with `pip`
```
$ pip install -r requirements.txt
```

## How to Use This Example

### Configuring and Running Server

* Check the configuration for database and collection where Caliper data stored (`event_dashboard/settings.py`) 
```python
MONGODB_URL = 'mongodb://localhost:27017'
MONGODB_DB = 'test'
MONGODB_COLLECTION = 'mongoEvent'
```

* Run Django server
```
$ python manage.py runserver [PORT_NUM]
```

### Test URL for sample dashboard

- Action: http://localhost:[PORT_NUM]/action/
- Event type: http://localhost:[PORT_NUM]/event/