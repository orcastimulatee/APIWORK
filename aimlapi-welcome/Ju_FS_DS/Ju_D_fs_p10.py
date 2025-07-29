
import requests
import json
from prompts import prompt_10
# References:
# [1] AI/ML API Dashboard — App Interface
#     https://aimlapi.com/app/
# [2] AI/ML API Documentation — GPT-4o (OpenAI) Reference
#     https://docs.aimlapi.com/api-references/text-models-llm/openai/gpt-4o
# [3] AI/ML API Documentation — Homepage
#     https://docs.aimlapi.com/
# [4] AI/ML API Documentation — Deepseek Chat Reference
#     https://docs.aimlapi.com/api-references/text-models-llm/deepseek/deepseek-chat

# system and user prompt
system_prompt = """You are a sign language coreference resolution assistant.  
Input: a list of glosses, speaker A & B are having a conversaiton, sentences(words seperated by comma or full stop) are seperated by '''''', each gloss with a unique gloss ID.  
1. Identify which glosses refer to entities.  
2. Cluster glosses that refer to the same entity. 
——— Example ———
Input:
||FIRMA1B || $LIST1:1of1 || FLUGHAFEN2 || $LIST1:2of2d || MERCEDES1 || FABRIK6* || $LIST1:3of3d || $ALPHA1:J-A-C-O-B-S**


Output:
Entity:Companies:
FIRMA1B (All three mentioned after are companies)
$LIST1:1of1 || FLUGHAFEN2 (First company: Airbus. First company: Airbus (Two glosses classify together)is the First company name points to the companies entity)
$LIST1:2of2d || MERCEDES1  || FABRIK6* ||  (Second company: Mercedes factory.)Three glosses classify together)is the Second company name points to the companies entity)
$LIST1:3of3d || $ALPHA1:J-A-C-O-B-S** (Third company: Jacobs.)(Tow glosses combined together point to the companies entity.)

Note:
||$LISTx:xofy|| only does not mean anything, only when it joins with another gloss(In this example: names) make it point to the before entity:Companies.
Learn this example concept, and think step by step afterwards.
"""

user_prompt = prompt_10

# Follow-up question:
follow_up = (
    "Please, in English, expand the description for each entity cluster (all entity IDs). "
    "For every entity, explain what it represents and why the glosses were grouped into that cluster."
)

# using DS modle
url = "https://api.aimlapi.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 2c43eb2b185545dcbfa1be051df6f2c8",
}

# having the frist message lines.
messages = [
    {"role": "system",  "content": system_prompt},
    {"role": "user",    "content": user_prompt},
]

# 1. request for the first time.
resp1 = requests.post(
    url, headers=headers,
    json={
        "model": "deepseek-chat",
        "temperature": 0,
        "max_tokens": 5025,
        "messages": messages,
    }
)
data1 = resp1.json()
ds_reply = data1["choices"][0]["message"]["content"]
print("=== DS First Reply ===")
print(ds_reply)

# 2. follow up messgages list
messages_followup = [
    {"role": "system",    "content": system_prompt},
    {"role": "user",      "content": user_prompt},
    {"role": "assistant", "content": ds_reply},
    {"role": "user",      "content": follow_up},
]

# 3. request the second time
resp2 = requests.post(
    url, headers=headers,
    json={
        "model": "deepseek-chat",
        "temperature": 0,
        "max_tokens": 5025,
        "messages": messages_followup,
    }
)
data2 = resp2.json()
ds_followup_reply = data2["choices"][0]["message"]["content"]
print("\n=== DS Follow-up Reply ===")
print(ds_followup_reply)
