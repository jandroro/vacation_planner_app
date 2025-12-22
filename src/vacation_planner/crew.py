import os

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool

@CrewBase
class VacationPlanner():
    """
    AI-Powered Vacation Planner App
    
    A sophisticated multi-agent system that democratizes expert travel planning
    by providing professional-level vacation planning accessible to everyone.
    
    This crew employs specialized AI agents working collaboratively to:
    - Research destinations with real-time information
    - Create optimized day-by-day itineraries
    - Provide authentic local insights
    - Optimize budgets and maximize value
    """
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self):
        """Initialize the crew with Bedrock Nova Pro LLM and tools"""
        # Initialize Amazon Bedrock Nova Pro LLM
        # Note: Do not add region attribute (not supported by Bedrock Nova as it is cross-region)
        self.llm = LLM(
            model=os.getenv("MODEL", "bedrock/us.amazon.nova-pro-v1:0"),
        )
        
        # Initialize tools for web research and information gathering
        # SerperDev for real-time web search
        self.serper_tool = SerperDevTool(
            api_key=os.getenv('SERPER_API_KEY', '')
        )
        
        # Website scraping for detailed information
        self.scrape_tool = ScrapeWebsiteTool()
        
        # Website search for finding specific information on sites
        self.website_search_tool = WebsiteSearchTool()
    
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
            tools=[
                self.serper_tool,
                self.scrape_tool,
                self.website_search_tool
            ],
            verbose=True,
            # allow_delegation=False,
            # max_iter=15,
            # memory=True
        )

    @agent
    def vacation_planner(self) -> Agent:
        """
        Expert Vacation Planning Architect Agent
        
        Transforms research into optimized, actionable itineraries that eliminate
        the need for expensive travel agents through intelligent scheduling and
        budget optimization.
        """
        return Agent(
            config=self.agents_config['vacation_planner'],
            llm=self.llm,
            verbose=True,
            # allow_delegation=False,
            # max_iter=15,
            # memory=True
        )

    @task
    def destination_research(self) -> Task:
        """
        Comprehensive Destination Research Task
        
        Gathers real-time information from multiple sources about potential
        destinations, attractions, accommodations, and practical travel details.
        """
        return Task(
            config=self.tasks_config['destination_research'],
        )
    
    @task
    def itinerary_creation(self) -> Task:
        """
        Intelligent Itinerary Generation Task
        
        Creates optimized day-by-day schedules that balance activities with
        relaxation, consider geographical proximity, and include realistic
        time estimates and transportation options.
        """
        return Task(
            config=self.tasks_config['itinerary_creation'],
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
        3. Local Expert enhances with authentic experiences
        4. Budget Optimizer ensures financial viability and value
        
        Returns:
            Crew: Configured CrewAI crew ready for execution
        """
        
        return Crew(
            agents=self.agents,  # Automatically uses all @agent decorated methods
            tasks=self.tasks,    # Automatically uses all @task decorated methods
            process=Process.sequential,
            verbose=True,
            # memory=True,
            # embedder={
            #     "provider": "amazon-bedrock",
            #     "config": {
            #         "model": os.getenv('EMBEDDING_MODEL', 'amazon.titan-embed-text-v1'),
            #         "region_name": os.getenv('AWS_REGION_NAME', 'us-west-2')
            #     }
            # },
            # max_rpm=10,  # Rate limiting for API calls
            # share_crew=False
        )
