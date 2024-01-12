#!/usr/bin/python3
"""
Log Parsing Module

This module provides functions for parsing
log files and generating statistics from log data.
"""
import sys
import re

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
count = 0

try:
    for line in sys.stdin:
        match = re.search(r'(\d+) (\d+)$', line)
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += file_size
        count += 1
        if count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes):
                if status_codes[code] > 0:
                    print("{}: {}".format(code, status_codes[code]))
    # Print the statistics one last time after all lines have been read
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
    raise
