"""
Simple maps4fs documentation Q&A bot
No greetings, just pure technical answers for community support
"""

from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import OllamaEmbeddings, OllamaLLM

from maps4fsbot.config import (
    CHROMA_DB_DIR,
    EMBEDDING_MODEL,
    LLM_MODEL,
    OLLAMA_BASE_URL,
    TOP_K_RESULTS,
)

# Enhanced prompt to prevent hallucinations and provide accurate information
PROMPT_TEMPLATE = """You are a technical support assistant for maps4fs, which is a web application for creating custom maps for Farming Simulator games.

IMPORTANT CONTEXT:
- maps4fs is a WEB APPLICATION accessible at https://maps4fs.xyz (main website)
- Documentation is available at https://maps4fs.gitbook.io/docs/
- There is NO CLI version of maps4fs - do not suggest command-line usage
- Users interact with maps4fs through a web browser interface
- The application helps create custom maps for Farming Simulator games (FS22, FS25, etc.)
- All functionality is accessed through the web interface, not through terminal commands

CRITICAL LINK RULES - FOLLOW THESE EXACTLY:
- You can ONLY create links if the documentation explicitly provides the exact URL or exact path components
- If you want to reference documentation sections, just mention the topic name WITHOUT creating a link
- When in doubt, NO LINK - just direct users to https://maps4fs.gitbook.io/docs/ to find the information
- NEVER construct URLs unless you have the exact path from the provided documentation

When providing answers:
- Be direct and technical. Include specific steps, file paths, or procedures when available from the documentation
- Direct users to https://maps4fs.xyz for the main application
- If the documentation doesn't contain information to answer the question, clearly state that
- Do not add greetings or pleasantries - just provide the answer
- Do not invent features, commands, or capabilities not mentioned in the documentation

Answer using ONLY the provided documentation below.

Documentation:
{context}

Question: {question}

Answer:"""


def format_docs(docs):
    """Format retrieved documents for context"""
    return "\n\n".join(doc.page_content for doc in docs)


def answer_question(question: str) -> str:
    """Answer the hardcoded question using the knowledge base"""

    print(f"Question: {question}")
    print("\nLoading knowledge base...")

    # Load embeddings and vector store
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL, base_url=OLLAMA_BASE_URL)
    vectorstore = Chroma(persist_directory=CHROMA_DB_DIR, embedding_function=embeddings)

    # Initialize LLM
    print("Initializing model...")
    llm = OllamaLLM(
        model=LLM_MODEL, temperature=0.2, base_url=OLLAMA_BASE_URL
    )  # Low temperature for factual answers

    # Setup retriever
    retriever = vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": TOP_K_RESULTS}
    )

    # Create simple QA chain
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    qa_chain = (  # type: ignore
        {"context": retriever | format_docs, "question": RunnablePassthrough()}  # type: ignore
        | prompt
        | llm
        | StrOutputParser()
    )

    # Generate answer
    print("Generating answer...\n")
    print("=" * 80)

    answer = qa_chain.invoke(question)
    print(answer)

    print("=" * 80)

    # Show retrieved chunks for debugging
    docs = retriever.invoke(question)
    print(f"\n[Used {len(docs)} chunks from documentation]")
    print("Retrieved sources:")
    for i, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "Unknown")
        print(f"  {i}. {source}")

    return answer
