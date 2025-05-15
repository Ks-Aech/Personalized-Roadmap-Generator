from pydantic import BaseModel, HttpUrl
from typing import List, Optional 

class RoadmapItem(BaseModel):
    milestone: str
    description: Optional[str]
    resources: List[HttpUrl]

class RoadmapResponse(BaseModel):
    topic: str
    prerequisites: List[str]
    estimated_time: str
    roadmap: List[RoadmapItem]

class TopicRequest(BaseModel):
    topic: str

