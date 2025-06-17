document.getElementById('summarize-btn').addEventListener('click', async () => {
  const link = document.getElementById('youtube-link').value.trim();
  const language = document.getElementById('language').value;
  const length = document.getElementById('length').value;
  const summaryBox = document.getElementById('summary-result');
  summaryBox.innerHTML = "Generating summary...";

  const videoId = extractYouTubeVideoID(link);
  if (!videoId) {
    alert("Invalid YouTube link.");
    return;
  }

  // Embed video
  document.getElementById('youtube-video').src = `https://www.youtube.com/embed/${videoId}`;

  try {
    const response = await fetch('/summarize_youtube', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ link, language, length })
    });

    const data = await response.json();
    document.getElementById('summary-result').innerText = data.summary;
  } catch (err) {
    console.error(err);
    alert("Failed to fetch summary.");
  }
});

function extractYouTubeVideoID(url) {
  const match = url.match(/(?:v=|\/)([0-9A-Za-z_-]{11})/);
  return match ? match[1] : null;
}
