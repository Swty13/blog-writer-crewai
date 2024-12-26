from crewai import Task
from textwrap import dedent
from datetime import date

class BlogTasks:
    def research_task(self, agent, topic, target_audience, keywords, source_content=None):
        source_instruction = ""
        if source_content:
            source_instruction = f"""
                Analyze and incorporate insights from the provided source material:
                {source_content}
                
                Extract key information, statistics, and insights from this material
                to enhance the blog post. Ensure proper attribution when using
                specific information from the source.
            """
        
        return Task(
            description=dedent(f"""
                Conduct comprehensive research on the blog topic, gathering
                credible information, statistics, and insights. Focus on finding
                unique angles and valuable information that will resonate with
                the target audience.
                
                {source_instruction}
                
                Your final answer must be a detailed research report including:
                - Key findings and insights
                - Relevant statistics and data
                - Competitor content analysis
                - Trending subtopics
                - Valuable sources to reference
                {self.__quality_bonus()}

                Topic: {topic}
                Target Audience: {target_audience}
                Target Keywords: {keywords}
            """),
            agent=agent,
            expected_output="Detailed research report with key insights, statistics, and valuable sources"
        )


    def strategy_task(self, agent, topic, target_audience, tone, word_count):
        return Task(
            description=dedent(f"""
                Develop a comprehensive content strategy for the blog post.
                Create an outline that will engage the target audience while
                optimizing for search engines. Consider the user intent and
                how to best structure the content to provide value.
                
                Your final answer must include:
                - Proposed headline options
                - Content outline with subheadings
                - Key points to cover
                - SEO recommendations
                - Content flow and structure
                - Tone and style guidelines
                {self.__quality_bonus()}

                Topic: {topic}
                Target Audience: {target_audience}
                Tone of Voice: {tone}
                Target Word Count: {word_count}
            """),
            agent=agent,
            expected_output="Complete content strategy with outline, SEO recommendations, and style guidelines"
        )

    def writing_task(self, agent, topic, tone, word_count):
        return Task(
            description=dedent(f"""
                Write an engaging and informative blog post based on the
                research and content strategy provided. Create content that
                is both valuable to readers and optimized for search engines.
                
                The blog post must:
                - Follow the outlined structure
                - Maintain consistent tone and style
                - Include relevant examples and evidence
                - Incorporate proper transitions
                - Be engaging and well-written
                - Meet the target word count
                {self.__quality_bonus()}

                Topic: {topic}
                Tone of Voice: {tone}
                Target Word Count: {word_count}
            """),
            agent=agent,
            expected_output="Complete, well-written blog post following the content strategy and guidelines"
        )

    def editing_task(self, agent, tone, target_audience):
        return Task(
            description=dedent(f"""
                Review and polish the blog post to ensure it meets high
                quality standards. Check for clarity, coherence, and
                engagement while maintaining the intended tone and style.
                
                Your editing must focus on:
                - Grammar and spelling
                - Content clarity and flow
                - Tone consistency
                - SEO optimization
                - Readability and engagement
                - Fact-checking
                - Formatting and structure
                
                Provide the final edited version along with a summary
                of major improvements made.
                {self.__quality_bonus()}

                Tone of Voice: {tone}
                Target Audience: {target_audience}
            """),
            agent=agent,
            expected_output="Polished blog post with editing summary and improvements made"
        )

    def __quality_bonus(self):
        return "Exceptional quality work will be rewarded with a significant bonus!"