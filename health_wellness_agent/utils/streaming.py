# SPDX-FileCopyrightText: 2025 Zohaib Javed
# SPDX-License-Identifier: MIT
"""
Filename: streaming.py
Description: Streamed CLI token-by-token output using Runner.stream_events.
Author: Zohaib Javed
Date Created: 2025-07-01
"""

# In this file I have implemented:
# • Live streaming token display in the CLI (+15 real-time streaming)
# • Filters noisy SDK output for clean display

import sys
from agents import Runner, RunContextWrapper
from health_wellness_agent.context import UserSessionContext

try:
    from openai.types.responses import ResponseTextDeltaEvent
except ImportError:
    class ResponseTextDeltaEvent: pass

def _is_token_delta(ev) -> bool:
    return (
        ev.type == "raw_response_event"
        and isinstance(ev.data, ResponseTextDeltaEvent)
        and isinstance(ev.data.delta, str)
    )

async def stream_response(
    agent,
    prompt: str,
    ctx: RunContextWrapper[UserSessionContext],
) -> None:
    run_stream = Runner.run_streamed(agent, input=prompt, context=ctx)
    started = False

    async for ev in run_stream.stream_events():
        # 1️⃣ Live assistant tokens
        if _is_token_delta(ev):
            if not started:
                sys.stdout.write("\nAssistant: ")
                started = True
            sys.stdout.write(ev.data.delta)
            sys.stdout.flush()
            continue

        # 2️⃣ Skip other low-level noise
        if ev.type == "raw_response_event":
            continue

        # 3️⃣ Only handle final assistant message end
        if ev.type == "run_item_stream_event":
            if ev.item.type == "message_output_item" and started:
                print()  # newline at end of assistant streaming
                started = False
            continue

        # 4️⃣ Agent switches
        if ev.type == "agent_updated_stream_event":
            print(f"\n[Agent switched → {ev.new_agent.name}]")
