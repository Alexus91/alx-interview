#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """

import sys


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def parse_line(line, status_codes):
    try:
        parts = line.split()
        if len(parts) >= 9:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            if status_code in status_codes:
                status_codes[status_code] += 1
            return file_size
    except (ValueError, IndexError):
        pass
    return 0



def main():
    total_size = 0
    status_c = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    try:
        line_count = 0
        for line in sys.stdin:
            file_size = parse_line(line.strip(), status_c)
            total_size += file_size
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_c)
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_c)


if __name__ == "__main__":
    main()
