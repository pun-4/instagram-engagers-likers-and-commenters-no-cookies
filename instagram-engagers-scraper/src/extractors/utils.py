thondef clean_text(text):
    """Cleans and sanitizes text data."""
    return text.strip()

def format_hashtags(hashtags):
    """Formats hashtags into a list."""
    return [hashtag.strip('#') for hashtag in hashtags]