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

# ==========================================
# TITLE
# ==========================================

st.title("📄 DocuMind")

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

                # Extract text
                text = extract_text(pdf_path)

                # Create chunks
                chunks = create_chunks(text)

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

            st.write(f"Characters Extracted: {len(text)}")
            st.write(f"Total Chunks: {len(chunks)}")

            # ==========================================
            # TEXT PREVIEW
            # ==========================================

            st.subheader("📄 Extracted Text Preview")

            st.write(text[:1000])

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

predefined_question = None

if summary_btn:
    predefined_question = "Provide a summary of this document."

elif methodology_btn:
    predefined_question = "What methodology is used in this document?"

elif results_btn:
    predefined_question = "What are the key results discussed in this document?"

elif limitations_btn:
    predefined_question = "What limitations are discussed in this document?"

elif future_work_btn:
    predefined_question = "What future work or future directions are suggested in this document?"

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

if predefined_question:
    question = predefined_question

if st.button("Ask") or predefined_question:

    if not question.strip():

        st.error("Please enter a question.")

    else:

        try:

            with st.spinner("🤖 Generating Answer..."):

                # Retrieve relevant chunks
                retrieved_chunks = retrieve_chunks(question)

                # Create context
                context = "\n\n".join(retrieved_chunks)

                # Generate answer
                answer = generate_answer(
                    context,
                    question
                )

                # Store in chat history
                st.session_state.chat_history.append(
                    {
                        "question": question,
                        "answer": answer
                    }
                )

            # ==========================================
            # SOURCES
            # ==========================================

            with st.expander("📚 View Sources"):

                for i, chunk in enumerate(retrieved_chunks):

                    st.markdown(
                        f"### Chunk {i+1}"
                    )

                    st.write(chunk)

                    st.divider()

            # ==========================================
            # ANSWER
            # ==========================================

            st.subheader("🤖 Answer")

            st.write(answer)

        except Exception as e:

            st.error(
                f"Error generating answer: {e}"
            )