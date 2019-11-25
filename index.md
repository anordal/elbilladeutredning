Problemstillinger
=================

Etterspørsel
------------

Hvor mange vil ha elbillader, som funksjon av pris?

Protokoller for lastbalansering og forbruksmåling
-------------------------------------------------

* OCPP er en etablert åpen standard som støtter alt vi strengt tatt trenger.
  - De fleste produsenter (Ensto, Garo, Salto, Schneider, Zaptec) har ladere som støtter OCPP.
  - Ingen begrensning på antall ladere som kan tilknyttes.
  - Støtter ikke dynamisk fasebalansering (det er det visstnok bare Zaptec som har, ifølge dem selv).
  - Støtter statisk ladeprofil som en ukentlig timeplan.
  - Ved nettverksfeil mister man den dynamiske biten av lastbalanseringa. Derfor viktig med en konservativ statisk ladeprofil i bunnen.
  - Sentralenheten kan kjøpes fra flere produsenter eller som en skybasert tjeneste.
* Salto og Garo tilbyr også lastbalansering basert på Modbus over RS485.

Innfase 400V TN?
----------------

(Dette punktet gjør seg gjeldende hvis vi enten *må* oppgradere strømnettet på noen måte,
eller hvis vi *risikerer* å måtte gjøre det i nær framtid.)

* IT-nett er av flere grunner suboptimialt for elbillading.
  * Ladeplugg type 2 på IT-nett må kobles med en av faselederne på nøytral, noe som neppe er i tråd med spekken. TN-nett er utvilsomt mindre problematisk i lengden.[2]
  * Høyere spenning = høyere effekt.
  * Merk at 230V like lett kan tas fra et 400V TN-nett, slik de gjør det i resten av Europa (det er bare snakk om hvilket ledningspar man tar fra). Så det er ikke noe i veien for å ta med et eksisterende 230V-nett i en slik oppgradering.
* Å oppgradere ladernes strømnett til 400V *i ettertid* vil kreve omkobling av hver lader.

Ønsker vi f.eks. 3-fase-lading ute? Det vil kreve et TN-nett.

Det å få enda en transformator der ute kan tenkes å falle inn under *anleggsbidrag*.[1]
Se forøvrig kost/nytte-beregninger med oppgradering til TN-nett.[2]

Hva gjør vi med dagens ladere på vaskeristrøm?
----------------------------------------------

Skal disse
1. Innlemmes i nytt kontrollsystem for lastbalansering og/eller forbruksmåling?
   - Dagens ladere er av type «Wallbox eMH1»[3], merket Salto og Abl. Dette er hjemmeladere som ikke er egnet for dynamisk styring og lastbelastning for mer enn 6 enheter/ladebokser. Det skulle bety at alle ladebokser av denne typen må byttes ut hvis de skal være en del av et felles anlegg for hele garasjen.
2. Få fortsette å operere uregulert i overskuelig framtid?
   - Med gulrot for oppgradering til lader som *kan* innlemmes?
3. Utfases?

Er vaskeristrømmen 1 eller 3 faser?
Evt. skjevlast blir urettferdig for de som lastbalanseres på samme fase.
Det er da man trenger dynamisk fasebalansering.
Se også skjevspenning.[1]

Lenker
------

* [1] [https://dev-hafslundnett.no/artikler/kunde/flere-detaljer-om-elbil-og-lading/LyVgmpv8eAwU2UawKeEGk](https://dev-hafslundnett.no/artikler/kunde/flere-detaljer-om-elbil-og-lading/LyVgmpv8eAwU2UawKeEGk)
* [2] [http://publikasjoner.nve.no/eksternrapport/2019/eksternrapport2019_07.pdf](http://publikasjoner.nve.no/eksternrapport/2019/eksternrapport2019_07.pdf)
* [3] [https://www.ablmobility.de/en/products/emh1.php](https://www.ablmobility.de/en/products/emh1.php)
