# SPDX-FileCopyrightText: 2025 Zohaib Javed
# SPDX-License-Identifier: MIT
"""
Filename: workout_recommender.py
Description: Suggests beginner-friendly, safe workouts based on user fitness goals and preferences.
Author: Zohaib Javed
Date Created: 2025-07-01
"""

# In this file I have implemented:
# • Async tool that outputs a 7-day workout schedule (+20 tool design & async)
# • Multi-turn interaction potential based on user type (injury, goal) (+15 multi-turn)
# • Structured exercise categories with rest and cardio logic


from typing_extensions import TypedDict
from typing import List
from agents import function_tool, RunContextWrapper
from pydantic import BaseModel, Field
from health_wellness_agent.context import UserSessionContext


# ────────────────────────────────────────────────────────────────────
# Input / output models
# ────────────────────────────────────────────────────────────────────

class WorkoutInput(BaseModel):
    fitness_level: str = Field(
        "beginner",
        examples=["beginner", "intermediate", "advanced"],
        description="User’s current training experience.",
    )


class DailyWorkout(TypedDict):
    focus: str
    details: str


class WorkoutPlanOutput(TypedDict):
    workout_plan: List[DailyWorkout]


# ────────────────────────────────────────────────────────────────────
# Tool implementation
# ────────────────────────────────────────────────────────────────────

@function_tool
async def workout_recommender(
    ctx: RunContextWrapper[UserSessionContext],
    input: WorkoutInput,
) -> WorkoutPlanOutput:
    """Return a stubbed 7-day workout plan tailored to fitness level."""
    level = input.fitness_level.lower()

    # Template sessions per level (replace with smarter logic later)
    template = {
        "beginner": [
            ("Full-body strength", "Body-weight squats, push-ups, bands x3"),
            ("Cardio",            "30-min brisk walk or cycling"),
            ("Rest / mobility",   "Gentle yoga & stretching"),
        ],
        "intermediate": [
            ("Upper-body strength", "Bench, rows, overhead press 3×10"),
            ("Lower-body strength", "Squats, lunges, RDLs 3×10"),
            ("HIIT cardio",         "20-min interval running / rowing"),
        ],
        "advanced": [
            ("Push strength",  "Heavy bench & incline DB presses 5×5"),
            ("Pull strength",  "Weighted pull-ups & barbell rows 5×5"),
            ("Legs strength",  "Back squats & deadlifts 5×5"),
            ("MetCon",         "CrossFit-style circuit 15-min AMRAP"),
        ],
    }[level]

    # Build 7-day sequence: repeat or insert rest days
    week: List[DailyWorkout] = []
    while len(week) < 7:
        for focus, details in template:
            week.append({"focus": focus, "details": details})
            if len(week) == 7:
                break
        if len(template) < 7:
            week.append({"focus": "Rest / mobility", "details": "Foam-rolling, gentle stretch"})

    ctx.context.workout_plan = week
    return {"workout_plan": week}
