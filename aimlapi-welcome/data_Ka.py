import krippendorff
import numpy as np
import re
P1 = """
$GEST-OFF^*  ||  【#ICH1  ||  $GEST-OFF^  ||  AUFWACHSEN1A  || 【 #ICH2  ||  AUFWACHSEN1A  ||  $GEST-OFF^  ||  【#ICH2  ||  AUFWACHSEN1A  ||  WIE-IMMER1*  ||  TAUB-GEHÖRLOS1A*  ||  GEBÄRDEN1A*  ||  【#ICH1*  || AUFWACHSEN1A  ||  BIS1  ||  【#ICH1  ||  $NUM-TEEN1:5  ||  ALT5A || #SCHULE3  ||  ENTLASSEN1  ||  SCHWIMMEN1  ||  $GEST-OFF^ || 【#ICH1  ||  AUFWACHSEN1A  ||  BIS1  ||  #SCHULE3  ||  ENTLASSEN1  ||  $NUM-TEEN1:5  ||  ALT5B  ||  【#ICH1 || DANN1A* || ELTERN1A  ||  FRAGE1
"""
P2 = """ELTERN1A  ||  FRAGE1 || ERLAUBNIS3  || 【# ICH1  ||  $INDEX1  ||  EINSTEIGEN1  ||  ERSTES-MAL3A  ||  【#TAUB-GEHÖRLOS1A  || 【 #VEREIN2A  ||  SCHWIMMEN1  ||  EINSTEIGEN1 || 【#DORT1  ||  ÜBEN1  ||  SCHWIMMEN1  ||  HIN-UND-HER1* || 【TAUB-GEHÖRLOS1A*  ||  【PERSON1*  ||  UNTERHALTUNG2A || 【#ICH1  ||  INTERESSE1B  ||  SPASS1  ||  ALLE1A^ || VORHER1  ||  JUNG2  || 【# ICH1*  ||  NICHT3A  ||  DARF1  ||  NICHT3A  ||  【#VEREIN2A  ||  $INDEX1 || JETZT1  ||  $INDEX1  ||  $GEST-OFF^* || UNTERHALTUNG2A  ||  TRAINING1  ||  SCHWIMMEN1  ||  HIN-UND-HER1*
"""
P3 = """$INDEX1  || 【# JUNG2  ||  【#LEITEN1B  ||  $INDEX1  ||  ZUSAMMEN1A*  ||  PFLEGE1  ||  AUFPASSEN1A  ||  ZUSAMMEN1A*  ||  UNTERHALTUNG2A  || INTERESSE1B  ||  ERWACHSENE2A*  ||  【#ICH1  ||  SPASS1  ||  UNTERHALTUNG2A || MEHR1*  ||  ERFAHRUNG2B  ||  $INDEX1  || 【# ICH2  ||  UNTERHALTUNG2A  ||  ALLE2A^ || UND-DANN1  ||  【#JUNG2  ||  【#LEITEN1B  ||  TERMIN1A  ||  DANN1A  ||  EINMAL1B  ||  SAMSTAG1  ||  【#ICH2  ||  ZUSAMMEN1A*  ||  AUSFLUG2* || UNTERHALTUNG2A  ||  SPIELEN2  ||  GEBÄRDEN1G*  ||  MEHR1*  ||  VIEL1A  ||  SPASS1 || UND3*  ||  DANN1A*  ||  ZUSAMMEN1A*  ||  DEUTSCH1  ||  MEISTERSCHAFT1  ||  AUCH3A  ||  TAUB-GEHÖRLOS1A  ||  FAHREN3  ||  ZUSAMMEN1A*  ||  JUNG2  ||  ALLE1A*  ||  FAHREN1*  ||  MIT1A  ||  ERWACHSENE2A* || AUCH3A*  ||  SCHWIMMEN1  ||  MIT1A  ||  MACHEN2  ||  MASSE-PERSON3^* || FAHREN3  ||  ZUG2A  ||  UNTERHALTUNG2A  ||  SPASS1*  ||  ABENTEUER1  ||  VIEL4  ||  【WIR1A*  ||  FERTIG1B  ||  $GEST-OFF^*
"""

P4 = """DANN1B*  ||  SPÄTER10*  ||  UM2A  || 【 #ICH1  || 【 #KEGELN1 || JAHR1B*  ||  MITGLIED1  || 【# KEGELN1  ||  UND2A* || FAHREN3*  ||  AKTIV3*  ||  【#KEGELN1*  ||  FERTIG1B  ||  SCHLUSS1 || BIS1*  || 【# ICH2  ||  KNIE1B  ||  FERTIG1B  ||  VORBEI4*
"""

P5 = """$GEST-OFF^*  ||  EINMAL1B  ||【 # ICH2  ||  WAR1*  ||  【#HAMBURG1  ||  【#DORT1  || 【 #ICH1  ||  【#HAMBURG1*  ||  【#DORT1  ||  【#SCHWIMMEN1*  ||  【#KAMPF1A  ||  【#DEUTSCH1  ||  【#MEISTERSCHAFT1  || 【 #ICH1  ||  DORTHIN-GEHEN1* ||SCHWIMMEN1*  ||  【#ICH2  ||  $PROD*  ||  SCHWIMMEN1  ||  $PROD* ||【#ICH1  ||  GRENZE1A^*  ||  LOS-START2  ||  STARTSCHUSS1*  ||  $GEST-OFF^*  ||  $GEST-ABWINKEN1^ ||【#ICH2*  ||  FALLEN1^  || 【 #ICH2*  ||  LAUFEN3^  ||  【#ICH1  ||  HIN-UND-HER1*  ||  BIS1  ||  ZIEL4 || $NUM-EINER1A:1d*  ||  ZUSAMMEN-PERSON1^  ||  KNAPP1  ||  【#ICH1  ||  BEGLEITEN1A^  ||  KOMMEN3*  ||  $INDEX1*  ||  FERTIG2* ||【#ICH1  ||  ATEMNOT1  || SEHR6^*  ||  WIE-FRAGE1*  ||  KAPUTT4 BEIDE2A*  ||  【#ICH1*  ||  LAUFEN8*  ||  FALLEN2A^*  ||  FERTIG1B  ||  $GEST-OFF^* ANSTRENGEND3*  ||  AKTIV1*  ||  WILLE6  ||  HIN-UND-HER1*  ||  $GEST-OFF^* $GEST^  ||  SCHAFFEN1A*  ||  $NUM-ORD1:2  ||  PLATZ9 ERFOLG2 FERTIG1B  ||  $INDEX1  ||  LETZTE2A*  ||  AUS-VORBEI1  ||  NICHT-MEHR1A  ||  SCHWIMMEN1 BIS-JETZT1  ||  NICHT-MEHR1A  ||  SCHWIMMEN1  ||  NEIN3B^*  ||  HEUTE1*  ||  FREI1  ||  ZEIT7C*  ||  ZEIT7C*  ||  SCHWIMMEN1  ||  FERTIG4
"""

P6 = """WANN2*  ||  NICHT-MEHR1A  ||  【#DU1* LETZTE1B  ||  VORBEI4  ||  $NUM-EINER1A:3d  ||  $NUM-ZEHNER1:2d*  ||  ALT8B  ||  SCHLUSS1  || 【# DU1* || $GEST-NM-SPRECHEN1^  ||  $GEST-NM-KOPFWIPPEN1^  ||  JUNG2  ||  $GEST-OFF^ || $NUM-ZEHNER1:2  ||  $NUM-TEEN1:9  ||  $NUM-ZEHNER1:2  ||  ALT5A  ||  【#ICH1 || SCHWIMMEN1  ||  ALLEIN2  ||  ANSTRENGEND5 || HIN-UND-HER1  ||  SCHWIMMEN1  ||  【#ICH1  ||  $PROD*  ||  KEINE-LUST1 ||【#DU1*  ||  SCHWIMMEN1*  ||  HIN-UND-HER1*  ||  ANSTRENGEND5  ||  SEHR7*
"""

P7 ="""$GEST-NM-KOPFSCHÜTTELN1^  ||  【#KAMPF1A  ||  WILLE6  ||  【#ICH1*  ||  HIN-UND-HER1* #KAMPF1A  ||  $ORAL^  ||  TRAINING1  ||  HIN-UND-HER1 SPASS1* || $GEST-NM-KOPFNICKEN1^  || 【#ICH1*  ||  SPASS1 【#WASSER1  ||  $INDEX1  ||  FRISCH1  ||  IMMER4A* ||【#ICH1  ||  【#ICH1  ||  LAND1A*  ||  BENUTZEN1  ||  FLACH1^  ||  #ICH1  ||  $PROD*  ||  BESSER1*  ||  ALS4  ||  【#WASSER11  ||  $INDEX1  ||  $PROD* || SPORT4B  ||  $PROD*  ||  GUT1  ||  $INDEX1  ||  SCHWIMMEN1  ||  GUT1 || FLEISSIG1  ||  $INDEX1  ||  FLEISSIG1  ||  【#ICH2  ||  FAUL1  ||  【#ICH2  ||  $ORAL^ 【#ICH1*  ||  GERN1  ||  【#ICH2  ||  HEUTE1  ||  NOCH4A*  ||  GERN1 || $GEST-OFF^*  ||  NUR4*  ||  PRIVAT1A  ||  FREI1  ||  FREIZEIT1B*  ||  SCHWIMMEN1  ||  GERN1  ||  DORTHIN-GEHEN1  ||  $ORAL^  || 【#KAMPF1A  ||  SCHLUSS1 || $GEST-OFF^
"""

P8 = """$INDEX1*  ||  DIENSTAG3A  ||  【#TRAINING1*  ||  SCHWIMMEN1*  ||  ABEND2  ||  SCHWIMMEN1  ||  【#TRAINING1  ||  PAAR-ANZAHL1*  ||  STUNDE2B*  ||  SCHLUSS1  || UND2A  ||  DANN1A  ||  FREITAG3B  ||  $GEST-ABWINKEN1^  ||  NUR2A  ||  STUNDE2B*  ||  【#TRAINING1  ||VIEL1A  ||  $GEST-OFF^*  ||【#TRAINING1  ||  SCHWIMMEN1  ||  FERTIG1B  ||  $GEST-OFF^  ||BESONDERS1A  ||  【#MEIN1*  ||  SPEZIAL1  ||  【#ICH2  ||  RÜCKENSCHWIMMEN1  ||  FERTIG1B  ||  $GEST^
"""

P9 = """UND2A  ||  DANN1A  ||  【#KEGELN1  || 【#KEGELN1  || $INDEX1  ||  【#KEGELN1  ||  FRÜHER1*  ||  【#ICH2  ||  AKTIV1  ||  【#KEGELN1  ||OFT1B  ||  KAMPF1A*  ||  PUNKT1C*  ||【#VERBAND1B  ||  【#VERBAND1B  ||  ODER4A*  ||  FREIZEIT1A  ||  $INDEX1 ||NEIN1B  ||  AKTIV2*  ||AKTIV3  ||【#VEREIN2A  ||  【#KEGELN1  ||  $INDEX1  ||  AKTIV1  ||$INDEX1  ||  OFT1B*  ||  ALLE2A  ||  SONNTAG1A  ||  【#ICH1  ||  【#PUNKT1C  ||  【#SPIELEN1  ||  【#SPIELEN2  ||  $GEST-OFF^  ||  $INDEX1  ||【WETTKAMPF2  ||  【#KEGELN1  ||  【VERGLEICH3  ||  IMMER3  ||  WOCHE1A*  ||  【#PUNKT1C  ||  【#SPIELEN2"""

P10 = """MIT1A  ||  【#HÖREND1A  ||  MIT1A  ||  $INDEX1  || 【#HÖREND1A  ||  EINSTEIGEN1  ||  【#HÖREND1A  ||  ALLE1A*  ||  GUT1  ||  KLAR1A  ||  LEISTUNG5*  ||  $INDEX1  ||  FERTIG1B  || ABLAUF2^  ||  AUCH3A  ||  【#ICH1  ||  【#KAMPF1A  ||  FAHREN1*  || $GEST-OFF^*  ||  DEUTSCH1  ||  MEISTERSCHAFT1  ||  $GEST-OFF^  || ES-GIBT3  ||  VERSCHIEDEN1  ||  $GEST^  || TOLL1A  || 【#$LIST1:1of1d  ||  【#KEGELN1  ||  【#$LIST1:2of2d  ||  【#SCHERE1*  ||  【#$LIST1:3of3d  ||  【#$NUM-EINER1A:3d  ||  【#BAHN-WEG1A*  ||  【#$GEST-OFF^*  ||  【#$LIST1:4of4d  ||  【#ASPHALT1*  || $ORAL^  ||  KANN1  ||  【#ALLES1A  || $LIST1:1of4d  ||  WECHSELN3A*  ||  $LIST-ZUSAMMEN3:1-4of4d  ||  $NUM-EINER1A:5*  ||  【#ALLE2D  || 【#KEGELN1  ||  GUT1*  || 【#ICH1  ||  IMMER5*  ||  TRAINING1  ||  FAHREN3  ||  #KAMPF1A  || OFT1B  ||  ALLE1A*  ||  【#WETTKAMPF2  ||  WILLE6  ||  UNTERHALTUNG2A  ||  VIEL1A  ||  INTERESSE1B  ||  GEBÄRDEN1G*  ||  UND7  || 【#ALLE1A  ||  SCHLUSS3  ||  ABEND2  ||  ABEND2*  ||  【KAMERAD1  ||  ABEND2
"""

P11 = """ALLE1A  ||  SCHLUSS3  ||  ABEND2  ||  ABEND2*  ||  KAMERAD1  ||  ABEND2  ||DANN1A  ||  MEISTENS1A  ||  $INDEX1  ||  STIMMUNG3  ||UNTERHALTUNG2A  ||  TRINKEN1  ||  BIER4  ||  ODER1*  ||  SEKT2*  ||$INDEX1  ||  GEWINNEN1  ||  WAS1A*  ||  GEWINNEN1  ||  MASS8B^  ||  BEKOMMEN3*  ||  MEHR1*  ||  STIMMUNG3  ||  UNTERHALTUNG2A  ||  【WIR1A*  ||KLAR1A*  ||PARTY1A  ||WAR1  ||  SCHÖN3  ||JUNG2  ||  ZEIT7A*  ||  NEIN3B^*  ||JETZT1*  ||  【#ICH2  ||  KNIE1A*  ||  SCHMERZ3  ||  $GEST-OFF^*  ||  RÜCKEN-UNTEN1E  ||  SCHMERZ3  ||HINKNIEN-SICH1  ||【#ICH1  ||  SCHLUSS1  ||ÜBER1*  ||  JAHR1A*  ||  AKTIV1  ||  【#ICH1  ||$GEST-OFF^*
"""
P12 = """HIER1  ||  NICHT1*  || GEBÄRDEN1A  ||  #DOZENT1  || FRÜHER1*  ||  【BERLIN1A*  ||  $INDEX1  ||  【#ICH1  ||  GEBÄRDEN1A  ||  #DOZENT1  ||  NICHT3A  ||  【#ICH1*  || $INDEX1  ||  DURCH2A  ||  KOMMEN1  ||  $INDEX1*  ||  $GEST-ABWINKEN1^  ||  【#MEIN1*  ||  【#LEBENSPARTNER1  ||  $INDEX1  ||  EMPFEHLEN1A*  ||  SAGEN1  ||  PASSEN1  ||  GEBÄRDEN1A  ||  PASSEN1  || 【#DU1*  ||  SOLL1  ||  GEBÄRDEN1A  ||  #DOZENT1  ||  GUT1  ||  EMPFEHLEN1A  || 【#ICH2  ||  ANFANG1A  ||  【#ICH2  ||  WOLLEN2  ||  NICHT3B*  ||  【#ICH1  ||  GRUND4A  ||  #FINGERALPHABET1  ||  【#ICH1  ||  KANN1  ||  KANN1*  ||  【#ICH2  ||  $GEST-OFF^  || FRÜHER1  ||  LERNEN1  ||  NICHT3B*  ||  【#ICH2  ||  【#FINGERALPHABET1  || 【#ICH2  ||  ANFANG1A  ||  $INDEX1  ||  UNTERRICHTEN1*  ||  【#FINGERALPHABET1  ||  ÜBEN1  || DANN1A  ||  【#ICH1  ||  ÜBEN1  ||  $INDEX1  ||  AUTOBAHN3  ||  $INDEX1  ||  ÜBEN1  ||  【#FINGERALPHABET1*  ||  $GEST-OFF^  || BIS-JETZT1  ||  PERFEKT-IN-ETWAS-SEIN1  ||  FERTIG1B  ||  【#FINGERALPHABET1  ||  $GEST-OFF^*  || GEBÄRDEN1A  ||  【#LEHRER5  ||  【#ICH1  ||  BIS-HEUTE2  ||  $GEST-OFF^*
"""

P13 = """【#ICH2  ||  LERNEN1  ||  $INDEX1  ||  HAMBURG1  ||  $INDEX1  || UND2A  ||  AUCH3A  ||  FRANKFURT1*  ||  $INDEX1  ||  LINGUISTIK1*  ||  $INDEX1  ||  AUCH3A  || 【#ICH2  ||  LERNEN1  ||  FERTIG1B  || VERINNERLICHEN1  ||  SICHER1  ||  【#ICH2  ||  GEBÄRDEN1A  ||  UNTERRICHTEN1*  || IMMER4A*  ||  AACHEN2  ||  $INDEX1  ||  FLUSS1^  ||  $INDEX1  ||  $NAME*  ||  $INDEX1  ||  $INDEX1  ||  MANCHMAL2  ||  KÖLN2  ||  $INDEX1  ||  UNTERRICHTEN1*  ||  $GEST-OFF^
"""

P_dict = {
    1: P1,
    2: P2,
    3: P3,
    4: P4,
    5: P5,
    6: P6,
    7: P7,
    8: P8,
    9: P9,
    10: P10,
    11: P11,
    12: P12,
    13: P13,
}

import re
def parse_P_to_matrix(P_str):
    items = [item.strip() for item in P_str.split("||")]
    matrix = []
    
    for item in items:
        A_label = None
        B_label = None
        
        if '【' in item:
            A_label = re.sub(r'[【#\*\^\$:\d-]', '', item).strip()
        
        if '#' in item:
            B_label = re.sub(r'[【#\*\^\$:\d-]', '', item).strip()
        
        matrix.append([A_label if A_label else None, B_label if B_label else None])
    
    return matrix


matrix_dict = {}

for key, P_str in P_dict.items():
    matrix_dict[key] = parse_P_to_matrix(P_str)

# print test.
for i in [1, 13]:
    print(f"Matrix for P{i}:")
    for row in matrix_dict[i]:
        print(row)
    print()

def parse_P_to_matrix(P_str):
    items = [item.strip() for item in P_str.split("||")]
    matrix = []
    for item in items:
        A_label = None
        B_label = None
        if '【' in item:
            A_label = re.sub(r'[【#\*\^\$:\d-]', '', item).strip()
        if '#' in item:
            B_label = re.sub(r'[【#\*\^\$:\d-]', '', item).strip()
        matrix.append([A_label if A_label else None, B_label if B_label else None])
    return matrix

def convert_matrix_to_binary(matrix):
    coder1 = []
    coder2 = []
    for a_label, b_label in matrix:
        coder1.append(1 if a_label is not None else 0)
        coder2.append(1 if b_label is not None else 0)
    return coder1, coder2

#save the codes.
binary_codings = {}

for i in range(1, 14):
    print(f"\nProcessing P{i}...")
    P_str = P_dict[i]
    matrix = parse_P_to_matrix(P_str)
    binary_coder1, binary_coder2 = convert_matrix_to_binary(matrix)
    binary_codings[i] = (binary_coder1, binary_coder2)
    print(f"Coder A binary: {binary_coder1}")
    print(f"Coder B binary: {binary_coder2}")


for i in range(1, 14):
    coder1, coder2 = binary_codings[i]
    data = [coder1, coder2]
    alpha = krippendorff.alpha(reliability_data=data, level_of_measurement='nominal')
    print(f"Krippendorff alpha for P{i}: {alpha}")