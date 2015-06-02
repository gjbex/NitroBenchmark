Fortran
=======

Fortran code to perform Legendre-Gauss quadrature, first the roots
of the Legendre polynoms up to the desired degree are computed, and
those are then used to perform the quadrature computation with the
appropriate weights.

What is it?
-----------
1. `quad_func_interface.f90`: interface that functionns to compute the
    quadrature off should implement.
1. `quad_mod.f90`: interface for quadrature procedures.
1. `gauss_mod.f90`: Legendre-Gauss quadrature implementation.
1. `gauss_test.f90`: driver program
1. `Makefile`: make file to build the application.

How to use it?
--------------

To build, simply run the make file, e.g., to use the Intel compiler:
```
$ make F90=ifort
```
The default compiler is GCC.

To run, `gauss_test.exe` expects three command line arguments:
1. the number of points to compute the quadrature with,
1. the lower bound of the integration domain, and
1. the upper bound of the integration domain.

Hence to compute the quadrature over the domain [-1.0, 3.0] using 100
points:
```
$ ./gauss_test.exe 100 -1.0 3.0
```
