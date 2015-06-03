#!/usr/bin/env python

import re
import sys

extract_regex = None
fmt_regex = None
sep = ','


def extract_cmd(line):
    match = extract_regex.search(line)
    if match:
        params = match.group(1)
        return fmt_regex.sub(sep, params)
    else:
        msg = "### error: unexpected line '{0}'\n"
        sys.stderr.write(msg.format(line.rstrip()))
        sys.exit(1)


def create_header(params_str):
    nr_params = params_str.count(sep) + 1
    param_names = ['param{0:d}'.format(i) for i in xrange(1, nr_params + 1)]
    return sep.join(param_names)


if __name__ == '__main__':
    extract_regex_str = r'cmd\s*=\s*\S+\s+(.+)$'
    fmt_regex_str = r'\s+'
    extract_regex = re.compile(extract_regex_str)
    fmt_regex = re.compile(fmt_regex_str)
    line = sys.stdin.readline()
    cmd = extract_cmd(line)
    header = create_header(cmd)
    print header
    print cmd
    for line in sys.stdin:
        cmd = extract_cmd(line)
        print cmd
