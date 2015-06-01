NitroBenchmarks
===============

A number of programs to use as work tiems for workload generations scripts
to be used for benchmarking subschedulers.

What is it?
-----------
1. `Fortran`: Fortran code that computes the quadrature of a function
    using the Legendre-Gauss algorithm.  It first generates the abscisses
    and weights, and then proceeds to compute a quadrature.
1. `R`: Script that computes a nonlinear regression on data points
    generated from a Gaussian function.  A driver to generate workloads
    according to various walltime distributions is included.
