from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🚀 Welcome to Karan's Flask App</h1>
    <p>This application is running inside Docker.</p>
    """

@app.route('/about')
def about():
    return """
    <h2>About Me</h2>
    <p>Learning Python, Linux, Docker and DevOps.</p>
    """

@app.route('/skills')
def skills():
    return """
    <h2>Skills Learned</h2>
    <ul>
        <li>Linux</li>
        <li>Bash Scripting</li>
        <li>Git & GitHub</li>
        <li>Python</li>
        <li>Docker</li>
    </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
