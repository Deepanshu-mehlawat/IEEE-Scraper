# IEEE Scraper API

## 📚 Overview
IEEE Scraper API is a Flask-based web service that allows users to search for academic papers from IEEE Xplore, retrieve metadata details for individual papers, and perform full scraping workflows. This project is ideal for researchers and developers who want to programmatically access paper details and build datasets.

## 🚀 Features
- **Search Papers**: Find papers using a search term.
- **Get Paper Details**: Retrieve metadata such as title, authors, abstract, keywords, citations, and views.
- **Full Scraping Process**: Search for papers and retrieve details for each paper in one step.

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.7+
- Git (for cloning the repository)
- Virtual Environment (optional but recommended)

### Installation
1. **Clone the Repository**
    ```bash
    git clone https://github.com/Deepanshu-mehlawat/IEEE-Scraper.git
    cd IEEE-Scraper
    ```

2. **Create and Activate a Virtual Environment (Optional)**
    ```bash
    python -m venv venv
    # Activate on Windows
    .\venv\Scripts\activate
    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3. **Install Required Packages**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Server
Start the Flask server:
```bash
python scraper.py
```
The server will run on http://127.0.0.1:5000/ .

## 📡 API Endpoints
following are all the APIs that will be running on your localhost.

### 🔎Search API
Used to get links of the top 25 papers from IEEE from last 5 years, sorted by citation count.

**ENDPOINT**: `POST http:/127.0.0.1:5000/search`

**PAYLOAD**: 
```html
{
"search_term":"xyz"
}
```

**OUTPUT FORMAT**:
```
{
    "message": "Search completed",
    "urls": [
        "https://ieeexplore.ieee.org/document/123456/",
        "https://ieeexplore.ieee.org/document/789012/"
    ]
}
```

### 📃 Details API
Used to get the details of a paper given the IEEE paper link.

**ENDPOINT**: `POST http:/127.0.0.1:5000/details`

**PAYLOAD**: 
```html
{
"url":"https://ieeexplore.ieee.org/document/paper-id/"
}
```

**OUTPUT FORMAT**:
```
{
    "message": "Details fetched",
    "data": {
        "Title": "Deep Learning for Image Processing",
        "Authors": ["Author A", "Author B"],
        "Abstract": "This paper explores deep learning for image processing...",
        "Keywords": ["Deep Learning", "Computer Vision"],
        "No. of Cites": 15,
        "Views": 350
    }
}
```

### 💯 Scraper API
Used to get the details of the 25 papers given search API.

**ENDPOINT**: `POST http:/127.0.0.1:5000/scrape`

**PAYLOAD**: 
```html
{
"search_term":"Machine Learning"
}
```

**OUTPUT FORMAT**:
```
{
    "message": "Scraping completed",
    "data": [
        {
            "Title": "Deep Learning for Image Processing",
            "Authors": ["Author A", "Author B"],
            "Abstract": "This paper explores deep learning for image processing...",
            "Keywords": ["Deep Learning", "Computer Vision"],
            "No. of Cites": 15,
            "Views": 350
        },
        {
            "Title": "Neural Networks in NLP",
            "Authors": ["Author C"],
            "Abstract": "Using neural networks in NLP...",
            "Keywords": ["NLP", "Neural Networks"],
            "No. of Cites": 10,
            "Views": 220
        }
    ]
}

```
