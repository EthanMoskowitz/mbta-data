import requests

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