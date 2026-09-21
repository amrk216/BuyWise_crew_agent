
from pydantic import BaseModel, Field, model_validator
from typing import List, Optional



class SuggestedSearchQueries(BaseModel):
    queries: List[str]= Field(..., title="Suggested search queries to be passed to the search engine", min_items = 1,max_length=5)



class SingleSearchResults(BaseModel):
    title: str
    url: str
    content: str
    score: float
    search_query: str


class SearchResults(BaseModel):
    results: List[SingleSearchResults] = Field(..., title="List of search results", min_items=1, max_items=15)

    @model_validator(mode="after")
    def limit_results(self):

        self.results = sorted(
            self.results,
            key=lambda x: x.score,
            reverse=True
        )

        self.results = self.results[:15]

        return self


class ProductSpec(BaseModel):
    specification_name: str
    specification_value: str

class SingleExtractedProduct(BaseModel):
    page_url: str = Field(..., title="The original url of the product page")
    product_title: str = Field(..., title="The title of the product")
    product_image_url: str = Field(..., title="The url of the product image")
    product_url: str = Field(..., title="The url of the product")
    product_current_price: float = Field(..., title="The current price of the product")
    product_original_price: Optional[float] = Field(title="The original price of the product before discount. Set to None if no discount", default=None)
    product_discount_percentage: Optional[float] = Field(title="The discount percentage of the product. Set to None if no discount", default=None)

    product_specs: List[ProductSpec] = Field(..., title="The specifications of the product. Focus on the most important specs to compare.", min_items=1, max_items=5)

    agent_recommendation_rank: int = Field(..., title="The rank of the product to be considered in the final procurement report. (out of 7, Higher is Better) in the recommendation list ordering from the best to the worst")
    agent_recommendation_notes: List[str]  = Field(..., title="A set of notes why would you recommend or not recommend this product to the company, compared to other products.")


class AllExtractedProducts(BaseModel):
    products: List[SingleExtractedProduct]