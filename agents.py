from crewai import Agent
from tools import *
from llm_call import get_llm

class BlogWriterAgents():

    def research_agent(self):
        return Agent(
            role='Research Specialist',
            goal='Conduct thorough research on blog topics and gather credible information',
            backstory="""Expert researcher with a keen eye for credible sources 
            and trending topics. Specialized in finding unique angles and 
            valuable insights for blog content.""",
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            verbose=True,
            llm=get_llm())

    def content_strategist(self):
        return Agent(
            role='Content Strategy Expert',
            goal='Develop engaging content strategies and optimize blog structure',
            backstory="""Experienced content strategist with expertise in SEO, 
            content planning, and audience engagement. Known for creating 
            compelling content structures that drive traffic.""",
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            verbose=True,
            llm=get_llm())

    def blog_writer(self):
        return Agent(
            role='Professional Blog Writer',
            goal="""Create engaging, well-researched, and SEO-optimized blog posts 
            that provide value to readers""",
            backstory="""Expert writer with years of experience in creating 
            compelling blog content. Skilled in various writing styles and 
            adapting tone for different audiences. Specializes in creating 
            content that balances information with engagement.""",
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            verbose=True,
            llm=get_llm())

    def editor(self):
        return Agent(
            role='Content Editor',
            goal="""Ensure blog posts are polished, error-free, and maintain 
            consistent quality and style""",
            backstory="""Meticulous editor with deep understanding of content 
            quality, grammar, and style guidelines. Expert in optimizing content 
            for readability and engagement while maintaining brand voice.""",
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            verbose=True,
            llm=get_llm())