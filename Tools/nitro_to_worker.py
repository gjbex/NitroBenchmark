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


if __name__ == '__main__':
    extract_regex_str = r'cmd\s*=\s*\S+\s+(.+)$'
    fmt_regex_str = r'\s+'
    extract_regex = re.compile(extract_regex_str)
    fmt_regex = re.compile(fmt_regex_str)
    for line in sys.stdin:
        cmd = extract_cmd(line)
        print cmd
