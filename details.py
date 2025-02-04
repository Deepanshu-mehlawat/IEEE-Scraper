import requests
from bs4 import BeautifulSoup
import re,json

def details(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
    }
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.content, 'html.parser')



    script_tag = soup.find("script", string=re.compile(r"xplGlobal\.document\.metadata"))

    if script_tag:
        # Extract the JavaScript code as text
        script_content = script_tag.string

        # Use regex to extract the metadata JSON string
        metadata_match = re.search(r"xplGlobal\.document\.metadata\s*=\s*(\{.*?\});", script_content, re.DOTALL)

        if metadata_match:
            # Get the JSON string
            metadata_json = metadata_match.group(1)

            # Parse the JSON string into a Python dictionary
            metadata = json.loads(metadata_json)
            #print("Extracted Metadata:", metadata)
        else:
            print("Metadata not found in the script")
    else:
        print("Script tag containing metadata not found")

    extracted_data = {
    "Title": metadata.get("title"),
    "Authors": [author["name"] for author in metadata.get("authors", [])],
    "Abstract": metadata.get("abstract"),
    "Keywords": [kw for keyword_group in metadata.get("keywords", []) for kw in keyword_group.get("kwd", [])],
    "No. of Cites": metadata.get("citationCount", metadata.get("metrics", {}).get("citationCountPaper", 0)),
    "Views": metadata.get("metrics", {}).get("totalDownloads", 0)
    }

    return extracted_data

if __name__ == "__main__":
    print(details("https://ieeexplore.ieee.org/document/8932614/"))
