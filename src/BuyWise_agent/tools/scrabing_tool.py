
import json

from crewai.tools import tool
from ..crews.buywise_crew.config.config import sgai
from BuyWise_agent.crews.buywise_crew.config.models import SingleExtractedProduct

@tool 
def web_scraper_tool(page_url: str, required_fields: list):
    """
    A tool that takes a URL and a list of required fields as input and returns the scraped content from the webpage.
    Useful for extracting specific information from web pages.
    example: web_scraper_tool("https://www.amazon.com/dp/B09V3HN1ZK", ["title", "price", "description", "image_url", "availability"])
    """
    details = sgai.scrape(
        website = page_url,                        
        user_prompt = f"Scrape the following fields from the webpage ```json\n"+SingleExtractedProduct.model_json_schema()+"```\nfrom the web page")

    if details.status == "success":
        print(details.data.results.get("markdown", {}).get("data", [None])[0])
    
    return {
        "page_url": page_url,
        "scraped_data": details
    }
