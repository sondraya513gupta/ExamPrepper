// Navigate to tool page
function navigateTo(page) {
  window.location.href = `/${page}`;
}

// Toggle dark/light mode
document.getElementById("mode-toggle").addEventListener("click", function () {
  document.body.classList.toggle("dark-mode");
});

