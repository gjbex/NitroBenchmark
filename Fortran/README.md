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
1. `gauss_quad_load.py`: workload generator for `quad_test.exe`.

How to use it?
--------------
To build, simply run the make file, e.g., to use the Intel compiler:
```
$ make F90=ifort
```
The default compiler is GCC.

To run, `gauss_test.exe` expects three command line arguments:
1. the number of points to compute the quadrature with,
1. the lower bound of the integration domain,
1. the upper bound of the integration domain, and
1. the number of quadratures to be computed, each over a slightly
    shifted domain; finally, the sum of all those quadratures is the
    output.

Hence to compute the quadrature over the domain [-1.0, 3.0] using 100
points:
```
$ ./gauss_test.exe 100 -1.0 3.0 1
```

To generate a workload for Nitro, the `gauss_quad_load.py` script can be
used.  It can generate workloads where the execution time of a work item
is:
1. constant _t_, using the `--length t` option to specify it,
1. drawn from a uniform distribution over [_a_, _b_], specifyed by
    `--min a  --max b`, and
1. drawn from a gamma distrution with shape _lambda_, specified by
    `--shape lambda`.

For example, to create a workload consisting of 70 work items with a
uniform distribution for their execution times in the interval
[10.0, 30.0] seconds:
```
$ ./gauss_quad_load.py  --n 70  --type uniform  --min 10.0  --max 30.0
```
