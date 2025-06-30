import requests
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

system_prompt = '''You are a sign language coreference resolution assistant.  
Input: a list of glosses, each with a unique gloss ID.  
1. Identify which glosses refer to entities.  
2. Cluster glosses that refer to the same entity.  
'''

user_prompt = (
    '''|| VORHER1#53 vorher  
|| JUNG2#54 jung  
|| ICH1*#55  
|| NICHT3A#56  
|| DARF1#57 darf  
|| NICHT3A#58 nicht  
|| VEREIN2A#59 verein  
|| $INDEX1#60  

|| JETZT1#61  
|| $INDEX1#62  
|| $GEST-OFF^*#63  

|| UNTERHALTUNG2A#64  
|| TRAINING1#65 training  
|| SCHWIMMEN1#66 schwimmen  
|| HIN-UND-HER1*#67  

|| $INDEX1#68 jugendleiter  
|| JUNG2#69  
|| LEITEN1B#70  
|| $INDEX1#71  
|| ZUSAMMEN1A*#72  
|| PFLEGE1#73 pflegen  
|| AUFPASSEN1A#74 aufpassen  
|| ZUSAMMEN1A*#75  
|| UNTERHALTUNG2A#76  

|| INTERESSE1B#77 interesse  
|| ERWACHSENE2A*#78 erwachsene  
|| ICH1#79  
|| SPASS1#80 spaß  
|| UNTERHALTUNG2A#81  

|| MEHR1*#82 mehr  
|| ERFAHRUNG2B#83  
|| $INDEX1#84  
|| ICH2#85  
|| UNTERHALTUNG2A#86  
|| ALLE2A^#87  

|| UND-DANN1#88 und dann  
|| JUNG2#89  
|| LEITEN1B#90  
|| TERMIN1A#91 termin  
|| DANN1A#92 und dann  
|| EINMAL1B#93 einmal samstag  
|| SAMSTAG1#94  
|| ICH2#95  
|| ZUSAMMEN1A*#96 zusammen  
|| AUSFLUG2*#97 ausflug  

|| UNTERHALTUNG2A#98  
|| SPIELEN2#99 und spielt  
|| GEBÄRDEN1G*#100  
|| MEHR1*#101 mehr  
|| VIEL1A#102 viel  
|| SPASS1#103 spaß  

|| UND3*#104  
|| DANN1A*#105  
|| ZUSAMMEN1A*#106  
|| DEUTSCH1#107  
|| MEISTERSCHAFT1#108  
|| AUCH3A#109 auch  
|| TAUB-GEHÖRLOS1A#110 gehörlose  
|| FAHREN3#111  
|| ZUSAMMEN1A*#112  
|| JUNG2#113 jugendliche  
|| ALLE1A*#114  
|| FAHREN1*#115  
|| MIT1A#116  
|| ERWACHSENE2A*#117 erwachsene  

|| AUCH3A*#118 auch  
|| SCHWIMMEN1#119 schwimmen mitmachen  
|| MIT1A#120  
|| MACHEN2#121  
|| MASSE-PERSON3^*#122  

|| FAHREN3#123 MG  
|| ZUG2A#124 zug  
|| UNTERHALTUNG2A#125  
|| SPASS1*#126 spaß abenteuer  
|| ABENTEUER1#127  
|| VIEL4#128  
|| WIR1A*#129  
|| FERTIG1B#130  
|| $GEST-OFF^*#131
    '''
)

url = "https://api.aimlapi.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 2c43eb2b185545dcbfa1be051df6f2c8",
}

follow_up = (
    "Please, in English, expand the description for each entity cluster (all entity IDs). "
    "For every entity, explain what it represents and why the glosses were grouped into that cluster."
)

url = "https://api.aimlapi.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 2c43eb2b185545dcbfa1be051df6f2c8",
}


resp1 = requests.post(
    url, headers=headers,
    json={
        "model": "deepseek-chat",
        "temperature": 0,       
        "max_tokens": 5025,        

        "messages": [
            {"role": "system",  "content": system_prompt},
            {"role": "user",    "content": user_prompt},
        ]
    }
)
data1 = resp1.json()
ds_reply = data1["choices"][0]["message"]["content"]
print("=== DS First Reply ===\n", ds_reply)


resp2 = requests.post(
    url, headers=headers,
    json={
        "model": "deepseek-chat",
        "temperature": 0,
        "max_tokens": 5025,
        "messages": [
            {"role": "system",    "content": system_prompt},
            {"role": "user",      "content": user_prompt},
            {"role": "assistant", "content": ds_reply},
            {"role": "user",      "content": follow_up},
        ]
    }
)
data2 = resp2.json()
print("\n=== DS Follow-up Reply ===\n", data2["choices"][0]["message"]["content"])