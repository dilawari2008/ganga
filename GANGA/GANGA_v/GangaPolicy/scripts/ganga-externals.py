## This file lists the set of Ganga externals. Is is simply executed by
## the lhcb-prepare script

# These are the external packages with only Python code.
externals_noarch = [['ApMon','2.2.11'],
                    ['httplib2', '0.8'],
                    ['python-gflags', '2.0'],
                    ['google-api-python-client', '1.1'],
                    ['figleaf', '0.6'],
                    ['paramiko', '1.7.3'],
                    ['PYTF','1.6'],
                    ['stomputil','2.3'],
                    ['ipython', '0.6.13_ganga_patch1']]


# These are the packages with architecture dependent code.
externals_arch = [['matplotlib','1.1.1'],
                  ['numpy','1.6.2'],
                  ['pycrypto','2.0.1']]
archs = ['x86_64-slc6-gcc48-opt','x86_64-slc6-gcc46-opt','x86_64-slc5-gcc46-opt']

# when comparing to top level Ganga PACKAGE.py need to compare just
# the numeric versions so list here the bits that bloat the version
# numbers and what to replace them with when checking. i.e. '.'
# seperated digits are compared
version_check_bloats = { 'ipython':[('_ganga_patch','.')],
                         'pyqt':[('_python2.5','')] }

