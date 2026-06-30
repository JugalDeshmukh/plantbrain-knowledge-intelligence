🏭 **PlantBrain AI: Unified Industrial Knowledge Intelligence & Regulatory Audit Engine**

PlantBrain AI is a high-performance, local-first industrial cognitive platform built for the ET AI Hackathon 2026 (Problem Statement 8: AI for Industrial Knowledge Intelligence). It bridges the gap between unstructured knowledge assets (SOPs, statutory regulatory frameworks, plant compliance manuals) and structured operational data streams (historical maintenance logs, incident records) to give engineers and field technicians a unified decision-making interface.

📌 **Problem Context & Business Value**

In asset-intensive industries, professionals spend an average of 35% of their working hours searching for or clarifying scattered operational information. In India specifically, large plants typically run across 7 to 12 disconnected document systems (P&IDs, work orders, operating procedures, safety guidelines). This fragmentation contributes to 18-22% of unplanned plant downtime events, as maintenance teams lack immediate context during safety-critical incidents.

PlantBrain AI solves this by consolidating information silos into a unified, serverless edge application, drastically compressing information discovery and response times.

🛠️ **System Architecture & Technology Stack**

Unlike traditional heavy cloud architectures that incur massive recurring data warehousing costs and network latency, PlantBrain utilizes a decoupled, edge-optimized blueprint:

Storage Layer: Local directory containing unstructured data (.pdf) and structured log transactions (.csv).

Compute Engine: DuckDB — an embedded, in-process columnar database that runs analytical SQL queries over data files at vector-speed directly within the app process.

Inference Pipeline: Groq API Cloud Architecture paired with Llama 3.3 (70B Versatile), providing sub-second engineering-grade reasoning and contextual precision.

UI Cockpit: Streamlit Framework structured as a professional industrial control dashboard.

📁 **Presentation & Submission Resources**

This repository functions as the central submission hub for our hackathon entry. The following accompanying resources are committed directly to the root folder:

📊 PlantBrain Presentation (PPTX): The editable PowerPoint pitch deck covering the Problem, Solution, System Architecture, and Business Impact.

📄 PlantBrain Project Documentation (PDF): A comprehensive engineering whitepaper outlining technical details, schema patterns, and enterprise ROI analysis.

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

1. Clone the Repository

git clone [https://github.com/JugalDeshmukh/plantbrain-knowledge-intelligence.git](https://github.com/JugalDeshmukh/plantbrain-knowledge-intelligence.git)
cd plantbrain-knowledge-intelligence


2. **Set Up a Virtual Environment**

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


3. **Install Required Dependencies**

pip install -r requirements.txt


4. **Configure Your Project Directory**

Ensure your local file structure matches the layout below:

plantbrain_hackathon/ <br>
├── app.py                             # Streamlit Core Application UI <br>
├── core_engines.py                    # Cognitive Inference Engine (RAG & Groq API Calls) <br>
├── database_analytics.py              # Embedded DuckDB SQL & Data Aggregator Engine <br>
├── PlantBrain Presentation.pptx       # Pitch Deck (PowerPoint Version) <br>
├── PlantBrain_Project_Documentation.pdf  # Technical Whitepaper Document <br>
├── README.md                          # Repository Homepage Documentation <br>
├── requirements.txt                   # Python Dependency List <br>
├── screenshots/                       # UI Action Screenshots <br>
│   └── Assets_Analytics_Tab.png       # UI Visual Screen Evidence <br>
└── data/   <br>
    ├── maintenance_logs.csv           # Structured Plant Maintenance Logs (Auto-generated on run) <br>
    └── protocol.pdf                   # Unstructured Standard Operating Procedure (SOP) <br>


5. **Secure Authentication Setup**

To run the AI-enabled tabs (Expert Knowledge Copilot & Compliance Auditor), you must authenticate with a Groq API Key. PlantBrain provides two secure methods to load your key without hardcoding it:

Method A: Sidebar UI Input (Recommended for Judges)

Simply run the application normally:

python -m streamlit run app.py


Paste your Groq API key directly into the secure password-masked text field located under 🔑 Authentication in the left sidebar console. This key is used on-the-fly and is never saved or exposed to git.

Method B: Local Environment Variable (Recommended for Local Dev)

Set your environment variables before running the application:

Windows (PowerShell):

$env:GROQ_API_KEY="your_actual_groq_api_key"
python -m streamlit run app.py


macOS/Linux:

export GROQ_API_KEY="your_actual_groq_api_key"
python -m streamlit run app.py


📊 **Hackathon Submission Impact Metrics**

Evaluation Metric

Legacy Operations Baseline

PlantBrain Target Impact

Information Discovery Latency

35 - 45 Minutes

< 2 Seconds (Sub-second via Groq)

Compliance Audit Cycle

Monthly Retrospective Review

Real-Time Automated Evaluation

Cloud Compute Overhead

High Recurring SaaS / DB Fees

Zero-Cost Edge Footprint

👨‍💻 Developed By

Jugal Deshmukh - AI Professional | Data Analyst | Microsoft Fabric Certified

Contact: mrjugaldeshmukh@gmail.com | +91 9010902225

LinkedIn: jugaldeshmukh

GitHub: JugalDeshmukh

