# services/llm_service.py

import openai
import os

# Ensure your OpenAI API key is correctly set
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_info(search_results, entity):
    """
    Uses OpenAI's gpt-3.5-turbo model to extract specific information from search results.
    """
    backend_prompt = (
        f"Extract the contact email and address for the company '{entity}' from the following search results:\n\n"
    )

    for result in search_results["results"]:
        backend_prompt += f"{result.get('title', '')}: {result.get('snippet', '')}\n"

    try:
        # Use ChatCompletion with the correct method
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that extracts information."},
                {"role": "user", "content": backend_prompt}
            ],
            max_tokens=150,
            temperature=0.3,
        )
        extracted_info = response.choices[0].message['content'].strip()
        return extracted_info
    except Exception as e:
        print(f"Error fetching data from OpenAI LLM: {e}")
        return f"Error extracting info for {entity}"