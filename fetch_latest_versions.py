import threading
import os
from flask import Flask
import requests
from bs4 import BeautifulSoup
import re
import json
import base64

# Get environment variables
GITHUB_OWNER = os.getenv("GITHUB_OWNER")
GITHUB_REPO = os.getenv("GITHUB_REPO")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

GITHUB_FILE_PATH = "script.txt"

# Flask setup
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def run_flask():
    """Function to run the Flask app on a dynamic port"""
    port = int(os.getenv('PORT', 4000))  # Use the PORT environment variable for Render
    app.run(host='0.0.0.0', port=port)  # Flask will bind to this port

# List of libraries and their respective changelog URLs
library_changelogs = {
    "Next.js": "https://nextjs.org/docs/upgrading",
    "Angular": "https://github.com/angular/angular/releases",
    "React": "https://react.dev/versions",
    "Vue.js": "https://github.com/vuejs/core/blob/main/CHANGELOG.md",
    "Svelte": "https://github.com/sveltejs/svelte/releases",
    "Ember.js": "https://github.com/emberjs/ember.js/blob/main/CHANGELOG.md",
    "Polymer": "https://github.com/Polymer/polymer/releases",
    "ExtJS": "https://docs.sencha.com/extjs/",
    "jQuery": "https://github.com/jquery/jquery/releases",
    "jQuery UI": "https://github.com/jquery/jquery-ui/releases",
    "jQuery UI Touch Punch": "https://www.npmjs.com/package/jquery-ui-touch-punch",
    "jQuery Migrate": "https://github.com/jquery/jquery-migrate/releases",
    "jQuery Mobile": "https://jquerymobile.com/changelog/",
    "Underscore.js": "https://github.com/esamattis/underscore.string/blob/master/CHANGELOG.markdown",
    "Lodash": "https://github.com/lodash/lodash/releases",
    "Moment.js": "https://github.com/moment/moment/blob/develop/CHANGELOG.md",
    "Redux": "https://github.com/reduxjs/redux/releases",
    "Axios": "https://github.com/axios/axios/releases",
    "Bootstrap": "https://github.com/twbs/bootstrap/releases",
    "Materialize": "https://github.com/Dogfalo/materialize/releases",
    "Highcharts": "https://www.highcharts.com/changelog/",
    "Chart.js": "https://github.com/chartjs/Chart.js/releases",
    "D3.js": "https://github.com/d3/d3/releases",
    "DataTables": "https://cdn.datatables.net/releases.html",
    "Toastr": "https://github.com/CodeSeven/toastr/releases",
    "Anime.js": "https://github.com/juliangarnier/anime/releases",
    "Three.js": "https://github.com/mrdoob/three.js/releases",
    "Fabric.js": "https://github.com/fabricjs/fabric.js/releases",
    "PixiJS": "https://github.com/pixijs/pixi.js/releases",
    "Paper.js": "https://github.com/paperjs/paper.js/releases",
    "Modernizr": "https://github.com/Modernizr/Modernizr/releases",
    "Handlebars": "https://github.com/handlebars-lang/handlebars.js/releases",
    "Leaflet": "https://github.com/Leaflet/Leaflet/releases",
    "TensorFlow.js": "https://github.com/tensorflow/tfjs/releases",
    "CKEditor": "https://github.com/ckeditor/ckeditor5/releases"
}

# fetch the latest stable version from changelog page
def fetch_latest_version(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # search for a version number pattern
        version = None
        for text in soup.stripped_strings:
            # look for a version number pattern
            match = re.search(r'(\d+\.\d+\.\d+(?:-[\w\d\.]+)?)\s*(?:\(\d{4}-\d{2}-\d{2}\))?', text)
            if match:
                version = match.group(1) # capture only the version part
                break

        return version
    except Exception as e:
        print(f"Failed to fetch version from {url}: {e}")
        return None

# fetch versions for all libraries and store in a dictionary
library_versions = {}

for library, url in library_changelogs.items():
    print(f"Fetching version for {library} from {url}...")
    version = fetch_latest_version(url)
    if version:
        library_versions[library] = version
    else:
        print(f"Could not fetch version for {library}")

def update_versions():
    """Fetch versions and update GitHub file"""
    library_versions = {}

    for library, url in library_changelogs.items():
        print(f"Fetching version for {library} from {url}...")
        version = fetch_latest_version(url)
        if version:
            library_versions[library] = version
        else:
            print(f"Could not fetch version for {library}")

    file_info = get_github_file_content()
    update_github_file(file_info, library_versions)

def get_github_file_content():
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return {"content": "", "sha": None}  # File doesn't exist yet
    
    response.raise_for_status()
    
    file_data = response.json()
    content = base64.b64decode(file_data["content"]).decode("utf-8")  # Decode the file content
    
    return {"content": content, "sha": file_data["sha"]}  # Return both content and sha


def update_github_file(file_info, new_versions):
    file_content = file_info["content"]
    file_sha = file_info["sha"]

    # Create the new versions JSON
    new_versions_json = json.dumps(new_versions, indent=4)

    # Replace `latestVersions` if it exists, otherwise append
    version_regex = r"const latestVersions = \{.*?\};"
    if re.search(version_regex, file_content, flags=re.DOTALL):
        updated_content = re.sub(version_regex, f"const latestVersions = {new_versions_json};", file_content, flags=re.DOTALL)
    else:
        updated_content = file_content + f"\nconst latestVersions = {new_versions_json};"

    # Encode the updated content in base64
    encoded_content = base64.b64encode(updated_content.encode("utf-8")).decode("utf-8")

    # Prepare the data for the update request
    update_data = {
        "message": "Force update: Updating versions in script.txt",
        "content": encoded_content,
        "sha": file_sha,
        "branch": "main"  # Change to your correct branch
    }

    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    update_url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
    response = requests.put(update_url, headers=headers, json=update_data)

    if response.status_code in [201]:
        print("GitHub file updated successfully with new versions.")
    else:
        print(f"Failed to update GitHub file: {response.status_code}, {response.text}")

def update_every_24_hours():
    """Run the update process every 24 hours"""
    while True:
        print("\n🔄 Running scheduled update...")
        update_versions()
        print("✅ Update complete. Sleeping for 24 hours...\n")
        time.sleep(86400)  # Sleep for 24 hours (24 * 60 * 60)

if __name__ == '__main__':
    file_info = get_github_file_content()
    update_github_file(file_info, library_versions)
    
    # Run Flask in the main thread
    run_flask()
