from openai import OpenAI
import json


base_url = "https://api.aimlapi.com/v1"
api_key = "2c43eb2b185545dcbfa1be051df6f2c8"  # 请确保这个 API key 是有效且已激活的
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

api = OpenAI(api_key=api_key, base_url=base_url)

def main():
    print("开始第一轮 API 调用...")
    try:
        # 第一轮调用
        first = api.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system",  "content": system_prompt},
                {"role": "user",    "content": user_prompt},
            ],
            temperature=0,
            max_tokens=5012,
        )
        print("第一轮完整响应：", first)

        assistant_reply = first.choices[0].message.content
        print("Assistant 回答：", assistant_reply)

        # 构造第二轮的 follow-up 提问
        follow_up = (
            "Please, in English, expand the description for each entity cluster (all entity IDs). "
            "For every entity, explain what it represents and why the glosses were grouped into that cluster."
        )

        print("开始第二轮 API 调用...")
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

        print("第二轮回答：", second.choices[0].message.content)

    except Exception as e:
        print("发生错误：", e)

if __name__ == "__main__":
    main()

