from openai import AzureOpenAI
import openai
import json
from openai import OpenAIError
from config import settings
from models import RoadmapResponse
from utils import extract_json_block

endpoint = settings.ENDPOINT
subscription_key = settings.API_KEY
deployment = settings.DEPLOYMENT_NAME

def generate_roadmap(topic: str) -> RoadmapResponse:
    prompt = f"""
    Create a detailed learning roadmap for the topic: '{topic}'. 
    Include: 
        - Prerequisites 
        - Estimated time to learn 
        - 4 to 6 milestones with 2-3 high-quality resources (URLs) per milestones 
    Format the response as a JSON object like:
    {{
        "topic": "...",
        "prerequisites": [...],
        "estimated_time": "....",
        "roadmap": [
            {{
                "milestone": "...",
                "description": "...", 
                "resources": ["...", "...."]
            }},
        ...
        ]
    }}
    """

    try:
        client = AzureOpenAI(
            azure_endpoint = endpoint,
            api_key = subscription_key,
            api_version = "2025-01-01-preview",
        )

        response = client.chat.completions.create(
            messages = [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model = settings.OPENAI_MODEL,
            temperature = 0.7,
        )
        raw_text = response.choices[0].message.content
        json_str = extract_json_block(raw_text)
        roadmap_data = json.loads(json_str)
        return RoadmapResponse(**roadmap_data)
    except OpenAIError as oe:
        raise RuntimeError(f"OpenAIError: {oe}")
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        raise ValueError(f"Failed to parse roadmap: {e}")