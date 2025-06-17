async function fetchPapers() {
  const branch = document.getElementById('branch').value;
  const semester = document.getElementById('semester').value;
  const subject = document.getElementById('subject').value;
  const year = document.getElementById('year').value;

  if (!branch || !semester || !subject || !year) {
      alert("Please select all filters.");
      return;
  }

  const res = await fetch("/previous_papers", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ branch, semester, subject, year })
  });

  const data = await res.json();
  const container = document.getElementById("paperLinks");
  container.innerHTML = "";

  if (data.length === 0) {
      container.innerHTML = "<p>No matching papers found.</p>";
      return;
  }

  data.forEach(paper => {
  const link = document.createElement("a");
  link.href = paper.file_url;
  
  // Extract the filename from the URL
  const fileName = paper.file_url.split('/').pop(); // gets 'nlp_23.pdf'

  // Use file name 
  link.textContent = `${fileName}`;
  link.target = "_blank";
  link.style.display = "block";
  
  container.appendChild(link);
});
}