Dependencies:

* [EPICS Base 3.14](http://www.aps.anl.gov/epics/base/R3-14/12.php)
* [Swig 3.0.2](http://sourceforge.net/projects/swig/files/swig/swig-3.0.2/)

```bash
export EPICS_BASE=/epics/base   # Set this appropriately
export EPICS_HOST_ARCH=linux-x86_64
sudo yum install python-devel python-pip zeromq-devel gcc-c++ gcc-gfortran \
                 libpng-devel freetype-devel lapack-devel blas-devel
sudo pip install -U ipython[notebook] numpy pyepics pcaspy \
                    matplotlib scipy pandas virtualenv requests flask
```
