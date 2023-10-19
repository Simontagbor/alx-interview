#!/usr/bin/python3
"""
This Module parses a stdin stream of logs
"""
import sys
import re
from collections import Counter, OrderedDict


def parse_line(lines):
    """Parse each line and process data """
    status_codes = []
    file_sizes = []
    pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(' \
              r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] ' \
              r'"GET /projects/\d+ HTTP/1\.1" (\d+) (\d+)$'
    count = 0
    for line in lines:
        if count <= 10:
            match = re.match(pattern, line)
            if match:
                status_codes.append(match.group(3))
                file_sizes.append(int(match.group(4)))
            count += 1
        else:
            break
    sorted_codes = sorted(status_codes)
    status_occurrences = dict(OrderedDict(Counter(sorted_codes)))
    return [sum(file_sizes), status_occurrences]


def print_stat(stats):
    print(f"File size: {stats[0]}")
    for key, value in stats[1].items():
        print(f"{key}: {value}")


def main():
    lines = sys.stdin
    try:
        while lines is not None:
            for _ in range(10):
                stats = parse_line(lines)
                print_stat(stats)
    except KeyboardInterrupt:
        pass


main()
