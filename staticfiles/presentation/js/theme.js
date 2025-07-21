
document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("theme-toggle");
    const currentTheme = localStorage.getItem("theme") || "light";

    // Appliquer le thème sauvegardé
    document.documentElement.setAttribute("data-theme", currentTheme);
    updateButtonText(currentTheme);

    toggleButton.addEventListener("click", function () {
        const newTheme = document.documentElement.getAttribute("data-theme") === "light" ? "dark" : "light";
        document.documentElement.setAttribute("data-theme", newTheme);
        localStorage.setItem("theme", newTheme);
        updateButtonText(newTheme);
    });

    function updateButtonText(theme) {
        toggleButton.textContent = theme === "light" ? "🌙 Mode Sombre" : "☀️ Mode Clair";
    }
});
