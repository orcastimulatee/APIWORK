from openai import OpenAI
import json
from openai import OpenAI
import json
from prompts import prompt_4
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
Input: a list of glosses, sentences(words seperated by comma or full stop) are seperated by , each gloss with a unique gloss ID.  
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
-LONDON1*  CITY2*

'''

user_prompt = prompt_4

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
