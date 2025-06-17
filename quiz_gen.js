document.getElementById("generate-quiz-btn").addEventListener("click", async () => {
  window.scrollTo({ top: 0, behavior: "smooth" });

  const topic = document.getElementById("quiz-input").value.trim();
  const quizContainer = document.getElementById("quiz-container");
  quizContainer.innerHTML = "Generating quiz...";

  const response = await fetch("/generater_quiz", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({topic})
  });

  const data = await response.json();

  if (!data.quiz || !data.quiz.questions) {
      quizContainer.innerHTML = "No quiz generated. Try again.";
      return;
  }

  quizContainer.innerHTML = `<h2>${data.quiz.title}</h2>`;
  data.quiz.questions.forEach((q, i) => {
      const qDiv = document.createElement("div");
      qDiv.className = "question-block";
      qDiv.innerHTML = `
          <p><strong>Q${i + 1}:</strong> ${q.question}</p>
          ${Object.entries(q.options).map(
              ([key, val]) => `<button class="option" data-correct="${q.correct_answer}" data-selected="${key}">${key}. ${val}</button>`
          ).join("<br>")}
          <p class="result"></p>
      `;
      quizContainer.appendChild(qDiv);
  });

  document.querySelectorAll(".option").forEach(btn => {
      btn.addEventListener("click", function () {
          const selected = this.getAttribute("data-selected");
          const correct = this.getAttribute("data-correct");
          const resultP = this.parentElement.querySelector(".result");

          if (selected === correct) {
              resultP.textContent = "✅ Correct!";
              resultP.style.color = "white";
          } else {
              resultP.textContent = `❌ Incorrect. Correct answer is ${correct}.`;
              resultP.style.color = "white";
          }
      });
  });
});
