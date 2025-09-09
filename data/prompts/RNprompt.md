Write out the JSON and nothing but the JSON. Each text field includes details about a specific topic (column name) - but any of these can also be missing. Sometimes text has been entered into the wrong text fields. The text is in finnish. Your task is to extract the most important information and present it in JSON format with the following fields:

Ruokonata: Null or 1. If you find one of Ruokonata names or its other spellings/abbreviations in the text fields, enter 1 in this field. Sometimes it (or other spellings or abbreviations) is not mentioned at all, and then you have to find out if one or more Ruokonata variety names from the "Ruokonata varieties" list are mentioned in the text fields. If one or more Ruokonata variety names are found, then a 1 is entered in this field. If Ruokonata or its other spellings is NOT mentioned at all or NONE of Ruokonata varieties were found in the text fields, then you enter null.

Ruokonata variety: Here you must enter the name of Ruokonata variety or a list of Ruokonata variety names found in text fields. If not found any Ruokonata variety names, then enter null. You'll find possible names of Ruokonata varieties in the list "Ruokonata varieties" below. 

Ruokonata %: Numeric (float/int) or null. This is the percentage that tells you how much Ruokonata the farmer has sown in that grass field or how much Ruokonata varieties have been sown in total (all mentioned Ruokonata or Ruokonata variety percentages must be added together). If no Ruokonata percentage or any Ruokonata variety percentage is found, then this should be null. You'll find possible names of Ruokonata varieties in the list "Ruokonata varieties" below. The main words referring to Ruokonata can be found in the "Ruokonata and its different spellings" list.

List of Ruokonata and its different spellings/abbreviations (there may be other similar ones):
    Ruokonata
    ruokonata
    RN
    rn
    R.nata
    Rnata
    rörsvingel

Ruokonata varieties. Note: there may be typos in the text fields, please enter the names in the JSON as they are written in this list:
    Greendale
    Kora
    Retu
    Eleanora
    Birgitta
    Swaj
    Seine
    Rahela
    Triumphant
    Karolina

Some of the values we are looking for can be missing or have typos in them.
The decimal separator in Finnish float numbers is a comma.
Normally the information in the text fields complement each other. But if there is completely contradictory information in the text fields, please select the information for the JSON based on the INFOTEKSTI field.
If values/text are not found do not fill them in, just put null. Null is better than a bad guess.

Examples:

Input: INFOTEKSTI: Timotei/Ruokonata/ruokonata	Tuure, Ilmari;Karoliina	Yara Y4 Hiven 430 kg kylv.10.5.;Kasvilajit: timotei, Ruokonata, ruokonata;Lajikkeet: TT Tuure, NN Ilmari, RK Karoliina;Nurmen ikä: nan;Lannoitus, ajankohta ja -määrä: Yara Y4 Hiven 430 kg kylv.10.5.;Maalaji: nan;Muut lisätiedot: Multamaa, Ct;

Output:
{{
    "Ruokonata": 1,
    "Ruokonata variety": "Karoliina",
    "Ruokonata %": null
}}

Input: INFOTEKSTI: TT Tuure 65%, NN Ilmari 25%, ER Riikka 10%, täydennetty TT Tuukka 80%, NN Ilmari 20%;Kasvilajit: nan;Lajikkeet: nan;Nurmen ikä: nan;Lannoitus, ajankohta ja -määrä: nan;Maalaji: nan;Muut lisätiedot: nan;

Output:
{{
    "Ruokonata": null,
    "Ruokonata variety": null,
    "Ruokonata %": null
}}

Input: INFOTEKSTI: 2v. nurmi. TT-NN-RN. Lannoitus 30.4 250 kg N58:P7:K20. Maalaji Htmr;Kasvilajit: nan;Lajikkeet: nan;Nurmen ikä: nan;Lannoitus, ajankohta ja -määrä: nan;Maalaji: nan;Muut lisätiedot: nan;

Output:
{{
    "Ruokonata": 1,
    "Ruokonata variety": null,
    "Ruokonata %": null
}}

Input: INFOTEKSTI: Korjuu 20.6.;Kasvilajit: nan;Lajikkeet: nan;Nurmen ikä: nan;Lannoitus, ajankohta ja -määrä: nan;Maalaji: nan;Muut lisätiedot: nan;

Output:
{{

    "Ruokonata": null,
    "Ruokonata variety": null,
    "Ruokonata %": null
}}

Input: INFOTEKSTI: Korjuu 17.6. TT Nuutti 34 %, Grindstad 30 %, RN Swaj 13 %, NN Kasper 10 %, engl RH Birger 7 %, Mathilde 6%. Lannoitus 3.5. YaraMila Y-25 440 kg/ha. Maalaji rm HHt;Kasvilajit: Timotei, Ruokonata, Ruokonata, engl.raiheinä;Lajikkeet: TT Nuutti 34 %, Grindstad 30 %, RN Swaj 13 %, NN Kasper 10 %, engl RH Birger 7 %, Mathilde 6%. Täydennyskylvö 2019 TT Nuutti 45 %, Grindstad 35 %, engl RH Riikka 10 %, Mathilde 10 %;Nurmen ikä: nan;Lannoitus, ajankohta ja -määrä: 3.5. YaraMila Y-25 440 kg/ha;Maalaji: rm HHt;Muut lisätiedot: nan;

Output:
{{
    "Ruokonata": 1,
    "Ruokonata variety": "Swaj",
    "Ruokonata %": 13
}}

Input: INFOTEKSTI: TT nuutti 29%, Tenho29%, NN Inkeri21%, EngRH Riikka17%, RN Karoliina4%. Y1 - 290 kg/ha. Täydennys -20 Carbo täyd.seoksella.;Kasvilajit: nan;Lajikkeet: nan;Nurmen ikä: nan;Lannoitus, ajankohta ja -määrä: nan;Maalaji: nan;Muut lisätiedot: nan;

Output:
{{
    "Ruokonata": 1,
    "Ruokonata variety": "Karoliina",
    "Ruokonata %": 4
}}

Now it's your turn. Fill the JSON template below using the values in the input below, return nothing but the filled JSON. Show the full input text without omitting anything.

Input:
{input_text}

Output:
{{
    "Ruokonata": ,
    "Ruokonata variety": ,
    "Ruokonata %": ,
}}