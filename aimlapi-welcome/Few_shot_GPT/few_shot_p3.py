from openai import OpenAI
import json
from openai import OpenAI
import json
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
api_key = "2c43eb2b185545dcbfa1be051df6f2c8"  # 请确保这个 API key 是有效且已激活的

system_prompt = '''You are a sign language coreference resolution assistant.  
Input: a list of glosses, each with a unique gloss ID.  
1. Identify which glosses refer to entities.  
2. Cluster glosses that refer to the same entity.  

——— Example ———

Context: A person is talking to someone else about Diana.

Input:
$INDEX1#0
$ALPHA1:D-I-A#1
STILL2*#2
TO-SEE1*#3
$INDEX1#4
MEMORY-OR-REMINDER2#5
PAST-OR-BACK-THEN2#6
$GEST-OFF^#7

Output (pure JSON):
{
"$INDEX1#0": 0,
"$ALPHA1:D-I-A#1": 0,
"$INDEX1#4": 1,
"MEMORY-OR-REMINDER2#5": 1
}

Entity descriptions:
Entity 0: “Diana”
Entity 1: “memory / reminder of the past”
'''

user_prompt = (
    '''|| DANN1B* und dann #132 || SPÄTER10* später #133 || UM2A um #134 || [[ICH1]] #135 || KEGELN1 kegeln #136
|| JAHR1B* zehn jahre #137 || MITGLIED1 mitglied #138 || KEGELN1 kegeln #139 || UND2A* #140
|| FAHREN3* [MG] #141 || AKTIV3* aktiv aktiv #142 || KEGELN1* #143 || FERTIG1B #144 || SCHLUSS1 #145
|| BIS1* bis #146 || [[ICH2]] ich #147 || KNIE1B knie #148 || FERTIG1B [MG] #149 || VORBEI4* #150 || $GEST-OFF^* #151

'''
)

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