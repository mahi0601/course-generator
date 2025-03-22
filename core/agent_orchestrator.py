from agents.research_agent import research_sources
from agents.structure_agent import generate_course_structure
from agents.content_agent import enrich_modules

def generate_complete_course(brief: str, target_audience: str):
    sources = research_sources(brief)
    structure = generate_course_structure(brief)
    enriched_modules = enrich_modules(structure["modules"], brief)

    return {
        "course_title": structure["course_title"],
        "description": structure["description"],
        "modules": enriched_modules,
        "references": sources
    }
