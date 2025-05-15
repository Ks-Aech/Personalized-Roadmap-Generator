import re

def extract_json_block(text: str) -> str:
    match = re.match(r"\{(?:.|\n)*\}", text)
    if not match:
        raise ValueError("No valid JSON object found in response.")
    return match.group(0)