from src.modules.subway_routes import getSubwayRoutes, findPathBetweenStops
from src.modules.subway_stops import findMaxStops, findMinStops, getStopsWithRoutes

# main application of the program
def app():
    # get json data of subway routes
    subwayRoutes = getSubwayRoutes()

    print("Subway Routes:", end = " ")

    # loop through all the routes in subwayRoutes
    for i, route in enumerate(subwayRoutes):
        print(route['attributes']['long_name'], end = "")

        # if not the last route in the list, follow the long name with ', '
        if i < len(subwayRoutes) - 1:
            print(", ", end = "")
    print()
    print()

    # get the route with the most stops and the number of those stops
    maxStops, maxRoute = findMaxStops(subwayRoutes)

    print("Subway Route With The Most Stops:")
    print(f"Route: {maxRoute} - Stops: {maxStops}")
    print()

    # get the route with the least stops and the number of those stops
    minStops, minRoute = findMinStops(subwayRoutes)

    print("Subway Route With The Least Stops:")
    print(f"Route: {minRoute} - Stops: {minStops}")
    print()

    # get all subway stops and their corresponding routes
    subwayStops = getStopsWithRoutes(subwayRoutes)

    print("Subway Stops With Two Or More Subway Routes:")

    # loop through all the stops in subwayStops
    for stop in subwayStops:

        # only printing out stops that connect two or more routes
        if len(subwayStops[stop]) > 1:
            print("Stop: " + stop, end=" - Routes: ")

            # loop through each route connected to the stop
            for i, route in enumerate(subwayStops[stop]):
                print(route, end="")

                # if not the last route in the list, follow the long name with ', '
                if i < len(subwayStops[stop]) - 1:
                    print(", ", end="")
            print()
    print()
    
    # loop for taking in valid user input
    while True:
        print("Finding Path From One Stop To Another Stop:")

        # prompt for starting stop
        startStop = input("Enter Starting Stop: ")

        # check if input is a valid stop
        if startStop not in subwayStops.keys():
            print("Station Not Found, Try Again")
            print()
            continue

        # prompt for end stop
        endStop = input("Enter End Stop: ")

        # check if input is a valid stop
        if endStop not in subwayStops.keys():
            print("Station Not Found, Try Again")
            print()
            continue

        # check that inputs are different
        if (startStop == endStop):
            print("Same Station Entered")
            print()
            continue

        # if inputs are valid, move on
        break
    
    # get the path between the start and end stops
    path = findPathBetweenStops(startStop, endStop, subwayStops)
    
    # if a path is found, print it out
    if len(path) > 0:
        print(startStop + " to " + endStop, end=" -> ")

        # print each stop
        for i, route in enumerate(path):
            print(route, end="")

            # if not the last route in the list, follow the long name with ', '
            if i < len(path) - 1:
                print(", ", end="")
    else:
        # if no path is found, print this
        print("No Path Found Between Stations")
    print()