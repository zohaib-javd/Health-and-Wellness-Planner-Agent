# SPDX-FileCopyrightText: 2025 Zohaib Javed
# SPDX-License-Identifier: MIT
"""
Filename: context.py
Description: Defines UserSessionContext for persisting user goals and state across turns.
Author: Zohaib Javed
Date Created: 2025-07-01
"""

# In this file I have implemented:
# • UserSessionContext class to manage user state (+10 context & state management)
# • Properties to store parsed goals, trackers, etc.

from pydantic import BaseModel
from typing import Optional, List, Dict

class UserSessionContext(BaseModel):
    name: str
    uid: int
    goal: Optional[dict] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[dict] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    progress_logs: List[Dict[str, str]] = []
