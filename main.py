from fastapi import FastAPI, HTTPException
from models import TopicRequest, RoadmapResponse
from roadmap_generator import generate_roadmap

app = FastAPI(title="Personalized Learning Roadmap Generator")

@app.post("/generate_roadmap", response_model=RoadmapResponse)
def get_roadmap(request: TopicRequest):
    try:
        roadmap = generate_roadmap(request.topic)
        roadmap = RoadmapResponse(**roadmap)
        return roadmap
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=502, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")