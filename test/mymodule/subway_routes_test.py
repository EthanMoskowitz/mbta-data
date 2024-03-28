import pytest
from myapp.mymodule.subway_routes import *

# test getSubwayRoutes function with pytest framework
def testGetSubwayRoutes():
    # test that function getSubwayRoutes does not raise an exception
    try:
        getSubwayRoutes()
    except Exception as exc:
        assert False, f"getSubwayRoutes() raised an exception {exc}"

    # test that function getSubwayRoutes returns the correct routes from api
    mockRoutes = [{'attributes': {'color': 'DA291C', 'description': 'Rapid Transit', 'direction_destinations': ['Ashmont/Braintree', 'Alewife'], 'direction_names': ['South', 'North'], 'fare_class': 'Rapid Transit', 'long_name': 'Red Line', 'short_name': '', 'sort_order': 10010, 'text_color': 'FFFFFF', 'type': 1}, 'id': 'Red', 'links': {'self': '/routes/Red'}, 'relationships': {'line': {'data': {'id': 'line-Red', 'type': 'line'}}}, 'type': 'route'}, {'attributes': {'color': 'DA291C', 'description': 'Rapid Transit', 'direction_destinations': ['Mattapan', 'Ashmont'], 'direction_names': ['Outbound', 'Inbound'], 'fare_class': 'Rapid Transit', 'long_name': 'Mattapan Trolley', 'short_name': '', 'sort_order': 10011, 'text_color': 'FFFFFF', 'type': 0}, 'id': 'Mattapan', 'links': {'self': '/routes/Mattapan'}, 'relationships': {'line': {'data': {'id': 'line-Mattapan', 'type': 'line'}}}, 'type': 'route'}, {'attributes': {'color': 'ED8B00', 'description': 'Rapid Transit', 'direction_destinations': ['Forest Hills', 'Oak Grove'], 'direction_names': ['South', 'North'], 'fare_class': 'Rapid Transit', 'long_name': 'Orange Line', 'short_name': '', 'sort_order': 10020, 'text_color': 'FFFFFF', 'type': 1}, 'id': 'Orange', 'links': {'self': '/routes/Orange'}, 'relationships': {'line': {'data': {'id': 'line-Orange', 'type': 'line'}}}, 'type': 'route'}, {'attributes': {'color': '00843D', 'description': 'Rapid Transit', 'direction_destinations': ['Boston College', 'Government Center'], 'direction_names': ['West', 'East'], 'fare_class': 'Rapid Transit', 'long_name': 'Green Line B', 'short_name': 'B', 'sort_order': 10032, 'text_color': 'FFFFFF', 'type': 0}, 'id': 'Green-B', 'links': {'self': '/routes/Green-B'}, 'relationships': {'line': {'data': {'id': 'line-Green', 'type': 'line'}}}, 'type': 'route'}, {'attributes': {'color': '00843D', 'description': 'Rapid Transit', 'direction_destinations': ['Cleveland Circle', 'Government Center'], 'direction_names': ['West', 'East'], 'fare_class': 'Rapid Transit', 'long_name': 'Green Line C', 'short_name': 'C', 'sort_order': 10033, 'text_color': 'FFFFFF', 'type': 0}, 'id': 'Green-C', 'links': {'self': '/routes/Green-C'}, 'relationships': {'line': {'data': {'id': 'line-Green', 'type': 'line'}}}, 'type': 'route'}, {'attributes': {'color': '00843D', 'description': 'Rapid Transit', 'direction_destinations': ['Riverside', 'Union Square'], 'direction_names': ['West', 'East'], 'fare_class': 'Rapid Transit', 'long_name': 'Green Line D', 'short_name': 'D', 'sort_order': 10034, 'text_color': 'FFFFFF', 'type': 0}, 'id': 'Green-D', 'links': {'self': '/routes/Green-D'}, 'relationships': {'line': {'data': {'id': 'line-Green', 'type': 'line'}}}, 'type': 'route'}, {'attributes': {'color': '00843D', 'description': 'Rapid Transit', 'direction_destinations': ['Heath Street', 'Medford/Tufts'], 'direction_names': ['West', 'East'], 'fare_class': 'Rapid Transit', 'long_name': 'Green Line E', 'short_name': 'E', 'sort_order': 10035, 'text_color': 'FFFFFF', 'type': 0}, 'id': 'Green-E', 'links': {'self': '/routes/Green-E'}, 'relationships': {'line': {'data': {'id': 'line-Green', 'type': 'line'}}}, 'type': 'route'}, {'attributes': {'color': '003DA5', 'description': 'Rapid Transit', 'direction_destinations': ['Bowdoin', 'Wonderland'], 'direction_names': ['West', 'East'], 'fare_class': 'Rapid Transit', 'long_name': 'Blue Line', 'short_name': '', 'sort_order': 10040, 'text_color': 'FFFFFF', 'type': 1}, 'id': 'Blue', 'links': {'self': '/routes/Blue'}, 'relationships': {'line': {'data': {'id': 'line-Blue', 'type': 'line'}}}, 'type': 'route'}]
    assert getSubwayRoutes() == mockRoutes

# test listOfStops function with pytest framework
def testListOfStops():
    # testing with blue line
    blueLine = "Blue Line"
    blueLineList = ['Bowdoin', 'Government Center', 'State', 'Aquarium', 'Maverick', 'Airport', 'Wood Island', 'Orient Heights', 'Suffolk Downs', 'Beachmont', 'Revere Beach', 'Wonderland']
    assert listOfStops(blueLine) == blueLineList

    # testing with orange line
    orangeLine = "Orange Line"
    orangeLineList = ['Forest Hills', 'Green Street', 'Stony Brook', 'Jackson Square', 'Roxbury Crossing', 'Ruggles', 'Massachusetts Avenue', 'Back Bay', 'Tufts Medical Center', 'Chinatown', 'Downtown Crossing', 'State', 'Haymarket', 'North Station', 'Community College', 'Sullivan Square', 'Assembly', 'Wellington', 'Malden Center', 'Oak Grove']
    assert listOfStops(orangeLine) == orangeLineList

# test findPathBetweenStops function with pytest framework
def testFindPathBetweenStops():
    # dictionary of all the stops for testing purposes
    stopDictionary = {'Alewife': ['Red Line'], 'Davis': ['Red Line'], 'Porter': ['Red Line'], 'Harvard': ['Red Line'], 'Central': ['Red Line'], 'Kendall/MIT': ['Red Line'], 'Charles/MGH': ['Red Line'], 'Park Street': ['Red Line', 'Green Line B', 'Green Line C', 'Green Line D', 'Green Line E'], 'Downtown Crossing': ['Red Line', 'Orange Line'], 'South Station': ['Red Line'], 'Broadway': ['Red Line'], 'Andrew': ['Red Line'], 'JFK/UMass': ['Red Line'], 'Savin Hill': ['Red Line'], 'Fields Corner': ['Red Line'], 'Shawmut': ['Red Line'], 'Ashmont': ['Red Line', 'Mattapan Trolley'], 'North Quincy': ['Red Line'], 'Wollaston': ['Red Line'], 'Quincy Center': ['Red Line'], 'Quincy Adams': ['Red Line'], 'Braintree': ['Red Line'], 'Cedar Grove': ['Mattapan Trolley'], 'Butler': ['Mattapan Trolley'], 'Milton': ['Mattapan Trolley'], 'Central Avenue': ['Mattapan Trolley'], 'Valley Road': ['Mattapan Trolley'], 'Capen Street': ['Mattapan Trolley'], 'Mattapan': ['Mattapan Trolley'], 'Forest Hills': ['Orange Line'], 'Green Street': ['Orange Line'], 'Stony Brook': ['Orange Line'], 'Jackson Square': ['Orange Line'], 'Roxbury Crossing': ['Orange Line'], 'Ruggles': ['Orange Line'], 'Massachusetts Avenue': ['Orange Line'], 'Back Bay': ['Orange Line'], 'Tufts Medical Center': ['Orange Line'], 'Chinatown': ['Orange Line'], 'State': ['Orange Line', 'Blue Line'], 'Haymarket': ['Orange Line', 'Green Line D', 'Green Line E'], 'North Station': ['Orange Line', 'Green Line D', 'Green Line E'], 'Community College': ['Orange Line'], 'Sullivan Square': ['Orange Line'], 'Assembly': ['Orange Line'], 'Wellington': ['Orange Line'], 'Malden Center': ['Orange Line'], 'Oak Grove': ['Orange Line'], 'Government Center': ['Green Line B', 'Green Line C', 'Green Line D', 'Green Line E', 'Blue Line'], 'Boylston': ['Green Line B', 'Green Line C', 'Green Line D', 'Green Line E'], 'Arlington': ['Green Line B', 'Green Line C', 'Green Line D', 'Green Line E'], 'Copley': ['Green Line B', 'Green Line C', 'Green Line D', 'Green Line E'], 'Hynes Convention Center': ['Green Line B', 'Green Line C', 'Green Line D'], 'Kenmore': ['Green Line B', 'Green Line C', 'Green Line D'], 'Blandford Street': ['Green Line B'], 'Boston University East': ['Green Line B'], 'Boston University Central': ['Green Line B'], 'Amory Street': ['Green Line B'], 'Babcock Street': ['Green Line B'], "Packard's Corner": ['Green Line B'], 'Harvard Avenue': ['Green Line B'], 'Griggs Street': ['Green Line B'], 'Allston Street': ['Green Line B'], 'Warren Street': ['Green Line B'], 'Washington Street': ['Green Line B'], 'Sutherland Road': ['Green Line B'], 'Chiswick Road': ['Green Line B'], 'Chestnut Hill Avenue': ['Green Line B'], 'South Street': ['Green Line B'], 'Boston College': ['Green Line B'], 'Cleveland Circle': ['Green Line C'], 'Englewood Avenue': ['Green Line C'], 'Dean Road': ['Green Line C'], 'Tappan Street': ['Green Line C'], 'Washington Square': ['Green Line C'], 'Fairbanks Street': ['Green Line C'], 'Brandon Hall': ['Green Line C'], 'Summit Avenue': ['Green Line C'], 'Coolidge Corner': ['Green Line C'], 'Saint Paul Street': ['Green Line C'], 'Kent Street': ['Green Line C'], 'Hawes Street': ['Green Line C'], "Saint Mary's Street": ['Green Line C'], 'Riverside': ['Green Line D'], 'Woodland': ['Green Line D'], 'Waban': ['Green Line D'], 'Eliot': ['Green Line D'], 'Newton Highlands': ['Green Line D'], 'Newton Centre': ['Green Line D'], 'Chestnut Hill': ['Green Line D'], 'Reservoir': ['Green Line D'], 'Beaconsfield': ['Green Line D'], 'Brookline Hills': ['Green Line D'], 'Brookline Village': ['Green Line D'], 'Longwood': ['Green Line D'], 'Fenway': ['Green Line D'], 'Science Park/West End': ['Green Line D', 'Green Line E'], 'Lechmere': ['Green Line D', 'Green Line E'], 'Union Square': ['Green Line D'], 'Heath Street': ['Green Line E'], 'Back of the Hill': ['Green Line E'], 'Riverway': ['Green Line E'], 'Mission Park': ['Green Line E'], 'Fenwood Road': ['Green Line E'], 'Brigham Circle': ['Green Line E'], 'Longwood Medical Area': ['Green Line E'], 'Museum of Fine Arts': ['Green Line E'], 'Northeastern University': ['Green Line E'], 'Symphony': ['Green Line E'], 'Prudential': ['Green Line E'], 'East Somerville': ['Green Line E'], 'Gilman Square': ['Green Line E'], 'Magoun Square': ['Green Line E'], 'Ball Square': ['Green Line E'], 'Medford/Tufts': ['Green Line E'], 'Bowdoin': ['Blue Line'], 'Aquarium': ['Blue Line'], 'Maverick': ['Blue Line'], 'Airport': ['Blue Line'], 'Wood Island': ['Blue Line'], 'Orient Heights': ['Blue Line'], 'Suffolk Downs': ['Blue Line'], 'Beachmont': ['Blue Line'], 'Revere Beach': ['Blue Line'], 'Wonderland': ['Blue Line']}

    # testing path that requires one route
    startStop1 = "Assembly"
    endStop1 = "Ruggles"
    path1 = ["Orange Line"]
    assert findPathBetweenStops(startStop1, endStop1, stopDictionary) == path1

    # testing path that requires one route
    startStop2 = "Davis"
    endStop2 = "Kendall/MIT"
    path2 = ["Red Line"]
    assert findPathBetweenStops(startStop2, endStop2, stopDictionary) == path2

    # testing path that requires two routes
    startStop3 = "Ashmont"
    endStop3 = "Arlington"
    path3 = ["Red Line", "Green Line B"]
    assert findPathBetweenStops(startStop3, endStop3, stopDictionary) == path3

    # testing path that requires three routes
    startStop4 = "Beachmont"
    endStop4 = "Harvard"
    path4 = ["Blue Line", "Green Line B", "Red Line"]
    assert findPathBetweenStops(startStop4, endStop4, stopDictionary) == path4
