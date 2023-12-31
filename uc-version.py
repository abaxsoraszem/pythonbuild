import requests
import re

# Download webpage content
response = requests.get('https://releases.usercentrics.com/loadMoreNews?app_id=nGxJmmsl20682&role=cmpv1%3Bcmpv2%3B&language=EN&user_id=70bb2f11-095e-415d-9712-2cf59a885f98&lastname=Cat&firstname=Blue&category=browser%20ui&publicPage=true&post=false&basePath=%2F%2Freleases.usercentrics.com%2Fen&standaloneLogoUrl=https%3A%2F%2Fstatic.getbeamer.com%2FnGxJmmsl20682%2Flogo_3269.png')
html_content = response.text

# Count the number of lines in the HTML file
num_lines = len(html_content.split('\n'))
print("Number of lines:", num_lines)

# Parse version from HTML body using regex
# version_pattern = r'\b\d+\.d+\.d+\b'
version_pattern = r'Version (\d+\.\d+\.\d+)'

version_match = re.search(version_pattern, html_content)
if version_match:
    version = version_match.group(1)
    version = version.replace("Version ", "")  # Remove the "Version " prefix
    print("Version:", version)
else:
    print("Version not found.")
