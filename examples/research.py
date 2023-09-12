#!/usr/bin/env python

import asyncio

import sys
sys.path.append('/Users/jasonlee/Desktop/practicalProject/MetaGPT/')

from metagpt.roles.researcher import RESEARCH_PATH, Researcher
from metagpt.tools import SearchEngineType


async def main():
    topic = "数字公共基础设施 vs. 数字中国"
    role = Researcher(language="zh-cn", engine=SearchEngineType.DIRECT_GOOGLE) #最新版本可以选择中文输出，zh-cn
    await role.run(topic)
    print(f"save report to {RESEARCH_PATH / f'{topic}.md'}.")
    

if __name__ == '__main__':
    asyncio.run(main())
