🏭 PlantBrain: Unified Industrial Knowledge Intelligence & Asset Brain

[cite_start]PlantBrain is a high-performance, local-first industrial cognitive platform built for the ET AI Hackathon 2026 (Problem Statement 8: AI for Industrial Knowledge Intelligence)[cite: 54, 331, 332, 333]. [cite_start]It bridges the gap between unstructured knowledge assets (SOPs, statutory regulatory frameworks, plant compliance manuals) and structured operational data streams (historical maintenance logs, incident records) to give engineers and field technicians a unified decision-making interface[cite: 336, 343, 348].

📌 Problem Context & Business Value

[cite_start]In asset-intensive industries, professionals spend an average of 35% of their working hours searching for or clarifying scattered operational information[cite: 335]. [cite_start]In India specifically, large plants typically run across 7 to 12 disconnected document systems[cite: 336]. [cite_start]This fragmentation contributes to 18-22% of unplanned plant downtime events, as maintenance teams lack immediate context during safety-critical incidents[cite: 337].

[cite_start]PlantBrain solves this by consolidating information silos into a unified, serverless edge application, drastically compressing information discovery and response times[cite: 343].

🛠️ System Architecture & Technology Stack

Unlike traditional heavy cloud architectures that incur massive recurring data warehousing costs and network latency, PlantBrain utilizes a decoupled, edge-optimized blueprint:

[cite_start]Storage Layer: Local directory containing unstructured data (.pdf) and structured log transactions (.csv)[cite: 343, 346].

Compute Engine: DuckDB — an embedded, in-process columnar database that runs analytical SQL queries over data files at vector-speed directly within the app process.

Inference Pipeline: Groq API Cloud Architecture paired with Llama 3.3 (70B Versatile), providing sub-second engineering-grade reasoning and contextual precision.

UI Cockpit: Streamlit Panel Framework structured as a professional industrial control dashboard.

🚀 Key Modules & Features

1. 💬 Expert Knowledge Copilot (Tab 1)

[cite_start]What it does: Uses a Retrieval-Augmented Generation (RAG) pipeline to ingest plant operations manuals[cite: 348, 357].

[cite_start]Hackathon Evaluation Focus: Provides strict, factual engineering responses complete with explicit document citations and reference coordinates, filtering out generic conversational AI filler text[cite: 348, 367].

2. 📊 Asset Maintenance Intelligence (Tab 2)

What it does: Leverages an embedded DuckDB engine to run instant multi-parameter SQL aggregations directly on top of raw log structures.

[cite_start]Hackathon Evaluation Focus: Live visualization of critical plant statistics, automatically calculating downtime impact metrics and surfacing high-risk assets using structured telemetry cards[cite: 350].

3. ⚠️ Automated Compliance Auditor (Tab 3)

[cite_start]What it does: Acts as an active agentic supervisor checking open plant system anomalies against industrial statutory guidelines (e.g., Section 21 of the Factory Act)[cite: 351].

[cite_start]Hackathon Evaluation Focus: Autonomously audits failure logs, outlines specific response timelines, and flags potential liability hazards before regulatory audits occur[cite: 351, 353].

⚙️ Installation & Local Setup

1. Clone the Repository

git clone [https://github.com/JugalDeshmukh/plantbrain-knowledge-intelligence.git](https://github.com/JugalDeshmukh/plantbrain-knowledge-intelligence.git)
cd plantbrain-knowledge-intelligence


2. Set Up a Virtual Environment

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


3. Install Required Dependencies

pip install streamlit pandas duckdb groq pypdf


4. Configure Your Project Directory

Ensure your file structure matches the layout below:

├── app.py
└── data/
    ├── maintenance_logs.csv  (Automatically generated on initial run)
    └── protocol.pdf          (Drop your plant SOP or safety guide PDF here)


5. Add Your API Credentials

Open app.py and add your Groq API token directly into the client initialization line:

GROQ_API_KEY = "your_actual_groq_api_key_here"


6. Boot the Dashboard Console

cd [project directory path]

pip install streamlit pandas duckdb groq pypdf matplotlib

python -m streamlit run app.py

