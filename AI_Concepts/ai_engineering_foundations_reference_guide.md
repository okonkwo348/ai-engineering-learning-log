# AI Engineering Foundations: Complete Reference Guide

This reference guide is designed to be a complete, standalone document covering all core AI engineering concepts explored in our masterclass, based on modern AI engineering frameworks (such as Chip Huyen's *AI Engineering*).

---

## Table of Contents
1. [Tokens (The Atomic Building Blocks)](#1-tokens-the-atomic-building-blocks)
2. [Context Window (The Short-Term Memory)](#2-context-window-the-short-term-memory)
3. [Embeddings (The GPS Map of Meaning)](#3-embeddings-the-gps-map-of-meaning)
4. [Vector Search & Databases](#4-vector-search--databases)
5. [RAG (Retrieval-Augmented Generation)](#5-rag-retrieval-augmented-generation)
6. [Pydantic (The Backend Security Guard)](#6-pydantic-the-backend-security-guard)
7. [Function Calling & Autonomous Agents](#7-function-calling--autonomous-agents)
8. [Complete Mini Project Blueprint](#8-complete-mini-project-blueprint)

---

## 1. Tokens (The Atomic Building Blocks)

### Concept & Analogy
Computers and Large Language Models (LLMs) do not process full words or sentences raw. Instead, text is split into smaller units called **Tokens**. Think of tokens as **individual Lego pieces** of text—they can be whole words (`"cat"`), parts of words (`"ing"` in `"running"`), or single punctuation marks (`"!"`).

### Quotable Definition
> **Tokens:** *"The atomic Lego pieces of text—words, parts of words, or punctuation—that an AI model uses to read and write language."*

---

## 2. Context Window (The Short-Term Memory)

### Concept & Analogy
An LLM’s **Context Window** is its active working memory for a single session or prompt. 
* **Analogy:** Imagine a **physical whiteboard**. The AI can only read what fits on the whiteboard at one time. If your prompt, system instructions, and historical context exceed the size of the whiteboard, the oldest information gets erased or truncated.

### Quotable Definition
> **Context Window:** *"The AI's short-term memory limit (like a whiteboard) governing how much text it can hold and read at once during a session."*

---

## 3. Embeddings (The GPS Map of Meaning)

### Concept & Analogy
An **Embedding** takes a piece of text (a word, sentence, or document) and converts it into a list of numbers (a vector) representing coordinates on a massive multi-dimensional map of language.
* **Analogy:** Think of embeddings as **GPS coordinates on a map of meaning**. Sentences with similar meanings (e.g., *"The dog barked loudly"* and *"A puppy made a sharp noise"*) land close to each other on the map, even if they share zero matching words.

### Quotable Definition
> **Embeddings:** *"A numerical coordinate (vector) on a GPS map of meaning that places concepts with similar intent near one another."*

---

## 4. Vector Search & Databases

### Concept & Analogy
In a traditional database (SQL/Keyword search), searching for *"fixing a leaky faucet"* looks for exact spelling matches. If your manual says *"repairing a dripping pipe"*, traditional search misses it.

**Vector Search** converts your search query into embedding coordinates and shines a searchlight around those coordinates to retrieve the closest matching paragraphs, regardless of exact word choices.

### Quotable Definition
> **Vector Search:** *"Searching a database by conceptual location and meaning rather than exact keyword spelling."*

---

## 5. RAG (Retrieval-Augmented Generation)

### Concept & Analogy
Without RAG, an LLM relies solely on what it learned during training (a "closed-book exam"), which leads to outdated answers or hallucinations.

**RAG** gives the AI an **"open-book exam"**:
1. You store your company documents in a Vector Database.
2. When the user asks a question, Vector Search retrieves the 3-4 most relevant document paragraphs.
3. You hand those exact paragraphs to the LLM right before it answers.

```
[User Question] ──> [Vector Search] ──> [Pulls 3 Relevant Docs]
                                                  │
                                                  ▼
[Final Answer] <─── [LLM reads Docs + Question] ──┘
```

### Quotable Definition
> **RAG (Retrieval-Augmented Generation):** *"An open-book exam for AI: pulling real-world documents from a vector database right before generating an answer to eliminate hallucinations."*

---

## 6. Pydantic (The Backend Security Guard)

### Concept & Analogy
LLMs output unstructured text, which can easily crash your Python code if a key is missing or formatted incorrectly. 

**Pydantic** acts as a **strict backend security guard with a custom mold**. You define a class blueprint, and Pydantic forces the raw output from the LLM into a validated, type-safe Python object.

### Python Example
```python
from pydantic import BaseModel, Field

class RAGAnswer(BaseModel):
    answer: str = Field(description="The final answer to the user's question.")
    sources_used: list[str] = Field(description="List of document names referenced.")
    confidence_score: float = Field(description="Confidence rating between 0.0 and 1.0.")
```

### Quotable Definition
> **Pydantic:** *"A strict backend security guard that validates messy LLM outputs and forces them into clean, predictable data structures."*

---

## 7. Function Calling & Autonomous Agents

### Concept & Analogy
* **Function Calling (Tool Use):** Handing the LLM a single tool (like a weather API) with a Pydantic-powered user manual so it can request your Python code to run real actions.
* **AI Agent:** Taking function calling a step further by putting the LLM into an autonomous loop called **ReAct (Reason + Act)**. The agent chains multiple tools together step-by-step to achieve a larger goal.

```
           ┌─────────────────────────────┐
           ▼                             │
[User Goal] ──> [Think/Reason] ──> [Act: Tool Call] ──> [Observe Result] 
                                                              │
                                    (Goal Achieved?) ─────────┼───────┐
                                              │ No            │ Yes   │
                                              └───────────────┘       ▼
                                                              [Final Answer]
```

### Quotable Definition
> **AI Agent:** *"An autonomous AI system that uses a reasoning loop to chain multiple tool calls together step-by-step until a complex goal is achieved."*

---

## 8. Complete Mini Project Blueprint

Below is the complete, working Python implementation combining **RAG + Pydantic + Tool Calling Agent**:

```python
import json
from pydantic import BaseModel, Field
from openai import OpenAI

client = OpenAI()

# 1. KNOWLEDGE BASE (Simulated Vector Database)
COMPANY_DOCUMENTS = [
    {"id": "doc_1", "topic": "remote_work", "content": "Employees are permitted to work remotely up to 2 days per week with manager approval."},
    {"id": "doc_2", "topic": "vacation_policy", "content": "Full-time employees receive 20 days of paid annual leave per calendar year."},
    {"id": "doc_3", "topic": "it_security", "content": "All laptops must be locked when away from desk and encrypted using company MDM software."}
]

# 2. PYDANTIC TOOL DEFINITION
class SearchCompanyPolicy(BaseModel):
    query: str = Field(description="The policy topic or question to search for in the company knowledge base.")

def search_company_policy_tool(query: str) -> str:
    """Simulates Vector Search over company documents."""
    query_lower = query.lower()
    matches = []
    for doc in COMPANY_DOCUMENTS:
        if any(word in doc['content'].lower() or word in doc['topic'].lower() for word in query_lower.split()):
            matches.append(doc['content'])
            
    if matches:
        return "Found matching policies:\n- " + "\n- ".join(matches)
    return "No matching policy found in the knowledge base."

# Register tool schema derived from Pydantic
tools = [{
    "type": "function",
    "function": {
        "name": "search_company_policy_tool",
        "description": "Search internal company manuals and policies for HR, remote work, and IT rules.",
        "parameters": SearchCompanyPolicy.model_json_schema(),
    }
}]

# 3. AGENT EXECUTION LOOP
def run_support_agent(user_prompt: str):
    print(f"User Question: '{user_prompt}'")
    
    # Step 1: Initial Prompt to LLM with Tools
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an HR/IT assistant. Always check policy tools before answering policy questions."},
            {"role": "user", "content": user_prompt}
        ],
        tools=tools
    )
    
    message = response.choices[0].message
    
    # Step 2: Check for Tool Call
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        func_name = tool_call.function.name
        
        # Validate tool arguments using Pydantic
        raw_args = json.loads(tool_call.function.arguments)
        validated_args = SearchCompanyPolicy(**raw_args)
        
        # Step 3: Execute Tool
        tool_output = search_company_policy_tool(query=validated_args.query)
        
        # Step 4: Final LLM Generation
        final_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an HR/IT assistant. Always check policy tools before answering policy questions."},
                {"role": "user", "content": user_prompt},
                message,
                {"role": "tool", "tool_call_id": tool_call.id, "content": tool_output}
            ]
        )
        
        print(f"\nFinal Agent Answer:\n{final_response.choices[0].message.content}")

# Run Agent
run_support_agent("How many vacation days do I get each year?")
```