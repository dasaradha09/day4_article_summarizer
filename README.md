# **Article Summarizer: Streamlit Web App for Article Summarization**

**Article Summarizer** is a web application that provides concise and clear summaries of articles sourced from Google. The app allows users to customize their summarization experience by selecting the type of summary, length, and more, making it easier to grasp key information quickly.

---

## **Live Link:**

https://day4-article-summarizer.onrender.com

---
## **Demo video :**



https://github.com/user-attachments/assets/4a970481-fcfe-42b5-a2bc-919eeaa1d80e



-------------------------

## **Features**

**Google Article Retrieval**: Extracts content from Google articles seamlessly.

**Point-based Summaries**: Users can opt for bullet points that highlight key information.

**Paragraph Summaries**: Users can choose a cohesive summary in paragraph format.

**Summary Length Selection**: Users can adjust the summary length in words using a slider.

**Highlighted Important Sentences**: Summaries are presented with important sentences bolded for emphasis.

**Download Capability** : Users can download the generated summary as a PDF file.


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
git clone https://github.com/yourusername/articl e-summarizer.git
cd article-summarizer
```

2.**Install Dependencies**:
``` bash
pip install -r requirements.txt
```

3.**get the api key**:
```
  goto https://aistudio.google.com/app/apikey and get your api key
  ```

4.**Configure API Keys in .env file**
```
GOOGLE_API_KEY=your-google-api-key
```

5.**Run the Application**:
``` bash
streamlit run article_summarizer.py
```

6. **Access the Application**: Open your browser and navigate to http://localhost:8501.


-------------------

## **How to Use**

1. **Enter Article URL**: Paste the link of the article you want to summarize.

2. **Select Summary Type**: Choose the type of summary (point-based or paragraph) and adjust the summary length using the slider.

3. **Adjust summary length** : choose the summary length length in words by adjusting the slider.

4. **Generate Summary**: Click the generate summary button. The app will extract text from the article and generate the summary within a few seconds.

5. **Download Summary**: Click the download button to save the summary as a PDF.

---

## **Future Enhancements**

- **Summary Translation**: Implement translation features to provide summaries in multiple languages.
 
- **Audio Summary**: Generate audio files of the summaries for auditory consumption.

 ------------------
