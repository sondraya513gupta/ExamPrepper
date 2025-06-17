// Firebase config

// Initialize Firebase

let isSignUp = false;

document.getElementById("toggleLink").addEventListener("click", (e) => {
  e.preventDefault();
  isSignUp = !isSignUp;
  document.getElementById("formTitle").innerText = isSignUp ? "Sign Up" : "Sign In";
  document.getElementById("authBtn").innerHTML = isSignUp
    ? '<i class="fas fa-user-plus"></i> Register'
    : '<i class="fas fa-sign-in-alt"></i> Login';
  document.getElementById("toggleText").innerText = isSignUp
    ? "Already have an account?"
    : "Don't have an account?";
  document.getElementById("toggleLink").innerText = isSignUp ? "Sign In" : "Sign Up";
});

document.getElementById("authForm").addEventListener("submit", (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (isSignUp) {
    createUserWithEmailAndPassword(auth, email, password)
      .then(() => window.location.href = "/home")
      .catch((error) => alert("Sign up failed: " + error.message));
  } else {
    signInWithEmailAndPassword(auth, email, password)
      .then(() => window.location.href = "/home")
      .catch((error) => alert("Login failed: " + error.message));
  }
});
