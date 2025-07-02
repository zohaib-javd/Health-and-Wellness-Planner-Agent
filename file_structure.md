# 🗂️ Project File Structure: Health & Wellness Agent
```
HEALTH_WELLNESS_AGENT_MAIN/
│
├── .venv/                              # Python virtual environment (ignore)
│
├── health_wellness_agent/              # Main package
│   ├── __init__.py
│   │
│   ├── custom_agents/                  # Specialized agent implementations
│   │   ├── __init__.py
│   │   ├── escalation_agent.py
│   │   ├── injury_support_agent.py
│   │   └── nutrition_expert_agent.py
│   │
│   ├── tools/                          # Modular agent tool scripts
│   │   ├── __init__.py
│   │   ├── goal_analyzer.py
│   │   ├── meal_planner.py
│   │   ├── scheduler.py
│   │   ├── tracker.py
│   │   └── workout_recommender.py
│   │
│   ├── utils/                          # Utilities (helpers, streaming, etc)
│   │   ├── __init__.py
│   │   └── streaming.py
│   │
│   ├── agent.py                        # Main agent definition
│   ├── context.py                      # User/session context
│   ├── guardrails.py                   # Guardrails/input validation
│   ├── hooks.py                        # Custom hooks (if used)
│   └── __init__.py
│
├── .env                                # API keys/env vars
├── .python-version                     # Python version (optional)
├── chat.py                             # CLI runner
├── pyproject.toml                      # Project dependencies/config
├── README.md                           # Overview & instructions
├── uv.lock                             # Dependency lockfile
├── .gitignore
```
