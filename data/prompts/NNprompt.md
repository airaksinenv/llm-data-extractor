You are a highly intelligent system that can transform human-written text fields into structured JSON format. Write out the JSON and nothing but the JSON. Each text field includes details about a specific topic (column name) - but any of these can also be missing. Sometimes text has been entered into the wrong text fields. The text is in finnish. Your task is to extract the most important information and present it in JSON format with the following fields:

Nurminata: Null or 1. If you find one of Nurminata names or its other spellings/abbreviations in the text fields, enter 1 in this field. Sometimes it (or other spellings or abbreviations) is not mentioned at all, and then you have to find out if one or more Nurminata variety names from the "Nurminata varieties" list are mentioned in the text fields. If one of Nurminata variety name is found, then a 1 is entered in this field. If Nurminata or its other spellings is NOT mentioned at all or NONE of Nurminata varieties were found in the text fields, then you enter null.

Nurminata variety: Here you must enter the name of Nurminata variety or a list of Nurminata variety names found in text fields. If not found any Nurminata variety names, then enter null. You'll find possible names of Nurminata varieties in the list "Nurminata varieties" below. 

Nurminata %: Numeric (float/int) or null. This is the percentage that tells you how much Nurminata the farmer has sown in that grass field or how much Nurminata varieties have been sown in total (all mentioned Nurminata or Nurminata variety percentages must be added together). If no Nurminata percentage or any Nurminata variety percentage is found, then this should be null. You'll find possible names of Nurminata varieties in the list "Nurminata varieties" below. The main words referring to Nurminata can be found in the "Nurminata and its different spellings" list.

List of Nurminata and its different spellings/abbreviations (there may be other similar ones):
    Nurminata
    nurminata
    NN
    nn
    N.nata
    Nnata
    ängssvingel

Nurminata varieties. Note: there may be typos in the text fields, please enter the names in the JSON as they are written in this list:
    Antti
    Arni
    Boris
    Cosmopolitan 
    DLF FPR-3159 (HYBERBOLA)
    Eevert
    Fp 6
    Fure
    Gunvor
    Ilmari
    Inkeri
    Jo 0807
    Kalevi
    Kasper
    Kasperi
    Klaara
    KVES 921
    Laura
    Lifara
    Preval
    Prior
    Salten
    Santtu
    SW Minto
    SW Revansch
    SWN ÄS9301
    Tored
    Vaaes 9702 (Vinjar)
    Valtteri
    Venni
    Vestar
    Vidvin
    Vigdis
    Vigris

Some of the values we are looking for can be missing or have typos in them.
The decimal separator in Finnish float numbers is a comma.
Normally the information in the text fields complement each other. But if there is completely contradictory information in the text fields, please select the information for the JSON based on the INFOTEKSTI field.
If values/text are not found do not fill them in, just put null. Null is better than a bad guess.

Examples:

Input: INFOTEKSTI: Timotei/nurminata/ruokonata	Tuure, Ilmari;Karoliina	Yara Y4 Hiven 430 kg kylv.10.5.;Kasvilajit: timotei, nurminata, ruokonata;Lajikkeet: TT Tuure, NN Ilmari, RK Karoliina;Nurmen ikä: nan;Lannoitus, ajankohta ja -määrä: Yara Y4 Hiven 430 kg kylv.10.5.;Maalaji: nan;Muut lisätiedot: Multamaa, Ct;

Output:
{{
    "Nurminata": 1,
    "Nurminata variety": "Ilmari",
    "Nurminata %": null
}}

Input: INFOTEKSTI: TT Tuure BOR 65%, NN Ilmari/Klaara BOR 25%, Eng Rh Riikka 10%,. Lannoitettu 9.5. 450 kg/ha Yara Y3. HtMr multava/ erittäin runsasmultainen;Kasvilajit: nan;Lajikkeet: nan;Nurmen ikä: nan;Lannoitus, ajankohta ja -määrä: nan;Maalaji: nan;Muut lisätiedot: nan;

Output:
{{
    "Nurminata": 1,
    "Nurminata variety": "Ilmari, Klaara",
    "Nurminata %": 25
}}

Input: INFOTEKSTI: 2v. nurmi. TT-NN-RN. Lannoitus 30.4 250 kg N58:P7:K20. Maalaji Htmr;Kasvilajit: nan;Lajikkeet: nan;Nurmen ikä: nan;Lannoitus, ajankohta ja -määrä: nan;Maalaji: nan;Muut lisätiedot: nan;

Output:
{{
    "Nurminata": 1,
    "Nurminata variety": null,
    "Nurminata %": null
}}

Input: INFOTEKSTI: Korjuu 20.6.;Kasvilajit: nan;Lajikkeet: nan;Nurmen ikä: nan;Lannoitus, ajankohta ja -määrä: nan;Maalaji: nan;Muut lisätiedot: nan;

Output:
{{

    "Nurminata": null,
    "Nurminata variety": null,
    "Nurminata %": null
}}

Input: INFOTEKSTI: Korjuu 17.6. TT Nuutti 34 %, Grindstad 30 %, RN Swaj 13 %, NN Kasper 10 %, engl RH Birger 7 %, Mathilde 6%. Lannoitus 3.5. YaraMila Y-25 440 kg/ha. Maalaji rm HHt;Kasvilajit: Timotei, Ruokonata, Nurminata, engl.raiheinä;Lajikkeet: TT Nuutti 34 %, Grindstad 30 %, RN Swaj 13 %, NN Kasper 10 %, engl RH Birger 7 %, Mathilde 6%. Täydennyskylvö 2019 TT Nuutti 45 %, Grindstad 35 %, engl RH Riikka 10 %, Mathilde 10 %;Nurmen ikä: nan;Lannoitus, ajankohta ja -määrä: 3.5. YaraMila Y-25 440 kg/ha;Maalaji: rm HHt;Muut lisätiedot: nan;

Output:
{{
    "Nurminata": 1,
    "Nurminata variety": "Kasper",
    "Nurminata %": 10
}}

Input: INFOTEKSTI: TT nuutti 29%, Tenho29%, NN Inkeri21%, EngRH Riikka17%, RN Karoliina4%. Y1 - 290 kg/ha. Täydennys -20 Carbo täyd.seoksella.;Kasvilajit: nan;Lajikkeet: nan;Nurmen ikä: nan;Lannoitus, ajankohta ja -määrä: nan;Maalaji: nan;Muut lisätiedot: nan;

Output:
{{
    "Nurminata": 1,
    "Nurminata variety": "Inkeri",
    "Nurminata %": 21
}}

Now it's your turn. Fill the JSON template below using the values in the input below, return nothing but the filled JSON. Show the full input text without omitting anything.

Input:
{input_text}

Output:
{{
    "Nurminata": ,
    "Nurminata variety": ,
    "Nurminata %": ,
}}