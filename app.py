from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Nick's Docker Portfolio</h1>
    <p>Built with Python, Flask, and Docker.</p>

    <h2>Pages</h2>
    <ul>
        <li><a href="/about">About Nick</a></li>
        <li><a href="/resume">Resume</a></li>
        <li><a href="/skills">Cybersecurity Skills</a></li>
        <li><a href="/projects">Projects</a></li>
    </ul>
    """

@app.route("/about")
def about():
    return """
    <h1>About Nick</h1>
    <p>English teacher transitioning into cybersecurity.</p>
    <p>Currently learning Docker, Linux, Python, Azure, Sentinel, and KQL.</p>
    <p><a href="/">Back Home</a></p>
    """

@app.route("/resume")
def resume():
    return """
    <h1>Future SOC Analyst</h1>
    <p>Hands-on learner building practical cybersecurity and cloud projects.</p>
    <p>Current focus: Docker, Flask, Azure, Microsoft Sentinel, KQL, and Linux.</p>
    <p><a href="/">Back Home</a></p>
    """

@app.route("/skills")
def skills():
    return """
    <h1>Cybersecurity Skills</h1>
    <ul>
        <li>Docker containers and images</li>
        <li>Python and Flask</li>
        <li>Linux basics</li>
        <li>Azure virtual machines</li>
        <li>Microsoft Sentinel and KQL</li>
        <li>Git and GitHub</li>
    </ul>
    <p><a href="/">Back Home</a></p>
    """

@app.route("/projects")
def projects():
    return """
    <h1>Projects</h1>

    <h2>CloudCover</h2>
    <p>Visualizes top attacking IPs from Microsoft Sentinel KQL output.</p>

    <p><a href="/">Back Home</a></p>
    """



app.run(host="0.0.0.0", port=5000)