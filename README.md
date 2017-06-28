# pyduckling - a native python interface to the haskell version of duckling

Duckling by wit.ai/Facebook (https://github.com/facebookincubator/duckling) is one of the best libraries to find and parse time expressions.

This package contains a native python wrapper to use duckling directly from within python. It basically provides a wrapper for the Haskell FFI (Foreign Function Interface).

**Note**: This code is experimental. Contributions are welcome, but I cannot guarantee to integrate stuff quickly. But please feel free to use it as an inspiration for your own work.


# Usage

The wrapper currently only supports the Time dimension, but should be easily extendable to other extensions (see `DucklingFFI.hs`). I only tested it within Docker containers. There the process is as follows:

* in the project root build the image `docker build -t pyduckling .`

* start a shell in the container `docker run -it pyduckling bash`

* start python

* run:


```
from datetime import datetime
from pyduckling import parse_time

now = int(1000 * datetime.timestamp(datetime.utcnow()))

parse_time('next week', 'EN', now)
parse_time('nächsten Montag', 'week', 'DE', now)
```

