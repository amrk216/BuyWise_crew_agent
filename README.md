# BuyWise AI

**BuyWise AI** is an intelligent multi-agent shopping assistant designed to automate product research, price comparison, and procurement analysis.

The system takes a user's purchasing requirements and uses AI agents to search across e-commerce websites, collect product information, compare available options, and generate a structured procurement report.

## Features

* AI-powered product search query generation
* Multi-agent architecture using CrewAI
* Search across multiple e-commerce websites
* Product page discovery and filtering
* Web scraping and product data extraction
* Product price and specification comparison
* Budget-aware product evaluation
* Product ranking based on value and relevance
* Product image and direct purchase URL extraction
* Automated procurement report generation
* Structured JSON outputs for each processing stage
* Support for different product conditions such as new and used

## Workflow

```text
User Requirements
       │
       ▼
Search Query Recommendation Agent
       │
       ▼
Search Engine Agent
       │
       ▼
Scraping Agent
       │
       ▼
Product Comparison & Ranking
       │
       ▼
Report Author Agent
       │
       ▼
Procurement Report
```

## Multi-Agent Architecture

### 1. Search Query Recommendation Agent

Analyzes the user's requirements and generates specific search queries targeting relevant products, brands, technologies, and product types.

### 2. Search Engine Agent

Uses the generated queries to discover relevant product pages from e-commerce websites while filtering out blogs, category pages, and irrelevant results.

### 3. Scraping Agent

Extracts structured information from product pages, including:

* Product name
* Product image
* Current price
* Original price
* Discount percentage
* Product specifications
* Product URL
* Page URL

### 4. Report Author Agent

Analyzes the collected product information and generates a professional procurement report containing product comparisons, recommendations, prices, specifications, and direct purchase links.

## Technologies

* Python
* CrewAI
* Large Language Models (LLMs)
* Tavily
* ScrapeGraphAI
* Pydantic
* FastAPI
* PostgreSQL
* Docker
* REST APIs
* HTML / Bootstrap

## Project Structure

```text
BuyWise_agent/
│
├── ai-agent-output/
│   ├── step_1_suggested_search_queries.json
│   ├── step_2_search_results.json
│   ├── step_3_scraped_data.json
│   └── step_4_procurement_report.html
│
├── src/
│   └── BuyWise_agent/
│       └── crews/
│           └── buywise_crew/
│               ├── agents.py
│               ├── tasks.py
│               ├── config.py
│               ├── models.py
│               └── buywise_crew.py
│
├── requirements.txt
├── README.md
└── .env
```

## Example Use Case

A company needs to purchase several laptops within a specific budget.

The user can provide requirements such as:

```text
Product:
Business laptops

Country:
Egypt

Budget:
50,000 EGP

Condition:
New

Preferred Stores:
Amazon Egypt, Jumia Egypt, Noon Egypt

Language:
English
```

BuyWise AI then:

1. Generates targeted search queries.
2. Searches multiple e-commerce sources.
3. Finds relevant product pages.
4. Extracts product information.
5. Compares prices and specifications.
6. Ranks the available products.
7. Generates a procurement report with direct purchase links.

## Output

The system produces structured outputs for every stage of the workflow:

### Search Queries

```json
{
  "queries": [
    "Dell Latitude business laptop 16GB RAM Egypt",
    "Lenovo ThinkPad 16GB RAM SSD Egypt"
  ]
}
```

### Search Results

```json
{
  "results": [
    {
      "title": "Example Product",
      "url": "https://example.com/product",
      "content": "Product information...",
      "score": 0.92,
      "search_query": "business laptop 16GB RAM Egypt"
    }
  ]
}
```

### Scraped Products

The scraping stage produces structured product information including price, specifications, images, discounts, and purchase URLs.

### Procurement Report

The final stage generates an HTML report containing:

* Executive Summary
* Introduction
* Methodology
* Product Findings
* Price Comparison
* Product Analysis
* Recommendations
* Direct Purchase Links
* Conclusion
* Appendices

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd BuyWise_agent
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
SCRAPEGRAPH_API_KEY=your_api_key
AGENTOPS_API_KEY=your_api_key
MODEL_NAME=your_model
```

## Running the Project

Run the BuyWise Crew:

```bash
PYTHONPATH=src python -m BuyWise_agent.crews.buywise_crew.buywise_crew
```

The generated results will be stored in:

```text
ai-agent-output/
```

## Project Goal

The goal of BuyWise AI is to transform manual product research into an automated AI-powered procurement workflow.

Instead of manually searching multiple stores, opening product pages, comparing prices, checking specifications, and creating a shortlist, BuyWise AI uses specialized AI agents to perform these tasks automatically and generate a structured purchasing report.

## Future Improvements

* Real-time product price tracking
* Price history and trend analysis
* More e-commerce integrations
* Product availability detection
* Automated price alerts
* Advanced recommendation algorithms
* User preference memory
* Telegram / WhatsApp integration
* Deployment as a production API
* Improved multi-agent evaluation and monitoring
