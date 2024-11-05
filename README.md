# **Article Summarizer: Streamlit Web App for Article Summarization**

**Article Summarizer** is a web application that provides concise and clear summaries of articles sourced from Google. The app allows users to customize their summarization experience by selecting the type of summary, length, and more, making it easier to grasp key information quickly.

---

## **Features**

### **Article Extraction:**
**Google Article Retrieval**: Extracts content from Google articles seamlessly.

### **Summary Types:**
**Point-based Summaries**: Users can opt for bullet points that highlight key information.
**Paragraph Summaries**: Users can choose a cohesive summary in paragraph format.

### **Customization Options:**
**Summary Length Selection**: Users can adjust the summary length in words using a slider.
**Highlighted Important Sentences**: Summaries are presented with important sentences bolded for emphasis.

### **Download Capability:**
Users can download the generated summary as a PDF file.

---

## **Tech Stack**

- **Streamlit**: Utilized for creating a user-friendly, interactive interface.
- **Google Gemini API**: The language model for generating summaries from extracted content.
- **FPDF**: A library for creating PDF files for summary downloads.
- **dotenv**: Used for managing environment variables securely.

---

## **Setup and Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/article-summarizer.git
   cd article-summarizer










## **How to Use**

1. **Enter Article URL**: Paste the link of the article you want to summarize.
2. **Select Summary Options**: Choose the type of summary (point-based or paragraph) and adjust the summary length using the slider.
3. **Generate Summary**: Click the generate summary button. The app will extract text from the article and generate the summary within a few seconds.
4. **Download Summary**: Click the download button to save the summary as a PDF.

---

## **Future Enhancements**

- **Summary Translation**: Implement translation features to provide summaries in multiple languages.
- **Audio Summary**: Generate audio files of the summaries for auditory consumption.
