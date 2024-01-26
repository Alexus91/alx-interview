#!/usr/bin/python3
"""
Log Parsing Script: Reads standard input line by line and computes metrics
"""


def parse_logs():
    """
    Parses logs from standard input and generates reports
    Reports:
        * Prints log size after reading every 10 lines & at KeyboardInterrupt
    Raises:
        KeyboardInterrupt (Exception): handles this exception and raises it
    """
    stdin = __import__('sys').stdin
    line_number = 0
    file_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    try:
        for line in stdin:
            line_number += 1
            line = line.split()
            try:
                file_size += int(line[-1])
                status_code = line[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except (IndexError, ValueError):
                pass
            if line_number == 10:
                report(file_size, status_codes)
                line_number = 0
        report(file_size, status_codes)
    except KeyboardInterrupt as e:
        report(file_size, status_codes)
        raise


def report(file_size, status_codes):
    """
    Prints generated report to standard output
    Args:
        file_size (int): total log size after every 10 successfully read line
        status_codes (dict): dictionary of status codes and counts
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == '__main__':
    parse_logs()
