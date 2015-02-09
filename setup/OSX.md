Dependencies:

* [Homebrew](http://brew.sh/)
* [EPICS Base 3.14](http://www.aps.anl.gov/epics/base/R3-14/12.php)
* [SWIG 3.0.2](http://sourceforge.net/projects/swig/files/swig/swig-3.0.2/) (the homebrew version is incompatible with pcaspy)

```bash
export EPICS_BASE=/Library/EPICS/Base   # Set this appropriately
export EPICS_HOST_ARCH=darwin-x86
brew install python gfortran freetype jpeg lzlib
pip install -U ipython[notebook] numpy pyepics pcaspy \
               matplotlib scipy pandas virtualenv requests flask
```
