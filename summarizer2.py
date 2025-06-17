import google.generativeai as genai

# Configure the API key
genai.configure(api_key="")

def summarize_text(text, word_limit=200, language='English'):
    """
    Summarizes the given text using the Gemini API.

    Args:
        text (str): The text to summarize.
        word_limit (int): Desired word limit for the summary.

    Returns:
        str: The summarized text.
    """
    try:
        # Initialize the GenerativeModel
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")

        # Generate content
        response = model.generate_content(
                        f"You are a text summarizer. Summarize the following text into approximately {word_limit} words:\n{text}in this particular {language} language")

        # Output the generated text
        summary  = response.text
        return summary

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    text = input("Enter the text to summarize: ")
    word_limit = int(input("Enter the desired word limit for the summary: "))
    language = input("Enter the desired language for the summary:")
    summary = summarize_text(text, word_limit, language)
    print("\nSummarized Text:\n")
    print(summary)
