from crewai import Agent
from crewai.tools import tool



from BuyWise_agent.tools import search_engine_tool, web_scraper_tool
from ..config import KILO_LLM,COHERE_MODEL,ATRIA_API_KEY

# Agent A


search_queries_recommendation_agent = Agent(
    role = "Search Queries Recommendation Agent",
    goal="\n".join([
                "To provide a list of suggested search queries to be passed to the search engine.",
                "The queries must be varied and looking for specific items."
            ]),
    backstory="The agent is designed to help in looking for products by providing a list of suggested search queries to be passed to the search engine based on the context provided.",
    llm=COHERE_MODEL,
    verbose=True,
)

# Agent B 

search_engine_agent = Agent(
    role = "Search Engine Agent",

    goal = "to search for products on the internet based on the provided search queries and return the search results.",

    backstory = """The agent is designed to help in looking for products by searching for them on the internet based on the provided search queries and returning the search results.""",

    llm=KILO_LLM,  
    verbose=True,
    tools=[search_engine_tool]  
    
)

# Agent C
scraping_agent = Agent(
    role = "Web Scraping Agent",
    goal = "to scrape specific information from web pages based on the provided URLs and required fields.",
    backstory = "The agent is designed to extract detailed information from web pages, ensuring accuracy and completeness of the scraped data.",
    llm=KILO_LLM,
    verbose=True,
    tools=[web_scraper_tool] 
)


#Agent D

Report_author_agent = Agent(
    role = "Report Author Agent",
    goal = "to generate a comprehensive procurement report based on the extracted product data.",
    backstory = "The agent is designed to analyze the scraped product data and compile it into a structured report, highlighting key insights and recommendations.",
    llm=COHERE_MODEL,
    verbose=True,
)
