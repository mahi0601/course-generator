def generate_course_structure(brief: str):
    return {
        "course_title": f"Complete Course on {brief}",
        "description": f"A comprehensive guide for beginners on {brief}.",
        "modules": [
            {"title": "Module 1: Introduction"},
            {"title": "Module 2: History & Evolution"},
            {"title": "Module 3: Practical Applications"},
            {"title": "Module 4: Case Studies"},
            {"title": "Module 5: Tools & Resources"},
            {"title": "Module 6: Final Assessment"},
        ]
    }
