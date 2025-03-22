from typing import List, Dict
from .research_agent import research_sources

def enrich_modules(modules: List[Dict], brief: str) -> List[Dict]:
    enriched = []
    for module in modules:
        enriched.append({
            "title": module["title"],
            "lessons": [
                {
                    "title": f"{module['title']} - Lesson 1",
                    "content": f"This lesson explores {module['title']} in the context of {brief}.",
                    "resources": ["https://example.com/video1", "https://example.com/image1.jpg"]
                },
                {
                    "title": f"{module['title']} - Lesson 2",
                    "content": f"Detailed insights into {module['title']}.",
                    "resources": ["https://example.com/video2"]
                }
            ]
        })
    return enriched
