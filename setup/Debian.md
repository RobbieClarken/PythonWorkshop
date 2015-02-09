Dependencies:

* [EPICS Base 3.14](http://www.aps.anl.gov/epics/base/R3-14/12.php)
* [SWIG 3.0.2](http://sourceforge.net/projects/swig/files/swig/swig-3.0.2/) (note: v3.0.3-3.0.5 are incompatible with pcaspy)

```bash
export EPICS_BASE=/epics/base   # Set this appropriately
export EPICS_HOST_ARCH=linux-x86_64
sudo apt-get install python-dev python-pip libzmq-dev gfortran \
                     libpng-dev libfreetype6-dev liblapack-dev libblas-dev
sudo pip install -U ipython[notebook] numpy pyepics pcaspy \
                    matplotlib scipy pandas virtualenv requests flask
```
