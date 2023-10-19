#!/usr/bin/python3
import sys
import re
from collections import Counter, OrderedDict
"""Parses log files"""


file_sizes = []
allowed_codes = [200, 301, 400, 401, 403, 404, 405, 500]


def parse_line(lines):
    status_codes = []
    pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(' \
              r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] ' \
              r'"GET /projects/\d+ HTTP/1\.1" (\d+) (\d+)$'
    count = 0
    for line in lines:
        match = re.match(pattern, line)
        if match:
            status_code = int(match.group(3))
            if status_code in allowed_codes:
                status_codes.append(status_code)
            file_sizes.append(int(match.group(4)))
        count += 1
        if count >= 10:
            break
    sorted_codes = sorted(status_codes)
    status_occurrences = dict(OrderedDict(Counter(sorted_codes)))
    return [sum(file_sizes), status_occurrences]


def print_stat(stats):
    print(f"Filesize: {stats[0]}")
    for key, value in stats[1].items():
        print(f"{key}: {value}")


def main():
    lines = sys.stdin
    try:
        while True:
            for _ in range(10):
                stats = parse_line(lines)
                print_stat(stats)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
