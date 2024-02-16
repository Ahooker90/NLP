import os
import openai
import chainlit as cl
from dotenv import load_dotenv, find_dotenv

def setup_client():
    _ = load_dotenv(find_dotenv()) # read local .env file
    openai.api_key  = os.environ['OPENAI_API_KEY']
    return openai.OpenAI()
    
client = setup_client()
    
def get_completion(prompt, model="gpt-3.5-turbo"):

    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

def get_knowledge_base():
    knowledge_base = """
    Dark Souls[c] is a 2011 action role-playing game developed by FromSoftware and published 
    by Namco Bandai Games. A spiritual successor to FromSoftware's Demon's Souls, the game is
    the first in the Dark Souls series. The game takes place in the kingdom of Lordran, where
    players assume the role of a cursed undead character who begins a pilgrimage to discover
    the fate of their kind. A port for Windows featuring additional content, known as the Prepare
    to Die Edition, was released in August 2012. It was also released for consoles under the
    subtitle Artorias of the Abyss in October 2012.

    Dark Souls has been cited as one of the greatest video games ever made. Critics praised the
    depth of its combat, intricate level design, and use of flavor text. However, the game's
    difficulty was both praised and criticized for being unforgiving. The original Windows version
    of the game was less well-received, with criticism directed at several technical issues.
    By April 2013, the game had sold over two million copies worldwide. Its success led to the
    development of two sequels—Dark Souls II (2014) and Dark Souls III (2016)—while a remastered
    version was released in 2018.
    """
    return knowledge_base
def get_prompt(user_input):
    prompt = f"""
    You are a helpful assistant. Your role is to ONLY provide relevant information delimited in ####. 
    It is crucial that you do not make up information and if you do not know simply say "I do not know :(".
    You are not allowed to use any prior knowledge and are restricted to only what is delimted between the ####.
    
    If the user input is a list of questions send your response back in a numbered list.
    
    Example:
    user: What is a plane? What is water?
    assistnat: 
    1. <response 1>
    2. <response 2>
    
    ####{get_knowledge_base()}####

    Do not forget only provide information that was provided in the previous #### delimted text.
    {user_input}
    """
    return prompt


@cl.on_chat_start
def on_chat_start():
    from datasets import load_dataset
    print("A new chat session has started!")
    dataset = load_dataset("databricks/databricks-dolly-15k")
    print("Data Loaded!")
    
@cl.on_message
async def on_message(msg: cl.Message):
    response = get_completion(get_prompt(msg.content))
    await cl.Message(content=response).send()

@cl.on_stop
def on_stop():
    print("The user wants to stop the task!")

@cl.on_chat_end
def on_chat_end():
    print("The user disconnected!")
























