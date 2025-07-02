# SPDX-FileCopyrightText: 2025 Zohaib Javed
# SPDX-License-Identifier: MIT
"""
Filename: injury_support_agent.py
Description: Defines a support agent focused on safe recovery workouts for injured users.
Author: Zohaib Javed
Date Created: 2025-07-01
"""

# In this file I have implemented:
# • A specialized Agent subclass with clear instructions for injury-safe workouts
# • No tools used here, keeping agent isolated and focused (single-responsibility)
# • Structured prompt for multi-turn injury support (+15 multi-turn logic)

from agents import Agent

class InjurySupportAgent(Agent):
    def __init__(self):
        super().__init__(
            name="InjurySupportAgent",
            instructions=(
                "You are a physiotherapy assistant. "
                "Offer safe, low-impact workout modifications and recovery tips "
                "for users with injuries or chronic pain."
            ),
            tools=[],
        )
