import requests
import json

# system prompt and user prompt
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
        "temperature": 0,       # 控制生成随机性（0.0–1.0）
        "max_tokens": 5025,        # 最多返回多少 token
        "messages": [
            {"role": "system",  "content": system_prompt},
            {"role": "user",    "content": user_prompt},
        ]
    }
)
data1 = resp1.json()
ds_reply = data1["choices"][0]["message"]["content"]
print("=== DS First Reply ===\n", ds_reply)

# 第二次 follow-up，同样加参数
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