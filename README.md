python-kyotocabinet
===================

my personal repo for kyotocabinet built for python2.6 on windows (hackish)

what i did : 

- MinGW 4.6.2
- compile manually *.cc in kc dir (some files requires -std=c++0x such as kcregex.cc and kcthreads.cc , except for kcutil.cc )
- combine all object file into library (`ar -r libkc.a *.o`)
- run `setup.py build -c mingw32` (don't forget to edit include dir in setup.py)

you will get kyotocabinet.pyd in build directory

WARNING: use at your own risk!