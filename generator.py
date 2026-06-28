from ollama import chat


def generate_answer(context, question, mode="qa"):

    if mode == "summary":

        prompt = f"""
You are an AI Research Paper Assistant.

Using ONLY the context below, write a structured summary of the paper.

Your response must contain these sections:

## Paper Overview
Briefly explain what this paper is about.

## Problem Addressed
What problem are the authors trying to solve?

## Why This Problem Matters
Why is solving this problem important?

## Proposed Solution
Explain the proposed approach in simple language.

## Main Contributions
List the major contributions.

## Key Findings
Summarize the most important experimental findings.

Rules:
- Explain as if the reader is reading the paper for the first time.
- Use simple, natural language.
- Do NOT generate questions.
- Do NOT create a FAQ.
- Do NOT invent information.
- If information is unavailable, write:
  "Not discussed in the retrieved context."

Context:
{context}
"""

    elif mode == "methodology":

        prompt = f"""
You are an AI Research Paper Assistant.

Using ONLY the context below, explain the methodology.

Your response must contain these sections:

## Overall Idea

## Model / Architecture

## Data Used

## Training Procedure

## Important Techniques

## Why This Approach Works

Rules:
- Explain step by step.
- Assume the reader is new to the paper.
- Do NOT generate questions.
- Do NOT repeat the paper word-for-word.
- Do NOT invent information.
- If information is unavailable, write:
  "Not discussed in the retrieved context."

Context:
{context}
"""

    elif mode == "results":

        prompt = f"""
You are an AI Research Paper Assistant.

Using ONLY the context below, explain the experimental evaluation.

Your response must contain these sections:

## Experimental Setup

## Baselines Compared

## Main Results

## Why These Results Matter

Rules:
- Explain the meaning of the results instead of simply copying numbers.
- Do NOT explain the methodology again.
- Do NOT generate questions.
- Do NOT create a FAQ.
- Do NOT invent information.
- If information is unavailable, write:
  "Not discussed in the retrieved context."

Context:
{context}
"""

    elif mode == "limitations":

        prompt = f"""
You are an AI Research Paper Assistant.

Using ONLY the context below, explain the limitations of the proposed approach.

Your response must contain:

## Limitations

Rules:
- Summarize only limitations supported by the context.
- Do NOT invent limitations.
- If limitations are not explicitly discussed, write:
  "The paper does not explicitly discuss its limitations."

Context:
{context}
"""

    elif mode == "future_work":

        prompt = f"""
You are an AI Research Paper Assistant.

Using ONLY the context below, explain the future directions of this work.

Your response must contain:

## Future Work

Rules:
- If the paper explicitly discusses future work, summarize it.
- If no explicit future work exists but the discussion suggests future research directions, clearly state that these are inferred from the discussion.
- Do NOT invent unsupported information.
- Do NOT generate questions.

Context:
{context}
"""

    else:

        prompt = f"""
You are an AI Research Paper Assistant.

Answer the user's question using ONLY the provided context.

Rules:
- Explain clearly.
- Use simple language.
- Do NOT use outside knowledge.
- If the answer cannot be found in the context, reply exactly:
I could not find this information in the document.

Context:
{context}

Question:
{question}
"""

    response = chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.message.content.strip()