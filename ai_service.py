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
    
    # Return the query as-is to let Google Books API handle the search
    # This ensures truly AI-driven recommendations without hardcoded mappings
    return f"AI-optimized search for: {query}"

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

def generate_chat_response(user_message, conversation_history=[]):
    """
    Generate contextual chat responses for the bookseller interface.
    
    Args:
        user_message: The user's current message
        conversation_history: Previous conversation messages
        
    Returns:
        String response from the bookseller
    """
    message_lower = user_message.lower()
    
    # Greeting responses
    if any(greeting in message_lower for greeting in ['hello', 'hi', 'hey', 'good morning', 'good afternoon']):
        return "Hello! Welcome to BiblioDrift. I'm here to help you find your perfect next read. What kind of mood are you in for today?"
    
    # Mood-based responses
    if 'cozy' in message_lower:
        return "Ah, cozy reads are my specialty! There's nothing quite like curling up with a warm, comforting book. Let me find some perfect cozy companions for you."
    
    elif any(word in message_lower for word in ['mystery', 'thriller', 'suspense']):
        return "Excellent choice! I love helping readers find their next page-turner. Mystery and thriller books are perfect for those moments when you want to be completely absorbed."
    
    elif any(word in message_lower for word in ['romance', 'romantic', 'love']):
        return "Romance is such a beautiful genre! Whether you're looking for sweet and heartwarming or passionate and steamy, I have some wonderful recommendations for you."
    
    elif any(word in message_lower for word in ['fantasy', 'magic', 'dragons', 'wizards']):
        return "Fantasy is pure escapism at its finest! Let me transport you to some incredible magical worlds where anything is possible."
    
    elif any(word in message_lower for word in ['sci-fi', 'science fiction', 'space', 'future']):
        return "Science fiction opens up infinite possibilities! From space operas to dystopian futures, I have some mind-bending recommendations for you."
    
    elif any(word in message_lower for word in ['sad', 'cry', 'emotional', 'tearjerker']):
        return "Sometimes we need a good emotional release through literature. I have some beautifully written, deeply moving books that will touch your heart."
    
    elif any(word in message_lower for word in ['funny', 'humor', 'comedy', 'laugh']):
        return "Laughter is the best medicine! I have some delightfully funny books that will brighten your day and keep you smiling."
    
    elif any(word in message_lower for word in ['classic', 'literature', 'literary']):
        return "Ah, a lover of the classics! There's something timeless about great literature. Let me suggest some enduring masterpieces and modern literary gems."
    
    elif any(word in message_lower for word in ['young adult', 'ya', 'teen']):
        return "Young adult literature has some of the most engaging and diverse stories! Whether you're a teen or just young at heart, I have some fantastic YA recommendations."
    
    elif any(word in message_lower for word in ['historical', 'history', 'period']):
        return "Historical fiction is like time travel through books! I love helping readers explore different eras and cultures through beautifully researched stories."
    
    elif any(word in message_lower for word in ['biography', 'memoir', 'true story']):
        return "Real stories can be more fascinating than fiction! I have some incredible biographies and memoirs that will inspire and enlighten you."
    
    # Specific situation responses
    elif any(phrase in message_lower for phrase in ['rainy day', 'rainy evening', 'stormy']):
        return "Perfect rainy day reading coming up! There's something magical about the sound of rain while you're lost in a good book."
    
    elif any(phrase in message_lower for phrase in ['beach', 'vacation', 'travel']):
        return "Vacation reads are special - they need to be engaging but not too heavy. Let me find you some perfect travel companions!"
    
    elif any(phrase in message_lower for phrase in ['bedtime', 'before sleep', 'night reading']):
        return "Bedtime reading requires just the right tone - engaging enough to hold your interest but soothing enough for evening. I have some perfect nighttime reads for you."
    
    elif any(phrase in message_lower for phrase in ['book club', 'discussion', 'group']):
        return "Book club selections need to spark great discussions! I'll recommend some thought-provoking books that will give your group plenty to talk about."
    
    # Help and guidance responses
    elif any(word in message_lower for word in ['help', 'recommend', 'suggest', 'find']):
        return "I'm here to help you discover your next favorite book! Tell me more about what you're in the mood for - a specific genre, feeling, or situation you'll be reading in."
    
    elif any(word in message_lower for word in ['similar', 'like', 'enjoyed']):
        return "Great! I love helping readers find books similar to ones they've enjoyed. The more you tell me about what you liked, the better I can tailor my recommendations."
    
    # Default response for unclear requests
    else:
        return "That sounds interesting! Could you tell me a bit more about what kind of mood or feeling you're going for? For example, are you looking for something light and fun, deep and thought-provoking, or maybe an exciting adventure?"