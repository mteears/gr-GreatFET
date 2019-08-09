#!/usr/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/root/Documents/GNURadio/oot/gr-GreatFET/python
export PATH=/root/Documents/GNURadio/oot/gr-GreatFET/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/root/Documents/GNURadio/oot/gr-GreatFET/build/swig:$PYTHONPATH
/usr/bin/python2 /root/Documents/GNURadio/oot/gr-GreatFET/python/qa_gpio_sink_f.py 
