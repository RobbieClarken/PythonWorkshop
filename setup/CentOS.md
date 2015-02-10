Dependencies:

* [EPICS Base 3.14](http://www.aps.anl.gov/epics/base/R3-14/12.php)
* [SWIG 3.0.2](http://sourceforge.net/projects/swig/files/swig/swig-3.0.2/) (note: v3.0.3-3.0.5 are incompatible with pcaspy)

Check which version of Python your system has with `python --version`. If it
is less than 2.7 you will need to install a newer version from source as follows:

```bash
sudo yum groupinstall "Development tools"
sudo yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel
wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tar.xz -O- | tar -xJ
cd Python-2.7.9
./configure --prefix=/usr/local
make
sudo make altinstall
sudo ln -sf /usr/local/bin/python2.7 /usr/local/bin/python
hash -r
sudo visudo
# Add "/usr/local/bin:" to the start of secure_path
wget https://bootstrap.pypa.io/ez_setup.py -O- | sudo python
wget https://bootstrap.pypa.io/get-pip.py -O- | sudo python
hash -r
```

Install the required python libraries:

```bash
export EPICS_BASE=/epics/base   # Set this appropriately
export EPICS_HOST_ARCH=linux-x86_64
sudo yum install python-devel python-pip zeromq-devel gcc-c++ gcc-gfortran \
                 libpng-devel freetype-devel lapack-devel blas-devel
sudo pip install -U ipython[notebook] numpy pyepics pcaspy \
                    matplotlib scipy pandas virtualenv requests flask
```
