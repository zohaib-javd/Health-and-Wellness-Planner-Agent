# SPDX-FileCopyrightText: 2025 Zohaib Javed
# SPDX-License-Identifier: MIT
"""
Filename: hooks.py
Description: Implements lifecycle hooks for logging agent/tool activity.
Author: Zohaib Javed
Date Created: 2025-07-01
"""

# In this file I have implemented:
# • Agent and tool lifecycle hook classes (+10 lifecycle hook usage)
# • Real-time event logging for agent/tool start/end

from agents import RunHooks, AgentHooks
from health_wellness_agent.context import UserSessionContext

class LoggingRunHooks(RunHooks):
    def on_agent_start(self, agent, context):
        print(f"[HOOK] {agent.name} starting")

    def on_tool_end(self, tool, output, context):
        print(f"[HOOK] {tool.name} returned {output}")

class LoggingAgentHooks(AgentHooks):
    def on_start(self, agent, input, context):
        print(f"[AGENT HOOK] Received: {input}")

    def on_end(self, agent, response, context):
        print(f"[AGENT HOOK] Responded: {response}")
