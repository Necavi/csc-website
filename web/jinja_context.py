from . import app

from pprint import pprint


pages = [("Home", "index"), ("Projects", "list_projects"), ("Events", "list_events"), ("Members", "list_members"),
         ("Resources", "resources"), ("Contact", "contact"), ("About", "about")]


@app.context_processor
def context():
    return {
        "pages": pages,
        "pprint": pprint,
        "current_page": "Home"
    }
