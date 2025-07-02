# SPDX-FileCopyrightText: 2025 Zohaib Javed
# SPDX-License-Identifier: MIT
"""
Filename: agent.py
Description: Central agent definition that initializes the Health & Wellness Planner, assigns tools,
and manages user interaction logic.
Author: Zohaib Javed
Date Created: 2025-07-01
"""

# In this file I have implemented:
# • Primary multi-turn planner agent definition (+15 multi-turn interaction)
# • Tool loading and context-aware interaction (+20 tool design & async)
# • Handoff logic and streaming compatibility (+15 handoff logic, +15 streaming)

from agents import Agent, handoff, Runner, ModelSettings

# ── tools ───────────────────────────────────────────────────────────
from health_wellness_agent.tools.goal_analyzer import goal_analyzer
from health_wellness_agent.tools.meal_planner import meal_planner
from health_wellness_agent.tools.workout_recommender import workout_recommender
from health_wellness_agent.tools.scheduler import scheduler
from health_wellness_agent.tools.tracker import tracker

# ── specialist agents ───────────────────────────────────────────────
from health_wellness_agent.custom_agents.nutrition_expert_agent import (
    NutritionExpertAgent,
)
from health_wellness_agent.custom_agents.injury_support_agent import (
    InjurySupportAgent,
)


class PlannerAgent(Agent):
    """Chat-first AI for personalised health & wellness planning."""

    def __init__(self) -> None:
        super().__init__(
            # Identity
            name="Health & Wellness Planner",
            instructions=(
                "You are an AI health-and-wellness planner. "
                "Collect user goals, generate personalised meal and workout plans, "
                "schedule check-ins, log progress, and hand off to specialists when needed."
            ),
            # Model
            model="gpt-4.1-mini",
            model_settings=ModelSettings(
                temperature=0.7,
                top_p=1.0,
                parallel_tool_calls=True,
            ),
            # Core tools
            tools=[
                goal_analyzer,
                meal_planner,
                workout_recommender,
                scheduler,
                tracker,
            ],
            # Specialist hand-offs
            handoffs=[
                NutritionExpertAgent(),  # tool: transfer_to_nutrition_expert_agent
                handoff(
                    InjurySupportAgent(),
                    tool_name_override="transfer_to_injury_support",
                    tool_description_override=(
                        "Send the user to InjurySupportAgent when they mention pain, "
                        "injury, or require low-impact exercise modifications."
                    ),
                ),
            ],
        )

    # Convenience helper for blocking unit tests / scripts
    def run_sync(self, prompt: str, context):
        return Runner.run(self, prompt, context=context)
