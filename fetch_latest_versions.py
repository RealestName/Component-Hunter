import requests
from bs4 import BeautifulSoup
import re
import json

GITHUB_FILE_PATH = "script.txt"

# Flask setup
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def run_flask():
    """Function to run the Flask app."""
    app.run(host='0.0.0.0', port=4000)  # Required for Render's web services

# List of libraries and their respective changelog URLs
library_changelogs = {
    "Next.js": "https://nextjs.org/docs/upgrading",
    "Angular": "https://github.com/angular/angular/releases",
    "React": "https://react.dev/versions",
    "Vue.js": "https://github.com/vuejs/vue/releases",
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

# get the current content of the file from github
def get_github_file_content():
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

# update the file on GitHub
def update_github_file(file_content, new_versions):
    # regex to match the `latestVersions` JSON object
    version_regex = r"const latestVersions = \{.*?\};"

    # create the new versions JSON
    new_versions_json = json.dumps(new_versions, indent=4)

    # replace the old `latestVersions` JSON with the new one
    updated_content = re.sub(version_regex, f"const latestVersions = {new_versions_json};", file_content, flags=re.DOTALL)

    # get the sha of the file to update it
    file_sha = file_content['sha']
    update_url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
    
    update_data = {
        "message": "Update versions in script.txt",
        "content": updated_content.encode("utf-8").decode("utf-8"),
        "sha": file_sha,
    }

    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.put(update_url, headers=headers, json=update_data)
    response.raise_for_status()

    print("GitHub file updated successfully with new versions.")

