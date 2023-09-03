#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/7 18:32
@Author  : alexanderwu
@File    : search_google.py
"""

import asyncio
import sys
sys.path.append('/Users/jasonlee/Desktop/practicalProject/MetaGPT/')


from metagpt.roles import Searcher
from metagpt.tools import SearchEngineType


async def main():
    # await Searcher().run("What are some good sun protection products?")
    await Searcher(engine=SearchEngineType.DIRECT_GOOGLE).run("What are some good sun protection products?")


if __name__ == '__main__':
    asyncio.run(main())       