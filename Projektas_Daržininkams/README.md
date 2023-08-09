# DARŽININKO PADĖJĖJAS

## PROJEKTO APRAŠYMAS

Šio projekto tikslas - sukurti Web aplikaciją, kuri padėtų daržininkams lengviau prižiūrėti savo augalus ir jais rūpintis. Taip pat sekti augalų istoriją, ją lyginti su praėjusių metų rodikliais. Gauti augalų priežiūros ir auginimo priminimus el. paštu.

## DUOMENYS

- Vartotojas
  - Vardas
  - Pavardė
  - Telefono numeris
  - El. paštas
  - Miestas (miestelis, kaimas)

- Augalas
  - Kategorija (daržovių sėklos, gėlių sėklos)
  - Pavadinimas (agurkai, pomidorai)
  - Veislė (paprastieji trumpavaisiai agurkai Mirabelle H...) 
  - Kiekis
  - Vazonų – daigyklų informacija (talpa, dydis)
  - Sėjimo data
  - Sėjimo vieta (šiltnamis, patalpa, lysvė, laukas)
  - Žemių rūšis (durpės, juodžemis)
  - Pastabos

- Daržas
  - **Augalas (foreign key)**
  - Pikiavimo data
  - Daigų kiekis
  - Daigų sodinimo data
  - Persodinimo vieta (šiltnamis, patalpa, lysvė, laukas)
  - Augalo užsodinimo plotas (arais)
  - Laistymo būdas (kapiliarinis laistymas, laistymas purkštuvu...)
  - Vandens kiekis reikalingas augalams (litrais)
  - Derliaus nuėmimo data
  - Derliaus kiekis
  - Derliaus sandėliavimo vieta
  - Derliaus laikymo laikotarpis (nuo – iki)

- Daržo darbas - modelis (jam bus priskirtos šios kategorijos)
  - **Daržas (foreign key)**
  - Augalų priežiūros data
  - Trąšos
  - Pesticidai
  - Trašų – pesticidų informacija
  - Ravėjimas
  - Dangos ir plėvelės tiesimas, uždengimas (agrodanga, agroplėvelė)
  - Augalų ligos
  - Pastabos
  
- Daržo atmintinė (modelis)
  - **Augalas (susieta su APPSU Augalas)**
  - **Daržas (susieta su APPSU Daržas)**
  - Priminimo data, nuo - iki.


## Procesai

- Augalo pridėjimas
  - Vartotojas paspaudžia  “Pridėti augalą“
  - Vartotojas užpildo augalo įvedimo laukelius
  - Vartotojas paspaudžia mygtuką “Išsaugoti augalą“, įvesti pasirinkimai išsisaugo
  - Vartotojas gali peržiūrėti įvestą informaciją apie augalą paspausdamas mygtuką “Augalo informacija“

- Augalo informacijos pildymas ir redagavimas
  - Vartotojo pagrindiniame profilio meniu yra mygtukas “mano augalai“, kurį paspaudus atsidaro langas su visa informacija apie vartotojo sukurtus augalus
  - Šiame lange prie kiekvieno augalo yra mygtukas “redaguoti“, kurį nuspaudus atsidaro nauja lentelė. Šioje lentelėje esančius duomenis galima redaguoti ir keisti
  - Naujai suredaguotus duomenis vartotojas išsaugo su mygtuku "išsaugoti".


- Įvestos informacijos paieška
  - Pagrindiniame vartotojo puslapyje rodomą augalų sąrašą galima filtruoti pagal įvairias parinktis pvz: kategorija, veislė, trąšos, augalų ligos... ir t.t.
  - Taip pat galima vykdyti paiešką pagal raktinius žodžius augalų sąraše.


- Daržo ir daržo darbo pridėjimo laukeliai
  - Vartotojas, taip pat turi galimybę pridėti “daržo“ ir “daržo darbo“ informaciją pasirinkdamas atitinkamus laukelius pagal “Augalo“ pridėjimo pavyzdį. 
  - Informaciją šiuose laukeliuose galima keisti, redaguoti, peržiūrėti ir išsaugoti.
  - Be to, esant poreikiui vartotojas gali iš šių sąrašų; “daržas“, “daržo darbas“ surasti sau reikalingą informaciją. Ir pagal pasirinktus filtrus ar raktinius žodžius ją paanalizuoti, palyginti.


- Vartotojo pasirinktų rodiklių priminimai
  - Vartotojas savo profilyje pasirenka vieną ar kelis kriterijus pagal kuriuos bus el. paštu siunčiami priminimai (sėjimo data, daigų kiekis, t.t.)
  - Toliau nurodo datą, kada jam bus siunčiamas vienas ar kitas priminimas
  - Galutinis žingsnis - patvirtinti savo pasirinkimus, nurodytus ankstesniuose punktuose.


## Vartotojo ir svetainės administratoriaus funkcijos

1. Vartotojas gali matyti ir redaguoti savo paskyros duomenis. Vartotojui, taip pat suteikiama teisė savo paskyroje įkelti, koreguoti, ir kitaip tvarkyti augalo ir daržo informaciją.
2. Svetainės administratorius gali matyti vartotojo duomenis. Gali trinti augalo ir daržo laukus, juos redaguoti. Gali keisti svetainės nustatymus. Gali ištrinti naudotojų paskyras.


## Dizainas

Svetainės dizainas funkcionalus, patogus vartotojui. 
