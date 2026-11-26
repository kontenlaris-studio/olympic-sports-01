#!/usr/bin/env python3
"""Rejected Olympic Sports — one funny single-line sport the Olympics rejected.

Entry (134 chars): an underwater basket-weaving final where the baskets keep
floating away — after 4 minutes the judges give up judging baskets and
score the swimmers on their excuses instead.
"""

import os

LINE = (
    "Underwater basket weaving: the baskets kept floating away, "
    "so after 4 minutes the judges scored the swimmers on their excuses instead."
)


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
