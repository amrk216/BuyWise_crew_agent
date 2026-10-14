from pydantic import BaseModel
from typing import List, Optional

from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d")

class ProcurementRequest(BaseModel):
    product_name: str
    budget: Optional[float] = None
    websites_list: List[str]
    country_name: str = "Egypt"
    no_keywords: int = 5
    language: str = "English"
    product_condition: str = "new"
    score_th: float = 0.10
    top_recommendations_no: int = 10
    # current_date: str = current_date,


