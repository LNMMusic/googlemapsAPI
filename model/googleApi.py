from urllib.parse import quote
from googlemaps   import convert
from .methods     import methods_converter
import requests;  import json
# Encoders [specifics]
def waypointer(data:list):
    url = ''
    if data[0]:
        url += 'optimize:true|'

    # Process
    for k, v in data[1]:
        if k:
            url+= k+':'
        
        if isinstance(v, str):
            url+= quote(v)
        elif isinstance(v, dict):
            url+= convert.latlng(v)
        
        url+= '|'

    return url[:-1]
def direction(data):
    if isinstance(data, dict):
        if 'place_id' in data.keys():
            url= convert.components(data)
        else:
            url= convert.latlng(data)
    elif isinstance(data, str):
        url= quote(data)
    
    return url
def area(data):
    if isinstance(data, str):
        url= quote(data)
    elif isinstance(data, dict):
        k, v = tuple(data.items())[0]
        
        if k == 'point':
            url= f'{k}:{convert.latlng(v)}'
        elif k=='circle':
            url= f'{k}:radius@{convert.latlng(v)}'
        elif k=='rectangle':
            url= f'{k}:{convert.bounds(v)}'
    return url


# OBJECT
class googleMapsApi:
    def __init__(self):
        self.scheme = 'https://'
        self.netloc = 'maps.googleapis.com/'
        self.path   = 'maps/api/'
        self.dtype  = 'json'

        self.key = 'INSERT YOUR API KEY [From google maps api]'
        self.methods = methods_converter

        # Dynamic
        self.response = {}

    # Methods [URL - Parameters]
    def url_base(self):
        return self.scheme + self.netloc + self.path + self.tool + self.dtype
    def url_encoded(self):
        url = self.url_base()+'?'

        for ix, val in enumerate(self.parameters):
            if val[1]:
                m = self.methods[val[0]]
                url+= f'{val[0]}='
                
                if m == 'quote':
                    url+= quote(val[1])
                elif m=='quote_only':                           # Need to be Checked!
                    url=  url[:-1]
                elif m=='components':
                    url+= convert.components(val[1])
                elif m=='bounds':
                    url+= convert.bounds(val[1])
                elif m=='latlng':
                    url+= convert.latlng(val[1])
                elif m=='waypointer':
                    url+= waypointer(val[1])
                elif m=='time':
                    url+= convert.time(val[1])
                elif m=='join_list':
                    url+= convert.join_list("|", val[1])
                elif m=='join_list2':
                    url+= convert.join_list(",", val[1])
                elif m=='direction':
                    url+= direction(val[1])
                elif m=='area':
                    url+= area(val[1])
                
                url+='&'
        url+= f'key={quote(self.key)}'
        return url
     
    def parametersData(self):
        return {_[0]: _[1] for _ in self.parameters}

    # Request
    def get_request(self):
        if self.response:
            return self.response
        
        r = requests.get(self.url_encoded())
        if r.status_code in range(200,299):
            self.response = r.json()

# GEOCODE MODULE [Geocoding API]        ________________________________________________________________________________________________
class geocodeLocation(googleMapsApi):
    def __init__(self, address, components=None, bounds=None, region=None, language=None):
        super().__init__()
        self.tool = 'geocode/'
        self.parameters = [('address',address),('components',components),('bounds',bounds),('region',region),('language',language)]
        
        # Dynamic
        self.latlng = None
class geocodeLocationInverse(googleMapsApi):
    def __init__(self, latlng, language=None, location_type=None, result_type=None):
        super().__init__()
        self.tool = 'geocode/'
        self.parameters = [('latlng',latlng),('language',language),('location_type',location_type),('result_type',result_type)]

        # Dynamic
        self.address = None
class geocodePlace(googleMapsApi):
    def __init__(self, place_id, language=None, location_type=None, result_type=None):
        super().__init__()
        self.tool = 'geocode/'
        self.parameters = [('place_id',place_id),('language',language),('location_type',location_type),('result_type',result_type)]

        # Dynamic
        self.address = None

# DIRECTIONS MODULE [Directions API]    ________________________________________________________________________________________________
class directionsLocation(googleMapsApi):
    def __init__(self, origin, destination, mode=None, waypoints=None, alternatives=False, avoid=None, language=None, units=None, region=None,
                 departure_time=None, arrival_time=None, transit_mode=None, transit_routing_preference=None, traffic_model=None):
        super().__init__()
        self.tool = 'directions/'
        self.parameters = [('origin',origin), ('destination',destination), ('mode',mode), ('waypoints',waypoints), ('alternatives',alternatives),
                           ('avoid',avoid), ('language',language), ('units',units), ('region',region), ('departure_time',departure_time),
                           ('arrival_time',arrival_time), ('transit_mode',transit_mode), ('transit_routing_preference',transit_routing_preference),
                           ('traffic_model',traffic_model)]

# PLACES MODULE [Places API]            ________________________________________________________________________________________________
class placesFind(googleMapsApi):
    def __init__(self, input_, inputtype, fields=None, language=None, locationbias=None):
        super().__init__()
        self.tool = 'place/findplacefromtext/'
        self.parameters = [('input',input_),('inputtype',inputtype),('fields',fields),('language',language),('locationbias',locationbias)]

class placesNearby(googleMapsApi):
    def __init__(self, location, fields=None, keyword=None, language=None, maxprice=None, minprice=None, name=None, opennow=None, pagetoken=None,
                 radius=None, rankby=None, type_=None):
        super().__init__()
        self.tool = 'place/nearbysearch/'
        self.parameters = [('location',location),('fields',fields),('keyword',keyword),('language',language),('maxprice',maxprice),('minprice',minprice),
                            ('name',name),('opennow',opennow),('pagetoken',pagetoken),('radius',radius),('rankby',rankby),('type',type_)]

class placesText(googleMapsApi):
    def __init__(self, query, language=None, location=None, maxprice=None, minprice=None, opennow=None, pagetoken=None, radius=None,
                 region=None, type_=None):
        super().__init__()
        self.tool = 'place/textsearch/'
        self.parameters = [('query',query),('language',language),('location',location),('maxprice',maxprice),('minprice',minprice),('opennow',opennow),
                            ('pagetoken',pagetoken),('radius',radius),('region',region),('type',type_)]