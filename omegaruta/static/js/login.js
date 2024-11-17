document.addEventListener("DOMContentLoaded", () => {
    const loginButton = document.querySelector(".login-button");
    loginButton.addEventListener("click", () => {
        loginButton.textContent = "Cargando...";
        loginButton.disabled = true;
    });
});
