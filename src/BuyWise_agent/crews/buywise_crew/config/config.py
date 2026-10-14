from dotenv import load_dotenv
import os
from litellm import completion
from crewai import LLM
from langfuse import get_client
from tavily import TavilyClient
from openinference.instrumentation.crewai import CrewAIInstrumentor
from scrapegraph_py import ScrapeGraphAI
from datetime import datetime
import uuid
load_dotenv()


KILO_API_KEY = os.environ["KILO_API_KEY"]
# OPEN_API_KEY = os.environ["OPEN_API_KEY"]
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
MINIMAX_MODEL = os.environ["MINIMAX_MODEL"]

TAVILY_API_KEY = os.environ["TAVILY_API_KEY"]
SCRAPEGRAPH_API_KEY = os.environ["SCRAPEGRAPH_API_KEY"]
MINIMAX_API_KEY = os.environ["MINIMAX_API_KEY"]

# KILO_MODEL = os.environ["KILO_MODEL"]
COHERE_MODEL = os.environ["COHERE_MODEL"]
NVIDIA_MODEL = os.environ["NVIDIA_MODEL"]
# OPEN_MODEL = os.environ["OPEN_API_KEY"]

LANGFUSE_SECRET_KEY = os.environ["LANGFUSE_SECRET_KEY"]
LANGFUSE_PUBLIC_KEY = os.environ["LANGFUSE_PUBLIC_KEY"]
LANGFUSE_BASE_URL = os.environ["LANGFUSE_BASE_URL"]


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
# OPEN_LLM = LLM(
#     model=OPEN_MODEL,
#     temperature=0,
#     base_url="https://openrouter.ai/api/v1",
#     provider="openrouter",
#     #max_tokens=3000

# )

# KILO_LLM = LLM(
#     model=KILO_MODEL,
#     temperature=0,
#     base_url = "https://api.kilo.ai/api/gateway",
#     provider="openrouter",
# )

COHERE_MODEL = LLM(
    model=COHERE_MODEL,
    temperature=0,
    base_url = "https://api.cohere.ai/v1",
    provider="cohere",
    
)

NVIDIA_MODEL = LLM(
    model=NVIDIA_MODEL,
    temperature=0,
    base_url = "http://127.0.0.1:1234/v1",
    # provider="google-genai",
)

MINIMAX_MODEL = LLM(
    model=MINIMAX_MODEL,
    api_key=MINIMAX_API_KEY,
    temperature=0,
    base_url = "https://api.minimax.io/v1",
    provider="minimax",
)

# Tavily
search_client = TavilyClient(
    api_key=TAVILY_API_KEY
)


sgai = ScrapeGraphAI(api_key=SCRAPEGRAPH_API_KEY)