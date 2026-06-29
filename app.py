import streamlit as st
import pandas as pd
import duckdb
import os
from pypdf import PdfReader
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="Industrial Knowledge Brain", layout="wide")
st.title("🏭 PlantBrain AI : Unified Industrial Knowledge Intelligence & Regulatory Audit Engine")

# 2. Sidebar Configuration & Security
st.sidebar.image("https://img.icons8.com/fluent/96/000000/factory.png", width=60)
st.sidebar.header("Control Center Settings")
selected_facility = st.sidebar.selectbox("Active Facility Unit", ["Unit 4 - Hyderabad", "Unit 2 - Pune", "Unit 1 - Bangalore"])
st.sidebar.divider()

# Secure Key Management: Check environment first, then provide UI override
env_key = os.environ.get("GROQ_API_KEY", "")

st.sidebar.subheader("🔑 Authentication")
user_api_key = st.sidebar.text_input(
    "Groq API Key", 
    value=env_key, 
    type="password", 
    placeholder="Paste gsk_... key here",
    help="Get a free API key at console.groq.com"
)

# Resolve final key priority
GROQ_API_KEY = user_api_key if user_api_key else env_key

st.sidebar.divider()
st.sidebar.subheader("System Status")
st.sidebar.success("DuckDB Engine: Connected")

if GROQ_API_KEY:
    st.sidebar.success("Groq Core Pipeline: Active")
else:
    st.sidebar.warning("Groq Core Pipeline: Pending Key")

st.sidebar.caption(f"Connected to {selected_facility} operational matrix.")

# Initialize Groq Client safely
client = None
if GROQ_API_KEY:
    try:
        client = Groq(api_key=GROQ_API_KEY)
    except Exception as e:
        st.sidebar.error(f"Initialization Error: {str(e)}")

# 3. Helper Function: Extract text from local PDFs
@st.cache_data
def extract_pdf_text(pdf_path):
    if not os.path.exists(pdf_path):
        return "Standard safety protocols apply. No specific document found."
    
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text[:4000]  # Limit characters to fit model context window easily
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

# 4. Helper Function: Call Groq API (Llama 3.3)
def get_llm_response(prompt, context=""):
    if not client:
        return "⚠️ system: Connection pipeline is inactive. Please provide a valid Groq API Key in the sidebar input box to run AI-powered modules."
        
    system_prompt = (
        "You are the central proprietary operating engine of PlantBrain. "
        "Provide a direct, engineering-grade response using the internal knowledge matrix. "
        "NEVER say phrases like 'Based on the provided context', 'According to the document', or 'As an AI'. "
        "Present the data directly as facts. "
        "At the very bottom of your response, create a clean line that says '📂 Reference Assets:' followed by the document citations."
    )
    
    full_prompt = f"Context from Plant Documents:\n{context}\n\nUser Query: {prompt}"
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.2,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error connecting to Groq API: {str(e)}"

# 5. Load and Setup Dummy Data
if not os.path.exists("data"):
    os.makedirs("data")

csv_path = "data/maintenance_logs.csv"
if not os.path.exists(csv_path):
    mock_data = """log_id,timestamp,asset_id,asset_name,issue_description,status,downtime_hours
1,2026-06-15,PUMP-04,Primary Water Pump,Cavitation detected and seal leaking,RESOLVED,3.5
2,2026-06-20,VALVE-12,Main Gas Feed Valve,Slight pressure drop observed during shift change,OPEN,1.2
3,2026-06-22,COMP-01,Air Compressor,High vibration and thermal cutoff triggered,OPEN,4.0"""
    with open(csv_path, "w") as f:
        f.write(mock_data)

df_logs = pd.read_csv(csv_path)

# Extract text from your sample PDF
pdf_context = extract_pdf_text("data/protocol.pdf")

# 6. Streamlit Multi-Tab UI Layout
tab1, tab2, tab3 = st.tabs(["💬 Expert Knowledge Copilot", "📊 Asset Analytics Brain", "⚠️ Compliance Auditor"])

# --- TAB 1: RAG COPILOT FOR FIELD TECHNICIANS ---
with tab1:
    st.header("Ask the Plant Brain")
    st.caption("Query industrial procedures, safety codes, and manuals instantly.")
    
    user_query = st.text_input("Enter operational question:", placeholder="e.g., What should I do if a gas valve drops pressure?")
    
    if user_query:
        if not GROQ_API_KEY:
            st.warning("⚠️ To run this operational query, please paste a Groq API Key into the sidebar authentication box first.")
        else:
            with st.status("🔍 Scanning internal document repositories...", expanded=True) as status:
                st.write("Reading historical asset protocols...")
                st.write("Cross-referencing telemetry data with regulatory standards...")
                response = get_llm_response(user_query, context=pdf_context)
                status.update(label="✅ Analysis complete", state="complete", expanded=False)
            
            st.subheader("📋 Operational Directive")
            st.markdown(response)

# --- TAB 2: ASSET ANALYTICS (DUCKDB) ---
with tab2:
    st.header("Asset Maintenance Intelligence")
    st.caption("Real-time operational metrics parsed via DuckDB analytics engine.")
    
    # Run a DuckDB analytical query over the dataframe
    query = """
        SELECT asset_name, SUM(downtime_hours) as total_downtime, COUNT(*) as failure_count
        FROM df_logs
        GROUP BY asset_name
        ORDER BY total_downtime DESC
    """
    metrics_df = duckdb.query(query).to_df()
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("High-Risk Assets Summary")
        if not metrics_df.empty:
            top_asset = metrics_df.iloc[0]
            st.metric(
                label="🚨 Highest Operational Risk Asset", 
                value=top_asset['asset_name'], 
                delta=f"{top_asset['total_downtime']} Hrs Total Downtime",
                delta_color="inverse"
            )
        
        st.dataframe(
            metrics_df.style.background_gradient(cmap="Reds", subset=["total_downtime"]),
            use_container_width=True,
            hide_index=True
        )
    with col2:
        st.subheader("Downtime Impact Analysis")
        st.bar_chart(data=metrics_df, x="asset_name", y="total_downtime")

# --- TAB 3: AGENTIC COMPLIANCE CHECKER ---
with tab3:
    st.header("Automated Compliance Audit Agent")
    st.caption("Evaluates open plant logs against safety and regulatory compliance baselines.")
    
    # Fetching open issues using DuckDB SQL
    open_issues = duckdb.query("SELECT * FROM df_logs WHERE status = 'OPEN'").to_df()
    
    if not open_issues.empty:
        selected_issue = st.selectbox("Select Anomaly Log to Audit:", open_issues['issue_description'].tolist())
        
        if st.button("Run Compliance Check"):
            if not GROQ_API_KEY:
                st.warning("⚠️ To evaluate regulatory compliance, please paste a Groq API Key into the sidebar authentication box first.")
            else:
                with st.spinner("Analyzing parameters..."):
                    audit_prompt = f"Analyze this specific issue log for regulatory breaches: {selected_issue}"
                    regulatory_context = "Factory Act Section 21: Any volatile asset anomaly (gas/vibration) must trigger an active technical dispatch within 2 hours."
                    
                    audit_result = get_llm_response(audit_prompt, context=f"{pdf_context}\n{regulatory_context}")
                    st.info("Audit Agent Findings:")
                    st.markdown(audit_result)
    else:
        st.success("All asset logs are closed and compliant.")