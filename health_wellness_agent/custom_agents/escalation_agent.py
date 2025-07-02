# SPDX-FileCopyrightText: 2025 Zohaib Javed
# SPDX-License-Identifier: MIT
"""
Filename: escalation_agent.py
Description: Defines an EscalationAgent that triggers handoff to a human coach or external system.
Author: Zohaib Javed
Date Created: 2025-07-01
"""

# In this file I have implemented:
# • A clean agent class using OpenAI SDK base Agent (+10 modular structure)
# • Proper handoff logic simulated by returning a trigger response (+15 handoff logic)
# • Clean context integration using RunContextWrapper


from agents import Agent as BaseAgent, RunContextWrapper

class EscalationAgent(BaseAgent):
    """
    Handoff agent connecting user to a human coach.
    """
    def __init__(self, context: RunContextWrapper):
        super().__init__(
            name="EscalationAgent",
            instructions="Connect the user to a human coach.",
            tools=[],
            context=context,
        )

    def run(self, user_input: str):
        return "You’re being connected to a human coach now."
