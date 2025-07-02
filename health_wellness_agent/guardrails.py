# SPDX-FileCopyrightText: 2025 Zohaib Javed
# SPDX-License-Identifier: MIT
"""
Filename: guardrails.py
Description: Adds input validation logic using Pydantic models.
Author: Zohaib Javed
Date Created: 2025-07-01
"""

# In this file I have implemented:
# • Pydantic models for goal parsing and type safety (+15 guardrails)
# • Clean input/output validation for tools and agents

from pydantic import BaseModel, Field

class GoalInput(BaseModel):
    """Validates a goal like 'lose 5 kg in 2 months'."""
    quantity: float = Field(..., gt=0, description="Numeric amount")
    metric: str     = Field(...,  description="e.g. kg, lbs")
    duration: str   = Field(...,  description="Timeframe, e.g. '6 months'")

class ToolOutput(BaseModel):
    data: dict
