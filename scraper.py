from flask import Flask, request, jsonify
import time
import json
from search import search  
from details import details  

app = Flask(__name__)

# API Route for Searching Papers
@app.route('/search', methods=['POST'])
def search_papers():
    try:
        data = request.get_json()
        if not data or 'search_term' not in data:
            return jsonify({"error": "Missing search_term in request"}), 400

        search_term = data['search_term']
        print(f"Received search term: {search_term}")

        # Get paper URLs using the search function
        paper_urls = search(search_term)

        if not paper_urls:
            return jsonify({"error": "No papers found"}), 404

        return jsonify({"message": "Search completed", "urls": paper_urls}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


# API Route for Getting Paper Details
@app.route('/details', methods=['POST'])
def get_paper_details():
    try:
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({"error": "Missing paper URL in request"}), 400

        paper_url = data['url']
        print(f"Fetching details for: {paper_url}")

        # Get details for the paper
        paper_details = details(paper_url)

        if not paper_details:
            return jsonify({"error": "Failed to retrieve details"}), 404

        return jsonify({"message": "Details fetched", "data": paper_details}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


# API Route for Full Scraping Process
@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        data = request.get_json()
        if not data or 'search_term' not in data:
            return jsonify({"error": "Missing search_term in request"}), 400

        search_term = data['search_term']
        print(f"Received search term: {search_term}")

        paper_urls = search(search_term)
        if not paper_urls:
            return jsonify({"error": "No papers found"}), 404
        
        print(f"Found {len(paper_urls)} papers. Fetching details...")

        extracted_data = []
        for idx, url in enumerate(paper_urls, start=1):
            print(f"Processing {idx}/{len(paper_urls)}: {url}")

            paper_details = details(url)
            if paper_details:
                extracted_data.append(paper_details)

            time.sleep(2 + (time.time() % 1))  # Adding delay between requests

        print("Scraping complete. Returning data...")

        return jsonify({"message": "Scraping completed", "data": extracted_data}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
