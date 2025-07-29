from openai import OpenAI
import json
from openai import OpenAI
import json
from prompts import prompt_6
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
# Speaker B\n
DU1 || DEUTSCH1 || MEISTER2A || WIE-VIEL5* || MAL3* || $INDEX1 || DEUTSCH1 || MEISTER2A


# Speaker A\n"
$NUM-EINER1A:1 || $NUM-ZEHNER2A:8d || ENDE1^ || $NUM-EINER1A:1 || $NUM-ZEHNER2A:8d* || ICH1* || MEISTER2A
Output:
Entity: Speaker A:
DU1: B is having conversation with A, and B is asking A question, therefore when B said “you”, it means A.
ICH1*: A is saying. When A said “I”, it means A.

Entity: German championship:
|| DEUTSCH1 || MEISTER2A ||,
|| DEUTSCH1 || MEISTER2A,
|| MEISTER2A ||


'''

user_prompt = prompt_6

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

        '''

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
        '''

    except Exception as e:
        print("error：", e)

if __name__ == "__main__":
    main()
