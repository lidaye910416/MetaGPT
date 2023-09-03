#!/usr/bin/env python

import asyncio

import sys
sys.path.append('/Users/jasonlee/Desktop/practicalProject/MetaGPT/')

from metagpt.roles.researcher import RESEARCH_PATH, Researcher
from metagpt.tools import SearchEngineType


async def main():
    topic = "dataiku vs. datarobot"
    role = Researcher(language="en-us")
    await role.run(topic)
    print(f"save report to {RESEARCH_PATH / f'{topic}.md'}.")


if __name__ == '__main__':
    asyncio.run(main())
