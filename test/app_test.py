import sys
from io import StringIO
import pytest
from src.app import app

# expected output from stdout
expectedOutput = """Subway Routes: Red Line, Mattapan Trolley, Orange Line, Green Line B, Green Line C, Green Line D, Green Line E, Blue Line

Subway Route With The Most Stops:
Route: Green Line D - Stops: 25

Subway Route With The Least Stops:
Route: Mattapan Trolley - Stops: 8

Subway Stops With Two Or More Subway Routes:
Stop: Park Street - Routes: Red Line, Green Line B, Green Line C, Green Line D, Green Line E
Stop: Downtown Crossing - Routes: Red Line, Orange Line
Stop: Ashmont - Routes: Red Line, Mattapan Trolley
Stop: State - Routes: Orange Line, Blue Line
Stop: Haymarket - Routes: Orange Line, Green Line D, Green Line E
Stop: North Station - Routes: Orange Line, Green Line D, Green Line E
Stop: Government Center - Routes: Green Line B, Green Line C, Green Line D, Green Line E, Blue Line
Stop: Boylston - Routes: Green Line B, Green Line C, Green Line D, Green Line E
Stop: Arlington - Routes: Green Line B, Green Line C, Green Line D, Green Line E
Stop: Copley - Routes: Green Line B, Green Line C, Green Line D, Green Line E
Stop: Hynes Convention Center - Routes: Green Line B, Green Line C, Green Line D
Stop: Kenmore - Routes: Green Line B, Green Line C, Green Line D
Stop: Science Park/West End - Routes: Green Line D, Green Line E
Stop: Lechmere - Routes: Green Line D, Green Line E

Finding Path From One Stop To Another Stop:
Enter Starting Stop: Enter End Stop: """

# integration test
# test app function with pytest framework
def testApp(monkeypatch):
    
    # integration test 1 with Ashmont to Arlington
    inputData1 = "Ashmont\nArlington\n"

    # initialize a buffer to capture stdout
    stdoutBuffer = StringIO()

    # set stdin to the manual input
    monkeypatch.setattr("sys.stdin", StringIO(inputData1))

    # set stdout to the buffer
    sys.stdout = stdoutBuffer

    # call the function app
    app()

    # get the output from app
    output1 = stdoutBuffer.getvalue().strip()

    # add the input specific fields to expected output
    ashToArl = expectedOutput + "Ashmont to Arlington -> Red Line, Green Line B"

    assert output1 == ashToArl

    ################################################

    # integration test 2 with Beachmont to Harvard
    inputData2 = "Beachmont\nHarvard\n"

    # initialize a buffer to capture stdout
    stdoutBuffer = StringIO()

    # set stdin to the manual input
    monkeypatch.setattr("sys.stdin", StringIO(inputData2))

    # set stdout to the buffer
    sys.stdout = stdoutBuffer

    # call the function app
    app()

    # get the output from app
    output2 = stdoutBuffer.getvalue().strip()

    # add the input specific fields to expected output
    beaToHar = expectedOutput + "Beachmont to Harvard -> Blue Line, Green Line B, Red Line"

    assert output2 == beaToHar



