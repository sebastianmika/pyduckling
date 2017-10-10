FROM python:3.5

ENV PATH=/root/.local/bin:$PATH

RUN apt-get update -y && apt-get install -y swig
RUN curl -sSL https://get.haskellstack.org/ | sh
RUN stack setup
COPY . /pyduckling
WORKDIR /pyduckling/pyduckling
RUN stack build
RUN stack ghc -- -c -dynamic -fPIC DucklingFFI.hs
RUN swig -python pyduckling.i
RUN gcc -fpic -c pyduckling.c pyduckling_wrap.c `python3.5-config --includes` -I`stack ghc -- --print-libdir`/include
RUN stack ghc --package duckling -- -o _pyduckling.so -shared -dynamic -fPIC pyduckling.o pyduckling_wrap.o DucklingFFI.o -lHSrts-ghc8.0.2
WORKDIR /pyduckling
RUN pip install pytest python-dateutil

