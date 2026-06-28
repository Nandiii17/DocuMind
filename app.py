import streamlit as st
import tempfile
from pdf_processor import extract_text
from chunking import create_chunks
from embeddings import generate_embeddings
from vector_store import store_chunks
from retrieval import retrieve_chunks
from generator import generate_answer

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="DocuMind",
    page_icon="📄"
)

# ==========================================
# SESSION STATE
# ==========================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "auto_ask" not in st.session_state:
    st.session_state.auto_ask = False

if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = ""

if "chunk_count" not in st.session_state:
    st.session_state.chunk_count = 0

if "retrieval_query" not in st.session_state:
    st.session_state.retrieval_query = None

if "answer_mode" not in st.session_state:
    st.session_state.answer_mode = None

# ==========================================
# TITLE
# ==========================================

st.title("📄 DocuMind")

# ==========================================
# SIDEBAR — CONFIGURATION
# ==========================================

with st.sidebar:

    st.header("⚙️ Configuration")

    st.write("Embedding Model")
    st.info("all-MiniLM-L6-v2")

    st.write("LLM")
    st.info("Phi-3")

    st.write("Vector Database")
    st.info("ChromaDB")

    st.write("Top-K")
    st.info("10")

    if st.session_state.chunk_count:

        st.write("Chunks")

        st.info(
            st.session_state.chunk_count
        )

    if st.session_state.pdf_name:

        st.write("Current PDF")

        st.info(
            st.session_state.pdf_name
        )

st.write("Upload a PDF and ask questions about it.")

# ==========================================
# FILE UPLOAD
# ==========================================

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

# ==========================================
# PROCESS PDF
# ==========================================

if uploaded_file is not None:

    st.session_state.pdf_name = uploaded_file.name

    st.success("PDF uploaded successfully!")

    if st.button("Process PDF"):

        try:

            with st.spinner("📄 Processing PDF..."):

                # Save uploaded PDF temporarily
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                ) as temp_pdf:

                    temp_pdf.write(uploaded_file.read())
                    pdf_path = temp_pdf.name

                # Extract pages
                pages = extract_text(pdf_path)

                # Build full text for stats/preview
                full_text = "\n".join(
                    page["text"]
                    for page in pages
                )

                # Create chunks
                chunks = create_chunks(pages)

                st.session_state.chunk_count = len(chunks)

                # Generate embeddings
                embeddings = generate_embeddings(chunks)

                # Store in ChromaDB
                stored_count = store_chunks(
                    chunks,
                    embeddings
                )

            # Success Message
            st.success(
                f"PDF processed successfully! Created and stored {stored_count} chunks."
            )

            # ==========================================
            # DOCUMENT STATS
            # ==========================================

            st.subheader("📊 Document Statistics")

            st.write(f"Characters Extracted: {len(full_text)}")
            st.write(f"Total Chunks: {len(chunks)}")

            # ==========================================
            # TEXT PREVIEW
            # ==========================================

            st.subheader("📄 Extracted Text Preview")

            st.write(full_text[:1000])

        except Exception as e:

            st.error(
                f"Error processing PDF: {e}"
            )

# ==========================================
# QUESTION SECTION
# ==========================================

st.divider()

st.header("❓ Ask Questions")

# ==========================================
# RESEARCH PAPER INTELLIGENCE
# ==========================================

st.subheader("🔬 Research Paper Intelligence")

col1, col2, col3 = st.columns(3)

with col1:
    summary_btn = st.button("📄 Summary")

with col2:
    methodology_btn = st.button("🔬 Methodology")

with col3:
    results_btn = st.button("📊 Results")

col4, col5 = st.columns(2)

with col4:
    limitations_btn = st.button("⚠️ Limitations")

with col5:
    future_work_btn = st.button("🚀 Future Work")

retrieval_query = None
display_question = None
answer_mode = None

if summary_btn:

    retrieval_query = (
        "abstract conclusion"
    )

    display_question = (
        "Provide a summary of this document."
    )

    answer_mode = "summary"

elif methodology_btn:

    retrieval_query = (
        "methodology approach framework training pipeline"
    )

    display_question = (
        "What methodology is used in this document?"
    )

    answer_mode = "methodology"

elif results_btn:

    retrieval_query = (
        "results experiments evaluation findings performance"
    )

    display_question = (
        "What are the key results discussed in this document?"
    )

    answer_mode = "results"

elif limitations_btn:

    retrieval_query = (
        "limitations challenges weaknesses"
    )

    display_question = (
        "What limitations are discussed in this document?"
    )

    answer_mode = "limitations"

elif future_work_btn:

    retrieval_query = (
        "future work future directions"
    )

    display_question = (
        "What future work or future directions are suggested in this document?"
    )

    answer_mode = "future_work"

# ==========================================
# CHAT HISTORY
# ==========================================

if st.session_state.chat_history:

    st.subheader("💬 Chat History")

    for chat in reversed(st.session_state.chat_history):

        st.markdown(
            f"**🙋 Question:** {chat['question']}"
        )

        st.markdown(
            f"**🤖 Answer:** {chat['answer']}"
        )

        st.divider()

question = st.text_input(
    "Ask a question about the document"
)

if display_question:

    question = display_question

    st.session_state.auto_ask = True
    st.session_state.answer_mode = answer_mode

ask_clicked = st.button("Ask")

if ask_clicked or st.session_state.auto_ask:

    if not question.strip():

        st.error("Please enter a question.")

    else:

        try:

            with st.spinner("🤖 Generating Answer..."):

                # Use optimized retrieval query if available
                search_query = (
                    retrieval_query
                    if retrieval_query
                    else question
                )

                # Retrieve relevant chunks
                retrieved_chunks = retrieve_chunks(
                    search_query
                )

                # Create context from chunk dicts
                context = "\n\n".join(
                    chunk["text"]
                    for chunk in retrieved_chunks
                )

                # Determine which mode to use for this answer
                active_mode = (
                    answer_mode
                    if answer_mode
                    else st.session_state.answer_mode
                )

                # Generate answer using mode-specific prompt
                if active_mode:

                    answer = generate_answer(
                        context,
                        question,
                        active_mode
                    )

                else:

                    answer = generate_answer(
                        context,
                        question
                    )

                st.session_state.auto_ask = False
                st.session_state.retrieval_query = None
                st.session_state.answer_mode = None

                # Store in chat history
                st.session_state.chat_history.append(
                    {
                        "question": question,
                        "answer": answer
                    }
                )

                st.session_state.chat_history = (
                    st.session_state.chat_history[-10:]
                )

            # ==========================================
            # SUPPORTING EVIDENCE
            # ==========================================

            with st.expander("📚 Supporting Evidence"):

                for i, chunk in enumerate(retrieved_chunks):

                    st.markdown(
                        f"### Evidence {i+1}"
                    )

                    st.markdown(
                        f"📄 Page {chunk['page']}"
                    )

                    st.text(
                        chunk["text"]
                    )

                    st.divider()

            # ==========================================
            # ANALYSIS
            # ==========================================

            st.subheader("📑 Analysis")

            st.write(answer)

            pages = sorted(
                set(
                    chunk["page"]
                    for chunk in retrieved_chunks
                )
            )

            st.markdown(
                f"**Sources: Pages {', '.join(map(str, pages))}**"
            )

        except Exception as e:

            st.error(
                f"Error generating answer: {e}"
            )

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown(
    "<p style='text-align: center; color: gray;'>"
    "Built using Streamlit • ChromaDB • Sentence Transformers • Phi-3 (Ollama)"
    "</p>",
    unsafe_allow_html=True
)