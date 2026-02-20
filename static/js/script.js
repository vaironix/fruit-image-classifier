// UPDATE THIS URL AFTER DEPLOYING TO RENDER
const API_URL = "https://your-app-name.onrender.com";

function previewImage() {
    const file = document.getElementById("imageInput").files[0];
    const preview = document.getElementById("preview");

    preview.src = URL.createObjectURL(file);
    preview.style.display = "block";
}

function predict() {
    const input = document.getElementById("imageInput");
    const formData = new FormData();
    formData.append("image", input.files[0]);

    fetch(`${API_URL}/predict`, {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            `Predicted Fruit: ${data.result} (${data.confidence}%)`;
    })
    .catch(err => {
        document.getElementById("result").innerText = "Error: " + err.message;
    });
}
