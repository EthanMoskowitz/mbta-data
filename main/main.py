from subway_routes import getSubwayRoutes
from subway_stops import getSubwayStops, findMaxStops, findMinStops, getStopsWithRoutes

# main driver of the program
def main():
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

# run main method
main()