#!/usr/bin/python3
import sys

def print_statistics(total_size, status_codes):
    print(f"File size: {total_size}")
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print(f"{status_code}: {status_codes[status_code]}")

if __name__ == "__main__":
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 7:
                total_size += int(parts[-1])  # The file size is the last element
                status_code = parts[-2]  # The status code is the second last element
                if status_code in status_codes:
                    status_codes[status_code] += 1

                count += 1
                if count % 10 == 0:
                    print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise
    finally:
        print_statistics(total_size, status_codes)
