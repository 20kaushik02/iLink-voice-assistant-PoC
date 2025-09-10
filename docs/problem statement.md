# Problem Statement and Business Idea

## Scenario

- Digital services company that contracts out data scientists, who are occasionally sent into the field, in domains like construction, manufacturing, etc.
- I.e. domains where the person has limited opportunities for interaction with the systems at hand, due to various factors like cost, time, resources, planning and more.
- In such cases, they may not be able to operate at their full efficiency, and multitasking is hindered.

## Idea/Requirement

A voice assistant that can alleviate some of the troubles of the scientist in terms of information retrieval, communication, planning and other knowledge worker tasks.

## Success criteria

- MUST be voice-based so it can be interacted with in a mostly hands-free manner
- MUST be able to process natural language queries (as opposed to pre-determined command sets)
- MUST have access to and retrieve information from provided documents and data files relevant to the domain
- MUST demonstrate end-to-end flow, from user speaking a query to playing back
- Interface SHOULD be designed for use from portable devices such as mobiles, tablets

## Initial proposal

RAG pipeline supporting an LLM, interfaced through a web application, complete with speech-to-text and text-to-speech.

## Refining Problem Scope and Assumptions

- Choice of tech stack or architecture is left open, no restrictions
  - Opted to use local models/services as much as possible to reduce charges
- Performance and accuracy are not critical
  - Sacrificed accuracy of RAG system for development speed
  - Sacrificed accuracy and performance w.r.t. speech models and LLM for cost optimization
- Interface is open-ended
  - Opted to develop web-based interface for development speed and portability
- Additional functionality can be minimal
  - Tool-calling and better prompt engineering for LLM are beyond current scope
  - Dedicated document parsing/cleaning for accuracy of RAG is beyond current scope
