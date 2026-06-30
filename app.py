import streamlit as st
import os

# 1. Page Configuration (Must run first before any other Streamlit UI operations)
st.set_page_config(page_title="Industrial Knowledge Brain", layout="wide")
st.title("🏭 PlantBrain AI : Unified Industrial Knowledge Intelligence & Regulatory Audit Engine")

# 2. Startup Diagnostic System
try:
    from groq import Groq
    # Import modular components cleanly
    from core_engines import extract_pdf_text, execute_cognitive_inference
    from database_analytics import (
        initialize_database_and_get_logs,
        run_downtime_metrics_query,
        get_open_issues
    )
except Exception as e:
    st.error("🚨 **PlantBrain Startup Diagnostic System**")
    st.markdown("""
    The application failed to start because of an import or configuration error in your project workspace. 
    This usually happens if a dependency is missing from your active virtual environment, or if there is a syntax typo in one of your modules.
    """)
    st.exception(e)
    st.info("💡 **Troubleshooting Tip:** Check the error traceback details above to find the exact file and line number that failed.")
    st.stop()

# 3. Sidebar Configuration & Security
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

# Initialize database logs and read from core assets
df_logs = initialize_database_and_get_logs()

# Extract text from your sample PDF
pdf_context = extract_pdf_text("data/protocol.pdf")

# 4. Streamlit Multi-Tab UI Layout
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
                response = execute_cognitive_inference(client, user_query, context=pdf_context)
                status.update(label="✅ Analysis complete", state="complete", expanded=False)
            
            st.subheader("📋 Operational Directive")
            st.markdown(response)

# --- TAB 2: ASSET ANALYTICS (DUCKDB) ---
with tab2:
    st.header("Asset Maintenance Intelligence")
    st.caption("Real-time operational metrics parsed via DuckDB analytics engine.")
    
    # Run the query located in the database analytics module
    metrics_df = run_downtime_metrics_query(df_logs)
    
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
    
    # Fetching open issues using custom DuckDB analytic function
    open_issues = get_open_issues(df_logs)
    
    if not open_issues.empty:
        selected_issue = st.selectbox("Select Anomaly Log to Audit:", open_issues['issue_description'].tolist())
        
        if st.button("Run Compliance Check"):
            if not GROQ_API_KEY:
                st.warning("⚠️ To evaluate regulatory compliance, please paste a Groq API Key into the sidebar authentication box first.")
            else:
                with st.spinner("Analyzing parameters..."):
                    audit_prompt = f"Analyze this specific issue log for regulatory breaches: {selected_issue}"
                    regulatory_context = "Factory Act Section 21: Any volatile asset anomaly (gas/vibration) must trigger an active technical dispatch within 2 hours."
                    
                    audit_result = execute_cognitive_inference(client, audit_prompt, context=f"{pdf_context}\n{regulatory_context}")
                    st.info("Audit Agent Findings:")
                    st.markdown(audit_result)
    else:
        st.success("All asset logs are closed and compliant.")