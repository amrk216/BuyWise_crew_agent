
from crewai import Crew,Process


about_crew ="""A crew of agents 
designed to assist in the procurement process by searching for products, scraping relevant information, and generating a comprehensive report.
This crew is designed to help in looking for products by providing a list of suggested search queries to be passed to the search engine based on the context provided. 
The crew will search for products on the internet based on the provided search queries and  return the search results.
 The crew will then scrape specific information from web pages based on the provided URLs and required fields. Finally, the crew will generate a comprehensive procurement report based on the extracted product data."""   

from .config import (
    search_queries_recommendation_agent, 
   search_engine_agent,
   Report_author_agent,
   scraping_agent,

   search_queries_recommendation_task,
   search_engine_task,
   Report_author_Task,
   scraping_task,
    langfuse
)

from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d")


buywise_crew = Crew(
    agents=[
        search_queries_recommendation_agent,
        search_engine_agent,
        scraping_agent,
        Report_author_agent,

    ],
    tasks=[
        search_queries_recommendation_task,
        search_engine_task,
        scraping_task,
        Report_author_Task,
    ],
    process=Process.sequential,
    
)


with langfuse.start_as_current_observation(
    as_type="span",
    name="buywise-agent"
):
    crew_results = buywise_crew.kickoff(
        inputs={
            "product_name": "backpack",
            "websites_list": [
            "www.google.com",
            "www.amazon.eg",
            "www.jumia.com.eg",
            "www.noon.com/egypt-en",
            "btech.com",
            "2b.com.eg",
            "dream2000.com",
            "www.rayashop.com",
            "www.egprices.com",
            "www.compumarts.com",
            "www.sigma-computer.com",
            "www.abstore.com.eg",
            "www.sharafdg.com/egypt-en",
            "www.egypt.souq.com",
        ],
            "country_name": "Egypt",
            "no_keywords": 5,
            "language": "English,Arabic",
            "current_date": current_date,
            "score_th": 0.10,
            "top_recommendations_no": 10,
            "product_condition": "new",
            "top_recommendations_no" : 8,
            "budget":2100,


        }
    )


langfuse.flush()
