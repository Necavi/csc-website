from flask import render_template, send_from_directory

from .models import Project
from . import app


@app.route("/")
def index():
    secondary_pages = [
            ["News",  "#top-news"],
            ["Join the Club", "#join"],
            ["Top Projects", "#project-spotlight"],
            ["Recent Events", "#"]
        ]
    return render_template("index.html", secondary_pages=secondary_pages, projects=Project.query.all())


@app.route("/projects/<project>")
def view_project(project):
    return ""


@app.route("/projects")
def list_projects():
    projects = Project.query.all()
    list_of_projects = {
        "top": projects[0:2],
        "secondary": projects[2:5],
        "archived": projects[5:]
    }
    return render_template("projects.html", current_page="Projects", list_of_projects=list_of_projects)


@app.route("/member/<member>")
def view_member(member):
    return ""


@app.route("/members")
def list_members():
    return ""


@app.route("/contact")
def contact():
    return render_template("contact.html", current_page="Contact")


@app.route("/events")
def list_events():
    return ""


@app.route("/events2")
def events():
    return ""


@app.route("/about")
def about():
    content = [
        {
            "header": "What we do",
            "body": "The Computer Science Club has brought many projects back to life like our new website or the srjc "
                    "scheduler by adding new features and capabilities as well as welcoming new projects based on the "
                    "interest from the club members. To make our projects grow and flourish, we strive on making "
                    "ourselves known by posting flyers with QR Codes to our website, which Snapchat can scan; we "
                    "schedule workshops to meet up about a specific project and get things done!",
            "image": "http://placehold.it/350x200"
        }, {
            "header": "What is the scope of this club",
            "body": "We welcome all project types such as web development, graphic design work, electrical/hardware "
                    "engineering, custom software design, artificial intelligence and any idea or concept that "
                    "includes collaborating code or assets such as code snippets, graphics and hardware parts. The "
                    "club wants to take part in achieving any idea from all skill levels ranging from beginning to "
                    "expert!",
            "image": "http://placehold.it/350x200"
        }, {
            "header": "Our philosophy",
            "body": "The club exposes members to begin their journey new tools and share a common convention that is "
                    "used in the real world. Currently, the club is working on taking memebers to local events and "
                    "tours to larger companies!",
            "image": "/static/images/about-3.jpg"
        }
    ]
    return render_template("about.html", current_page="About", content=content)


@app.route("/resources")
def resources():
    return render_template("resources.html", current_page="Resources")


@app.route("/resources/tutorials")
def list_tutorial_categories():
    return render_template("tutorial_categories.html")


@app.route("/resources/tutorials/<int:id>")
def get_tutorial_category(id):
    return ""


@app.route("/static/<path:path>")
def mystatic(path):
    return send_from_directory("static", path)


