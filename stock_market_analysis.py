import warnings
warnings.filterwarnings('ignore')

import os
import json
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from utils import get_openai_api_key, get_serper_api_key

# Setup environment
os.environ["OPENAI_API_KEY"] = get_openai_api_key()
os.environ["SERPER_API_KEY"] = get_serper_api_key()
os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"
os.environ["OPENAI_API_BASE"] = "https://api.openai.com/v1"

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# Define agents with updated roles and backstories
data_analyst_agent = Agent(
    role="Market Research Analyst",
    goal="Analyze Indian stock market data and news to uncover emerging trends for investment decisions.",
    backstory=(
        "With expertise in the Indian equities market and financial analytics, this agent uses historical data, "
        "real-time trends, and company fundamentals to deliver insights that drive informed trading strategies."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[scrape_tool, search_tool]
)

trading_strategy_agent = Agent(
    role="Quantitative Strategy Developer",
    goal="Formulate effective trading strategies using technical and fundamental insights from Indian equities.",
    backstory=(
        "This agent designs profit-maximizing strategies tailored to investor preferences like intraday or swing trades. "
        "It merges AI-driven technical analysis with data-backed decision-making frameworks."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[scrape_tool, search_tool]
)

execution_agent = Agent(
    role="Trade Execution Planner",
    goal="Propose the best order execution method including timing, risk control, and slippage handling.",
    backstory=(
        "Specialized in trade logistics, this agent analyzes volume, volatility, and pricing models to advise "
        "on optimal order types (e.g., market, limit, stop-loss) ensuring successful execution of strategies."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[scrape_tool, search_tool]
)

risk_management_agent = Agent(
    role="Risk and Compliance Advisor",
    goal="Analyze and communicate potential risk exposure in stock trading strategies.",
    backstory=(
        "This agent provides a detailed risk evaluation including position sizing, volatility exposure, sectoral risks, "
        "and recommends contingency mechanisms to minimize financial losses and stay within compliance bounds."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[scrape_tool, search_tool]
)

# Define tasks with detailed descriptions and expected output
data_analysis_task = Task(
    description="Analyze recent stock data, earnings, and financial news for {stock_selection}. "
                "Use machine learning and statistics to identify key market drivers and patterns.",
    expected_output="A detailed insight report with recent stock price behavior, earnings highlights, and news sentiment analysis.",
    agent=data_analyst_agent,
)

strategy_development_task = Task(
    description="Develop a data-driven trading strategy for {stock_selection} considering {risk_tolerance} risk appetite. "
                "Include entry price, target, stop-loss, and time horizon based on analysis results.",
    expected_output="A ready-to-execute trading plan including rationale, technical levels, and indicators used.",
    agent=trading_strategy_agent,
)

execution_planning_task = Task(
    description="Design the best execution plan for the given strategy, factoring in volatility, volume, and market timing. "
                "Also include fallback plan if price deviates from ideal entry range.",
    expected_output="Execution plan with order types, market conditions to monitor, and timing recommendations.",
    agent=execution_agent,
)

risk_assessment_task = Task(
    description="Assess risk profile for {stock_selection} based on strategy, exposure, and sector volatility. "
                "Propose ways to reduce risk through hedging, alerts, or trade sizing.",
    expected_output="Comprehensive risk assessment with risk metrics and 3 actionable mitigation strategies.",
    agent=risk_management_agent,
)

# Create Crew
financial_trading_crew = Crew(
    agents=[
        data_analyst_agent,
        trading_strategy_agent,
        execution_agent,
        risk_management_agent
    ],
    tasks=[
        data_analysis_task,
        strategy_development_task,
        execution_planning_task,
        risk_assessment_task
    ],
    manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.6),
    process=Process.hierarchical,
    verbose=True
)

# Define input
financial_trading_inputs = {
    'stock_selection': 'TATA',
    'initial_capital': '100000',
    'risk_tolerance': 'Moderate',
    'trading_strategy_preference': 'Swing Trading',
    'news_impact_consideration': True
}

# Run the Crew
print("\n🔍 Running trading crew agents for stock: INFY...\n")

try:
    result = financial_trading_crew.kickoff(inputs=financial_trading_inputs)

    log_output = "\n📈 FINANCIAL TRADING STRATEGY REPORT 📈\n\n"

    for task_output in result.task_outputs:
        log_output += f"🧠 Task: {task_output.task.agent.role} - {task_output.task.description}\n\n"
        log_output += f"{task_output.output.strip()}\n"
        log_output += "-" * 80 + "\n"

    print(log_output)

    # Save log to file
    with open("trading_report.log", "w", encoding="utf-8") as f:
        f.write(log_output)

    print("\n✅ Trading report saved to 'trading_report.log'.")

except Exception as e:
    print(f"\n❌ Error during execution: {str(e)}")
