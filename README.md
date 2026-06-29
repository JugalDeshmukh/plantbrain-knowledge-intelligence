🏭 **PlantBrain: Unified Industrial Knowledge Intelligence & Asset Brain**

PlantBrain is a high-performance, local-first industrial cognitive platform built for the ET AI Hackathon 2026 (Problem Statement 8: AI for Industrial Knowledge Intelligence).It bridges the gap between unstructured knowledge assets (SOPs, statutory regulatory frameworks, plant compliance manuals) and structured operational data streams (historical maintenance logs, incident records) to give engineers and field technicians a unified decision-making interface.

📌 **Problem Context & Business Value**

In asset-intensive industries, professionals spend an average of 35% of their working hours searching for or clarifying scattered operational information.In India specifically, large plants typically run across 7 to 12 disconnected document systems.This fragmentation contributes to 18-22% of unplanned plant downtime events, as maintenance teams lack immediate context during safety-critical incidents

PlantBrain solves this by consolidating information silos into a unified, serverless edge application, drastically compressing information discovery and response times

🛠️ **System Architecture & Technology Stack**

Unlike traditional heavy cloud architectures that incur massive recurring data warehousing costs and network latency, PlantBrain utilizes a decoupled, edge-optimized blueprint:

Storage Layer: Local directory containing unstructured data (.pdf) and structured log transactions (.csv)

Compute Engine: DuckDB — an embedded, in-process columnar database that runs analytical SQL queries over data files at vector-speed directly within the app process.

Inference Pipeline: Groq API Cloud Architecture paired with Llama 3.3 (70B Versatile), providing sub-second engineering-grade reasoning and contextual precision.

UI Cockpit: Streamlit Panel Framework structured as a professional industrial control dashboard.

🚀 **Key Modules & Features**

1. 💬 **Expert Knowledge Copilot (Tab 1)**
What it does: Uses a Retrieval-Augmented Generation (RAG) pipeline to ingest plant operations manuals.
Hackathon Evaluation Focus: Provides strict, factual engineering responses complete with explicit document citations and reference coordinates, filtering out generic conversational AI filler text.

2. 📊 **Asset Maintenance Intelligence (Tab 2)**

What it does: Leverages an embedded DuckDB engine to run instant multi-parameter SQL aggregations directly on top of raw log structures.

Hackathon Evaluation Focus: Live visualization of critical plant statistics, automatically calculating downtime impact metrics and surfacing high-risk assets using structured telemetry cards.

3. ⚠️ **Automated Compliance Auditor (Tab 3)**

What it does: Acts as an active agentic supervisor checking open plant system anomalies against industrial statutory guidelines (e.g., Section 21 of the Factory Act).

Hackathon Evaluation Focus: Autonomously audits failure logs, outlines specific response timelines, and flags potential liability hazards before regulatory audits occur.

⚙️ **Installation & Local Setup**

1. **Clone the Repository**

git clone [https://github.com/JugalDeshmukh/plantbrain-knowledge-intelligence.git](https://github.com/JugalDeshmukh/plantbrain-knowledge-intelligence.git)
cd plantbrain-knowledge-intelligence


2. **Set Up a Virtual Environment**

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


3. **Install Required Dependencies**

pip install streamlit pandas duckdb groq pypdf


4. **Configure Your Project Directory**

Ensure your file structure matches the layout below:

├── app.py
└── data/
    ├── maintenance_logs.csv  (Automatically generated on initial run)
    └── protocol.pdf          (Drop your plant SOP or safety guide PDF here)

5. **Secure Authentication Setup**

To run the AI-enabled tabs (Expert Knowledge Copilot & Compliance Auditor), you must authenticate with a **Groq API Key**. PlantBrain provides two secure methods to load your key without hardcoding it (protecting your credentials from public leaks and GitHub security blocks):

* **Method: Sidebar UI Input (Recommended for Judges)**
Simply launch the application normally. In the left sidebar under the **🔑Authentication** section, paste your **Groq API key** directly into the secure, password-masked text field. This key is processed entirely in-memory and will never be saved or committed to GitHub.

6. **Boot the Dashboard Console via Powershell**

cd [project directory path]

pip install streamlit pandas duckdb groq pypdf matplotlib

python -m streamlit run app.py

