#!/usr/bin/env python3
import asyncio
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Now import and run
from core.db import main

if __name__ == "__main__":
    asyncio.run(main())