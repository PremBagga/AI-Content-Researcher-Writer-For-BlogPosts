# AI-Content-Researcher-Writer-For-BlogPosts
# AI Content Researcher & Writer for Blog Posts

🚀 **Automate Your Blog Writing with AI!**

This AI-powered tool researches and generates high-quality blog content using Groq API and Serper API. Simply provide a topic, and the AI will generate well-structured blog posts with relevant insights.

---

## 🌟 Features

- **AI-Powered Research**: Uses Serper API to fetch real-time data for relevant content.
- **Automated Blog Writing**: Generates structured and engaging blog posts.
- **Customizable AI Model**: Easily switch Groq API models by modifying `streamlit_app.py`.
- **Simple UI**: Built using Streamlit for a smooth user experience.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Set Up the Environment
Create a `.env` file in the root directory and add your API keys:
```env
SERPER_API_KEY=your-serper-api-key
GROQ_API_KEY=your-groq-api-key
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```sh
streamlit run streamlit_app.py
```

---

## 📁 File Structure
```
📂 AI-Content-Writer
│-- 📄 streamlit_app.py   # Main Streamlit application
│-- 📄 requirements.txt   # Dependencies list
│-- 📄 .env               # Store API keys securely

```

---

## 📜 Requirements
Make sure you have Python installed. The required dependencies are listed in `requirements.txt`:
```
streamlit
openai
python-dotenv
requests
```
Install using:
```sh
pip install -r requirements.txt
```

---

## 🎯 Customization
To change the AI model, modify `streamlit_app.py` and update the Groq model name:
```python
llm = llm("groq\your-preferred-model")
```

---

## 🎉 Contribution & Support
Feel free to fork, improve, and contribute to this project! If you encounter any issues, open a GitHub issue or contact us.

Happy Blogging! ✍️🚀

