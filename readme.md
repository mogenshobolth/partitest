# Partitest

Ved afholdelse af valg i Danmark bliver der ofte på de større nyhedssites lanceret forskellige tests, hvor man gennem en række spørgsmål kan få vist, hvor enig/uenig man er med feltet af kandidater. Til folketingsvalget i 2019 udarbejdede f.x. dr.dk endvidere end partitest, hvor man ved at tage stilling til en række "markante" lovforslag fik vist, hvilket parti der havde en afstemningshistorik tættest på en selv. 

Formålet med dette projekt er at stille en partitest til offentlig rådighed, som er baseret på en automatisk indhentning af lovforslagsdata fra ft.dk og en statistisk/analytisk model til at automatisk finde det bedste lille sæt af spørgsmål til at kunne pålideligt måle egne præferencer op imod partiernes afslørede holdninger. Det er i den sammenhæng en vigtig pointe, at partiernes afstemningsadfærd ikke alene afspejsler partipolitiske holdninger men også parliamentarisk taktisk adfærd.

Den data og analytiske side af projektet består af følgende filer: 

* get_data_from_ft: Python notebook som henter lovforslagsdata fra ft.dk og opbygger et datasæt, som kan bruges til udvælge spørgsmål til testen.
* explore_data: Python notebook med deskriptiv statistik om de indhentede lovforslag
* sample_test_questions: Python notebook med logikken for udvælgelse af spørgsmål til testen

Selve partitesten er lavet som en hjemmeside og består af følgende filer: 

* app.py: Backend kode, som sørger for at servicere brugeren med spørgsmål og beregne stemmeligheden med de forskellige partier ud fra de afgivne svar. 
* templates/partitest.html: Frontend kode med selve brugergrænsefladen