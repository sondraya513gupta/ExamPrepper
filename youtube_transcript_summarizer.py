from youtube_transcript_api import YouTubeTranscriptApi
from summarizer2 import summarize_text

def YT_summarizer(url, length, language):
    print("URL: ",url)

    video_id = url.replace("https://www.youtube.com/watch?v=","")
    print("Video id: ",video_id)

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    # print(transcript)

    extracted_text = ""
    for x in transcript:
        sentence = x['text']
        extracted_text += f' {sentence}\n'

    num_words = length
    summarized_text = summarize_text(extracted_text, num_words, language)
    return summarized_text

if __name__ == '__main__':
    youtube_link = input("Enter youtube link:")
    length = int(input("Enter length of summay:"))
    language = input("Enter the language:")

    summary = YT_summarizer(youtube_link,length,language)
    print("summary:",summary)