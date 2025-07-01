# stock_market_ai_nalysis

# 📈 AI Trading Bot with Multiple Agents (For Indian Stocks 🇮🇳)

Welcome to the **AI-powered Trading Strategy Crew**! This project uses different AI agents to analyze the stock market, make smart trading strategies, and help you manage risks.

---

## 🧠 What’s Inside?

We have 4 AI agents working together:

1. **Market Research Analyst** → Studies stock prices and news (like for TATA or INFY).
2. **Strategy Developer** → Builds a smart plan: when to buy, sell, or exit.
3. **Execution Planner** → Decides the *best way* to place trades.
4. **Risk Advisor** → Makes sure the plan is safe and helps you avoid big losses.

---

## 🛠 How It Works

Each AI agent performs a task in order, like a team:

1. Analyst gets the info ✅
2. Strategy Developer builds the plan 🧠
3. Execution Planner tells when and how to buy/sell 💹
4. Risk Advisor checks for danger and fixes it 🚨

---

## 🚀 How to Run

### ✅ Step 1: Install Required Libraries

```bash
pip install crewai langchain-openai crewai-tools


✅ Step 2: Add Your API Keys
Create a .env file or utils.py with:

def get_openai_api_key():
    return "YOUR_OPENAI_API_KEY"

def get_serper_api_key():
    return "YOUR_SERPER_API_KEY"

These keys help the bot fetch live data and respond smartly.

✅ Step 3: Run the File

python stock_market_analysis.py

You’ll see:

Printed strategy output

A saved report in trading_report.log


✏️ How to Change the Stock
In the code, modify:

'stock_selection': 'TATA',

Change it to RELIANCE, INFY, HDFCBANK, or any BSE/NSE stock.


📂 Output Example

📈 FINANCIAL TRADING STRATEGY REPORT 📈

🧠 Task: Market Research Analyst - Analyze recent stock data...

Stock is showing bullish momentum after strong earnings.

🧠 Task: Strategy Developer - Develop a trading plan...

Buy at ₹3100, Target ₹3350, Stop-loss ₹2980

🧠 Task: Execution Planner - Plan your trade...

Use limit orders during morning dip. Watch for FII volume spike.

🧠 Task: Risk Advisor - Be safe!

Avoid over-exposure. Use 10% capital. Add trailing stop-loss.

✅ Report saved to trading_report.log


Code Details

💡 Agent & Task Breakdown (For Humans 😄)
🧠 1. Market Research Analyst (Agent)
Job: This agent reads financial news, stock charts, and reports to figure out if the company (like TATA) is doing well or not.

Task: Analyze stock data and news.

📊 Looks at recent prices.

📰 Reads earnings and news.

🤖 Uses machine learning to find trends.

📊 2. Quantitative Strategy Developer (Agent)
Job: This agent takes the information from the Market Research Analyst and builds a plan to make money — like when to buy or sell.

Task: Develop a trading strategy.

💡 Suggests buying price, target, and stop-loss.

🧮 Based on risk and market insights.

📆 Tells how long to keep the stock.

📦 3. Trade Execution Planner (Agent)
Job: This agent figures out how to place the trade. Should we buy now? Use a special order? Wait for a better price?

Task: Plan execution strategy.

⏱ Best time to buy/sell.

💰 Suggests order type (market/limit).

🛡 Adds backup plan if price changes.

🚨 4. Risk and Compliance Advisor (Agent)
Job: Makes sure you don’t lose too much money. Helps protect your money with safety suggestions.

Task: Assess risk.

🔍 Measures how risky the plan is.

⚠️ Finds sector and stock volatility.

✅ Recommends stop-loss, hedges, alerts.

