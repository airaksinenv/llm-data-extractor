# llm-data-extractor (Customer project 2)
-Valtteri Airaksinen TTV20SAI / Valio Primary production team 

This repository contains code and documentation about extracting unstructured data and using an LLM -model to turn it into structured JSON data 

### Course requirements
- 200h of documented work.
- All documentation must be done in English.
- The following documents must be created during the course:
    - Customer requirements specification (table)
    - Project plan
    - Architecture plan
    - Final report
    - Test plan and report (not mandatory)
    - Customer value assessment document
    - Self-assessment form

- The course must include the following elements:

    - A customer need, described through customer requirements
    - Application of AI to the problem (It is not necessary to train a model yourself, but you must justify why you choose to adopt an existing AI solution if one is available.)
    - Evaluation of customer value (including customer satisfaction, fulfillment of customer requirements, an estimate of how much the customer might be willing to pay for the project, and what could be a potential follow-up project the customer might purchase)
    - Preparation of a test plan and reporting of results (not mandatory)

# Models

## Ollama


### Download Ollama:

https://ollama.com/download

---


### User guide

Startup command:

`ollama serve`

Fetch the models:

Open a new terminal -> Activate venv

`source .venv/Scripts/activate`

You can now select the model you want and fetch it for example with the command:

`ollama pull llama3:8b`

### Llama models
Available Llama 3 models:

| Name | Size |
|:-:|:-:|
| llama3:8b | 4.7GB |
| llama3:70b | 40GB |
| llama3.1:8b | 4.9GB |
| llama3.1:70b | 43GB |
| llama3.1:405b | 243GB |
| llama3.2:1b | 1.3GB |
| llama3.2:3b | 2GB |
| llama3.3:70b | 43GB |
---

