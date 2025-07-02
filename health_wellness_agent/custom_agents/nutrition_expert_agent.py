# SPDX-FileCopyrightText: 2025 Zohaib Javed
# SPDX-License-Identifier: MIT
"""
Filename: nutrition_expert_agent.py
Description: Defines a certified nutritionist agent that provides dietary advice for various needs.
Author: Zohaib Javed
Date Created: 2025-07-01
"""

# In this file I have implemented:
# • Expert agent definition for nutrition guidance (modular design)
# • Framework-ready for future integration of nutrition tools
# • Scoped prompt tailored to special diets like diabetic/vegan (+10 structure)


from agents import Agent

class NutritionExpertAgent(Agent):
    def __init__(self):
        super().__init__(
            name="NutritionExpertAgent",
            instructions=(
                "You are a certified nutritionist. "
                "Provide evidence-based dietary guidance, especially for "
                "allergies, diabetes, or vegetarian/vegan needs."
            ),
            tools=[],          
        )
