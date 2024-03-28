import requests
from .subway_stops import getSubwayStops

# gets subway routes from mbta api
#
# @return data section from the json returned from the get request to mbta api
# @raises JSONDecodeError exception upon failed connection to mbta api
def getSubwayRoutes():
    # set the url for the get request
    url = "https://api-v3.mbta.com/routes"

    # set parameters for get request to filter for light and heavy rail
    # also includes generated api key for access to the api data
    payload = {"filter[type]": "0,1", "api_key": "fec1b0ff62e047ca972e2571a62cf156"}

    # utilize requests library to make a get request using the url and parameters
    request = requests.get(url, params=payload)

    # turn the get request into json form
    routes = request.json()

    # return the 'data' information from the json routes
    return routes["data"]

# produce a list of the names of stops on a given route
#
# @params name of the route to get stops from
# @return a list of the stops on the given route
def listOfStops(route):
    # get all the routes in JSON form
    tempRoutes = getSubwayRoutes()

    # get the JSON of the given route
    chosenRoute = [item for item in tempRoutes if item.get("attributes", {}).get("long_name") == route]
    pickRoute = chosenRoute[0]

    # get the JSON list of stops for the given route
    stops = getSubwayStops(pickRoute)
    newList = []

    # create the list of the names of stops
    for stop in stops:
        newList.append(stop['attributes']['name'])
    
    # return the list
    return newList

# finds a path of routes between two given stops
#
# @params start stop, end stop, stop dictionary, visited stops set (initially None)
# @return a list of the routes to take to get from start to end
def findPathBetweenStops(start, end, stops, visited=None):
    # if the first call, initialize visited to an empty set
    if visited is None:
        visited = set()

    # if the start stop and end stop are the same,
    # return empty list
    if start == end:
        return []

    # add the current start stop to visited
    visited.add(start)

    # check if the current start stop and end stop
    # are in the same route and then return that route
    for route in stops[start]:
        if route in stops[end]:
            return [route]

    # iterate through each route connected to start stop
    for route in stops[start]:
        # get a list of the stops on current route
        stopList = listOfStops(route)

        # iterate through each of the stops
        for stop in stopList:

            # if current stop hasn't been visited
            if stop not in visited:

                # find a path from that stop to the end stop
                # pass visited set to make sure stops aren't revisited
                path = findPathBetweenStops(stop, end, stops, visited)

                # if a path is found
                if path is not None:

                    # if the route is already in the path,
                    # remove it from path
                    if route in path:
                        path.remove(route)
                    
                    # return the a list with the current route
                    # and the path found
                    return [route] + path

    # return empty list if no route found
    return []

