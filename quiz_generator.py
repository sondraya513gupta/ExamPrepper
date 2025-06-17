import google.generativeai as genai
import json
import re

# Set the API key for the Gemini model (Google AI Studio)
genai.configure(api_key="")

def generate_quiz(topic, num_questions=10):
    """
    Generates a multiple-choice quiz based on the given topic.

    Args:
        topic (str): The topic for the quiz.
        num_questions (int): The number of questions to generate.

    Returns:
        list: A list of dictionaries containing questions, options, and the correct answer.
    """
    prompt = f"""
    You are a Quiz Generator which creates a {num_questions}-question multiple-choice quiz on the topic "{topic}". 
    Each question should have:
    - One correct answer and three incorrect options.
    - Format: Question, followed by four options labeled A, B, C, and D.
    - Indicate the correct answer for each question in the format:
        Question: ...
        Options: A. ..., B. ..., C. ..., D. ...
        Correct Answer: (e.g., A, B, C, or D)
    Return the quiz in JSON format with:
    {{
        \"quiz\": {{
            \"title\": \"<title>\",
            \"questions\": [
                {{
                    \"question\": \"...\",
                    \"options\": {{\"A\": \"...\", \"B\": \"...\", \"C\": \"...\", \"D\": \"...\"}},
                    \"correct_answer\": \"A\"
                }}
            ]
        }}
    }}
    """

    try:
        # Initialize the GenerativeModel
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")

        # Use the Gemini API to generate the quiz
        response = model.generate_content(prompt)

        # Extract the generated text from the response
        quiz_text = response.text.strip() if response and response.text else ""

        # Remove markdown-style code block wrappers like ```json ... ```
        quiz_text = re.sub(r"^```(?:json)?\s*|\s*```$", "", quiz_text.strip(), flags=re.DOTALL)
        
        try:
            quiz_json = json.loads(quiz_text)
            return quiz_json
        
        except json.JSONDecodeError as e:
            print("JSON parsing error:", e)

    except Exception as e:
        print(f"Error generating quiz: {str(e)}")
        return []

if __name__ == '__main__':
    topic = input("Enter the topic:")
    quiz = generate_quiz(topic)
    print(quiz)
    
