let uploadedFilename = null;

document.getElementById("upload-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const fileInput = document.getElementById("pdf-file");
  const formData = new FormData();
  formData.append("pdf", fileInput.files[0]);

  try {
    const response = await fetch("/upload_pdf", {
      method: "POST",
      body: formData
    });

    const data = await response.json();
    if (data.success) {
      uploadedFilename = data.filename;
      document.getElementById("upload-status").innerText = "Upload successful!";
    } else {
      document.getElementById("upload-status").innerText = "Upload failed.";
    }
  } catch (error) {
    console.error("Upload error:", error);
    document.getElementById("upload-status").innerText = "Error uploading file.";
  }
});

document.getElementById("summarize-btn").addEventListener("click", async function () {
  const wordLimit = document.getElementById("word-limit").value;
  const summaryBox = document.getElementById('pdf-summary');
  summaryBox.innerHTML = "Generating summary...";

  if (!uploadedFilename) {
    alert("Please upload a PDF first.");
    return;
  }

  try {
    const response = await fetch("/summarize_pdf", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        filename: uploadedFilename,
        word_limit: wordLimit
      })
    });

    const data = await response.json();
    document.getElementById("pdf-summary").innerText = data.summary;

    if (data.download_url) {
      document.getElementById("download-link-container").innerHTML = `
        <a href="${data.download_url}" download="summary.pdf">
          <button>Download Summary PDF</button>
        </a>
      `;
    }
  } catch (error) {
    console.error("Summarization error:", error);
    document.getElementById("pdf-summary").innerText = "Failed to summarize.";
  }
});
