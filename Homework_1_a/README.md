# How to run code

## 1. Create Conda Environment:

**conda env create -f environment.yml**

## 2. Activate Conda Environment:

**conda activate NLP_311**

## 3. Create Env File:

**touch .env** (feel free to use any text editor you are comfortable with) \
**vim .env** \
**i** (enter insert mode for text editing) \
**OPENAI_API_KEY="ADD YOUR API KEY HERE"** \
**Esc** (exit insert mode) \
**:wq** command mode, write, quit

## 4. Clone Project Repo:

**git clone https://github.com/Ahooker90/NLP.git**

## 5. Change Directory Into Assignment:

**cd Homework_1_a**

## 6. Run Application:

**chainlit run app.py -w** 


# Assignment Instructions

**Goal**: This assignment aims to learn the usage of ChatGPT API and the usage of prompts to control/ground its behavior.

**Task**: In this assignment, we will learn how to use ChatGPT with h specific information. Initially, we will provide the API with a knowledge base. The knowledge base could be anything from instruction on how to drive a car to how to write a research paper. Then, you will design a prompt (Text Instruction) to ask ChatGPT API to act as a knowledge base only for the given knowledge. Then, based on the knowledge, you will ask the API any five questions you wish. Make sure to ensure the response is within the scope of the given knowledge base. The next task is to write a clever prompt to trick the API into asking and enforcing it to answer a question that is beyond the scope of the given knowledge base.

The following steps should be followed:

**Input Formation**: Find a knowledge base on any topic. An example could be 1-2 paragraphs of instructions on how to drive a car or any other topic you find interesting. (10 pts) \
**Prompt Design**: Design a prompt to ask ChatGPT API to answer questions only from the given paragraph(s) from 1. (30 pts) \
**Q/A**: Design 5 questions based on the paragraph. Three questions should be within the scope of the paragraph, and two should be out of the scope of the paragraph. (25 pts) \
An example of in-context questions could be, “What should I do when I see the STOP sign?”
Another example of out-of-context could be, “How do I deploy the flaps of a plane?” \
**Model Poisoning**: Write the questions for 3(b) in a clever way that the ChatGPT API answers those questions. (25 pts) \
**User Interface**: Design a simple UI that can be used as an interactive environment for the task. (10 pts) \
**Sample input-output**:

**User**: Input (1),

**User**: Write the prompt (2)

**User**:  Ask Q1 (3)

**ChatGPT**: Answer to Q1.

**User**: Poisoning Question (4)

**ChatGPT**: Response

 

Deliverables:

Upload your code written in Python to interact with ChatGPT.
Upload the interaction as a text file.
Upload a screenshot(image file) of the designed UI.