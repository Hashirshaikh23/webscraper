from flask import Flask, render_template, request, send_file
import uuid
import os
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        urls = request.form.get("urls")
        if not urls:
            return "No URLs provided", 400

        with open("urls.txt", "w") as f:
            f.write(urls)

        # Generate a unique filename for each scraping session
        result_filename = f"result_{uuid.uuid4().hex}.json"
        subprocess.run(["python", "main.py", "--urls", "urls.txt", "--output", "json"])

        # Move result to uniquely named file
        os.rename("output/result.json", result_filename)

        return send_file(result_filename, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
