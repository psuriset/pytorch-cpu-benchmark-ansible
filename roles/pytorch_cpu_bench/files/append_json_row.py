#!/usr/bin/env python3
"""Emit one CSV row for summary.csv from a pytorch_cpu_threads_*.json file."""
import json
import sys


def main():
    path = sys.argv[1]
    with open(path, encoding="utf-8") as fp:
        data = json.load(fp)
    print(
        f"{data['hostname']},{data['torch_num_threads']},{data['matrix_size']},"
        f"{data['median_seconds']},{data['mean_seconds']},{data['iqr_seconds']},"
        f"{data['torch_version']}"
    )


if __name__ == "__main__":
    main()
