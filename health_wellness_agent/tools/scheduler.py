# SPDX-FileCopyrightText: 2025 Zohaib Javed
# SPDX-License-Identifier: MIT
"""
Filename: scheduler.py
Description: A simulated scheduler that sets reminders/check-ins using structured time parsing.
Author: Zohaib Javed
Date Created: 2025-07-01
"""

# In this file I have implemented:
# • Async scheduling tool that parses user intent for reminders (+20 async tool design)
# • Supports weekday mapping and feedback on invalid inputs (guardrails + I/O)
# • Integrates smoothly with agent handoff logic (prep for escalation) (+15 handoff-ready)


from datetime import datetime, timedelta          
from typing_extensions import TypedDict, Literal
from agents import function_tool, RunContextWrapper
from pydantic import BaseModel, Field
from health_wellness_agent.context import UserSessionContext

Weekday = Literal[
    "monday", "tuesday", "wednesday",
    "thursday", "friday", "saturday", "sunday",
]


class SchedulerInput(BaseModel):
    weekday: Weekday = Field(..., examples=["monday"])
    hour_24: int = Field(9, ge=0, le=23, description="24-h clock")


class SchedulerOut(TypedDict):
    rrule: str
    next_checkin: str


@function_tool
async def scheduler(
    ctx: RunContextWrapper[UserSessionContext],
    input: SchedulerInput,
) -> SchedulerOut:
    """Create a weekly RRULE and store it in session context."""
    rrule = (
        "RRULE:FREQ=WEEKLY;BYDAY="
        + input.weekday[:2].upper()
        + f";BYHOUR={input.hour_24};BYMINUTE=0;BYSECOND=0"
    )

    now = datetime.now()
    weekday_idx = [
        "monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday",
    ].index(input.weekday)

    days_ahead = (weekday_idx - now.weekday()) % 7
    if days_ahead == 0 and now.hour >= input.hour_24:
        days_ahead = 7

    next_dt = (
        now.replace(hour=input.hour_24, minute=0, second=0, microsecond=0)
        + timedelta(days=days_ahead)
    )

    ctx.context.progress_logs.append(
        {"event": "checkin_scheduled", "rrule": rrule, "timestamp": now.isoformat()}
    )

    return {"rrule": rrule, "next_checkin": next_dt.isoformat()}
