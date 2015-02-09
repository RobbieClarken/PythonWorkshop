Dependencies:

* [Anaconda Python distribution](https://store.continuum.io/cshop/anaconda/)
* [EPICS Base 3.14](http://www.aps.anl.gov/epics/base/R3-14/12.php)
* [Swig 3.0.2](http://sourceforge.net/projects/swig/files/swigwin/swigwin-3.0.2/) (just copy the folder in the zip to C:\ and add it to your `PATH`)

```
set EPICS_BASE=C:\EPICS\base      # Set this appropriately
set EPICS_HOST_ARCH=win32-x86
set PATH=C:\Users\<username>\Anaconda\Scripts;%PATH%
conda install virtualenv
pip install pyepics pcaspy
```

To make EPICS on Windows
