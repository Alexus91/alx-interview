#!/usr/bin/python3
"""
A script: Reads standard input line by line and computes metrics
"""


def parseLogs():
    """
    Reads logs from standard input and generates reports """
    stdin = __import__('sys').stdin
    lineNumber = 0
    fileSize = 0
    statusCodes = {'200': 0, '301': 0, '400': 0, '401': 0,
                   '403': 0, '404': 0, '405': 0, '500': 0}
    try:
        for line in stdin:
            lineNumber += 1
            line = line.split()
            try:
                fileSize += int(line[-1])
                status_code = line[-2]
                if status_code in statusCodes:
                    statusCodes[status_code] += 1
            except (IndexError, ValueError):
                pass
            if lineNumber == 10:
                report(fileSize, statusCodes)
                lineNumber = 0
        report(fileSize, statusCodes)
    except KeyboardInterrupt as e:
        report(fileSize, statusCodes)
        raise


def report(fileSize, statusCodes):
    """
    Prints generated report to standard output
    """
    print("File size: {}".format(fileSize))
    for code in sorted(statusCodes.keys()):
        print("{}: {}".format(code, statusCodes[code]))


if __name__ == '__main__':
    parseLogs()
