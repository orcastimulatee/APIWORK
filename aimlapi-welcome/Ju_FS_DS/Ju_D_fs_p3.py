
import requests
import json
from prompts import prompt_3
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
Input: a list of glosses, sentences(words seperated by comma or full stop) are seperated by '|', each gloss with a unique gloss ID.  
1. Identify which glosses refer to entities.  
2. Cluster glosses that refer to the same entity.
——— Example ———

Input:
VACATION8B*  ||  I2*  ||  EXPERIENCE1B*  ||  A-MOMENT-AGO2*  ||  I2  ||  BETWEEN1B^*  ||  I1  ||  LONDON1*  ||  TO-COME1  ||  I1  ||  $GEST-OFF^*  |
|  BEAUTIFUL1A  |
|  I1  ||  $INDEX1  ||  $NUM-ONE-TO-TEN1A:8d  ||  TIMES3*  ||  LONDON1*  ||  $INDEX1  ||  I1  ||  LOVE1C  ||  LONDON1*  ||  CITY2*


Output:

entity 1: 'I'
- I2*
- I2
- I1
- I1
- I1
- I1
--
entity 2: 'London', a city name.
-LONDON1*
-LONDON1*
-LONDON1* CITY2*(CITY2* combined with LONDON1* to refer to a specific entity 'London')
"""

user_prompt = prompt_3

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

'''# 2. follow up messgages list
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
'''