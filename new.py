import feedparser
from flask import Flask

app = Flask(__name__)

# Updated News RSS Feeds
rss_feeds = {
    'philnews': 'https://philnews.ph/feed/',
    'interaksyon': 'https://interaksyon.philstar.com/feed/',
    'abante_tonite': 'https://tonite.abante.com.ph/feed/'
}

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Philippine News</title>
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
        <!-- Font Awesome Icons -->
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f8f9fa; /* Light gray background */
                padding: 20px;
                font-family: Arial, sans-serif;
            }
            .navbar {
                margin-bottom: 20px;
                background-color: #007bff; /* Blue navbar */
            }
            .navbar-brand, .nav-link {
                color: white !important; /* White text for navbar */
            }
            .nav-link:hover {
                color: #ffcc00 !important; /* Yellow hover effect */
            }
            .footer {
                margin-top: 40px;
                text-align: center;
                color: #6c757d;
            }
            .card {
                transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
            }
            .card:hover {
                transform: scale(1.05); /* Slight zoom on hover */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Shadow effect */
            }
            .btn-primary {
                background-color: #007bff; /* Blue button */
                border: none;
            }
            .btn-primary:hover {
                background-color: #0056b3; /* Darker blue on hover */
            }
            .btn-secondary {
                background-color: #6c757d; /* Gray button */
                border: none;
            }
            .btn-secondary:hover {
                background-color: #495057; /* Darker gray on hover */
            }
            .card-title a {
                color: #007bff; /* Blue link for article titles */
                text-decoration: none;
            }
            .card-title a:hover {
                color: #ffcc00; /* Yellow hover effect for links */
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <!-- Navbar -->
        <nav class="navbar navbar-expand-lg navbar-light">
            <div class="container-fluid">
                <a class="navbar-brand" href="/">
                    <i class="fas fa-newspaper"></i> Philippine News
                </a>
                <div class="collapse navbar-collapse">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item"><a class="nav-link" href="/philnews">PhilNews</a></li>
                        <li class="nav-item"><a class="nav-link" href="/interaksyon">Interaksyon</a></li>
                        <li class="nav-item"><a class="nav-link" href="/abante_tonite">Abante Tonite</a></li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- Main Content -->
        <div class="container">
            <h1>Welcome to Philippine News</h1>
            <p>Stay updated with the latest headlines from top Philippine news outlets.</p>
            <div class="row">
                <div class="col-md-4">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title"><i class="fas fa-globe-asia"></i> PhilNews</h5>
                            <p class="card-text">Get the latest news from PhilNews.</p>
                            <a href="/philnews" class="btn btn-primary">View Headlines</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title"><i class="fas fa-bullhorn"></i> Interaksyon</h5>
                            <p class="card-text">Stay informed with Interaksyon's updates.</p>
                            <a href="/interaksyon" class="btn btn-primary">View Headlines</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title"><i class="fas fa-newspaper"></i> Abante Tonite</h5>
                            <p class="card-text">Read the latest stories from Abante Tonite.</p>
                            <a href="/abante_tonite" class="btn btn-primary">View Headlines</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <footer class="footer">
            <div class="container">
                <p>&copy; 2023 Philippine News. All rights reserved.</p>
            </div>
        </footer>
    </body>
    </html>
    """

@app.route("/philnews")
def philnews_news():
    return get_news('philnews')

@app.route("/interaksyon")
def interaksyon_news():
    return get_news('interaksyon')

@app.route("/abante_tonite")
def abante_tonite_news():
    return get_news('abante_tonite')

def get_news(publication):
    feed = feedparser.parse(rss_feeds[publication])
    if not feed.entries:
        return f"""
        <html>
        <head>
            <title>{publication.replace('_', ' ').title()} - No News</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" rel="stylesheet">
            <style>
                body {{
                    background-color: #f8f9fa;
                    padding: 20px;
                    font-family: Arial, sans-serif;
                }}
                .navbar {{
                    margin-bottom: 20px;
                    background-color: #007bff;
                }}
                .navbar-brand, .nav-link {{
                    color: white !important;
                }}
                .nav-link:hover {{
                    color: #ffcc00 !important;
                }}
                .btn-secondary {{
                    background-color: #6c757d;
                    border: none;
                }}
                .btn-secondary:hover {{
                    background-color: #495057;
                }}
            </style>
        </head>
        <body>
            <nav class="navbar navbar-expand-lg navbar-light">
                <div class="container-fluid">
                    <a class="navbar-brand" href="/">
                        <i class="fas fa-newspaper"></i> Philippine News
                    </a>
                    <div class="collapse navbar-collapse">
                        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                            <li class="nav-item"><a class="nav-link" href="/philnews">PhilNews</a></li>
                            <li class="nav-item"><a class="nav-link" href="/interaksyon">Interaksyon</a></li>
                            <li class="nav-item"><a class="nav-link" href="/abante_tonite">Abante Tonite</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
            <div class="container">
                <h1>No news available for {publication.replace('_', ' ').title()}</h1>
                <a href="/" class="btn btn-secondary">Back to Home</a>
            </div>
        </body>
        </html>
        """
    
    articles = ""
    for entry in feed.entries[:5]:  # Display the top 5 news articles
        articles += f"""
        <div class="card news-card">
            <div class="card-body">
                <h3 class="card-title"><a href="{entry.link}" target="_blank">{entry.title}</a></h3>
                <p class="card-subtitle mb-2 text-muted"><i class="far fa-clock"></i> {entry.get('published', 'No publication date')}</p>
                <p class="card-text">{entry.get('summary', 'No summary available')}</p>
            </div>
        </div>
        """
    
    return f"""
    <html>
    <head>
        <title>{publication.replace('_', ' ').title()} Headlines</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" rel="stylesheet">
        <style>
            body {{
                background-color: #f8f9fa;
                padding: 20px;
                font-family: Arial, sans-serif;
            }}
            .navbar {{
                margin-bottom: 20px;
                background-color: #007bff;
            }}
            .navbar-brand, .nav-link {{
                color: white !important;
            }}
            .nav-link:hover {{
                color: #ffcc00 !important;
            }}
            .card {{
                transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
            }}
            .card:hover {{
                transform: scale(1.05);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }}
            .btn-secondary {{
                background-color: #6c757d;
                border: none;
            }}
            .btn-secondary:hover {{
                background-color: #495057;
            }}
            .card-title a {{
                color: #007bff;
                text-decoration: none;
            }}
            .card-title a:hover {{
                color: #ffcc00;
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light">
            <div class="container-fluid">
                <a class="navbar-brand" href="/">
                    <i class="fas fa-newspaper"></i> Philippine News
                </a>
                <div class="collapse navbar-collapse">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item"><a class="nav-link" href="/philnews">PhilNews</a></li>
                        <li class="nav-item"><a class="nav-link" href="/interaksyon">Interaksyon</a></li>
                        <li class="nav-item"><a class="nav-link" href="/abante_tonite">Abante Tonite</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="container">
            <h1>{publication.replace('_', ' ').title()} Headlines</h1>
            {articles}
            <a href="/" class="btn btn-secondary">Back to Home</a>
        </div>
        <footer class="footer">
            <div class="container">
                <p>&copy; 2023 Philippine News. All rights reserved.</p>
            </div>
        </footer>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(port=5000, debug=True)