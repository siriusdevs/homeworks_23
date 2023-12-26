"""tests for hw3."""
import pytest

import hw3

FLIGHT = hw3.Flight('007R43', 'sochi airport', 'novokuzneck')
PASSANGER = hw3.Passenger('Vika', 8)

DATA_FLIGHT = (
    (
        ('nomer', 'aeroport dudkovo', 'pekarnya aeroport'),
        'nomer aeroport dudkovo pekarnya aeroport',
    ),
)

DATA1_FLIGHT = (
    (
        ('Mm017R43', 'Stambul airport', 'Novokuzneck airport'),
        'Mm017R43 Stambul airport Novokuzneck airport',
    ),
)

DATA_PASSANGER = (
    (
        ('Nika', 9),
        'Nika 9',
    ),
)

DATA1_PASSANGER = (
    (
        ('artemka228', 6),
        'artemka228 6',
    ),
)

DATA_TICKET = (
    (
        ('F00765', FLIGHT, PASSANGER),
        'F00765 007R43 sochi airport novokuzneck Vika 8',
    ),
)

DATA1_TICKET = (
    (
        ('MMLK00T5', FLIGHT, PASSANGER),
        'MMLK00T5 007R43 sochi airport novokuzneck Vika 8',
    ),
)


@pytest.mark.parametrize('input_data, expected', DATA_FLIGHT)
def test_flight_fst(input_data: tuple, expected: str) -> None:
    """Test for correct flight data.

    Args:
        input_data (tuple): info about flight
        expected (str): output info from code
    """
    test_flight = str(hw3.Flight(*input_data))
    assert test_flight == expected


@pytest.mark.parametrize('input_data2, expected', DATA_PASSANGER)
def test_passanger_fst(input_data2: tuple, expected: str) -> None:
    """Test for correct passanger data.

    Args:
        input_data2 (tuple): info about passenger
        expected (str): output info from code
    """
    test_passanger = str(hw3.Passenger(*input_data2))
    assert test_passanger == expected


@pytest.mark.parametrize('input_data4, expected', DATA_TICKET)
def test_ticket_fst(input_data4: tuple, expected: str) -> None:
    """Test for correct ticket data.

    Args:
        input_data4 (tuple): info about ticket
        expected (str): output info from code
    """
    test_ticket = str(hw3.Ticket(*input_data4))
    assert test_ticket == expected


@pytest.mark.parametrize('input_data5, expected', DATA1_TICKET)
def test_ticket_sec(input_data5: tuple, expected: str) -> None:
    """Test for correct ticket data the second one.

    Args:
        input_data5 (tuple): info about ticket
        expected (str): output info from code
    """
    test_ticket = str(hw3.Ticket(*input_data5))
    assert test_ticket == expected


FLIGHT1 = hw3.Flight('0079KK0', 'Dubai airportt', 'Moskow airport')
PASSANGER1 = hw3.Passenger('Alex', 8)
TICKET = hw3.Ticket('T4300', FLIGHT, PASSANGER)
TICKET1 = hw3.Ticket('MN0T5', FLIGHT1, PASSANGER1)
AIRLINE_TEST = (
    (
        (
            'Uralskie Avialinii',
            [FLIGHT, FLIGHT1],
            [PASSANGER, PASSANGER1],
            [TICKET, TICKET1],
        ),
        f'Uralskie Avialinii {[FLIGHT, FLIGHT1]} {[PASSANGER, PASSANGER1]} {[TICKET, TICKET1]}',
    ),
)


@pytest.mark.parametrize('input_data6, expected', AIRLINE_TEST)
def test_airline_fst(input_data6: tuple, expected: str) -> None:
    """Test for correct airline data.

    Args:
        input_data6 (tuple): ifo abot airline
        expected (str): output info from code
    """
    test_airline = str(hw3.Airline(*input_data6))
    assert test_airline == expected


FLIGHT2 = hw3.Flight('008K0', 'Spritc airportt', 'Downtown airport')
PASSANGER2 = hw3.Passenger('Soniya', 6)
TICKET2 = hw3.Ticket('0T000005', FLIGHT2, PASSANGER2)
AIRLINE_METODS_TEST = (
    (
        (
            'Uralskie Avialinii',
            [FLIGHT, FLIGHT1],
            [PASSANGER, PASSANGER1],
            [TICKET, TICKET1],
        ),
        f'Uralskie Avialinii {[FLIGHT, FLIGHT2]} {[PASSANGER1, PASSANGER2]} {[TICKET, TICKET2]}',
    ),
)


@pytest.mark.parametrize('input_data7, expected', AIRLINE_METODS_TEST)
def test_airline_sec(input_data7: tuple, expected: str) -> None:
    """Test for airline metods data.

    Args:
        input_data7 (tuple): info about airline
        expected (str): output info from code
    """
    test_airline = hw3.Airline(*input_data7)
    test_airline.add_flight(FLIGHT2)
    test_airline.remove_flight(FLIGHT1)
    test_airline.add_passenger(PASSANGER2)
    test_airline.remove_passenger(PASSANGER)
    test_airline.buy_ticket(TICKET2)
    test_airline.cancel_ticket(TICKET1)
    test_airline = str(test_airline)
    assert test_airline == expected


@pytest.mark.xfail
def test_fail_thr():
    """Error test for flight."""
    hw3.Flight(1, 'sharik', 'novosib airport')


@pytest.mark.xfail
def test_fail_fif():
    """Error test for passenger."""
    hw3.Passenger('Bob', '4444908755667634')


@pytest.mark.xfail
def test_fail_six():
    """Error test for ticket."""
    hw3.Ticket('21FPL0099', FLIGHT, 1)


@pytest.mark.xfail
def test_fail_nin():
    """Error test for Airline."""
    hw3.Airline(3)
