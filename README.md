# 🎓 Advanced College Admissions Essay Agent

**An AI-powered platform helping high school students brainstorm, discover their story, and write compelling college essays that get them noticed by top universities.**

## 🌟 Key Features

### 💡 Brainstorming Engine
- Generates 8-10 unique, compelling essay ideas
- Provides hooks, angles, and why each story works
- Tailored for different grade levels

### 🔍 Story Discovery
- Interactive questionnaire to help students find their unique narrative
- AI analysis of background, challenges, achievements, and values
- Identifies core story themes and essay types
- Provides actionable next steps

### ✍️ Essay Generator
- **Multiple Essay Types**: Common App, Why School, Coalition, Supplemental
- **Smart Prompting**: Tailored requirements for each essay type
- **Word Count Tracking**: Ensures essays meet requirements
- **Context-Aware**: Incorporates student profile and goals

### 📊 Deep Essay Analysis
- Admissions-officer-level feedback
- Scores on 6 key dimensions (Hook, Voice, Insight, Technical, Impact)
- Specific strengths and improvement areas
- Overall admissions potential score

### ✨ Intelligent Essay Improvement
- **6 Focused Improvement Options**:
  - 🎣 Better Hook - Open with impact
  - 🎤 Authentic Voice - Sound like a real person
  - ❤️ More Emotion - Add vulnerability
  - 🎯 Add Details - Specific examples
  - ⚡ Better Flow - Improved pacing
  - ✨ Clearer - Crisper writing

### 💾 Draft Management
- Save multiple versions of essays
- Track version history
- Access drafts anytime with student name
- Built-in database (SQLite)

### 📚 Tips & Resources
- College essay writing best practices
- Essay-type-specific guidance
- Common mistakes and how to fix them
- Pro tips from admissions officers

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key (get free $5 credit at https://platform.openai.com)
- Modern web browser

### Installation

**1. Install Dependencies**
```bash
pip install -r requirements.txt
```

**2. Setup Environment**
Create/edit `.env`:
```
OPENAI_API_KEY=sk-your_api_key_here
FLASK_ENV=development
DEBUG=True
```

**3. Run the Server**
```bash
python app.py
```

**4. Open in Browser**
```
http://127.0.0.1:5000
```

## 📖 How to Use

### For Students

#### **Step 1: Brainstorm Ideas** 💡
- Go to "Brainstorm" tab
- Enter a topic you want to write about
- Get 8-10 fresh ideas with hooks and angles
- Pick your favorite and move to next step

#### **Step 2: Discover Your Story** 🔍
- Go to "Story Discovery" tab
- Answer 6 simple questions about yourself
- Get AI analysis of your unique narrative
- Learn which essay types fit your story best

#### **Step 3: Generate Your Essay** ✍️
- Go to "Essay Writer" tab
- Select essay type (Common App, Why School, etc.)
- Fill in your profile information
- Click "Generate Essay"
- Get a polished, ready-to-refine first draft

#### **Step 4: Analyze & Improve** 📊
- Go to "Analyze & Improve" tab
- Paste your essay
- Get deep feedback like an admissions officer would give
- Try different improvement focuses
- Keep refining until it's perfect

#### **Step 5: Save Your Drafts** 💾
- Save versions as you work
- Load drafts anytime with your name
- Keep your best work accessible

#### **Step 6: Learn Best Practices** 📚
- Go to "Tips & Resources" tab
- Read essay-type-specific guidance
- Learn what makes essays stand out
- Avoid the 5 biggest essay killers

## 🎯 API Endpoints

### POST `/brainstorm`
Generate essay ideas
```json
{
  "topic": "overcoming challenge",
  "grade": "12"
}
```

### POST `/discovery-quiz`
Analyze student story
```json
{
  "responses": {
    "background": "...",
    "challenge": "...",
    "achievement": "...",
    "unique": "...",
    "passion": "...",
    "cultural": "..."
  }
}
```

### POST `/generate-essay`
Generate essay in multiple formats
```json
{
  "name": "John Smith",
  "essayType": "common-app",
  "profile": {
    "background": "...",
    "challenge": "...",
    "achievement": "...",
    "unique": "...",
    "goals": "..."
  }
}
```

### POST `/analyze-essay`
Deep essay analysis
```json
{
  "essay": "...",
  "essayType": "common-app"
}
```

### POST `/improve`
Improve specific aspects
```json
{
  "essay": "...",
  "focus": "hook|voice|emotion|specifics|pacing|clarity"
}
```

### POST `/save-draft`
Save essay draft
```json
{
  "studentName": "John Smith",
  "essayType": "common-app",
  "title": "My College Essay",
  "content": "..."
}
```

### GET `/get-drafts/<student_name>`
Retrieve saved drafts

## 📊 Supported Essay Types

| Essay Type | Length | Purpose |
|-----------|--------|---------|
| **Common App** | 650 words | Main application essay |
| **Why School** | 400-500 words | School-specific fit |
| **Coalition** | 650 words | Alternative to Common App |
| **Supplemental** | 250-350 words | School-specific short answer |

## 💡 Writing Tips Summary

### For All Essays
- ✅ Be authentic - your real voice stands out
- ✅ Show, don't tell - use vivid examples
- ✅ Reflect and grow - explain what you learned
- ✅ Stay focused - one story beats five scattered ones
- ✅ Edit ruthlessly - every sentence should matter

### For Common App Essay
- 🎣 Hook them in first 2 sentences
- 🚫 Avoid clichés and overused topics
- 💪 Show vulnerability as strength
- 📊 Use exactly 650 words (not more, not less)
- ❌ Don't list achievements or test scores

### For Why School Essay
- 🔍 Research deeply - mention specific programs and professors
- 🎯 Connect to YOUR goals specifically
- 📍 Avoid generic statements
- 👨‍🎓 Name professors and research centers
- ✨ Show initiative (campus visits, emails to professors)

### For Coalition/Personal Statement
- 📖 Go deep into ONE story
- 🔄 Find the turning point or change
- 🎨 Use sensory details
- 👀 Show your unique perspective
- 🌟 What can only YOU bring to this story?

## ⚙️ Technical Details

### Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **AI**: OpenAI GPT-4o-mini
- **Database**: SQLite3
- **API**: RESTful architecture

### File Structure
```
ESSAYAIAGENTPRJ/
├── app.py                 # Flask backend (all API endpoints)
├── index.html             # SPA frontend (6 tabs)
├── essays.db              # SQLite database (created on first run)
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
├── README.md             # Full documentation (this file)
├── QUICKSTART.md         # Simple setup guide
└── .gitignore            # Git ignore file
```

### Database Schema
```sql
-- Students table
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name TEXT UNIQUE,
  profile_data TEXT,
  created_at TIMESTAMP
);

-- Drafts table
CREATE TABLE drafts (
  id INTEGER PRIMARY KEY,
  student_id INTEGER,
  essay_type TEXT,
  title TEXT,
  content TEXT,
  version INTEGER,
  created_at TIMESTAMP,
  FOREIGN KEY (student_id) REFERENCES students(id)
);
```

## 🔒 Security & Privacy

- ⚠️ **NEVER commit `.env` file** - contains API key
- ✅ Use `.gitignore` to prevent accidental commits
- 🔐 API key is only used server-side, never exposed to browser
- 📝 Drafts are stored locally in SQLite
- 🛡️ CORS is configured for development only

## 🐛 Troubleshooting

### Error: "OPENAI_API_KEY not found"
**Solution**: Check `.env` file has correct API key with no quotes

### Error: "Connection refused"
**Solution**: Make sure Flask server is running (`python app.py`)

### Error: "ModuleNotFoundError"
**Solution**: Run `pip install -r requirements.txt`

### Slow responses
**Normal**: Essay generation takes 10-30 seconds. This is expected.

### CORS errors
**Solution**: Use `http://127.0.0.1:5000` (not `localhost`)

## 🚀 Advanced Usage

### Customizing Prompts
Edit the prompt templates in `app.py` to match your school's specific requirements or focus areas.

### Running on Different Port
```python
app.run(debug=True, host='127.0.0.1', port=8000)
```

### Production Deployment
For production, consider:
- Using Gunicorn instead of Flask development server
- Deploying to Heroku, Render, or Railway
- Using PostgreSQL instead of SQLite
- Setting up proper logging and monitoring

## 📚 College Essay Best Practices

### What Admissions Officers Want
1. **Authentic voice** - writes like a real person, not a robot
2. **Specific details** - shows not tells
3. **Self-awareness** - reflects on growth and lessons
4. **Vulnerability** - shares struggles and how they overcame them
5. **Growth mindset** - demonstrates learning and improvement

### The 5 Essay Killers ❌
1. Generic statements ("I want to change the world")
2. Bragging or achievement listing
3. Formal/artificial language (try to impress = fail)
4. Clichés ("sports taught me teamwork")
5. Grammar errors (shows lack of care)

### The 5 Essay Winners ✅
1. Authentic, conversational voice
2. Vivid, specific examples and details
3. Clear growth/insight/reflection
4. Vulnerability + strength balanced
5. Flawless grammar + powerful words

## 📞 Support & Resources

- **OpenAI Documentation**: https://platform.openai.com/docs
- **Common App Guide**: https://www.commonapp.org
- **Coalition App**: https://www.coalitionforcollegeaccess.org
- **Essay Tips**: https://blog.collegeessayguy.com

## 🎯 Future Enhancements

- [ ] User authentication and accounts
- [ ] Plagiarism checker integration
- [ ] Grammar/spell check integration
- [ ] PDF export functionality
- [ ] Real-time collaboration
- [ ] Video tutorials for each essay type
- [ ] Success stories and examples
- [ ] Integration with college application portals
- [ ] Mobile app version
- [ ] University-specific essay database

## 📄 License

This project is open source. Feel free to modify and use for educational purposes.

---

**Built with ❤️ to help students tell their best story**

*Last Updated: April 2026*
