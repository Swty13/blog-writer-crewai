import streamlit as st
from crewai import Crew
from agents import BlogWriterAgents
from task import BlogTasks
from dotenv import load_dotenv
import PyPDF2
import io
import requests
from PIL import Image
import base64

class BlogWriterCrew:
    def __init__(self, topic, target_audience, word_count, tone, keywords, source_content=None):
        self.topic = topic
        self.target_audience = target_audience
        self.word_count = word_count
        self.tone = tone
        self.keywords = keywords
        self.source_content = source_content

    def run(self):
        agents = BlogWriterAgents()
        tasks = BlogTasks()

        research_agent = agents.research_agent()
        content_strategist = agents.content_strategist()
        blog_writer = agents.blog_writer()
        editor = agents.editor()

        research_task = tasks.research_task(
            research_agent,
            self.topic,
            self.target_audience,
            self.keywords,
            self.source_content
        )

        strategy_task = tasks.strategy_task(
            content_strategist,
            self.topic,
            self.target_audience,
            self.tone,
            self.word_count
        )

        writing_task = tasks.writing_task(
            blog_writer,
            self.topic,
            self.tone,
            self.word_count
        )

        editing_task = tasks.editing_task(
            editor,
            self.tone,
            self.target_audience
        )

        crew = Crew(
            agents=[research_agent, content_strategist, blog_writer, editor],
            tasks=[research_task, strategy_task, writing_task, editing_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result

def process_url(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        return f"Error processing URL: {str(e)}"

def process_pdf(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error processing PDF: {str(e)}"

def process_image(image_file):
    try:
        # Here you would typically use OCR or image analysis
        # For now, we'll just confirm we received the image
        image = Image.open(image_file)
        return f"Image processed: {image.size}"
    except Exception as e:
        return f"Error processing image: {str(e)}"


def main():

    st.title("AI Blog Writer")
    st.write("Welcome to the AI Blog Writer! Upload your source material and fill in the details below.")

    # Source material input section
    st.subheader("Source Material")
    source_type = st.radio(
        "Choose your source type:",
        ["URL", "PDF", "Image", "None"]
    )

    source_content = None
    if source_type == "URL":
        url = st.text_input("Enter the URL:")
        if url:
            source_content = process_url(url)
            st.success("URL processed successfully!")
            
    elif source_type == "PDF":
        uploaded_file = st.file_uploader("Upload your PDF", type="pdf")
        if uploaded_file:
            source_content = process_pdf(uploaded_file)
            st.success("PDF processed successfully!")
            
    elif source_type == "Image":
        uploaded_file = st.file_uploader("Upload your image", type=["png", "jpg", "jpeg"])
        if uploaded_file:
            source_content = process_image(uploaded_file)
            st.success("Image processed successfully!")

    # Blog details input section
    st.subheader("Blog Details")
    topic = st.text_input("What topic would you like to write about?")
    target_audience = st.text_input("Who is your target audience?")
    
    word_count = st.number_input(
        "Approximate word count",
        min_value=300,
        max_value=3000,
        value=800,
        step=100
    )
    
    tone = st.selectbox(
        "Select the tone of voice",
        ["Professional", "Casual", "Technical", "Conversational", "Educational"]
    )
    
    keywords = st.text_input("Enter target keywords (comma-separated)")

    if st.button("Generate Blog Post"):
        if topic and target_audience and keywords:
            with st.spinner('Generating your blog post... This may take a few minutes.'):
                blog_crew = BlogWriterCrew(
                    topic,
                    target_audience,
                    word_count,
                    tone,
                    keywords,
                    source_content
                )
                result = blog_crew.run()
                
                st.write("## Your Generated Blog Post")
                st.write(result)
                
                st.download_button(
                    label="Download Blog Post",
                    data=result,
                    file_name=f"blog_post_{topic.lower().replace(' ', '_')}.txt",
                    mime="text/plain"
                )
        else:
            st.error("Please fill in all the required fields to generate your blog post.")

    st.sidebar.title("Tips for Better Results")
    st.sidebar.write("""
    - Upload relevant source material for more accurate content
    - Be specific with your topic
    - Define your target audience clearly
    - Include relevant keywords
    - Choose a tone that matches your brand
    """)

if __name__ == "__main__":
    main()