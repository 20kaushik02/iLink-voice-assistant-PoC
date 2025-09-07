# Initial questions to define and clarify the problem

## 1. Business Context and Goals

- What specific problems are the field data scientists experiencing currently?

- **What is the primary goal of this voice assistant: efficiency, data capture, information access, or something else?**

- How will you measure the success of this PoC? - time saved, error-freeness, better UX, etc.

- Is this PoC meant to validate technical feasibility, test user adoption, or measure potential business value?

## 2. Users and Environment

- Who are the target users - junior scientists, senior consultants, site managers?

- In what environments will they use the assistant (offices, field sites, noisy areas)?

- Do they have reliable internet access in these environments?

- **In what ways will they interact with the assistant? Will they primarily use mobile devices, laptops, headsets, or wearables? Do they also have access to a PC/laptop?**

## 3. Scope of Functionality

- **Which workflows are most critical: note-taking, document lookup, timed reminders, communication?**

- Should the assistant be proactive (push reminders) or reactive (respond only to queries)?

- Is integration with collaboration tools (Teams, Outlook, Slack, SharePoint) important for the PoC?

## 4. Data and Knowledge Sources

- What kinds of documents should the assistant work with (PDFs, reports, manuals, SharePoint knowledge base, Excel spreadsheets, Python notebooks)?

- Are these documents updated? If so, how frequently?

- **Are there sensitive/confidential data that must stay on-premises? How are they distinguished from non-confidential data?**

- Should the assistant access external resources as well (e.g., public standards, OSHA guidelines, Internet)?

- How accurate/complete are the documents? Are there gaps in the knowledge available?

## 5. Technology and Integration

- Do you have a preferred technology stack (Azure, AWS, Google Cloud)?

- Are there existing AI/LLM investments (OpenAI subscription, custom ML models) we should leverage?

- Is integration with internal systems (ERP, CRM, project management tools) expected in this PoC?

## 6. Security, Privacy and Compliance

- What are the data security/compliance requirements (GDPR, HIPAA, SOC2, industry standards)?

- **Can data be processed in the cloud, or must it remain on-premises?**

- Are there restrictions on storing voice recordings or transcripts?

## 7. User Experience

- Should the assistant respond via voice, text, or both?

- How natural should the interaction be - fixed set of commands, or fully conversational?

- What’s the tolerance for latency - Within a second? Less than 5 seconds? More?

- **Should the PoC include a user interface (dashboard, mobile app) or remain voice-only?**

- Do users expect offline functionality, or is always-online acceptable?

## 8. Timeline and Deliverables

- What are the minimum features you must see in the PoC demo?

- Who are the stakeholders evaluating the outcome (technical, business, end-users)?

- **Should we prioritize breadth (many small features) or depth (fewer but polished features)?**

- After the PoC, what’s the envisioned next step - develop from it as a pilot version, integration with minimal changes, or mostly discard?

## 9. Risks and Constraints

- What are the biggest risks you foresee (adoption, accuracy, cost, security)?

- What constraints should I be aware of (budget, licenses, existing vendor lock-in)?

## 10. Long-Term Vision

- If the PoC is successful, how do **you** imagine this scaling to production?

- Would you want multi-user/team support, or focus only on individual assistants?

- Do you see this evolving into a broader company-wide knowledge assistant?
