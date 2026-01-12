from flask import Flask, request, Response, render_template
from marktest import markdown_to_html

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/convert", methods=["POST"])
def convert():
    file = request.files.get("markdown")
    if not file:
        return Response("missing file", status=400)
    
    markdown_bytes = file.read()
    markdown = markdown_bytes.decode("utf-8")

    html = markdown_to_html(markdown)

    return Response(html, mimetype="text/html")


if __name__ == "__main__":
    app.run(debug=True)
