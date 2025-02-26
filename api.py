from fastapi import FastAPI
from pydantic import BaseModel
from elasticsearch import Elasticsearch
import uvicorn
from typing import Optional
from clientElasticsearch import EsClient
import os


app = FastAPI()
esClient = EsClient()

class QueryInput(BaseModel):
    name: Optional[str] = None
    website: Optional[str] = None
    phone: Optional[str] = None
    facebook: Optional[str] = None


@app.post("/api/match")
async def matchCompany(query: QueryInput):
    mustClauses = []
    if query.name:
        mustClauses.append({"multi_match": {
            "query": query.name,
            "fields": ["allNames", "commercialName", "legalName"],
            "fuzziness": "AUTO"
        }})
    if query.website:
        mustClauses.append({"match": {"website": query.website}})
    if query.phone:
        mustClauses.append({"match": {"phones": query.phone}})
    if query.facebook:
        mustClauses.append({"match": {"socialLinks": query.facebook}})

    if not mustClauses:
        return {"error": "At least one query parameter required"}

    response = esClient.search(index="companyProfiles", body={"query": {"bool": {"must": mustClauses}}}, size=1)
    hits = response['hits']['hits']
    return hits[0]['_source'] if hits else {"error": "No match found"}


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000)