#!/usr/bin/env python

import os, os.path
import sys
import numpy as np

size = 100000
noise = 0.001
payload = 'gauss_fit_driver.sh'
cmd = 'cmd={script} {size} {mu} {sigma} {noise} {n} &> {output}\n'
output_fmt = '{scratch_path}/output_R/out-{i:06d}.txt'


def generate_output(script, n, output):
    mu = np.random.uniform(-1.5, 0.0)
    sigma = np.random.uniform(0.2, 2.0)
    sys.stdout.write(cmd.format(script=script, size=size,
                                mu=mu, sigma=sigma, noise=noise,
                                n=n, output=output))


def create_constant(nr_cmds, length, path, scratch_path):
    n = int(np.ceil(length/0.3))
    script = os.path.join(path, payload)
    for i in xrange(nr_cmds):
        output = output_fmt.format(scratch_path=scratch_path, i=i)
        generate_output(script, n, output)


def create_uniform(nr_cmds, min_time, max_time, path, scratch_path):
    min_n = int(np.ceil(min_time/0.3))
    max_n = int(np.ceil(max_time/0.3)) + 1
    script = os.path.join(path, payload)
    for i in xrange(nr_cmds):
        n = np.random.randint(min_n, max_n)
        output = output_fmt.format(scratch_path=scratch_path, i=i)
        generate_output(script, n, output)


def create_gamma(nr_cmds, avg_time, path, scratch_path):
    avg_n = int(np.ceil(avg_time/0.3))
    script = os.path.join(path, payload)
    for i in xrange(nr_cmds):
        n = int(np.ceil(np.random.gamma(avg_n, 1.0)))
        output = output_fmt.format(scratch_path=scratch_path, i=i)
        generate_output(script, n, output)


if __name__ == '__main__':
    from argparse import ArgumentParser
    arg_parser = ArgumentParser(description='Create Nitro payload for '
                                            'gauss_fit.R script')
    arg_parser.add_argument('--path', help='path to the driver script')
    arg_parser.add_argument('--scratch_path',
                            help='path to the driver script')
    arg_parser.add_argument('--n', type=int, default=10,
                            help='number of computations')
    arg_parser.add_argument('--type', default='uniform',
                            choices=['uniform', 'constant', 'gamma'],
                            help='type of distribution to use')
    arg_parser.add_argument('--min', type=float, default=5.0,
                            help='minimum value for uniform distribution')
    arg_parser.add_argument('--max', type=float, default=15.0,
                            help='maximum value for uniform distribution')
    arg_parser.add_argument('--length', type=float, default=10.0,
                            help='value for constant time distirbution')
    arg_parser.add_argument('--avg', type=float, default=10.0,
                            help='shape of gamma distribution')
    options = arg_parser.parse_args()
    path = options.path if options.path else os.getcwd()
    if options.scratch_path:
        scratch_path = options.scratch_path
    else:
        scratch_path = os.getenv('VSC_SCRATCH')
    if options.type == 'constant':
        if options.length < 0.2:
            sys.stderr.write('# error: run time to short')
            sys.exit(1)
        create_constant(options.n, options.length, path, scratch_path)
    elif options.type == 'uniform':
        if options.min >= options.max:
            sys.stderr.write('# error: maximum time is less than minimum')
            sys.exit(1)
        create_uniform(options.n, options.min, options.max, path,
                       scratch_path)
    elif options.type == 'gamma':
        if options.avg < 0.3:
            sys.stderr.write('# error: average runtime is too short')
            sys.exit(1)
        create_gamma(options.n, options.avg, path, scratch_path)
