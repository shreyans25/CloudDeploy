from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>CloudDeploy Demo</title>
      <style>
        body{font-family:Arial,sans-serif;margin:0;background:#f3f7fb;color:#183044}
        header{background:linear-gradient(120deg,#12304a,#087e8b);color:white;padding:64px 9%}
        h1{font-size:clamp(2rem,5vw,3.6rem);margin:0 0 14px}
        p{line-height:1.6}.wrap{max-width:1000px;margin:35px auto;padding:0 20px}
        .cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px}
        .card{background:white;border-radius:14px;padding:22px;box-shadow:0 6px 22px #18304412}
        .tag{display:inline-block;background:#d7f4ed;color:#087e70;padding:6px 10px;border-radius:20px}
      </style>
    </head>
    <body>
      <header><span class="tag">CI/CD • Containers • Cloud</span>
        <h1>CloudDeploy</h1>
        <p>A demo web app deployed through an automated cloud deployment pipeline.</p>
      </header>
      <main class="wrap">
        <h2>Deployment pipeline</h2>
        <div class="cards">
          <div class="card"><h3>1. Commit</h3><p>Code is pushed to the GitHub repository.</p></div>
          <div class="card"><h3>2. Build</h3><p>GitHub Actions builds and checks the application.</p></div>
          <div class="card"><h3>3. Containerize</h3><p>Docker packages the app and its dependencies.</p></div>
          <div class="card"><h3>4. Deploy</h3><p>The package is deployed to a cloud platform.</p></div>
        </div>
        <p>Health endpoint: <a href="/health">/health</a></p>
      </main>
    </body></html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy", app="CloudDeploy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
