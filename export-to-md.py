import json
import os
import glob
import frontmatter

EXPORT_TO = "/home/orange/Notes/github"
WANTED = ("html_url", "title", "id", "state")


def create_markdown_file(issue):
    filename = os.path.join(EXPORT_TO, f"{issue['id']}.md")

    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write("")

    issue_selected = {k: v for k, v in issue.items() if k in WANTED}

    with open(filename, 'r') as file:
        existing_content = frontmatter.load(file)
        existing_content.metadata.update(issue_selected)
        new_content = frontmatter.dumps(existing_content)

    with open(filename, 'w') as file:
        file.write(new_content)

def process_json_files():
    json_files = glob.glob("issues-*.json")

    for file in json_files:
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            issues_data = data["items"]

        for issue in issues_data:
            create_markdown_file(issue)

def main():
    process_json_files()

if __name__ == "__main__":
    main()

