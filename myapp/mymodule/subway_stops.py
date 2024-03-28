import requests

# gets subway stops from mbta api
#
# @return data section from the json returned from the get request to mbta api
# @raises JSONDecodeError exception upon failed connection to mbta api
def getSubwayStops(route):
    # get the route id from the given route to filter the stops correctly
    routeID = route["id"]

    # set the url for the get request
    url = "https://api-v3.mbta.com/stops"

    # set parameters for get request to filter for given route stops
    # also includes generated api key for access to the api data
    payload = {"filter[route]": routeID, "api_key": "fec1b0ff62e047ca972e2571a62cf156"}

    # utilize requests library to make a get request using the url and parameters
    request = requests.get(url, params=payload)

    # turn the get request into json form
    stops = request.json()

    # return the 'data' information from the json routes
    return stops["data"]

# finds the route with the most stops
#
# @param subway routes
# @return number of stops on route, and route with the most stops
def findMaxStops(routes):
    maxStops = 0
    maxRoute = None

    # iterate through every route
    for route in routes:
        stops = getSubwayStops(route)

        # if current route has more stops than maxStops
        # update maxStops to number of stops on current route and
        # update maxRoute to be the current route
        if maxStops < len(stops):
            maxStops = len(stops)
            maxRoute = route["attributes"]["long_name"]
    
    # return the maxStops and maxRoute
    return maxStops, maxRoute

# finds the route with the least stops
#
# @param subway routes
# @return number of stops on route, and route with the least stops
def findMinStops(routes):
    minStops = float('inf')
    minRoute = None

    # iterate through every route
    for route in routes:
        stops = getSubwayStops(route)

        # if current route has less stops than minStops
        # update minStops to number of stops on current route and
        # update minRoute to be the current route
        if minStops > len(stops):
            minStops = len(stops)
            minRoute = route["attributes"]["long_name"]
    
    # return the minStops and minRoute
    return minStops, minRoute

# gets all the subway stops with a list of the routes they are connected to
#
# @param subway routes
# @return dictionary with subway stops as keys
# and list of routes they are connected to as value
def getStopsWithRoutes(routes):
    # create an empty dictionary
    subwayStops = {}

    # iterate through all the routes
    for route in routes:
        stops = getSubwayStops(route)

        # iterate through all the stops for the current route
        for stopJSON in stops:
            # create an empty list for else case
            listRoutes = []

            # get the name of the stop
            stop = stopJSON['attributes']['name']

            # if the stop is already a key in subwayStops
            # then simply add the current route to the list
            if stop in subwayStops.keys():
                subwayStops[stop].append(route['attributes']['long_name'])
            # if the stop is not a key in subwayStops then
            # add the current route to the empty list and add
            # it to subwayStops with the key being the current stop
            else:
                listRoutes.append(route['attributes']['long_name'])
                subwayStops[stop] = listRoutes
    
    # return the dictionary
    return subwayStops