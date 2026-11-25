# AI Projects

Practical AI projects in Python that automate everyday business tasks. They use local LLMs through Ollama (Qwen) and the OpenAI API, plus sentence-transformers for semantic search.

## Projects

| Folder | What it does |
|---|---|
| **AI-Customer-Support-Classifier** | Classifies customer messages by category, priority and sentiment, routes them to the right team and drafts a reply. |
| **RAG Knowledge Assistant** | Finds relevant company documents using semantic search, then answers questions using only that information. |
| **AI Semantic Search** | Searches a knowledge base by meaning instead of keywords. |
| **AI-Meeting-Analyzer** | Turns meeting notes into a summary and action items with owners and deadlines. |
| **AI-Resume-Analyzer** | Compares a resume to a job description and gives a match score, skill gaps and a recommendation. |
| **AI-Sales-Intelligence** | Scores leads and writes a sales report, then runs a second AI check that flags unsupported claims. Run `python local_ai_test.py`. |
| **AI-Document-Summarizer** | Creates short, detailed or bullet-point summaries of pasted text. |
| **AI-Email-Assistant** | Rewrites rough messages as clear emails in a chosen tone. |
| **AI Agent** | Lets the model choose between a calculator and a company-info tool. |

## Setup

1. Install [Ollama](https://ollama.com) and run `ollama pull qwen3:1.7b`
2. Install the packages: `pip install ollama sentence-transformers openai`
3. Open a project folder and run `python main.py`

## About

Built by Rahim Zahid, a Computer Science graduate with a business development background, as hands-on practice in applied AI and automation.
