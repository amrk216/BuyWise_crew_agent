
from crewai import Task


from .config import output_dir
import os
from .agents import ( Report_author_agent, search_queries_recommendation_agent,
                    search_engine_agent,
                     scraping_agent
)
from .models import ( SuggestedSearchQueries, SearchResults, AllExtractedProducts
)
search_queries_recommendation_task = Task(
    description="\n".join([
        "Buywise is looking to buy {product_name} at the best prices (value for a price strategy)",
        "The company target any of these websites to buy from: {websites_list}",
        "The company wants to reach all available products on the internet to be compared later in another stage.",
        "The stores must sell the product in {country_name}",
        "Generate at maximum {no_keywords} queries.",
        "The search keywords must be in {language} language.",
        "Search keywords must contains specific brands, types or technologies. Avoid general keywords.",
        "The search query must reach an ecommerce webpage for product, and not a blog or listing page.",
        "The required product condition is: {product_condition}.",
        "Include the required product condition in the search queries when relevant.",
        "The customer's budget is: {budget}.",
        "Use the customer's budget as an important constraint when generating search queries."
    ]),
    expected_output="A JSON object containing a list of suggested search queries.",
    output_json=SuggestedSearchQueries,
    output_file=os.path.join(output_dir, "step_1_suggested_search_queries.json"),
    agent=search_queries_recommendation_agent
)

search_engine_task = Task(
    description="\n".join([
        "Search for relevant and specific product pages.",
        "Avoid general category pages, listing pages, blogs, and informational pages.",
        "Collect as many relevant products as possible.",
        "Avoid duplicate products.",
        "The collected products will be passed to another stage for comparison and recommendation.",
        "Ignore any search results with confidence score less than {score_th}.",
        "Ignore any suspicious links or non-ecommerce single product page links.",
        "The search results will be used to compare prices of products from different websites and recommend the best options to buy.",
        "The required product condition is: {product_condition}.",
        "Include the required product condition in the search query when relevant.",
        "Only return products matching the requested condition: new, used, or both.",
        "Today's date is {current_date}.",
        "Use this date as the current date and do not assume an older date.",
        "The customer's budget is: {budget}.",
        "Use the customer's budget as an important constraint when generating search queries.",
        "Prioritize products that are within or close to the customer's budget.",
        "Do not generate search queries for products that are clearly far above the customer's budget unless there are no suitable products within the budget range.",
        "Consider the budget together with the requested product, condition, country, and target websites."
    ]),
    expected_output="A JSON object containing a list of search results.",
    output_json=SearchResults,
    output_file=os.path.join(output_dir, "step_2_search_results.json"),
    agent=search_engine_agent   
)

scraping_task = Task(
    description="\n".join([
        "Scrape specific information from web pages based on the provided URLs and required fields.",
        "Ensure accuracy and completeness of the scraped data.",
        "Collect the best {top_recommendations_no} products based on the agent's recommendation rank.",
        "Extract the main product image URL from each product page.",
        "The product_image_url must point directly to the main product image, not to a logo, banner, thumbnail, or unrelated image.",
        "Use the image URL provided by the product page whenever available.",
        "Today's date is {current_date}.",
        "Use this date as the current date and do not assume an older date.",
    ]),
    expected_output="A JSON object containing the scraped data from the web pages.",
    output_json=AllExtractedProducts,
    output_file=os.path.join(output_dir, "step_3_scraped_data.json"),
    agent=scraping_agent
)


Report_author_Task = Task(
    description="\n".join([
        "The task is to generate a professional HTML page for the procurement report.",
        "You have to use Bootstrap CSS framework for a better UI.",
        "Use the provided context about the company to make a specialized report.",
        "The report will include the search results and prices of products from different websites.",
        "The report should be structured with the following sections:",
        "1. Executive Summary: A brief overview of the procurement process and key findings.",
        "2. Introduction: An introduction to the purpose and scope of the report.",
        "3. Methodology: A description of the methods used to gather and compare prices.",
        "4. Findings: Detailed comparison of prices from different websites, including tables and charts.",
        "5. Analysis: An analysis of the findings, highlighting any significant trends or observations.",
        "6. Recommendations: Suggestions for procurement based on the analysis.",
        "7. Conclusion: A summary of the report and final thoughts.",
        "8. Appendices: Any additional information, such as raw data or supplementary materials.",
        "Each product must include a clickable 'Buy Now' link that points directly to the product purchase page.",
    ]),

    expected_output="A professional HTML page for the procurement report.",
    output_file=os.path.join(output_dir, "step_4_procurement_report.html"),
    agent=Report_author_agent
)