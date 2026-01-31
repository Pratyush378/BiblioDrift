# BiblioDrift 📚☕

> **"Find yourself in the pages."**

BiblioDrift is a cozy, visual-first book discovery platform designed to make finding your next read feel like wandering through a warm, quiet bookstore rather than scrolling through a database.

## 🌟 Core Philosophy
- **"Zero UI Noise"**: No popups, no aggressive metrics. Just calm browsing.
- **Tactile Interaction**: 3D books that you can pull from the shelf and flip over.
- **Vibe-First**: Search for feelings ("rainy mystery"), not just keywords.

## 🚀 Features (MVP & Roadmap)
- **Interactive 3D Books**: Hover to pull, click to flip and **expand**.
- **Virtual Library**: Realistic wooden shelves to save your "Want to Read", "Currently Reading", and "Favorites" list (Persistent via LocalStorage).
- **Glassmorphism UI**: A soothing, modern interface that floats above the content.
- **AI-Powered Recommendations** (Planned): All book recommendations must be generated exclusively by AI.  
     No manual curation, static lists, or hardcoded recommendations are permitted.
- **Dynamic Popups**: Click a book to see an expanded view with AI-generated blurbs.
- **Curated Tables**: Horizontal scrolling lists based on moods like "Monsoon Reads".

## 🛠️ Tech Stack
- **Frontend**: Vanilla JavaScript, CSS3 (3D Transforms), HTML5
- **API**: Google Books API (Real-time data)
- **Storage**: LocalStorage (MVP), PostgreSQL (Planned)
- **Backend (Planned)**: Python Flask
- **AI (Planned)**: LLM integration for "Bookseller Notes"

## 🤖 AI Recommendation Policy

BiblioDrift follows a **strict AI-only recommendation model**.

- All recommendations must be generated dynamically using AI/LLMs.
- Manual curation, editor picks, static mood lists, or hardcoded book mappings are **not allowed**.
- AI outputs should be based on abstract signals such as:
  - Vibes
  - Mood descriptors
  - Emotional tone
  - Reader intent

This ensures discovery stays organic, scalable, and aligned with BiblioDrift’s philosophy of vibe-first exploration.

## 📦 Installation & Setup

### Frontend (Current MVP)
1. Clone the repository:
   ```bash
   git clone https://github.com/devanshi14malhotra/bibliodrift.git
   ```
2. Open `index.html` in your browser.
   - That's it! No build steps required for the vanilla frontend.

### Backend (Future)
Planned implementation using Python Flask.

## 🧠 AI Service Integration
To keep the frontend and backend synced, use the following mapping:

| Feature | Frontend Call (`app.js`) | API Endpoint (`app.py`) | Logic Provider (`ai_service.py`) |
| :--- | :--- | :--- | :--- |
| **Book Vibe** | `POST /api/v1/generate-note` | `handle_generate_note()` | `generate_book_note()` |

### API Integration
- **Endpoint**: `POST /api/v1/generate-note`
- **Logic**: Processed by `ai_service.py`

## 🤝 Contributing
We welcome contributions to make BiblioDrift cozier!

1. Fork the repo.
2. Create a feature branch (`e.g. git checkout -b feature/cozy-mode`).
3. Commit your changes.
4. Push and open a Pull Request.

## 📄 License
MIT License.

---
*Built with ☕ and code.*
