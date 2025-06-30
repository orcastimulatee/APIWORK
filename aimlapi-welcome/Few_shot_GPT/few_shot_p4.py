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

Input: 
1. A natural-language question in English.  
2. A list of glosses, each with a unique gloss ID.  
Your tasks:
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
    '''Was it successful for you? Did you have a great time or a bad one? With bad experiences? Let's hear more.
||$GEST-OFF^*#151 ||EINMAL1B#152||ICH2#153 ||WAR1*#154 || HAMBURG1#155 ||DORT1#156 ||ICH1 #157 ||HAMBURG1*#158 ||DORT1#159  ||SCHWIMMEN1*#160 || KAMPF1A#161 ||DEUTSCH1#162 ||MEISTERSCHAFT1#163 ||ICH1#164  ||DORTHIN-GEHEN1*#165
||SCHWIMMEN1*#166||ICH2 #167 ||$PROD*#168 ||SCHWIMMEN1#169 ||$PROD*#170 
|| ICH1#171 || GRENZE1A^*#172 || LOS-START2#173 || STARTSCHUSS1* [MG]#174 || $GEST-OFF^*#175 || $GEST-ABWINKEN1^#176
|| ICH2*#177 || FALLEN1^ [MG]#178 || ICH2*#179 || LAUFEN3^ [MG]#180 || ICH1 [MG]#181 || HIN-UND-HER1* [MG]#182 || BIS1#183 || ZIEL4#184
|| $NUM-EINER1A:1d* ein#185 || ZUSAMMEN-PERSON1^#186 || KNAPP1 knapp#187 || ICH1#188 || BEGLEITEN1A^ [MG]#189 || KOMMEN3*#190 || $INDEX1*#191 || FERTIG2*#192
||ICH1 #193||ATEMNOT1 [MG]#194
||SEHR6^* [MG]#195 ||WIE-FRAGE1* wie#196 ||KAPUTT4 #197
|| BEIDE2A*#198 || ICH1*#199 || LAUFEN8* lauf#200 || FALLEN2A^* [MG]#201 || FERTIG1B#202 || $GEST-OFF^*#203
|| ANSTRENGEND3*#204 || AKTIV1*#205 || WILLE6 [MG]#206 || HIN-UND-HER1*#207 || $GEST-OFF^*#208
|| $GEST^ aber#209 || SCHAFFEN1A* schaff#210 || $NUM-ORD1:2 zweite#211 || PLATZ9 platz#212
||ERFOLG2 erfolg#213
|| FERTIG1B#214 || $INDEX1 letztes mal#215 || LETZTE2A*#216 || AUS-VORBEI1#217 || NICHT-MEHR1A#218 || SCHWIMMEN1 schwimmen#219
|| BIS-JETZT1#220 || NICHT-MEHR1A nicht mehr#221 || SCHWIMMEN1 schwimmen#222 || NEIN3B^*#223 || HEUTE1* freizeit#224 || FREI1#225 || ZEIT7C*#226 || ZEIT7C*#227 || SCHWIMMEN1 schwimmen#228 || FERTIG4#229

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