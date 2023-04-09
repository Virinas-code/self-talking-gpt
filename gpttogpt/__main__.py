# -*- coding: utf-8 -*-
"""
ChatGPT talks to itself

Launch script
"""
import os
import sys

from . import broken, main

if __name__ == "__main__":
    if "GPT_API_KEY" not in os.environ:
        print(
            "Please set the GPT_API_KEY environment variable.", file=sys.stderr
        )
        sys.exit(1)

    if len(sys.argv) == 1:
        main()
    elif sys.argv[1] == "broken":
        broken()
