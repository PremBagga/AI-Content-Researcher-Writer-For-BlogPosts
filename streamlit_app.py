from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(page_title="Content Researcher & Writer", page_icon="✍️", layout="wide")

# Title and Description
st.title("📝 Content Researcher & Writer, By Prem Bagga")
st.markdown("Generate blog posts about any topic using AI agents.")

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Content Settings")
    
    # Topic Input
    topic = st.text_area("Enter Your Topic", height=100, placeholder="Enter your topic here...")

    # LLM Settings
    st.markdown("### 🔧 LLM Settings")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)

    # Divider
    st.markdown("---")

    # Generate Button
    generate_button = st.button("🚀 Generate Content", type="primary", use_container_width=True)

    # Instructions
    with st.expander("ℹ️ How To Use"):
        st.markdown("""
        1. Enter your desired content topic.
        2. Adjust the temperature (higher = more creative).
        3. Click **Generate Content** to start.
        4. Wait for AI to generate your article.
        5. Download the result as a Markdown file.
        """)


def generate_content(topic):
    """Function to generate content using CrewAI agents."""
    if not topic.strip():
        st.error("⚠️ Please enter a topic before generating content.")
        return ""

    # llm = LLM(model="deepseek-ai/deepseek-r1")
    llm = LLM(model="groq/deepseek-r1-distill-llama-70b")

    # Web Search Tool
    search_tool = SerperDevTool(n=10)

    # Research Analyst Agent
    senior_research_analyst = Agent(
        role="Senior Research Analyst",
        goal=f"Research, analyze, and synthesize information on {topic}.",
        backstory="""You're an expert research analyst with advanced web research skills.
        You excel at finding, analyzing, and synthesizing information from across the internet.
        You're skilled at distinguishing reliable sources, fact-checking, and cross-referencing.""",
        allow_delegation=False,
        verbose=False,
        tools=[search_tool],
        llm=llm
    )

    # Content Writer Agent
    content_writer = Agent(
        role="Content Writer",
        goal="Transform research findings into engaging blog posts while maintaining accuracy.",
        backstory="""You're a skilled content writer specialized in making technical research accessible.
        You balance engaging writing with accuracy, ensuring all facts are properly incorporated.""",
        allow_delegation=False,
        verbose=False,
        llm=llm
    )

    # Research Task
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
        agent=senior_research_analyst
    )

    # Writing Task
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
        agents=[senior_research_analyst, content_writer],
        tasks=[research_task, writing_task],
        verbose=False
    )

    return crew.kickoff(inputs={"topic": topic})


# Main Content Generation
if generate_button:
    with st.spinner("⏳ Generating content... This may take a moment."):
        try:
            result = generate_content(topic)
            if result:
                st.markdown("## 📜 Generated Content")
                st.markdown(result)

                # Download Button
                st.download_button(
                    label="📥 Download Content",
                    data=result,
                    file_name=f"{topic.lower().replace(' ', '_')}_article.md",
                    mime="text/markdown"
                )
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

# Footer
st.markdown("---") 
st.markdown("🚀 Built with CrewAI & DeepseekR1 Model")
