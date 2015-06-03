R
=

R code to perform a non-linear regression on noisy Gaussian data.

What is it?
-----------
1. `base_line.R`: a script that performs a single assignment statement so
    one can establish a base line, i.e., the time it takes to launch R.
1. `gauss_fit.R`: script that constitutes the actual payload, i.e., the
    work item.
1. `gauss_fit_driver.sh`: driver Bash shell script to load the appropriate
    R module, change to working directory and executing the script using
    `Rscript`.
1. ``gauss_fit_load.py`: workload generator for `gauss_fit.R`.

How to use it?
--------------
To run, `gauss_fit.R` expects five command line arguments:

1. the number of data points to perform the fit,
1. the mean value of the Gaussian curve,
1. the standard deviation of the Gaussian curve,
1. the amplitude of the noise added to the pure Gaussian function values,
    note that this should *not* be zero since R's `nls` method will fail
    on exact data.
1. the number of times a fit should be performed with (slightly) increasing
    mean values to ensure linear scaling of execution time.

Hence to compute the regression for 100 points obtained from a Gaussian
function with mean 0.1 and standard deviation 0.5, repeated 7 times, with
a noise level of 0.001:
```
$ Rscript ./gauss_fit.R 100 0.1 0.5 0.001 7
```

To generate a workload for Nitro, the `gauss_fit_load.py` script can be
used.  It can generate workloads where the execution time of a work item
is:

1. constant _t_, using the `--length t` option to specify it,
1. drawn from a uniform distribution over [_tmin, _tmax], specifyed by
    `--min tmin  --max tmax`, and
1. drawn from a gamma distrution with shape _t_, specified by
    `--shape t`.

Times are in seconds, but the distributions may be shifted depeding on the
performance of the compute nodes, and the quality of the compiler.

For example, to create a workload consisting of 70 work items with a
uniform distribution for their execution times in the interval
[10.0, 30.0] seconds:
```
$ ./gauss_quad_load.py  --n 70  --type uniform  --min 10.0  --max 30.0
```
