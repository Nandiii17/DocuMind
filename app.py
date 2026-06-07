import streamlit as st
import tempfile

from pdf_processor import extract_text
from chunking import create_chunks

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="DocuMind",
    page_icon="📄"
)

# ==========================================
# TITLE
# ==========================================

st.title("📄 DocuMind")

st.write("Upload a PDF and process it.")

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

        # Success Message
        st.success(
            f"PDF processed successfully! Created {len(chunks)} chunks."
        )

        # ==========================================
        # DOCUMENT STATS
        # ==========================================

        st.subheader("📊 Document Statistics")

        st.write(f"Characters Extracted: {len(text)}")
        st.write(f"Total Chunks: {len(chunks)}")

        # ==========================================
        # PREVIEW TEXT
        # ==========================================

        st.subheader("📄 Extracted Text Preview")

        st.write(text[:1000])

        # ==========================================
        # FIRST CHUNK
        # ==========================================

        st.subheader("🧩 First Chunk")

        st.write(chunks[0])

        # ==========================================
        # ALL CHUNKS
        # ==========================================

        with st.expander("View All Chunks"):

            for i, chunk in enumerate(chunks):

                st.markdown(f"### Chunk {i+1}")

                st.write(chunk)

                st.divider()