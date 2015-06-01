#!/usr/bin/env Rscript
# ------------------------------------------------------------------------
# Compute a nonlinear least square regression from a sample of specified
# size, based on a model of a Gaussian function with specified mean and
# stardard deviation, adding noise drawn from a uniform distribution
# with maximum amplitude given (do not choose this equal to 0.0).
# Parameters are specified on the command line, e.g.,
#
# $ Rscript gauss_fit.R 100 0.1 0.5 0.001, 3
#
# Here, the number of points is 100, the mean of the target function is 0.1,
# the standard deviation is 0.5, and the random noise is drawn uniformly
# from the interval [0.0, 0.001], this computation will be repeated 3
# times for a range of mu values
#
# Tested with R 3.1.x
#
# Author: Geert Jan Bex (geertjan.bex@uhasselt.be)
#
# ------------------------------------------------------------------------

# handle command line arguments
args <- commandArgs(TRUE)
sample_size <- as.integer(args[1])
distr.mean <- as.double(args[2])
distr.stddev <- as.double(args[3])
noise <- as.double(args[4])
nr.points = as.integer(args[5])
# domain
x.min <- -5.0
x.max <- 5.0
distr.delta <- 0.01

for (i in seq(nr.points)) {
# generate exact data set
    x <- runif(sample_size, min=x.min, max=x.max)
    y <- exp(-((x - distr.mean)/distr.stddev)^2)

# add noise, not so realistically, from a uniform distribution
    y <- y + runif(length(y), min=0.0, max=noise)

# define initial guesses for mu and sigma
    mu.start <- 0.0
    sigma.start <- 1.0

# fit nonlinear model
    fit <- nls(y ~ exp(-((x - mu)/sigma)^2),
               start=list(mu=mu.start, sigma=sigma.start))

# compute deviation from original distribution parameters
    if (abs(distr.mean) > 1.0e-6) {
        mean.err = abs(distr.mean - coef(fit)['mu'])/abs(distr.mean)
    } else {
        mean.err = abs(distr.mean - coef(fit)['mu'])
    }
    stddev.err = abs(distr.stddev - coef(fit)['sigma'])/distr.stddev

# output the result
    cat(coef(fit)['mu'], mean.err, coef(fit)['sigma'], stddev.err,
        sum(resid(fit)^2),  sep=',')
    cat('\n')
    distr.mean <- distr.mean + distr.delta
}
