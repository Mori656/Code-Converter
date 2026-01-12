const ta = document.getElementById('code-area');
const preview = document.getElementById('preview');
const previewRaw = document.getElementById("preview-raw");

async function convertMarkdown() {
    const mdContent = ta.value;
    const mdFile = new File([mdContent], "markdown.md", {type: "text/plain"});

    const formData = new FormData();
    formData.append("markdown", mdFile);

    const response = await fetch("/convert", {
        body: formData,
        method: "post"
    });

    const htmlResponse = await response.text();

    preview.innerHTML = htmlResponse;
    previewRaw.textContent = htmlResponse;
}

const convertBtn = document.getElementById("convert-btn");
convertBtn.addEventListener("click", convertMarkdown);

document.getElementById("preview-btn").addEventListener("click", ()=>{
    preview.style.display = "block";
    previewRaw.style.display = "none";
});
document.getElementById("preview-raw-btn").addEventListener("click", ()=>{
    preview.style.display = "none";
    previewRaw.style.display = "block";
});
