# prompts.py

prompt_1 = (
    '''$GEST-OFF^*#1  ||  ICH1#2  ||  $GEST-OFF^#3  ||  AUFWACHSEN1A#4  ||  ICH2#5  ||  AUFWACHSEN1A#6  ||  $GEST-OFF^#7  ||  ICH2#8  ||  AUFWACHSEN1A#9  ||  WIE-IMMER1*#10  ||  TAUB-GEHÖRLOS1A*#11  ||  GEBÄRDEN1A*#12  ||  ICH1*#13'''
    '''AUFWACHSEN1A#14  ||  BIS1#15  ||  ICH1#16  ||  $NUM-TEEN1:5#17  ||  ALT5A#18'''
    '''SCHULE3#19  ||  ENTLASSEN1#20  ||  SCHWIMMEN1#21  ||  $GEST-OFF^#22'''
    '''ICH1#23  ||  AUFWACHSEN1A#24  ||  BIS1#25  ||  SCHULE3#26  ||  ENTLASSEN1#27  ||  $NUM-TEEN1:5#28  ||  ALT5B#29  ||  ICH1#30'''
    '''DANN1A*#31'''
    '''ELTERN1A#32  ||  FRAGE1#33'''
)


prompt_2 = (
    '''ELTERN1A#34  ||  FRAGE1#35'''
    '''ERLAUBNIS3#36  ||  ICH1#37  ||  $INDEX1#38  ||  EINSTEIGEN1#39  || '''
    '''ERSTES-MAL3A#40  ||  TAUB-GEHÖRLOS1A#41  ||  VEREIN2A#42  ||  SCHWIMMEN1#43  ||  EINSTEIGEN1#44'''
    '''DORT1#45  ||  ÜBEN1#46  ||  SCHWIMMEN1#47  ||  HIN-UND-HER1*#48'''
    '''TAUB-GEHÖRLOS1A*#49  ||  PERSON1*#50  ||  UNTERHALTUNG2A#51'''
    '''ICH1#52  ||  INTERESSE1B#53  ||  SPASS1#54  ||  ALLE1A^#55'''
    '''VORHER1#56  ||  JUNG2#57  ||  ICH1*#58  ||  NICHT3A#59  ||  DARF1#60  ||  NICHT3A#61  ||  VEREIN2A#62  ||  $INDEX1#63'''
    '''JETZT1#64  ||  $INDEX1#65  ||  $GEST-OFF^*#66'''
    '''UNTERHALTUNG2A#67  ||  TRAINING1#68  ||  SCHWIMMEN1#69  ||  HIN-UND-HER1*#70'''
)



prompt_3 = (
    '''$INDEX1#71  ||  JUNG2#72  ||  LEITEN1B#73  ||  $INDEX1#74  ||  ZUSAMMEN1A*#75  ||  PFLEGE1#76  ||  AUFPASSEN1A#77  ||  ZUSAMMEN1A*#78  ||  UNTERHALTUNG2A#79'''
    '''INTERESSE1B#80  ||  ERWACHSENE2A*#81  ||  ICH1#82  ||  SPASS1#83  ||  UNTERHALTUNG2A#84'''
    '''MEHR1*#85  ||  ERFAHRUNG2B#86  ||  $INDEX1#87  ||  ICH2#88  ||  UNTERHALTUNG2A#89  ||  ALLE2A^#90'''
    '''UND-DANN1#91  ||  JUNG2#92  ||  LEITEN1B#93  ||  TERMIN1A#94  ||  DANN1A#95  ||  EINMAL1B#96  ||  SAMSTAG1#97  ||  ICH2#98  ||  ZUSAMMEN1A*#99  ||  AUSFLUG2*#100'''
    '''UNTERHALTUNG2A#101  ||  SPIELEN2#102  ||  GEBÄRDEN1G*#103  ||  MEHR1*#104  ||  VIEL1A#105  ||  SPASS1#106'''
    '''UND3*#107  ||  DANN1A*#108  ||  ZUSAMMEN1A*#109  ||  DEUTSCH1#110  ||  MEISTERSCHAFT1#111  ||  AUCH3A#112  ||  TAUB-GEHÖRLOS1A#113  ||  FAHREN3#114  ||  ZUSAMMEN1A*#115  ||  JUNG2#116  ||  ALLE1A*#117  ||  FAHREN1*#118  ||  MIT1A#119  ||  ERWACHSENE2A*#120'''
    '''AUCH3A*#121  ||  SCHWIMMEN1#122  ||  MIT1A#123  ||  MACHEN2#124  ||  MASSE-PERSON3^*#125'''
    '''FAHREN3#126  ||  ZUG2A#127  ||  UNTERHALTUNG2A#128  ||  SPASS1*#129  ||  ABENTEUER1#130  ||  VIEL4#131  ||  WIR1A*#132  ||  FERTIG1B#133  ||  $GEST-OFF^*#134'''
)

prompt_4 = (
    '''DANN1B*#135  ||  SPÄTER10*#136  ||  UM2A#137  ||  ICH1#138  ||  KEGELN1#139'''
    '''JAHR1B*#140  ||  MITGLIED1#141  ||  KEGELN1#142  ||  UND2A*#143'''
    '''FAHREN3*#144  ||  AKTIV3*#145  ||  KEGELN1*#146  ||  FERTIG1B#147  ||  SCHLUSS1#148'''
    '''BIS1*#149  ||  ICH2#150  ||  KNIE1B#151  ||  FERTIG1B#152  ||  VORBEI4*#153'''
)

prompt_5 = (
    '''$GEST-OFF^*#154  ||  EINMAL1B#155  ||  ICH2#156  ||  WAR1*#157  ||  HAMBURG1#158  ||  DORT1#159  ||  ICH1#160  ||  HAMBURG1*#161  ||  DORT1#162  ||  SCHWIMMEN1*#163  ||  KAMPF1A#164  ||  DEUTSCH1#165  ||  MEISTERSCHAFT1#166  ||  ICH1#167  ||  DORTHIN-GEHEN1*#168'''
    '''SCHWIMMEN1*#169  ||  ICH2#170  ||  $PROD*#171  ||  SCHWIMMEN1#172  ||  $PROD*#173'''
    '''ICH1#174  ||  GRENZE1A^*#175  ||  LOS-START2#176  ||  STARTSCHUSS1*#177  ||  $GEST-OFF^*#178  ||  $GEST-ABWINKEN1^#179'''
    '''ICH2*#180  ||  FALLEN1^#181  ||  ICH2*#182  ||  LAUFEN3^#183  ||  ICH1#184  ||  HIN-UND-HER1*#185  ||  BIS1#186  ||  ZIEL4#187'''
    '''$NUM-EINER1A:1d*#188  ||  ZUSAMMEN-PERSON1^#189  ||  KNAPP1#190  ||  ICH1#191  ||  BEGLEITEN1A^#192  ||  KOMMEN3*#193  ||  $INDEX1*#194  ||  FERTIG2*#195'''
    '''ICH1#196  ||  ATEMNOT1#197  ||  SEHR6^*#198  ||  WIE-FRAGE1*#199  ||  KAPUTT4#200'''
    '''BEIDE2A*#201  ||  ICH1*#202  ||  LAUFEN8*#203  ||  FALLEN2A^*#204  ||  FERTIG1B#205  ||  $GEST-OFF^*#206'''
    '''ANSTRENGEND3*#207  ||  AKTIV1*#208  ||  WILLE6#209  ||  HIN-UND-HER1*#210  ||  $GEST-OFF^*#211'''
    '''$GEST^#212  ||  SCHAFFEN1A*#213  ||  $NUM-ORD1:2#214  ||  PLATZ9#215'''
    '''ERFOLG2#216'''
    '''FERTIG1B#217  ||  $INDEX1#218  ||  LETZTE2A*#219  ||  AUS-VORBEI1#220  ||  NICHT-MEHR1A#221  ||  SCHWIMMEN1#222'''
    '''BIS-JETZT1#223  ||  NICHT-MEHR1A#224  ||  SCHWIMMEN1#225  ||  NEIN3B^*#226  ||  HEUTE1*#227  ||  FREI1#228  ||  ZEIT7C*#229  ||  ZEIT7C*#230  ||  SCHWIMMEN1#231  ||  FERTIG4#232'''
)

prompt_6 = (
    "# Speaker B\n"
    "'''WANN2*#233 || NICHT-MEHR1A#234 || DU1*#235'''\n"
    "'''LETZTE1B#236 || VORBEI4#237 || $NUM-EINER1A:3d#238 || $NUM-ZEHNER1:2d*#239 || ALT8B#240 || SCHLUSS1#241 || DU1*#242'''\n"
    
    "# Speaker A\n"
    "'''$GEST-NM-SPRECHEN1^#243 || $GEST-NM-KOPFWIPPEN1^#244 || JUNG2#245 || $GEST-OFF^#246'''\n"
    "'''$NUM-ZEHNER1:2#247 || $NUM-TEEN1:9#248 || $NUM-ZEHNER1:2#249 || ALT5A#250 || ICH1#251'''\n"
    
    "# Speaker B\n"
    "'''SCHWIMMEN1#252 || ALLEIN2#253 || ANSTRENGEND5#254'''\n"
    "'''HIN-UND-HER1#255 || SCHWIMMEN1#256 || ICH1#257 || $PROD*#258 || KEINE-LUST1#259'''\n"
    "'''DU1*#260 || SCHWIMMEN1*#261 || HIN-UND-HER1*#262 || ANSTRENGEND5#263 || SEHR7*#264'''\n"
)


prompt_7 = (
    "# Speaker A\n"
    "'''$GEST-NM-KOPFSCHÜTTELN1^#265  ||  KAMPF1A#266  ||  WILLE6#267  ||  ICH1*#268  ||  HIN-UND-HER1*#269'''\n"
    
    "# Speaker B\n"
    "'''KAMPF1A#270  ||  $ORAL^#271  ||  TRAINING1#272  ||  HIN-UND-HER1#273'''\n"
    "'''SPASS1*#274'''\n"
    
    "# Speaker A\n"
    "'''$GEST-NM-KOPFNICKEN1^#275  ||  ICH1*#276  ||  SPASS1#277'''\n"
    "'''WASSER1#278  ||  $INDEX1#279  ||  FRISCH1#280  ||  IMMER4A*#281'''\n"
    
    "# Speaker B\n"
    "'''ICH1#282  ||  ICH1#283  ||  LAND1A*#284  ||  BENUTZEN1#285  ||  FLACH1^#286  ||  ICH1#287  ||  $PROD*#288  ||  BESSER1*#289  ||  ALS4#290  ||  WASSER11#291  ||  $INDEX1#292  ||  $PROD*#293'''\n"
    
    "# Speaker A\n"
    "'''SPORT4B#294  ||  $PROD*#295  ||  GUT1#296  ||  $INDEX1#297  ||  SCHWIMMEN1#298  ||  GUT1#299'''\n"
    
    "# Speaker B\n"
    "'''FLEISSIG1#300  ||  $INDEX1#301  ||  FLEISSIG1#302  ||  ICH2#303  ||  FAUL1#304  ||  ICH2#305  ||  $ORAL^#306'''\n"
    
    "# Speaker A\n"
    "'''ICH1*#307  ||  GERN1#308  ||  ICH2#309  ||  HEUTE1#310  ||  NOCH4A*#311  ||  GERN1#312'''\n"
    "'''$GEST-OFF^*#313  ||  NUR4*#314  ||  PRIVAT1A#315  ||  FREI1#316  ||  FREIZEIT1B*#317  ||  SCHWIMMEN1#318  ||  GERN1#319  ||  DORTHIN-GEHEN1#320  ||  $ORAL^#321  ||  KAMPF1A#322  ||  SCHLUSS1#323'''\n"
    "'''$GEST-OFF^#324'''\n"
)


prompt_8 = (
    "'''$INDEX1*#325  ||  DIENSTAG3A#326  ||  #TRAINING1*#327  ||  SCHWIMMEN1*#328  ||  ABEND2#329  ||  SCHWIMMEN1#330  ||  #TRAINING1#331  ||  PAAR-ANZAHL1*#332  ||  STUNDE2B*#333  ||  SCHLUSS1#334'''\n"
    "'''UND2A#335  ||  DANN1A#336  ||  FREITAG3B#337  ||  $GEST-ABWINKEN1^#338  ||  NUR2A#339  ||  STUNDE2B*#340  ||  #TRAINING1#341'''\n"
    "'''VIEL1A#342  ||  $GEST-OFF^*#343'''\n"
    "'''#TRAINING1#344  ||  SCHWIMMEN1#345  ||  FERTIG1B#346  ||  $GEST-OFF^#347'''\n"
    "'''BESONDERS1A#348  ||  #MEIN1*#349  ||  SPEZIAL1#350  ||  #ICH2#351  ||  RÜCKENSCHWIMMEN1#352  ||  FERTIG1B#353  ||  $GEST^#354'''\n"
)


prompt_9 = (
    "# Speaker A\n"
    "'''UND2A#355  ||  DANN1A#356  ||  KEGELN1#357'''\n"
    "'''KEGELN1#358'''\n"
    
    "# Speaker A\n"
    "'''$INDEX1#359  ||  KEGELN1#360  ||  FRÜHER1*#361  ||  ICH2#362  ||  AKTIV1#363  ||  KEGELN1#364'''\n"
    "'''OFT1B#365  ||  KAMPF1A*#366  ||  PUNKT1C*#367'''\n"
    
    "# Speaker B\n"
    "'''VERBAND1B#368  ||  VERBAND1B#369  ||  ODER4A*#370  ||  FREIZEIT1A#371  ||  $INDEX1#372'''\n"
    
    "# Speaker A\n"
    "'''NEIN1B#373  ||  AKTIV2*#374'''\n"
    
    "# Speaker B\n"
    "'''AKTIV3#375'''\n"
    
    "# Speaker A\n"
    "'''VEREIN2A#376  ||  KEGELN1#377  ||  $INDEX1#378  ||  AKTIV1#379'''\n"
    "'''$INDEX1#380  ||  OFT1B*#381  ||  ALLE2A#382  ||  SONNTAG1A#383  ||  ICH1#384  ||  PUNKT1C#385  ||  SPIELEN1#386  ||  SPIELEN2#387  ||  $GEST-OFF^#388  ||  $INDEX1#389'''\n"
    "'''WETTKAMPF2#390  ||  KEGELN1#391  ||  VERGLEICH3#392  ||  IMMER3#393  ||  WOCHE1A*#394  ||  PUNKT1C#395  ||  SPIELEN2#396'''\n"
)


prompt_10 = (
    "# Speaker B\n"
    "'''MIT1A#397  ||  HÖREND1A#398  ||  MIT1A#399  ||  $INDEX1#400'''\n"
    
    "# Speaker A\n"
    "'''HÖREND1A#401  ||  EINSTEIGEN1#402  ||  HÖREND1A#403  ||  ALLE1A*#404  ||  GUT1#405  ||  KLAR1A#406  ||  LEISTUNG5*#407  ||  $INDEX1#408  ||  FERTIG1B#409'''\n"
    "'''ABLAUF2^#410  ||  AUCH3A#411  ||  ICH1#412  ||  KAMPF1A#413  ||  FAHREN1*#414'''\n"
    "'''$GEST-OFF^*#415  ||  DEUTSCH1#416  ||  MEISTERSCHAFT1#417  ||  $GEST-OFF^#418'''\n"
    "'''ES-GIBT3#419  ||  VERSCHIEDEN1#420  ||  $GEST^#421'''\n"
    
    "# Speaker B\n"
    "'''TOLL1A#422'''\n"
    
    "# Speaker A\n"
    "'''$LIST1:1of1d#423  ||  KEGELN1#424  ||  $LIST1:2of2d#425  ||  SCHERE1*#426  ||  $LIST1:3of3d#427  ||  $NUM-EINER1A:3d#428  ||  BAHN-WEG1A*#429  ||  $GEST-OFF^*#430  ||  $LIST1:4of4d#431  ||  ASPHALT1*#432'''\n"
    
    "# Speaker B\n"
    "'''$ORAL^#433  ||  KANN1#434  ||  ALLES1A#435'''\n"
    
    "# Speaker A\n"
    "'''$LIST1:1of4d#436  ||  WECHSELN3A*#437  ||  $LIST-ZUSAMMEN3:1-4of4d#438  ||  $NUM-EINER1A:5*#439  ||  ALLE2D#440'''\n"
    "'''KEGELN1#441  ||  GUT1*#442'''\n"
    "'''ICH1#443  ||  IMMER5*#444  ||  TRAINING1#445  ||  FAHREN3#446  ||  KAMPF1A#447'''\n"
    "'''OFT1B#448  ||  ALLE1A*#449  ||  WETTKAMPF2#450  ||  WILLE6#451  ||  UNTERHALTUNG2A#452  ||  VIEL1A#453  ||  INTERESSE1B#454  ||  GEBÄRDEN1G*#455  ||  UND7#456'''\n"
    "'''ALLE1A#457  ||  SCHLUSS3#458  ||  ABEND2#459  ||  ABEND2*#460  ||  KAMERAD1#461  ||  ABEND2#462'''\n"
)


prompt_11 = (
    "# Speaker A\n"
    "'''ALLE1A#463  ||  SCHLUSS3#464  ||  ABEND2#465  ||  ABEND2*#466  ||  KAMERAD1#467  ||  ABEND2#468'''\n"
    "'''DANN1A#469  ||  MEISTENS1A#470  ||  $INDEX1#471  ||  STIMMUNG3#472'''\n"
    "'''UNTERHALTUNG2A#473  ||  TRINKEN1#474  ||  BIER4#475  ||  ODER1*#476  ||  SEKT2*#477'''\n"
    "'''$INDEX1#478  ||  GEWINNEN1#479  ||  WAS1A*#480  ||  GEWINNEN1#481  ||  MASS8B^#482  ||  BEKOMMEN3*#483  ||  MEHR1*#484  ||  STIMMUNG3#485  ||  UNTERHALTUNG2A#486  ||  WIR1A*#487'''\n"
    
    "# Speaker B\n"
    "'''KLAR1A*#488'''\n"
    "'''PARTY1A#489'''\n"
    
    "# Speaker A\n"
    "'''WAR1#490  ||  SCHÖN3#491'''\n"
    "'''JUNG2#492  ||  ZEIT7A*#493  ||  NEIN3B^*#494'''\n"
    "'''JETZT1*#495  ||  ICH2#496  ||  KNIE1A*#497  ||  SCHMERZ3#498  ||  $GEST-OFF^*#499  ||  RÜCKEN-UNTEN1E#500  ||  SCHMERZ3#501'''\n"
    
    "# Speaker B\n"
    "'''HINKNIEN-SICH1#502'''\n"
    
    "# Speaker A\n"
    "'''ICH1#503  ||  SCHLUSS1#504'''\n"
    "'''ÜBER1*#505  ||  JAHR1A*#506  ||  AKTIV1#507  ||  ICH1#508'''\n"
    "'''$GEST-OFF^*#509'''\n"
)


prompt_12 = (
    "# Speaker A\n"
    "'''HIER1#510  ||  NICHT1*#511'''\n"
    "'''GEBÄRDEN1A#512  ||  DOZENT1#513'''\n"
    "'''FRÜHER1*#514  ||  BERLIN1A*#515  ||  $INDEX1#516  ||  ICH1#517  ||  GEBÄRDEN1A#518  ||  DOZENT1#519  ||  NICHT3A#520  ||  ICH1*#521'''\n"
    "'''$INDEX1#522  ||  DURCH2A#523  ||  KOMMEN1#524  ||  $INDEX1*#525  ||  $GEST-ABWINKEN1^#526  ||  MEIN1*#527  ||  LEBENSPARTNER1#528  ||  $INDEX1#529  ||  EMPFEHLEN1A*#530  ||  SAGEN1#531  ||  PASSEN1#532  ||  GEBÄRDEN1A#533  ||  PASSEN1#534'''\n"
    "'''DU1*#535  ||  SOLL1#536  ||  GEBÄRDEN1A#537  ||  DOZENT1#538  ||  GUT1#539  ||  EMPFEHLEN1A#540'''\n"
    "'''ICH2#541  ||  ANFANG1A#542  ||  ICH2#543  ||  WOLLEN2#544  ||  NICHT3B*#545  ||  ICH1#546  ||  GRUND4A#547  ||  FINGERALPHABET1#548  ||  ICH1#549  ||  KANN1#550  ||  KANN1*#551  ||  ICH2#552  ||  $GEST-OFF^#553'''\n"
    "'''FRÜHER1#554  ||  LERNEN1#555  ||  NICHT3B*#556  ||  ICH2#557  ||  FINGERALPHABET1#558'''\n"
    "'''ICH2#559  ||  ANFANG1A#560  ||  $INDEX1#561  ||  UNTERRICHTEN1*#562  ||  FINGERALPHABET1#563  ||  ÜBEN1#564'''\n"
    "'''DANN1A#565  ||  ICH1#566  ||  ÜBEN1#567  ||  $INDEX1#568  ||  AUTOBAHN3#569  ||  $INDEX1#570  ||  ÜBEN1#571  ||  FINGERALPHABET1*#572  ||  $GEST-OFF^#573'''\n"
    "'''BIS-JETZT1#574  ||  PERFEKT-IN-ETWAS-SEIN1#575  ||  FERTIG1B#576  ||  FINGERALPHABET1#577  ||  $GEST-OFF^*#578'''\n"
    "'''GEBÄRDEN1A#579  ||  LEHRER5#580  ||  ICH1#581  ||  BIS-HEUTE2#582  ||  $GEST-OFF^*#583'''\n"
)



prompt_13 = (
    "# Speaker A\n"
    "'''ICH2#584  ||  LERNEN1#585  ||  $INDEX1#586  ||  HAMBURG1#587  ||  $INDEX1#588'''\n"
    "'''UND2A#589  ||  AUCH3A#590  ||  FRANKFURT1*#591  ||  $INDEX1#592  ||  LINGUISTIK1*#593  ||  $INDEX1#594  ||  AUCH3A#595  ||  ICH2#596  ||  LERNEN1#597  ||  FERTIG1B#598'''\n"
    "'''VERINNERLICHEN1#599  ||  SICHER1#600  ||  ICH2#601  ||  GEBÄRDEN1A#602  ||  UNTERRICHTEN1*#603'''\n"
    "'''IMMER4A*#604  ||  AACHEN2#605  ||  $INDEX1#606  ||  FLUSS1^#607  ||  $INDEX1#608  ||  $NAME*#609  ||  $INDEX1#610  ||  $INDEX1#611  ||  MANCHMAL2#612  ||  KÖLN2#613  ||  $INDEX1#614  ||  UNTERRICHTEN1*#615  ||  $GEST-OFF^#616'''\n"
)

# ...依次补全PROMPT4~PROMPT13
