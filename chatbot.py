import google.generativeai as genai

# Set your Google Gemini API key
genai.configure(api_key="")

def chatbot_response(user_input):
    """
    Generate a chatbot response using Google Gemini API.

    Args:
        user_input (str): The user input or query.

    Returns:
        str: The chatbot's response.
    """
    try:
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")

        # Generate a response using the Gemini model
        response = model.generate_content(f"You are a helpful Examprepper assistant who will assist the students preparing for exams through the website called Examprepper. The website contains different tools to prepare for exams. Respond to the following query:\n{user_input}")

        # Extract and return the chatbot's response
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        # Get chatbot's response
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
