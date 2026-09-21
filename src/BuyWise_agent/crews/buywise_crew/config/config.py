from dotenv import load_dotenv
import os

from crewai import LLM
from langfuse import get_client
from tavily import TavilyClient
from openinference.instrumentation.crewai import CrewAIInstrumentor
from scrapegraph_py import ScrapeGraphAI
from datetime import datetime
import uuid
load_dotenv()


KILO_API_KEY = os.environ["KILO_API_KEY"]
LANGFUSE_SECRET_KEY = os.environ["LANGFUSE_SECRET_KEY"]
LANGFUSE_PUBLIC_KEY = os.environ["LANGFUSE_PUBLIC_KEY"]
LANGFUSE_BASE_URL = os.environ["LANGFUSE_BASE_URL"]
SCRAPEGRAPH_API_KEY = os.environ["SCRAPEGRAPH_API_KEY"]
KILO_MODEL = os.environ["KILO_MODEL"]
COHERE_MODEL = os.environ["COHERE_MODEL"]
TAVILY_API_KEY = os.environ["TAVILY_API_KEY"]
ATRIA_API_KEY = os.environ["ATRIA_API_KEY"]
ATRIA_MODEL = os.environ["ATRIA_MODEL"]


# Initialize Langfuse
langfuse = get_client()


# Verify Langfuse connection
if langfuse.auth_check():
    print("Langfuse client is authenticated and ready!")
else:
    print("Authentication failed. Please check your credentials and host.")


# Initialize CrewAI instrumentation
CrewAIInstrumentor().instrument(skip_dep_check=True)

BASE_OUTPUT_DIR = "./ai-agent-output"


# Output directory  
def create_output_dir(base_dir=BASE_OUTPUT_DIR):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = str(uuid.uuid4())[:8]  # Generate a short unique ID
    output_dir = os.path.join(base_dir, f"run_{timestamp}_{unique_id}")
    os.makedirs(output_dir, exist_ok=True)
    return output_dir
output_dir = create_output_dir()



# LLM
KILO_LLM = LLM(
    model=KILO_MODEL,
    temperature=0,
    base_url = "https://api.kilo.ai/api/gateway",
    provider="openrouter",
)

COHERE_MODEL = LLM(
    model=COHERE_MODEL,
    temperature=0,
    base_url = "https://api.cohere.ai/v1",
    provider="cohere",
)

ATRIA_MODEL = LLM(
    model=ATRIA_MODEL,
    temperature=0,
    base_url = "https://api.atria-asi.ai/v1",
    provider="atria",
)

# Tavily
search_client = TavilyClient(
    api_key=TAVILY_API_KEY
)


sgai = ScrapeGraphAI(api_key=SCRAPEGRAPH_API_KEY)