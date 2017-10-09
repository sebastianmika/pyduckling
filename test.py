import pytest
from datetime import time, date, timedelta, datetime
from dateutil import parser
from pyduckling import parse_time


@pytest.fixture
def current_time():
    return int(1000 * datetime.timestamp(datetime.utcnow()))


def test_parse_time():
    result = parse_time(
        u'Let\'s meet at 11:45am')
    assert len(result) == 1
    assert time(11, 45) == parser.parse(result[0][u'value'][u'value']).time()


def test_parse_time_with_reference_date():
    result = parse_time(
        u'Let\'s meet tomorrow', date=u'1990-12-30')
    assert len(result) == 1
    assert parser.parse(u'1990-12-30').date() + \
        timedelta(days=1) == parser.parse(result[0][u'value'][u'value']).date()

def test_parse_time_with_reference_date_and_time():
    result = parse_time(
        u'Let\'s meet tomorrow at 5pm', date=u'1990-12-30T08:26:07.470413')
    assert len(result) == 1
    assert parser.parse(u'1990-12-30').date() + \
        timedelta(days=1) == parser.parse(result[0][u'value'][u'value']).date()
    assert time(17, 00) == parser.parse(result[0][u'value'][u'value']).time()

def test_parse_time_with_reference_date_and_time_2():
    result = parse_time(
        u'Let\'s meet tomorrow at 17h', date=u'1990-12-30T08:26:07')
    assert len(result) == 1
    assert parser.parse(u'1990-12-30').date() + \
        timedelta(days=1) == parser.parse(result[0][u'value'][u'value']).date()
    assert time(17, 00) == parser.parse(result[0][u'value'][u'value']).time()

def test_parse_time_with_reference_date_and_time_3():
    result = parse_time(
        u'Let\'s meet tomorrow at 17:45', date=u'1990-12-30T08:26:07')
    assert len(result) == 1
    assert parser.parse(u'1990-12-30').date() + \
        timedelta(days=1) == parser.parse(result[0][u'value'][u'value']).date()
    assert time(17, 45) == parser.parse(result[0][u'value'][u'value']).time()

def test_parse_time_with_reference_date_and_time_4():
    result = parse_time(
        u'Let\'s meet in one week', date=u'1990-12-30T08:26:07')
    assert len(result) == 1
    assert parser.parse(u'1990-12-30').date() + \
        timedelta(days=7) == parser.parse(result[0][u'value'][u'value']).date()

def test_parse_time_with_reference_date_and_time_5():
    result = parse_time(
        u'Let\'s meet in 2h', date=u'1990-12-30T08:26:07')
    assert len(result) == 1
    assert parser.parse(u'1990-12-30').date() + \
        timedelta(days=0) == parser.parse(result[0][u'value'][u'value']).date()
    assert time(10, 26) == parser.parse(result[0][u'value'][u'value']).time()

def test_parse_multiple_times():
    result = parse_time(
        u'Let\'s meet at 11:45am or tomorrow', date=current_time())
    assert len(result) == 2
    assert time(11, 45) == parser.parse(result[0][u'value'][u'value']).time()
    assert date.today() + \
        timedelta(days=1) == parser.parse(result[1][u'value'][u'value']).date()

def test_parse_multiple_times_2():
    result = parse_time(
        u'Let\'s meet at 11:45am, or tomorrow at 11am or in one week', date=current_time())
    assert len(result) == 3
    assert time(11, 45) == parser.parse(result[0][u'value'][u'value']).time()
    assert date.today() + \
        timedelta(days=1) == parser.parse(result[1][u'value'][u'value']).date()
    assert time(11, 00) == parser.parse(result[1][u'value'][u'value']).time()
    assert date.today() + \
        timedelta(days=7) == parser.parse(result[2][u'value'][u'value']).date()


