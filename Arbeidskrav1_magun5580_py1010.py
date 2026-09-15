# -*- coding: utf-8 -*-
"""
Arbeidskrav 1

Programmet under regner ut hva elbil og bensinbil totalt vil koste per år samt forskjellen i pris. Bruker kan selv velge antall km 

Følgende priser er brukt i beregningen: 
    
Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.

Created on Tue Sep 15 08:53:01 2026

@author: mariegu_a
"""


kjlengde = int(input("hvor mang km vil du kjøre i året? "))         #[Lar bruker velge antall km]


FE = 5000       #[Forsikring elbil]
FB=7500          #[Forsikring bensinbil]

TFA=8.38*365    #[Trafikkforsikringsavgift, lik både for elbil og bensinbil]

DE=0.2*kjlengde*2       #[Drivstoffforbruk elbil]
DB=1*kjlengde           #[Drivstoffforbruk bensinbil]

BE=0.1*kjlengde         #[Bomavgift elbil]
BB=0.3*kjlengde         #[Bomavgift bensinbil]

Årlig_elbil = FE+TFA+DE+BE       #[Årlig pris for elbil]
Årlig_bensinbil=FB+TFA+DB+BB        #[Årlig pris bensinbil]


print("En elbil som kjører ", kjlengde, "km per år, koster ",Årlig_elbil, "kr i året")

print("En bensinbil som kjører ", kjlengde, "km per år, koster ",Årlig_bensinbil, "kr i året")

print("Med en kjørelengde på ", kjlengde, " km er bensinbilen ", Årlig_bensinbil-Årlig_elbil, "dyrere per år")
