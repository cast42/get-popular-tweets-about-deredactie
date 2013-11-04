get-popular-tweets-about-deredactie
===================================

Small script that loads the last 500 tweets that match with 'deredactie'. Then it tries to get the correct url's pointing to
deredactie.be by unshorten all bit.ly, iff.tt links. In a last step URL's are counted, sorted and
tabulated. In order to match url's, the permalink is retrieved. Remark that mobile versions have their own permalink
that is not related to the 'desktop' version and hence are counted as seperated articles.

Example output on monday 4 nov 2013 16:19:41 CET running 'python deredactie.py':

	    +----------------------------------------------------------------------------------+-------+
		| Title                                                                            | Count |
		+----------------------------------------------------------------------------------+-------+
		| Girls’ Generation: "YouTube is mijn beste vriend"                                |    34 |
		| Grootste klimzaal van Europa komt in Gent                                        |    23 |
		| Supermarktketen scant gezichten om "juiste" reclames te tonen                    |    22 |
		| Nederlandse omroep urenlang uit de lucht na stroomtest                           |    21 |
		| Ontruiming rustig verlopen na hardhandige politie-inval                          |    18 |
		| "Waarom zouden we deze hond niet redden?"                                        |    15 |
		| "Geef roekeloze surfers een GAS-boete"                                           |    15 |
		| "Hautekiet" lanceert de Taal-IQ-test                                             |    15 |
		| "Niet samenwonen met iemand die het huis in brand wil steken"                    |    15 |
		| De Coninck lanceert sensibiliseringscampagne tegen burn-out                      |    14 |
		| Editors geeft "retestrak" concert in Sportpaleis                                 |    12 |
		| "Waarom btw-verlaging op elektriciteit niet onmiddellijk invoeren?"              |    10 |
		| "Voorlopig geen adoptiekinderen meer uit Marokko"                                |    10 |
		| "Eerste ziektedag moet niet worden uitbetaald"                                   |     9 |
		| "Voor een periode van 10 jaar zullen velen tekenen"                              |     9 |
		| Freddy Thielemans stopt als burgemeester van Brussel                             |     9 |
		| The New York Times looft Veerle Baetens                                          |     8 |
		| Arcade Fire op 24 november in Hallen van Schaarbeek                              |     8 |
		| De kleine garnaal is de pineut - Jan Nolf                                        |     8 |
		| Nobelprijswinnaars bezoeken Flanders Fields                                      |     8 |
		| Bert Schelfhout is nieuwe voorzitter van Jong VLD                                |     8 |
		| BV's vragen "Ode aan het papier" op de Boekenbeurs                               |     8 |
		| FOD Financiën weerlegt verklaring van Jambon                                     |     8 |
		| De Groote Oorlog                                                                 |     8 |
		| Waarom bevriest warm water sneller dan koud water?                               |     8 |
		| "Radicalisering in Syrië is bedreiging voor Europa"                              |     8 |
		| Cuba sluit van de ene op de andere dag alle privébioscopen                       |     8 |
		| Uitzetting Gesù-klooster is nakend                                               |     6 |
		| Grote vondst van naziroofkunst gedaan in München                                 |     6 |
		| "Nertsen: een warm en duurzaam product"                                          |     6 |
		| "Geen treinverkeer Leuven-Mechelen voor donderdag"                               |     6 |
		| Ontmanteling paviljoen Toyo Ito van start gegaan                                 |     5 |
		| "Samenwerking mogelijk als N-VA communautaire knoop ontwart"                     |     5 |
		| "N-VA sluit zichzelf uit van federale niveau"                                    |     5 |
		| "Israël is een illegitiem bastaardregime"                                        |     4 |
		| Opnieuw val van acrobaat Cirque du Soleil                                        |     4 |
		| Stierf Toetanchamon door ongeval met strijdwagen?                                |     4 |
		| Directrice SamuSocial woont in een OCMW-woning                                   |     4 |
		| Eminem en Taylor Swift winnen YouTube Music Awards                               |     4 |
		| "40 is oud? Nee, dit is oud!"                                                    |     4 |
		| 1.130 ressortissants de l’UE expulsés pour avoir abusé de notre sécurité sociale |     4 |
		| "Ons zelfgemaakt miniatuurmensje Leon is geweldig"                               |     4 |
		| Film over Mandela in première in Johannesburg                                    |     4 |
		| Op feestdag Sint-Hubertus krijgen alle dieren de zegen                           |     3 |
		| Krakers worden opgevangen in crisiscentrum                                       |     3 |
		| Olivier Strelli terug op de markt                                                |     3 |
		| Ryanair verwacht dat winst zal dalen                                             |     3 |
		| Hoe pakt Nederland (succesvol) de files aan?                                     |     3 |
		| Nederlandse musical "Yentl" mag niet van Streisand                               |     3 |
		| 7-2 - Carl Devos                                                                 |     3 |
		| Wegenwachter ziet auto in ravijn belanden                                        |     3 |
		| Disruption after freight train derailment                                        |     3 |
		| Arsenal stelt op 19 april nieuw werk voor in Antwerpen                           |     3 |
		| Zwart - Kolet Janssen                                                            |     3 |
		| Parachutiste zwaargewond na mislukte landing                                     |     3 |
		| Koeien stoten tot 15 procent minder uit door tijm en look                        |     3 |
		| Verkiezingen in Kosovo draaien uit op mislukking                                 |     3 |
		| We maken een ritje op de Weg van de Toekomst                                     |     3 |
		| Schulz: "Europese idee verzoenen met verwachtingen burgers"                      |     2 |
		| Wouter Beke: "Niet onderhandelen over confederalisme"                            |     2 |
		| "Geen formatiegesprekken over nieuwe staatshervorming"                           |     2 |
		| Agalev is dood - Van Dievel Consulting                                           |     2 |
		| Wesphael blijft bij zijn verhaal                                                 |     2 |
		| "Kom naar België om ons bier te proeven"                                         |     2 |
		| 1,500 protest against mink farm                                                  |     2 |
		| Brussels pets receive blessing from priest                                       |     2 |
		| Lots of storms and low humidity                                                  |     2 |
		| Manifestation contre l'implantation d'un élevage de visons à Wervik              |     2 |
		| China straft militaire leider van provincie Xinjiang                             |     2 |
		| John Kerry is in Caïro, waar spanning oploopt                                    |     2 |
		| Noodtoestand in Tunesië 8 maanden verlengd                                       |     2 |
		| N-VA verliest Franstalige vrienden - Véronique Lamquin                           |     2 |
		| Eric Van Rompuy laat zich scherp uit over plannen van de N-VA                    |     2 |
		| Panorama: Legally high                                                           |     2 |
		| Rail services could be (seriously) disrupted next Tuesday                        |     2 |
		| "Oef, ik krijg aandacht omdat ik niet perfect ben"                               |     2 |
		| Pierre Lemaitre wint de Prix Goncourt                                            |     2 |
		| Franse president wil grondig onderzoek naar dood journalisten                    |     2 |
		| "Geef Snowden asiel in Duitsland"                                                |     2 |
		| WAT IS CONFEDERALISME VOLGENS OPEN VLD?                                          |     2 |
		| Beke: "Ja, maar niet zonder N-VA"                                                |     1 |
		| Spectacular accident on Antwerp motorway                                         |     1 |
		| Allerzielen in Mexico is dansen op het kerkhof                                   |     1 |
		| Meer dan 200.000 mensen naar "Het vonnis"                                        |     1 |
		| Van buurmeisje tot perfect fotomodel                                             |     1 |
		| Het journaal 7 - 02/11/13                                                        |     1 |
		| Flemish series to get US remake                                                  |     1 |
		| The Guardian visits “vibrant Matonge”                                            |     1 |
		| Zeldzame zonsverduistering te zien in grote delen van de wereld                  |     1 |
		| Police in force to remove squatters                                              |     1 |
		| Maduro: "Fascistische aanval van Twitter"                                        |     1 |
		| VTM-reeks "Clan" krijgt Amerikaanse remake                                       |     1 |
		| Eerste stralingsvrije zone in Hautes-Alpes in Frankrijk                          |     1 |
		| Met veel machtsvertoon trekt politie Gesù-klooster binnen                        |     1 |
		| Koppen XL: Vermageren tegen elke prijs                                           |     1 |
		| Sven Nys wint voor vijfde keer in Zonhoven                                       |     1 |
		| Festival of light brighten up Brussels' canal                                    |     1 |
		| Wins for Anderlecht, Genk, Lierse and Kortrijk                                   |     1 |
		| Zwarte Piet wordt misbruikt - Marc Jacobs                                        |     1 |
		| Frietautomaat in Molenbeek alweer afgevoerd                                      |     1 |
		| Dit jaar 1.130 EU-burgers uitgewezen na misbruik sociale zekerheid               |     1 |
		| Hoe onbetaalbaar wordt onze gezondheidszorg?                                     |     1 |
		| Koppen - 31/10/2013                                                              |     1 |
		| NMBS informeert reizigers nu ook via Twitter                                     |     1 |
		| 1,130 EU social security fraudsters expelled                                     |     1 |
		| Man riskeert eigen leven voor zes blikjes bier                                   |     1 |
		| Open VLD: "Confederaal model is eindstation"                                     |     1 |
		| Freddy Thielemans stopt als burgemeester van Brussel                             |     1 |
		| Un train de marchandises déraille près de Wilsele                                |     1 |
		| Gesú squatters to march on Town Hall                                             |     1 |
		| Wins for both Bruges teams on Sunday evening                                     |     1 |
		| "6 verdachten opgepakt voor moord op Franse journalisten"                        |     1 |
		| Olivier Strelli is back                                                          |     1 |
		| Lou Reed is "de meest gemiste artiest"                                           |     1 |
		| China lanceert volgende maand robotjeep naar de maan                             |     1 |
		| Twintig jaar verdrag van Maastricht - Elisabeth Lannoo                           |     1 |
		| Terzake: Russische goelags bestaan nog altijd                                    |     1 |
		| Burgemeester Kir blijft bij standpunt over krakers in Gesú-klooster              |     1 |
		| Stroomstootwapens zijn levensgevaarlijk                                          |     1 |
		| no title found                                                                   |     1 |
		| "Film "Marina" gaat over iemand die gelooft in zijn passie"                      |     1 |
		| Justin Bieber geraakt door fles tijdens concert                                  |     1 |
		| L'épouse de Bernard Wesphael est décédée de mort violente                        |     1 |
		| "Het maakte me mysterieus en aantrekkelijk"                                      |     1 |
		| Supermarktketen scant gezichten om "juiste" reclames te tonen                    |     1 |
		| Twee Franse journalisten in Mali vermoord                                        |     1 |
		| Dienstencheque-bedrijven nemen te weinig werklozen aan                           |     1 |
		| "Soldiers of love" op één in Homo Top 100                                        |     1 |
		| Freddy Thielemans stopt als burgemeester van Brussel                             |     1 |
		| Macabere souvenirs aan holocaust verwijderd van eBay                             |     1 |
		| Moroccan adoptions suspended                                                     |     1 |
		| Nieuwe koepel voor Belgische restaurants                                         |     1 |
		| Proces tegen Mursi gestart... en meteen uitgesteld                               |     1 |
		| Pussy Riotlid vermist na overbrenging naar ander kamp                            |     1 |
		| "Ontruiming Gesú-klooster kan voor elk moment zijn"                              |     1 |
		| Smet stopt na volgende termijn met politiek                                      |     1 |
		| Directrice SamuSocial woont in een OCMW-woning                                   |     1 |
		| Dieren worden gezegend op feestdag van Sint-Hubertus                             |     1 |
		| Cuba sluit van de ene op de andere dag alle privébioscopen                       |     1 |
		| "Het Zilverfonds is een lege doos zonder maatschappelijke waarde"                |     1 |
		+----------------------------------------------------------------------------------+-------+
