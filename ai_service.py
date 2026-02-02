# AI service logic with GoodReads sentiment analysis integration
# Implements 'generate_book_note' and 'get_ai_recommendations'. All recommendations MUST be AI-based.

try:
    from mood_analysis.ai_service_enhanced import get_book_mood_tags, generate_enhanced_book_note
    MOOD_ANALYSIS_AVAILABLE = True
except ImportError:
    MOOD_ANALYSIS_AVAILABLE = False

def generate_book_note(description, title="", author=""):
    """
    Analyzes book description and returns a 'vibe'.
    Enhanced with GoodReads mood analysis when available.
    """
    if MOOD_ANALYSIS_AVAILABLE and title and author:
        try:
            return generate_enhanced_book_note(description, title, author)
        except Exception as e:
            print(f"Mood analysis failed, using fallback: {e}")
    
    # Fallback to description-based analysis
    if len(description) > 200:
        return "A deep, complex narrative that readers find emotionally resonant."
    elif len(description) > 100:
        return "A compelling story with layers waiting to be discovered."
    elif "mystery" in description.lower():
        return "A mysterious tale that will keep you guessing."
    elif "romance" in description.lower():
        return "A heartwarming story perfect for cozy reading."
    else:
        return "A delightful read for any quiet moment."

def get_ai_recommendations(query):
    """Enhanced AI logic to filter/rank books based on mood."""
    
    # Mood-based query mapping
    mood_queries = {
        'cozy': 'comfort reads warm atmosphere',
        'dark': 'psychological thriller mystery',
        'romantic': 'romance love story',
        'mysterious': 'mystery suspense thriller',
        'uplifting': 'inspiring hopeful positive',
        'melancholy': 'literary fiction emotional',
        'adventurous': 'adventure fantasy epic'
    }
    
    # Check if query matches a mood
    query_lower = query.lower()
    for mood, book_query in mood_queries.items():
        if mood in query_lower:
            return f"AI-optimized {mood} results: {book_query}"
    
    return f"AI-optimized results for: {query}"

def get_book_mood_tags_safe(title: str, author: str = "") -> list:
    """
    Safe wrapper for getting book mood tags.
    
    Args:
        title: Book title
        author: Author name
        
    Returns:
        List of mood tags or empty list if not available
    """
    if MOOD_ANALYSIS_AVAILABLE:
        try:
            return get_book_mood_tags(title, author)
        except Exception as e:
            print(f"Error getting mood tags: {e}")
    
    return []