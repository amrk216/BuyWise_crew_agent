from crewai.tools import tool
from ..crews.buywise_crew.config.config import search_client

@tool
def search_engine_tool(query: str):
    """
    A tool that takes a search query as input and returns the search results.,
    Useful for search-based queries. Use this to find current information about any query related pages using a search engine
    """
    return search_client.search(query)