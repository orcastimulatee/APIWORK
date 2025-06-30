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
1. Identify which glosses refer to entities.
2. Cluster glosses that refer to the same entity.

System:
You are a sign-language coreference resolution assistant.
1. Identify which glosses refer to entities.
2. Cluster glosses that refer to the same entity.
3. Assign each entity a new numeric entity ID.
4. Return a pure JSON object mapping each gloss ID to its entity ID.
5. Finally, list each entitys description in plain English.

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
    '''$GEST-OFF^*#0 ICH1#1 MG $GEST-OFF^#2 AUFWACHSEN1A#3 ICH2#4 AUFWACHSEN1A#5 aufwachsen $GEST-OFF^#6 ICH2#7 ich AUFWACHSEN1A#8 aufwachsen WIE-IMMER1*#9 TAUB-GEHÖRLOS1A*#10 GEBÄRDEN1A*#11 ICH1*#12  
AUFWACHSEN1A#13 BIS1#14 bis ICH1#15 $NUM-TEEN1:5#16 fünfzehn  
SCHULE3#18 schule ENTLASSEN1#19 SCHWIMMEN1#20 schwimmen $GEST-OFF^#21  
ICH1#22 AUFWACHSEN1A#23 BIS1#24 bis SCHULE3#25 schule ENTLASSEN1#26 entlassen $NUM-TEEN1:5#27 fünfzehn alt ALT5B#28 ICH1#29  
ELTERN1A#31 eltern FRAGE1#32 frage  
ERLAUBNIS3#33 erlaubt ICH1#34 $INDEX1#35 EINSTEIGEN1#36 MG ERSTES-MAL3A#37 erste mal gehörlosenverein TAUB-GEHÖRLOS1A#38 VEREIN2A#39 SCHWIMMEN1#40 schwimmen EINSTEIGEN1#41  
gehörlosen TAUB-GEHÖRLOS1A*#46 PERSON1*#47 UNTERHALTUNG2A#48  
ICH1#49 INTERESSE1B#50 MG SPASS1#51 spaß ALLE1A^#52  
VORHER1#53 vorher JUNG2#54 jung ICH1*#55 NICHT3A#56 DARF1#57 darf NICHT3A#58 nicht VEREIN2A#59 verein $INDEX1#60  
JETZT1#61 $INDEX1#62 $GEST-OFF^*#63
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