# from crewai import Agent,Task , Crew , LLM
# from crewai_tools import SerperDevTool

# from dotenv import load_dotenv

# load_dotenv()

# topic = "Medical Industry Using Generative AI"

# #Tool1
# # llm = LLM(model ="gpt-3.5-turbo")
# llm = LLM(model ="llama-3.3-70b-versatile")

# #Tool2
# search_tool = SerperDevTool(n=10)

# #Agent1 - You can get all these parameters through crewai website
# Senior_Research_Analyst = Agent(role = "Senior_Research_Analyst",
#                                 goal = f"Research , analyze , and synthesize comprehensive information on {topic} from reliable web sources",
#                                 backstory="You're an expert research analyst with advanced web research skils."
#                                 "You excel at finding , analyzing , and synthesizing information from."
#                                 "across the internet using search tools. you're skilled at "
#                                 "distinguishing reliable sources from unreliable ones,"
#                                 "fact-checking, cross-referencing information , and"
#                                 "identifying key patterns and insights. you provide"
#                                 "well-organized research brief with proper with citations"
#                                 "and source verification. your analysis include both"
#                                 "raw data and interpreted insights, making complex "
#                                 "information accessible and actionable.",
#                                 allow_delegation=False,
#                                 verbose=True,
#                                 tools=[search_tool],
#                                 llm = llm
                                
#                                 )

# #AGENT2 - Content Writer
# content_writer = Agent(
#     role="Content Writer",
#     goal="Transform Research Findings Into Enagaging Blog Posts While Maintaining Accuracy",
#     backstory="You're skilled content writterspecialized in creating"
#     "engaging, accessible content from technical research."
#     "You work closely with the senior research analyst and excel at maintaining the perfect"
#     "balance between information and entertaining writing,"
#     "while ensuring all facts and citations from the research"
#     "are properly incorporated. you have a talent for making "
#     "complex topics approachable without oversimplifying them.",
#     allow_delegation=False,
#     verbose=True,
#     llm = llm
# )

# #  Task 1 : Comprehensive Task For Senior_Research_Analyst Agent 1
# research_task = Task(
#     description=("""1. Conduct comprehensive research on {topic} indulging:
#                        -Recent Development And News
#                        -key industry trends and innovations
#                        -Expert opinions and analysis
#                        -Statistical Data and market insights
#                     2.Evaluate source credibility and fact-check all information
#                     3.Organize findings into structured research brief
#                     4.Include all relevent citations and sources"""),
#     expected_output=""" A detailed research report containing:
#                      -Executive summary of key findings
#                      -Comprehensive analysis of current trends and developments
#                      -List of verified facts and statistics
#                      -All citations and links to original sources
#                      -Clear Categorization of main theme and patterns
#                      Please format with clear sections and bullet points for easy reference.""",
#     agent=Senior_Research_Analyst                 )


# #Task 2 : Content_Writing
# writing_task = Task(
#     description =( """ Using this research brief provided, create an engaging blog post that:
#                      1.Transform Tecnical information into accessible content
#                      2.Maintains all factual accuracy and citations from the research
#                      3.Includes : 
#                       - Attention grabbing introduction
#                        -well-structured body sections with clear headings
#                         -Compelling conclusion
#                      4. Preserves all source citations in [Source: URL] format
#                      5. Includes a references section at the end            """),
#     expected_output="""A polished blog post in markdown format that : 
#     -Engages readers while maintaining accuracy
#     -Contains properly structured sections
#     -Includes Inline citations hyperlinked to the original source url
#     -Presents information in an accessible yet informative way
#     -Follows proper markdown formatting , use H1 for the title and H3 for the sub-sections"""   ,
#     agent=content_writer              
# )
# # Crew Class , crew oblect
# crew = Crew(
#     agent=[Senior_Research_Analyst,content_writer],
#     tasks= [research_task ,writing_task],
#     verbose=True
# )

# result = crew.kickoff(inputs={"topic":topic})

# print(result)

import os
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")


if not groq_api_key:
    raise ValueError("GROQ_API_KEY is missing. Check your .env file!")

# Set up LLM with Groq API
# llm = LLM(model="llama3-70b", provider="groq", api_key=groq_api_key)

# Set up LLM with Groq API
# llm = LLM(model="llama-3.3-70b-versatile", provider="groq", api_key=groq_api_key)
llm = LLM(model="groq/deepseek-r1-distill-llama-70b")



# Set up web search tool
search_tool = SerperDevTool(n=10)

# Topic
topic = "Medical Industry Using Generative AI"

# Agent 1: Senior Research Analyst
Senior_Research_Analyst = Agent(
    role="Senior Research Analyst",
    goal=f"Research, analyze, and synthesize information on {topic}.",
    backstory="""You're an expert research analyst with advanced web research skills.
    You excel at finding, analyzing, and synthesizing information from across the internet.
    You're skilled at distinguishing reliable sources, fact-checking, and cross-referencing.""",
    allow_delegation=False,
    # verbose=True,
    verbose=False,
    tools=[search_tool],
    llm=llm
)

# Agent 2: Content Writer
content_writer = Agent(
    role="Content Writer",
    goal="Transform research findings into engaging blog posts while maintaining accuracy.",
    backstory="""You're a skilled content writer specialized in making technical research accessible.
    You balance engaging writing with accuracy, ensuring all facts are properly incorporated.""",
    allow_delegation=False,
    # verbose=True,
    verbose=False,
    llm=llm
)

# Task 1: Research Task
# research_task = Task(
#     description=f"""Conduct research on {topic}, including:
#         - Recent developments and news
#         - Key industry trends and innovations
#         - Expert opinions and analysis
#         - Statistical data and market insights.
#         Ensure all sources are cited and fact-checked.""",
#     expected_output="""A detailed research report including:
#         - Executive summary
#         - Industry trends and expert analysis
#         - Verified facts and statistics
#         - Cited sources with URLs
#         - Well-organized sections with bullet points.""",
#     agent=Senior_Research_Analyst
# )
research_task = Task(
    description=f"""Conduct a brief research summary on {topic}, covering:
        - 3 recent news highlights
        - 3 major industry trends
        - 2 expert opinions
        - 2 key statistics (only relevant ones).
        Ensure accuracy and include 2-3 source links.""",
    expected_output="""A concise research summary including:
        - Short executive summary (Max 100 words)
        - 3 key industry trends (Brief, 2 sentences each)
        - 2 expert insights (1 sentence each)
        - 2 statistical data points
        - 2-3 cited sources with hyperlinks only.
        Keep bullet points minimal and concise.""",
    agent=Senior_Research_Analyst
)


# Task 2: Writing Task
# writing_task = Task(
#     description="""Using the research brief, create an engaging blog post that:
#         - Transforms technical info into accessible content
#         - Maintains accuracy and citations
#         - Has a structured format with headings
#         - Includes an introduction, body, and conclusion.
#         - Uses proper Markdown formatting.""",
#     expected_output="""A polished blog post in Markdown with:
#         - Engaging, accurate content
#         - Structured sections with H1 & H3 headings
#         - Inline citations with hyperlinks
#         - References at the end.""",
#     agent=content_writer
# )
writing_task = Task(
    description="""Create a concise, engaging blog post from the research brief:
        - Summarize key insights in a simple and engaging style.
        - Keep explanations concise (avoid unnecessary details).
        - Use a clear structure with headings (Intro, Body, Conclusion).
        - Include only essential citations (2-3 hyperlinks).
        - Format using Markdown with minimal complexity.""",
    expected_output="""A structured Markdown blog post with:
        - Clear, engaging writing (max 500 words).
        - Concise sections with H1 and H3 headings.
        - Inline citations (max 2-3 relevant hyperlinks).
        - A short references section at the end.""",
    agent=content_writer
)


# Crew: Combining Agents and Tasks
crew = Crew(
    agents=[Senior_Research_Analyst, content_writer],  # Fixed from `agent=`
    tasks=[research_task, writing_task],
    # verbose=True
    verbose=False
)

# Run the AI Crew
try:
    result = crew.kickoff(inputs={"topic": topic})
    print("\n--- Final Output ---\n")
    print(result)
except Exception as e:
    print(f"Error during AI execution: {e}")

# venv\scripts\activate
# python app.py
