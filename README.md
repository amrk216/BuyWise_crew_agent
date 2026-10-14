BuyWise AI Agent

BuyWise is a Python project that uses CrewAI to organize an AI-assisted product research workflow: generating search queries, finding candidate product pages, extracting product information, and organizing results for review.

## Features

- AI-assisted product search-query generation
- Web search for relevant product pages
- Product information extraction where supported by the source website
- Structured JSON outputs for inspecting workflow steps
- Product comparison and ranking, based on the fields and criteria implemented in the current version
- HTML report generation for reviewing collected options
- Optional LLM tracing with Langfuse when configured

## Workflow

```text
Shopping requirements
        |
        v
Generate search queries
        |
        v
Search for product pages
        |
        v
Extract and structure product information
        |
        v
Compare available options
        |
        v
Export JSON results and HTML report
```

## Tech Stack

- Python
- CrewAI
- Large Language Models (LLMs)
- Tavily for web search
- ScrapeGraphAI for supported page extraction
- Pydantic for structured data
- JSON and HTML for output artifacts
- Langfuse for optional observability

Exact integrations depend on the current project configuration.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/amrk216/BuyWise_crew_agent.git
cd BuyWise_crew_agent
```

### 2. Create a virtual environment

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root. Add the credentials required by the integrations and variable names used in your configuration. Example:

```dotenv
OPENROUTER_API_KEY=your_openrouter_api_key
TAVILY_API_KEY=your_tavily_api_key
SCRAPEGRAPH_API_KEY=your_scrapegraph_api_key

# Optional: Langfuse observability
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_HOST=your_langfuse_host
```

These are examples, not a guarantee that every variable is required or matches your current configuration. Check the code and configuration files for the exact names expected by your version. Never commit real API keys to GitHub.

### 5. Run the agent

From the repository root, try:

```bash
PYTHONPATH=src python -m BuyWise_agent.crews.buywise_crew.buywise_crew
```

If the entry point has changed in your branch, use the command specified by the current code.

## Outputs

Depending on the current implementation, the workflow may produce JSON files containing suggested queries, search results, and extracted product details, as well as an HTML procurement report. Check the output directory and filenames in the source code.

## Reliability Notes

- Search and extraction depend on provider availability, API limits, and website structure.
- Some websites block automated scraping or omit product details.
- Prices and availability change; confirm important information on the retailer's original page.
- Review the generated results before using them to make a purchase.

## Potential Improvements

- Validate extracted data and handle missing fields
- Add configurable budget and comparison criteria
- Integrate additional search providers and retailers
- Add automated tests for the workflow
- Provide a user-facing interface or API
- Track price history and notify users about changes

## Author

**Amr Khaled Salama**

- GitHub: [@amrk216](https://github.com/amrk216)
- Repository: [BuyWise_crew_agent](https://github.com/amrk216/BuyWise_crew_agent)

## Disclaimer

BuyWise is a product research project. It does not guarantee that third-party product details, prices, or availability are accurate or complete. Verify information with the seller before purchasing.
'''