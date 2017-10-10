import atexit
from . pyduckling import py_init, py_exit, parse
import json
from datetime import datetime
from dateutil import parser

atexit.register(py_exit)
py_init([])


def parse_time(text, lang='EN', date=0):
    """parse a text using duckling and return the Time dimension as
    json

    :param text string: The text to be parsed
    :param lang string: The language of the text as two letter code
        (see duckling)
    :param date int: The current time in milliseconds since the epoch
        (UTC) (e.g. int(1000 * datetime.timestamp(datetime.utcnow())))

    :returns: The duckling json representation of all found time
              expressions.
    """
    try:
        type(date) != int
        date = int(1000 * datetime.timestamp(parser.parse(date)))
        return json.loads(parse(text, lang, date))
    except:
        return json.loads(parse(text, lang, date))
