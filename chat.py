#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Zohaib Javed
# SPDX-License-Identifier: MIT
"""
Filename: chat.py
Description: CLI entrypoint for interacting with the Health & Wellness Agent.
Author: Zohaib Javed
Date Created: 2025-07-01
"""

# In this file I have implemented:
# • CLI wrapper to launch planner agent with real-time streaming
# • Clean and simple command-line input loop

import asyncio, warnings, sys
from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=DeprecationWarning, module="pydantic")

from health_wellness_agent.context import UserSessionContext
from health_wellness_agent.agent import PlannerAgent
from health_wellness_agent.utils.streaming import stream_response
from agents import RunContextWrapper

async def main():
    load_dotenv()                               # needs OPENAI_API_KEY
    ctx = UserSessionContext(name="Guest", uid=1)
    agent = PlannerAgent()
    wrapper = RunContextWrapper(ctx)

    print(">>> Health & Wellness Agent (type 'quit' to exit)")
    while True:
        user = input("\nYou: ").strip()
        if user.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        await stream_response(agent, user, wrapper)

if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
