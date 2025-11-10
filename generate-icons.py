import json
import os
import re
from xml.etree import ElementTree as ET

def generate_icon(app_name, template_path, output_path):
    # Read the SVG template
    with open(template_path, 'r') as f:
        svg_content = f.read()
    
    # Replace the placeholder text with the app name
    svg_content = re.sub(
        r'>APP NAME<',
        f'>{app_name.upper()}<',
        svg_content
    )
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Write the modified SVG
    with open(output_path, 'w') as f:
        f.write(svg_content)

def update_apps_json(apps_json_path):
    # Read the apps.json file
    with open(apps_json_path, 'r') as f:
        data = json.load(f)
    
    # Update icon paths for each app
    for app in data['apps']:
        app_id = app['id']
        app['icon'] = f'assets/icons/{app_id}.svg'
    
    # Write the updated JSON back
    with open(apps_json_path, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(base_dir, 'logo-template.svg')
    apps_json_path = os.path.join(base_dir, 'data', 'apps.json')
    
    # Read the apps data
    with open(apps_json_path, 'r') as f:
        data = json.load(f)
    
    # Generate icons for each app
    for app in data['apps']:
        output_path = os.path.join(base_dir, 'assets', 'icons', f"{app['id']}.svg")
        generate_icon(app['name'], template_path, output_path)
    
    # Update the apps.json with new icon paths
    update_apps_json(apps_json_path)

if __name__ == '__main__':
    main()