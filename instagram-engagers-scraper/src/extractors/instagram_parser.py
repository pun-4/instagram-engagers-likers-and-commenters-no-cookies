thonimport requests
from bs4 import BeautifulSoup

class InstagramParser:
    def __init__(self, input_data):
        self.input_data = input_data
    
    def parse_comments(self):
        comments_data = []
        for post_url in self.input_data['posts']:
            try:
                response = requests.get(post_url)
                soup = BeautifulSoup(response.content, 'html.parser')
                comments = self._extract_comments(soup)
                comments_data.append(comments)
            except Exception as e:
                print(f"Error fetching or parsing {post_url}: {e}")
        return comments_data
    
    def _extract_comments(self, soup):
        comments = []
        for comment in soup.find_all('span', class_='C4VMK'):
            comment_data = {
                "text": comment.get_text(),
                "created_at": "timestamp_here",
                "like_count": 0,  # Placeholder, implement logic to extract likes
                "hashtags": self._extract_hashtags(comment.get_text()),
                "mentions": self._extract_mentions(comment.get_text())
            }
            comments.append(comment_data)
        return comments
    
    def _extract_hashtags(self, text):
        return [word for word in text.split() if word.startswith('#')]
    
    def _extract_mentions(self, text):
        return [word for word in text.split() if word.startswith('@')]