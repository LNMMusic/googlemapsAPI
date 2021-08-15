methods_structure = {
    'quote': {
        'parameter': 'data'
    },

    'components': {
        # Included in Filtering
        'postal_code': None,
        'postal_code_prefix': None,
        'country': None,

        # Won't Be Forzed
        'route': None,
        'locality': None,
        'administrative_area': None,
    },

    'bounds' : {
        "northeast" : {
            "lat" : float(),
            "lng" : float()
        },
        "southwest" : {
            "lat" : float(),
            "lng" : float()
        }
    },

    'latlng': {
        'lat': float(),
        'lng': float()
    },

    'location_list': [{"lat" : float(), "lng" : float()}, "Sydney"],            # waypoints=via:Charlestown,MA|via:Lexington,MA

    'time': 'datetime.now() or datetime.datetime or int()',

    'origin': {
        'place_id': ''
    },
    
    'waypoints': [True, [
            ('', '1600 Harvoard, Catalan, CF'),
            ('via', 'as f a s, fas'),
            ('', {
                'lat': float(),
                'lng': float()
            }),
            ('via', {
                'lat': float(),
                'lng': float()
            })
    ]]
}

methods_converter = {
    'address': 'quote',                            #   =>  '1600 Amphitheatre Parkway, Mountain View, CA'
    'language': 'quote',                           #   =>  'ES'
    'region': 'quote',                             #   =>  'es' [https://en.wikipedia.org/wiki/Country_code_top-level_domain]
    'place_id': 'quote',                           #   =>  'ChIJ3S-JXmauEmsRUcIaWtf4MzE'
    'mode': 'quote',                               #   =>  'driving' / 'walking' / 'bicycling' / 'transit'
    'alternatives': 'quote',                       #   =>   only be able to set in True
    'units': 'quote',
    'transit_routing_preference': 'quote',
    'traffic_model': 'quote',

    'components': 'components',                     #   =>  check methods_structure
    'bounds': 'bounds',

    'latlng': 'latlng',                             #   =>  check methods_structure
    
    'origin': 'direction',
    'destination': 'direction',

    'location_type': 'join_list',                   #   =>  'ROOFTOP' / 'RANGE-INTERPOLATED' / 'GEOMETRIC-CENTER' / 'APPROXIMATE'
    'result_type': 'join_list',                     #   =>  'street_address' / 'route' / 'intersection' / 'political' / 'country'
                                                    #       'administrative_area_level_(1,2,3,4,5)' / 'colloquial_area' / 'locality'
                                                    #       'sublocality' / 'neighborhood' / 'premise' / 'subpremise' / 'plus_code'
                                                    #       'postal_code' / 'natural_feature' / 'airport' / 'park' / 'point_of_interest'
    'avoid': 'join_list',                           #   =>  'tolls' / 'highways' / 'ferries' / 'indoor'
    'transit_mode': 'join_list',

    'waypoints': 'waypointer',                      #   =>  place_id  /  address  /  latlng  /  encoded polyline  [prefix: via - side_of_road]

    'departure_time': 'time',                       #   =>  1343641500 (int) or datetime.now() or datetime.datetime()
    'arrival_time': 'time',

    # PLACES API [Find]
    'input': 'quote',                               #   =>  name / address / phone_number
    'inputtype': 'quote',                           #   =>  'textquery' / 'phonenumber'
    
    'fields': 'join_list2',                         #   =>  'address_component' / 'adr_address' / 'business_status' / 'formatted_address' / 'geometry'
                                                    #       'icon' / 'icon_mask_base_uri' / 'icon_background_color' / 'name' / 'photo' / 'place_id'
                                                    #       'plus_code' / 'type' / 'url' / 'utc_offset' / 'vicinity' / 'formatted_phone_number'
                                                    #       'international_phone_number' / 'opening_hours' / 'website' / 'price_level' / 'rating'
                                                    #       'review' / 'user_ratings_total'
    
    'locationbias': 'area',                         #   =>  IPBias / Point [latlng] / Circular [meters <circle:radius@lat,lng]
                                                    #       Rectangular [<rectangle:south,west|north,east>]

    # PLACES API [Nearby]
    'location': 'laglng',
    
    'keyword': 'quote',
    'name': 'quote',                                #   =>  similar to keyword [not recommended, better use keyword]
    
    'maxprice': 'quote',                            #   =>  RANK:   0 [Most Affordable]    >    4 [Most Expensive]
    'minprice': 'quote',                            #   =>  RANK:   0 [Most Affordable]    >    4 [Most Expensive]

    'opennow': 'quote_only',                        #   =>  NEED TO BE CHECKED!
    'pagetoken': 'quote',                           #   =>  Token Code
    'radius': 'quote',                              #   =>  meters (example: 100 - 1500 - 750)
    'rankby': 'quote',                              #   =>  'prominence' / 'distance'
    'type': 'quote',                                #   =>  check TABLE of Types 
                                                    #       [https://developers.google.com/maps/documentation/places/web-service/supported_types]

    # PLACES API [Text]
    'query': 'quote'                                #   =>  example <restaurants in Sydney>
}