🛡️ EasyInsurance

EasyInsurance is a GenAI-powered virtual assistant that simplifies the insurance process through natural language conversations and smart document handling. Built with Streamlit and OpenAI/Gemini, it helps users ask insurance-related questions and generate claim summaries or policy document summaries instantly.

🌐 Live Demo

👉 Click to Use the App

🚀 Features

🤖 Chat-based Insurance SupportAsk any insurance question and get AI-generated answers.

📄 PDF SummarizationUpload an insurance policy or claim document in PDF format — get a summarized version in simple language.

🧠 GenAI Response EngineUses OpenAI GPT-3.5 or Gemini models for intelligent, empathetic responses.

📤 Downloadable AI Summary PDFExport AI-written summaries into a new PDF file.

🧰 Tech Stack

Streamlit – For UI and app framework

OpenAI / Gemini API – GenAI for chat and summarization

PyPDF2 – Extract text from PDFs

ReportLab – Generate downloadable summary PDFs

Python-dotenv – API key handling (optional)

🛠️ Setup Instructions

🔹 1. Clone the Repo

git clone https://github.com/Prakriti2603/EasyInsurance.git
cd EasyInsurance

🔹 2. Install Requirements

pip install -r requirements.txt

🔹 3. Add API Key (Option A: In Code)

Edit genai_response.py and paste your key:

openai.api_key = "sk-..."  # or use Gemini key

(Option B: Use a .env file)

OPENAI_API_KEY=your_openai_key_here

🔹 4. Run the App

streamlit run app.py

🧠 Use Cases

Simplify complex policy documents

Help users file insurance claims step-by-step

Reduce dependency on agents

Provide a hygienic, contactless support system

📁 Project Structure

EasyInsurance/
├── app.py                # Main Streamlit app
├── genai_response.py     # GenAI logic for chat & summaries
├── requirements.txt      # Python dependencies
├── README.md             # You are here!

✅ Submission Checklist



💡 Credits

Made with ❤️ by Prakriti Ranka as part of the GenAI Hackathon.

📬 Contact

For questions or collaboration, message via GitHub.

