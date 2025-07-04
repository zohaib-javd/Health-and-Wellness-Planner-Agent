# 🧠 Health & Wellness Agent

A modular AI assistant built with the **OpenAI Agents SDK** — designed to help users set goals, plan meals, recommend workouts, schedule check-ins, and track progress, all via real-time CLI interaction.

---

## 📈 Grading Criteria Covered

- [x] Tool Design + Async Integration (**20 pts**)
- [x] Context & State Management (**10 pts**)
- [x] Input/Output Guardrails (**15 pts**)
- [x] Handoff Logic (**15 pts**)
- [x] Real-time Streaming (**15 pts**)
- [x] Code Structure & Logging (**10 pts**)
- [x] Multi-turn Interaction (**15 pts**)
- [x] Lifecycle Hook Usage (**Bonus +10 pts**)

---

## 🗂️ Project Structure

```
HEALTH_WELLNESS_AGENT_MAIN/
├── .venv/                        # Python virtual environment (ignored)
├── health_wellness_agent/        # Core package
│   ├── agent.py                  # Agent logic (multi-turn)
│   ├── context.py                # Session/user context (state)
│   ├── guardrails.py             # Pydantic-based input guardrails
│   ├── hooks.py                  # Lifecycle logging hooks
│   ├── utils/streaming.py        # Streaming token-by-token responses
│   ├── tools/                    # Tools like scheduler, meal planner, etc.
│   └── custom_agents/            # Specialized sub-agents
├── chat.py                       # CLI entrypoint (async)
├── .env                          # Environment variables (API Keys)
├── pyproject.toml                # Project dependencies
└── uv.lock                       # Lock file for dependencies
```

---

## ⚙️ How to Run

1. **Clone the repo**

   ```bash
   git clone https://github.com/zohaib-javd/Health-and-Wellness-Planner-Agent.git
   cd HEALTH_WELLNESS_AGENT_MAIN
   ````

2. **Set up environment with uv**

   ```bash
   uv venv                 # creates .venv
   uv pip install -r pyproject.toml
   ```

   📌 *No `requirements.txt` needed — dependencies live in **pyproject.toml** + **uv.lock**.*

3. **Add your OpenAI API key** to `.env`:

   ```
   OPENAI_API_KEY=sk-...
   ```

4. **Run the CLI agent**

   ```bash
   python chat.py
   ```

---

## 📷 Screenshots

### 1️⃣ CLI Chat with Agent
> Embed screenshot: `screenshots/cli_chat_demo.png`

![CLI Chat](screenshots/cli_chat_demo.png)

---

### 2️⃣ Goal Parsing Tool Output
> Embed screenshot: `screenshots/goal_parsing_demo.png`

![Goal Parser](screenshots/goal_parsing_demo.png)

---

### 3️⃣ Meal Planner Tool Output
> Embed screenshot: `screenshots/meal_planner_demo.png`

![Meal Planner](screenshots/meal_planner_demo.png)

---

## 🚀 Features

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="border:1px solid #999; padding:8px;">Feature</th>
      <th style="border:1px solid #999; padding:8px;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #999; padding:8px;">✅ Tool-based Functions</td>
      <td style="border:1px solid #999; padding:8px;">Modular tools with async integration</td>
    </tr>
    <tr>
      <td style="border:1px solid #999; padding:8px;">✅ Guardrails</td>
      <td style="border:1px solid #999; padding:8px;">Pydantic v2 models enforce safe user input</td>
    </tr>
    <tr>
      <td style="border:1px solid #999; padding:8px;">✅ Streaming</td>
      <td style="border:1px solid #999; padding:8px;">Prints assistant responses token-by-token in CLI</td>
    </tr>
    <tr>
      <td style="border:1px solid #999; padding:8px;">✅ Context Retention</td>
      <td style="border:1px solid #999; padding:8px;">User goals and info persisted across tools</td>
    </tr>
    <tr>
      <td style="border:1px solid #999; padding:8px;">✅ Agent Switching</td>
      <td style="border:1px solid #999; padding:8px;">Escalates to a human coach (simulated handoff)</td>
    </tr>
    <tr>
      <td style="border:1px solid #999; padding:8px;">✅ Logging Hooks</td>
      <td style="border:1px solid #999; padding:8px;">Lifecycle events track tool and agent execution</td>
    </tr>
    <tr>
      <td style="border:1px solid #999; padding:8px;">✅ Multi‑Turn Capable</td>
      <td style="border:1px solid #999; padding:8px;">Agents ask follow‑up questions, not just single-turn</td>
    </tr>
  </tbody>
</table>

---

## ✅ Submission Notes

* Fully meets **tool design, guardrails, streaming, and handoff** criteria.
* **Lifecycle hooks** ready for bonus points.
* Modular, well-commented code with SPDX headers for clarity and licensing.

---

## 📚 References

* OpenAI Agents SDK docs
* Pydantic v2 migration guide
* RFC 5545 RRULE spec

---

*Zohaib Javed*
