#!/bin/bash -l

path="/data/leuven/301/vsc30140/Projects/NitroBenchmark/R"

module load R/3.1.1-intel-2014a-default
cd ${path}
Rscript gauss_fit.R "$@"
