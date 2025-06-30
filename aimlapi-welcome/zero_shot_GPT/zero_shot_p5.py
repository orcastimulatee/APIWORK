from openai import OpenAI
import json
from openai import OpenAI
import json

base_url = "https://api.aimlapi.com/v1"
api_key = "2c43eb2b185545dcbfa1be051df6f2c8"  # 请确保这个 API key 是有效且已激活的

system_prompt = '''You are a sign language coreference resolution assistant. 
Input:
1. A conversation between two signers, A and B.
- Speaker B utterances are enclosed in double brackets [[ … ]].
- Speaker A utterances appear outside of [[ … ]].
2. Each utterance is given as a sequence of glosses, each gloss having a unique gloss ID.

Your tasks:
1. Identify which glosses refer to entities.  
2. Cluster glosses that refer to the same entity.  
'''

user_prompt = (
    '''[[WANN2*#544  NICHT-MEHR1A#545 DU1*#546]]
[[LETZTE1B#547 VORBEI4#548  $NUM-EINER1A:3d#549 $NUM-ZEHNER1:2d*#550 ALT8B#551 SCHLUSS1#552 DU1*#553]]
$GEST-NM-SPRECHEN1^[LM:oh]#230|| $GEST-NM-KOPFWIPPEN1^ [MG] #231||JUNG2 jung #232||$GEST-OFF^#233
||$NUM-ZEHNER1:2 zwanzig#234 ||$NUM-TEEN1:9 neunzehn#235 ||$NUM-ZEHNER1:2 zwanzig jahre alt#236 ||ALT5A#237 ||ICH1#238
[[SCHWIMMEN1#554 ALLEIN2#555 ANSTRENGEND5#556]]
[[HIN-UND-HER1#557 SCHWIMMEN1#558 ICH1#559 $PROD*#560 KEINE-LUST1#561]]
[[DU1*#562 SCHWIMMEN1*#563 HIN-UND-HER1*#564 ANSTRENGEND5#565 SEHR7*#566]]
$GEST-NM-KOPFSCHÜTTELN1^ [MG]#239 || KAMPF1A wettkampf#240 || WILLE6 [MG]#241 || ICH1*#242 || HIN-UND-HER1*#243
[[KAMPF1A#567 $ORAL^#568 TRAINING1#569 HIN-UND-HER1#570]]
$GEST-NM-KOPFNICKEN1^ [MG]#244 || ICH1*macht#245  || SPASS1 spaß#246
[[SPASS1*#571]]	
|| WASSER1#247 || $INDEX1#248 || FRISCH1 frisch#249 || IMMER4A* immer#250
[[ICH1#572 ICH1#573 LAND1A*#574 BENUTZEN1#575 FLACH1^#576 ICH1#577 $PROD*#578 BESSER1*#579 ALS4#580 WASSER11#581 $INDEX1#582 $PROD*#583]]
|| SPORT4B sport#251 || $PROD* [MG] bewegung#252 || GUT1 gut#253 || $INDEX1 gut#254 || SCHWIMMEN1 schwimmen#255 || GUT1 [MG]#256
[[FLEISSIG1#584 $INDEX1#585 FLEISSIG1#586 ICH2#587 FAUL1#588 ICH2#589 $ORAL^#590]]
|| ICH1*#257 || GERN1 gern#258 || ICH2#259 || HEUTE1 heute#260 || NOCH4A* noch#261 || GERN1 gern#262
||$GEST-OFF^*#263 ||NUR4* nur#264 ||PRIVAT1A privat freizeit #265 ||FREI1#266 ||FREIZEIT1B*#267 || SCHWIMMEN1 schwimmen gerne #268 ||GERN1#269 ||DORTHIN-GEHEN1#270 ||$ORAL^ aber #271||KAMPF1A wettkampf #272||SCHLUSS1 schluss#273
||$GEST-OFF^#274

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
