import streamlit as st
import PyPDF2
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from claim_flow import handle_claim_flow
from genai_response import get_response

st.set_page_config(page_title="EasyInsurance", page_icon="🛡️")
st.title("🛡️ EasyInsurance – GenAI Insurance Assistant")

mode = st.radio("Choose a mode:", ("File a Claim", "Upload Policy File"))

# ---------------- CLAIM MODE ------------------
if mode == "File a Claim":
    st.subheader("📝 Guided Claim Filing")
    user_input = st.text_input("Describe your issue or incident:")

    if user_input:
        response = handle_claim_flow(user_input)
        st.markdown(response)

# ---------------- FILE UPLOAD MODE ------------------
elif mode == "Upload Policy File":
    st.subheader("📄 Upload Insurance PDF to Get a Summary")
    uploaded_file = st.file_uploader("Upload a PDF file (policy or claim)", type=["pdf"])

    def extract_text_from_pdf(file):
        try:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                content = page.extract_text()
                if content:
                    text += content + "\n"
            return text
        except Exception as e:
            st.error(f"❌ Error reading PDF: {e}")
            return None

    def generate_pdf(summary_text):
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        y = height - 40

        for line in summary_text.split("\n"):
            if y < 40:
                c.showPage()
                y = height - 40
            c.drawString(40, y, line)
            y -= 20

        c.save()
        buffer.seek(0)
        return buffer

    if uploaded_file:
        st.success("✅ PDF uploaded successfully!")
        pdf_text = extract_text_from_pdf(uploaded_file)

        if pdf_text:
            st.text_area("📖 Extracted Text (Preview)", pdf_text[:1000], height=200)
            short_text = pdf_text[:3000]  # ✂️ Gemini context limit
            st.text(f"Sending {len(short_text)} characters to Gemini...")

            if st.button("✨ Generate Summary with Gemini"):
                with st.spinner("Talking to Gemini..."):
                    response = get_response(f"Summarize this insurance document:\n\n{short_text}")
                    st.markdown("### 📋 Summary:")
                    st.write(response)

                    # PDF download
                    pdf_buffer = generate_pdf(response)

                    st.download_button(
                        label="📥 Download Summary as PDF",
                        data=pdf_buffer,
                        file_name="insurance_summary.pdf",
                        mime="application/pdf"
                    )
        else:
            st.error("⚠️ Unable to extract text from this PDF. Try another file.")
