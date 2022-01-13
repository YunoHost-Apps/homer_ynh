#!/usr/bin/env python3

from pathlib import Path
import json
import yaml
import subprocess
import requests
from jinja2 import Environment, BaseLoader

page_template = '''
---
title: "Yunohost apps"
subtitle: "App dashboard"
logo: false
# icon: "fas fa-skull-crossbones" Optional icon

header: true
# Optional theme customization
theme: default
colors:
  light:
    highlight-primary: "#3367d6"
    highlight-secondary: "#4285f4"
    highlight-hover: "#5a95f5"
    background: "#f5f5f5"
    card-background: "#ffffff"
    text: "#363636"
    text-header: "#ffffff"
    text-title: "#303030"
    text-subtitle: "#424242"
    card-shadow: rgba(0, 0, 0, 0.1)
    link-hover: "#363636"
  dark:
    highlight-primary: "#3367d6"
    highlight-secondary: "#4285f4"
    highlight-hover: "#5a95f5"
    background: "#131313"
    card-background: "#2b2b2b"
    text: "#eaeaea"
    text-header: "#ffffff"
    text-title: "#fafafa"
    text-subtitle: "#f5f5f5"
    card-shadow: rgba(0, 0, 0, 0.4)
    link-hover: "#ffdd57"

# Optional navbar
# links: [] # Allows for navbar (dark mode, layout, and search) without any links
links: []

# Services
# First level array represent a group.
# Leave only a "items" key if not using group (group name, icon & tagstyle are optional, section separation will not be displayed).
services:
  - name: Yunohost aplications
    items:
{% for app in apps %}
        {% if app.logo %}
      - name: {{app.label}}
        subtitle: {{app.description}}
        url: {{app.url}}
        logo: {{app.logo}}
        {% endif %}
{% endfor %}
'''


apps_full = None
def get_apps_full():
    global apps_full
    if not apps_full:
        apps_full = json.loads(subprocess.check_output(
            ["yunohost", "app", "list", "--json", "--full"]
        ).decode('utf-8'))["apps"]
    return apps_full

def final_path():
    this_app = Path(__file__).parent.parent.name
    this_app_details = [app for app in get_apps_full() if app["id"] == this_app][0]
    return Path(this_app_details["settings"]["final_path"])

def get_apps():
    apps_full = get_apps_full()
    apps = [
        {
            "label": app["label"],
            "description": app["description"],
            "url": "https://" + app.get("domain_path", ""),
            "id": app["manifest"]["id"],
            "version": app["version"]
        }
        for app in apps_full
    ]

    return apps

def get_logos():
    with open(Path(__file__).parent / "icons.yaml", encoding="utf-8") as file:
        logos = yaml.load(file)["logos"]
    return logos


def get_logo(app_id, output_dir):
    try:
        url = logos[app_id]
        file = output_dir / (app_id + Path(url).suffix)
        if not file.exists():
            imgdata = requests.get(url, allow_redirects=True)
            open(file, 'wb').write(imgdata.content)
        return file
    except KeyError:
        print(f"Logo not found for {app_id}")
        return None


if __name__ == "__main__":
    apps = get_apps()
    logos = get_logos()
    imgs_path = final_path() / 'assets' / 'icons'

    for app in apps:
        logo = get_logo(app["id"], imgs_path)
        if logo:
            app["logo"] = f"assets/icons/{logo.name}"

    template = Environment(loader=BaseLoader).from_string(page_template)

    result = template.render(apps=apps)

    with open(final_path() / 'assets' / 'yunohost_apps.yml', 'w') as out:
        out.write(result)
