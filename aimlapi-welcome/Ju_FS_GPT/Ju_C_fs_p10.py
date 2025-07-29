from openai import OpenAI
import json
from openai import OpenAI
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

base_url = "https://api.aimlapi.com/v1"
api_key = "2c43eb2b185545dcbfa1be051df6f2c8"  # This API will be avaliable until June of 26th,2025.IF not runable, please contact from email.

system_prompt = '''You are a sign language coreference resolution assistant.  
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
'''

user_prompt = prompt_10

api = OpenAI(api_key=api_key, base_url=base_url)

def main():
    print("Starting API ...")
    try:
        # frist round
        first = api.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system",  "content": system_prompt},
                {"role": "user",    "content": user_prompt},
            ],
            temperature=0,
            max_tokens=5012,
        )
        print("Frist round respond：", first)

        assistant_reply = first.choices[0].message.content
        print("Assistant：", assistant_reply)

        # follow up question 
        follow_up = (
            "Please, in English, expand the description for each entity cluster (all entity IDs). "
            "For every entity, explain what it represents and why the glosses were grouped into that cluster."
        )

        print("Starting second round API ...")
        second = api.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system",    "content": system_prompt},
                {"role": "user",      "content": user_prompt},
                {"role": "assistant", "content": assistant_reply},
                {"role": "user",      "content": follow_up},
            ],
            temperature=0,
            max_tokens=5012,
        )

        print("Secound round：", second.choices[0].message.content)

    except Exception as e:
        print("error：", e)

if __name__ == "__main__":
    main()
