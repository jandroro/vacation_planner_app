import os

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

# --------------------------------------------------
# AGENTCORE IMPORTS
# --------------------------------------------------

from bedrock_agentcore.runtime import BedrockAgentCoreApp
app = BedrockAgentCoreApp()

# --------------------------------------------------

@CrewBase
class VacationPlanner():
    """
    AI-Powered Vacation Planner App
    
    A sophisticated multi-agent system that democratizes expert travel planning
    by providing professional-level vacation planning accessible to everyone.
    
    This crew employs specialized AI agents working collaboratively to:
    - Research destinations with real-time information
    - Create optimized day-by-day itineraries
    """
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self):
        """Initialize the crew with Bedrock Nova Pro LLM and tools"""
        # Initialize Amazon Bedrock Nova Pro LLM
        # Note: Do not add region attribute (not supported by Bedrock Nova as it is cross-region)
        self.llm = LLM(
            model=os.getenv("MODEL", "bedrock/us.amazon.nova-pro-v1:0"),
            temperature=0.1,
        )
        
        # Initialize tools for web research and information gathering
        # SerperDev for real-time web search
        self.serper_tool = SerperDevTool(
            api_key=os.getenv('SERPER_API_KEY', '')
        )
    
    @agent
    def vacation_researcher(self) -> Agent:
        """
        Senior Vacation Research Specialist Agent
        
        Responsible for comprehensive destination research, gathering real-time
        information from multiple sources, and democratizing expert travel planning
        knowledge.
        """
        return Agent(
            config=self.agents_config['vacation_researcher'],
            llm=self.llm,
            tools=[self.serper_tool],
            verbose=True,
        )

    @agent
    def itinerary_planner(self) -> Agent:
        """
        Itinerary Planner Agent

        Transforms research into optimized, actionable itineraries that eliminate
        the need for expensive travel agents through intelligent scheduling and
        budget optimization.
        """
        return Agent(
            config=self.agents_config['itinerary_planner'],
            llm=self.llm,
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        """
        Comprehensive Destination Research Task
        
        Gathers real-time information from multiple sources about potential
        destinations, attractions, accommodations, and practical travel details.
        """
        return Task(
            config=self.tasks_config['research_task'],
        )
    
    @task
    def reporting_task(self) -> Task:
        """
        Intelligent Itinerary Generation Task
        
        Creates optimized day-by-day schedules that balance activities with
        relaxation, consider geographical proximity, and include realistic
        time estimates and transportation options.
        """
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """
        Vacation Planner Crew Assembly
        
        Creates a collaborative multi-agent system where agents work sequentially,
        sharing memory and context to deliver professional-level vacation planning.
        
        Process Flow:
        1. Research Specialist gathers comprehensive destination information
        2. Planning Architect creates optimized itinerary
        
        Returns:
            Crew: Configured CrewAI crew ready for execution
        """
        
        return Crew(
            agents=self.agents,  # Automatically uses all @agent decorated methods
            tasks=self.tasks,    # Automatically uses all @task decorated methods
            process=Process.sequential,
            verbose=True,
        )

# --------------------------------------------------
# ADD AGENTCORE ENTRYPOINT DECORATOR

# Python decorator within the Bedrock AgentCore SDK.
# Function to be executed by the runtime on an event (prompt)
# # Creates webserver endpoints.
# --------------------------------------------------

@app.entrypoint
def agent_invocation(payload, context):
    """Handler for agent invocation"""
    print(f'Payload: {payload}')
    
    try:
        # Extract user input from payload
        user_input = payload.get('topic', 'Tokyo, Japan')
        print(f"Processing vacation destination: {user_input}")
        
        # Crew execution - Creates an instance of the VacationPlanner class and run crew method
        research_crew_instance = VacationPlanner()
        crew = research_crew_instance.crew()
        
        # Starts the sequential agent workflow
        result = crew.kickoff(inputs={'topic': user_input})
        
        print("Context:\n----------------\n", context)
        print("Result Raw:\n*************\n", result.raw)
        
        # Safely access json_dict if it exists
        if hasattr(result, 'json_dict'):
            print("Result JSON:\n***********\n", result.json_dict)
        
        return {"result": result.raw}
    
    except Exception as e:
        print(f"Error ocurred: {e}")
        return {"error": f"An error ocurred: {str(e)}"}

# Local test function
def test_local():
    """Test the crew locally without Bedrock AgentCore"""
    try:
        crew_instance = VacationPlanner()
        crew = crew_instance.crew()
        result = crew.kickoff(inputs={'topic': 'Plan a vacation to Germany'})
        print("Result:", result.raw)
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Run AgentCore server - HTTP server on port 8080
    app.run(port=8080)