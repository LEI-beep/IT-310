from flask import Flask, request, render_template_string
import feedparser
from bs4 import BeautifulSoup

app = Flask(__name__)

rss_feeds = {
    'PhilNews': {'url': 'https://philnews.ph/feed/'},
    'Interaksyon': {'url': 'https://interaksyon.philstar.com/feed/'},
    'Abante Tonite': {'url': 'https://tonite.abante.com.ph/feed/'}
}

def clean_html(raw_html):
    return BeautifulSoup(raw_html, "html.parser").get_text()

def extract_image(entry):
    if 'media_content' in entry and entry.media_content:
        return entry.media_content[0]['url']
    return "https://nbhc.ca/sites/default/files/styles/article/public/default_images/news-default-image%402x_0.png?itok=B4jML1jF"  # Larger placeholder image

@app.route("/", methods=["GET", "POST"])
def home():
    query = request.form.get("search", "").strip().lower()
    all_articles = []

    for source, data in rss_feeds.items():
        feed = feedparser.parse(data['url'])
        for entry in feed.entries[:10]:
            summary_clean = clean_html(entry.get("summary", "No summary available"))
            image_url = extract_image(entry)

            all_articles.append({
                "title": entry.title,
                "link": entry.link,
                "summary": summary_clean,
                "source": source,
                "image": image_url
            })

    if request.method == "POST" and query:
        all_articles = [a for a in all_articles if query in a["title"].lower() or query in a["summary"].lower()]

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Philippine News</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { font-family: Arial, sans-serif; }
            .navbar { background-color: #004085; }
            .navbar-brand, .nav-link { color: #ffffff !important; }
            .container { max-width: 1000px; }
            .news-card { border: none; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); transition: transform 0.2s; }
            .news-card:hover { transform: scale(1.02); }
            .article-image { width: 100%; height: 200px; object-fit: cover; border-top-left-radius: 10px; border-top-right-radius: 10px; }
            .headline-card { margin-top: 20px; padding: 10px; background: #f8f9fa; border-radius: 10px; }
            .headline-text { padding: 10px; }
            .navbar-nav { margin-left: auto; }
            .nav-link:hover { color: #ffcc00 !important; }
            .category-nav { font-size: 1.1rem; }
            .footer { background-color: #f1f1f1; padding: 20px 0; text-align: center; }
            .social-links i { font-size: 1.5rem; margin: 0 10px; cursor: pointer; }
        </style>
    </head>
    <body>

        <nav class="navbar navbar-expand-lg navbar-dark">
            <div class="container">
                <a class="navbar-brand fw-bold" href="/">Philippine News</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item">
                            <a class="nav-link" href="#">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">World</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Technology</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Sports</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Entertainment</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Business</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Politics</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container mt-4">
            <h2 class="text-center mb-4">Latest Philippine News</h2>

            <form method="POST" class="mb-4 d-flex">
                <input type="text" name="search" id="search" placeholder="Search news..." class="form-control me-2">
                <button type="submit" class="btn btn-primary">Search</button>
                <a href="/" class="btn btn-secondary ms-2">Clear</a>
            </form>

            {% if all_articles %}
                <div class="headline-card">
                    <img src="{{ all_articles[0].image }}" class="article-image" alt="">
                    <div class="headline-text">
                        <h3><a href="{{ all_articles[0].link }}" target="_blank" class="text-dark">{{ all_articles[0].title }}</a></h3>
                        <p>{{ all_articles[0].summary[:150] }}...</p>
                    </div>
                </div>
                
                <div class="row mt-4">
                    {% for article in all_articles[1:] %}
                        <div class="col-md-6">
                            <div class="card news-card mb-3">
                                <img src="{{ article.image }}" class="article-image" alt="">
                                <div class="card-body">
                                    <h5 class="card-title"><a href="{{ article.link }}" target="_blank" class="text-dark">{{ article.title }}</a></h5>
                                    <p class="card-text">{{ article.summary[:100] }}...</p>
                                    <div class="fw-bold">{{ article.source }}</div>
                                </div>
                            </div>
                        </div>
                    {% endfor %}
                </div>
            {% else %}
                <p class="text-center text-muted">No articles found matching your search.</p>
            {% endif %}
        </div>

        <div class="footer">
            <p>&copy; 2025 Philippine News. All Rights Reserved.</p>
            <div class="social-links">
                <a href="#" target="_blank"><i class="bi bi-facebook"></i></a>
                <a href="#" target="_blank"><i class="bi bi-twitter"></i></a>
                <a href="#" target="_blank"><i class="bi bi-linkedin"></i></a>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """, all_articles=all_articles)

if __name__ == "__main__":
    app.run(port=5000, debug=True)



# pip install flask
# pip install newsparer
#pip install beautifulsoup4