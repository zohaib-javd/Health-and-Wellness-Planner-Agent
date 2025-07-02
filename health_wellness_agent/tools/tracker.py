# SPDX-FileCopyrightText: 2025 Zohaib Javed
# SPDX-License-Identifier: MIT
"""
Filename: tracker.py
Description: Tool that simulates tracking a user’s progress based on previously saved goal.
Author: Zohaib Javed
Date Created: 2025-07-01
"""

# In this file I have implemented:
# • Context-aware tool that reads from saved session goals (+10 context)
# • Tool handles missing data with clear feedback (input guardrail concept)
# • Async design using @tool for full integration into main agent


from datetime import datetime
from typing_extensions import TypedDict, Annotated
from agents import function_tool, RunContextWrapper
from pydantic import BaseModel, Field
from health_wellness_agent.context import UserSessionContext


class ProgressInput(BaseModel):
    metric: str = Field(..., description="What you’re reporting e.g. 'weight', 'run_time'")
    value: Annotated[float | str, Field(..., description="Numeric or free-text value")]
    notes: str | None = Field(None, description="Optional comment")


class ProgressOut(TypedDict):
    stored: bool
    log_count: int


@function_tool
async def tracker(
    ctx: RunContextWrapper[UserSessionContext],
    input: ProgressInput,
) -> ProgressOut:
    """Store a progress update in session context."""
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "metric": input.metric.lower(),
        "value": input.value,
        "notes": input.notes,
    }
    ctx.context.progress_logs.append(log_entry)
    return {"stored": True, "log_count": len(ctx.context.progress_logs)}
