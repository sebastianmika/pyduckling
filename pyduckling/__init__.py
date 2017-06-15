import atexit
import pyduckling
import json

atexit.register(pyduckling.py_exit)
pyduckling.py_init([])


def parse_time(text, lang='EN', date=0):
    """parse a text using duckling and return the Time dimension as
    json

    :param text string: The text to be parsed
    :param lang string: The language of the text as two letter code
        (see duckling)
    :param date int: The current time in milliseconds since the epoch
        (UTC)

    :returns: The duckling json representation of all found time
              expressions.
    """
    return json.loads(pyduckling.parse(text, lang, date))
