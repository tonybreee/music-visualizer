document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("file");
    const submitButton = document.getElementById("generate");

    fileInput.addEventListener("change", function () {
        if (fileInput.files.length > 0) {
            submitButton.disabled = false;
        }
    });
});
