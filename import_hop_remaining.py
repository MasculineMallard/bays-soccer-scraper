#!/usr/bin/env python3
"""Import remaining HOP seasons: Spring 2024, Fall 2023, Spring 2023, Fall 2022, Spring 2022, Fall 2021, Spring 2021"""

from universal_import import save_and_import

# Spring 2024
print("\n=== IMPORTING HOP SPRING 2024 ===\n")
spring2024_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
G8 Academy	32872	Girls 8 3/H	2	8	0	0	6	19	35	-16	Iain Martin	None
Hawks (G8)	32886	Girls 8 4/J	8	1	0	0	24	37	13	24	Joe Eagley	Adele Haber
Fire	32885	Girls 6 1/B	7	3	0	0	21	22	15	7	Dave Fine	Denis Murphy
Cyclones	32883	Girls 6 3/F	3	4	3	0	12	15	19	-4	Michael Twardowski	Randy Sanborn
G6 Academy	32871	Girls 6 3/H	0	7	3	0	3	6	27	-21	Devin Ramos	Iain Martin
Blaze	33586	Girls 5 3/F	6	2	2	0	20	28	19	9	Dave Salerno	David Kubiak
Reign	33585	Girls 5 3/G	7	2	1	0	22	33	12	21	Mark Haranas	James Casady
G5 Academy	32870	Girls 5 4/A	6	2	2	0	20	31	18	13	Devin Lacroix	Iain Martin
G4 Academy	33398	Girls 4 2/E	7	1	2	0	23	26	12	14	Heather DeLude	Iain Martin
United (G4)	32879	Girls 4 3/G	9	1	0	1	26	31	8	23	Bryan Memmelaar	Jaime Vivian
Hawks (G4)	33566	Girls 4 4/B	0	5	5	0	5	15	33	-18	Gayla Langlois	Amy Steppacher
Strikers	33587	Girls 4 4/B	7	3	0	0	21	39	18	21	Nima Fatouretchi	Ken O'Toole
G3 Academy	32868	Girls 3 3/C	3	1	1	0	10	18	13	5	Florent Martin	Iain Martin
Hurricanes (G3)	32874	Girls 3 3/G	2	2	1	0	7	12	11	1	Dan Gyllstrom	Peter Fogg
Blizzards	32875	Girls 3 4/A1	7	2	1	0	22	49	22	27	John Jannino	Dave Salerno
Hillers	64	Boys 10 2/B	3	1	3	0	12	17	9	8	Todd Garron	Doug Gordon
Galaxy (B8)	32907	Boys 8 2/A	2	5	3	0	9	20	29	-9	Patrick Morrissey	Shaun Fitzgibbon
B8 Academy	32912	Boys 8 3/K	2	7	1	0	7	11	20	-9	Heather DeLude	Iain Martin
Hurricanes (B8)	32906	Boys 8 4/D	3	5	2	0	11	21	30	-9	Eric Wieland	Steven Jackson
United (B6)	32903	Boys 6 3/E	1	4	1	0	4	16	26	-10	TJ Paparazzo	Colleen Rommel
B6 Academy Orange	32911	Boys 6 4/A	1	3	2	0	5	10	18	-8	Florent Martin	Iain Martin
B6 Academy White	32910	Boys 6 4/B	3	5	2	0	11	22	32	-10	Devin Lacroix	Iain Martin
United (B5)	33404	Boys 5 2/A	4	5	1	0	13	33	34	-1	Jarred Sakakeeny	Kristin Dykstra
Avengers (B5)	32900	Boys 5 4/B	2	7	1	0	7	27	44	-17	Ambikesh Khiriya	None
B4 Academy	33408	Boys 4 3/A1	5	4	1	0	16	30	28	2	Iain Martin	None
Revolution (B4)	32896	Boys 4 4/A	3	6	1	1	9	24	31	-7	Emily Jackson-Unger	Tom St.Pierre
Dynamo	33401	Boys 4 4/A	0	9	1	0	1	23	58	-35	Carlos Henkle	Amar Prabhu
United (B4)	32897	Boys 4 4/B2	1	6	1	0	4	11	27	-16	Kayhan Yegenoglu	Jamie Yegenoglu
B3 Academy	33407	Boys 3 3/B	5	4	1	0	16	32	26	6	Devin Ramos	Iain Martin
Breakers	32890	Boys 3 3/C2	2	7	1	0	7	31	59	-28	David Weibe	Jeff Strassman
Avengers (B3)	33588	Boys 3 3/C2	1	6	2	0	5	27	48	-21	Michelle Midkiff	None"""

save_and_import(spring2024_data, 'HOP', 2024, 'Spring')

# Fall 2023
print("\n=== IMPORTING HOP FALL 2023 ===\n")
fall2023_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Hawks Green	33399	Girls 8 3/E	3	2	0	0	9	9	8	1	Joe Eagley	Heather Smith
G8 Academy	32872	Girls 8 4/B	6	2	2	0	20	29	25	4	Iain Martin	Florent Martin
Hawks Orange	32886	Girls 8 4/K	1	8	1	0	4	6	30	-24	Adele Haber	None
Fire	32885	Girls 6 2/B1	7	1	2	0	23	33	16	17	Dave Fine	Denis Murphy
Cyclones	32883	Girls 6 3/F	2	8	0	0	6	11	30	-19	Michael Twardowski	Jennifer Vale
Lightning (G6)	32884	Girls 6 3/F	5	5	0	0	15	16	11	5	Randy Sanborn	Heather Vinci
G6 Academy	32871	Girls 6 4/B	5	5	0	0	15	26	24	2	Devin Ramos	Iain Martin
Storm	32882	Girls 5 2/C	1	8	1	0	4	5	18	-13	Matt Tighe	Dave Salerno
Reign	32881	Girls 5 4/B	3	2	1	0	10	21	20	1	Allison Pachecho	Heather Marusa
G5 Academy	32870	Girls 5 4/C	7	2	1	0	22	31	15	16	Devin Lacroix	Iain Martin
Blaze	32880	Girls 5 4/F	5	3	2	0	17	21	20	1	James Casady	None
G4 Academy	33398	Girls 4 2/D	3	5	1	0	10	14	21	-7	Heather DeLude	Iain Martin
United (G4)	32879	Girls 4 3/F	3	6	1	0	10	19	34	-15	Meaghan Alexander	Jaime Vivian
Tornadoes	32877	Girls 4 4/B	3	7	0	0	9	23	38	-15	Miranda Ippolito	None
Rays	32878	Girls 4 4/B	7	1	2	0	23	36	14	22	Heather Smith	Masilo Grant
Stars	32876	Girls 4 4/E2	2	5	1	0	7	17	21	-4	Nima Fatouretchi	None
G3 Academy	32868	Girls 3 2/A2	3	5	0	0	9	24	32	-8	Florent Martin	Iain Martin
Hurricanes (G3)	32874	Girls 3 3/E	3	7	0	0	9	30	35	-5	Mark Gordon	Kristin Dykstra
Blizzards	32875	Girls 3 3/E	3	7	0	0	9	22	31	-9	Dave Salerno	None
Huskies	32873	Girls 3 3/F	8	2	0	0	24	38	13	25	Peter Fogg	None
Boys HS	33438	Boys 912 3/B	2	5	0	0	6	17	31	-14	Michelle Midkiff	None
Galaxy (B8)	32907	Boys 8 2/C	5	2	3	0	18	18	14	4	Patrick Morrissey	Shaun Fitzgibbon
Hurricanes (B8)	32906	Boys 8 4/C	1	1	3	0	6	7	8	-1	Eric Wieland	Ed O'Donnell
B8 Academy	32912	Boys 8 4/G	9	0	1	0	28	30	5	25	Heather DeLude	Iain Martin
Thunder (B8)	33406	Boys 8 4/M	1	8	1	0	4	11	43	-32	David Howell	None
Revolution (B6)	32904	Boys 6 2/D1	7	2	1	0	22	34	15	19	Steve Quinn	Brian Heaton
B6 Academy Orange	32911	Boys 6 3/F	3	7	0	0	9	19	32	-13	Florent Martin	Iain Martin
B6 Academy White	32910	Boys 6 4/A	2	4	0	0	6	16	20	-4	Devin Lacroix	Iain Martin
United (B6)	32903	Boys 6 4/C	4	5	1	0	13	27	29	-2	TJ Paparazzo	None
Athletics	33391	Boys 6 4/C	5	3	2	0	17	37	25	12	Greg Gilson	Melissa Recos
Fury	33403	Boys 5 2/D	8	1	1	0	25	34	18	16	Brad Wilson	Ed O'Donnell
Hooligans (B5)	33404	Boys 5 2/E	10	0	0	0	30	40	14	26	Jarred Sakakeeny	Aico Van Nunen
Raptors	32900	Boys 5 3/J	2	6	2	0	8	13	24	-11	Peter Fogg	Matt Hodges
Avengers	33405	Boys 5 4/J	0	6	0	0	0	11	41	-30	Michelle Midkiff	None
B4 Academy	33408	Boys 4 3/C	3	2	5	0	14	39	38	1	Iain Martin	Florent Martin
Hillers	33402	Boys 4 3/J	5	3	2	0	17	34	27	7	Nate Repucci	Tom St.Pierre
Revolution (B4)	32896	Boys 4 3/K	3	6	1	0	10	18	28	-10	Liz Fleming	Jill Spinale
United (B4)	32897	Boys 4 3/K	5	3	2	0	17	37	31	6	John DelPrete	None
Huskies (B4)	33400	Boys 4 4/A	4	0	0	0	12	21	9	12	Drew Griffin	Bradley Leyshon
Dynamo	33401	Boys 4 4/A	0	4	0	1	-1	4	12	-8	Carlos Henkle	Kai Wittpennig
B3 Academy	33407	Boys 3 2/D	0	9	1	0	1	10	51	-41	Devin Ramos	Iain Martin
Galaxy (B3)	32888	Boys 3 3/A	1	6	3	1	5	17	29	-12	Marilyn Gibbs	None
Thunder (B3)	32889	Boys 3 3/A	3	7	0	0	9	17	35	-18	Ted Smith	None
Breakers	32890	Boys 3 3/B	3	7	0	1	8	25	44	-19	David Weibe	Hugh Gregg
Hurricanes (B3)	32891	Boys 3 3/B	7	3	0	2	19	37	18	19	Leigh Murray	Sara Labrecque
Lightning (B3)	32892	Boys 3 3/D	4	4	2	0	12	40	26	14	Aico Van Nunen	Jitender Kataria"""

save_and_import(fall2023_data, 'HOP', 2023, 'Fall')

# Spring 2023
print("\n=== IMPORTING HOP SPRING 2023 ===\n")
spring2023_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Girls HS Academy	32867	Girls 10 2/A	2	2	3	0	9	16	15	1	Heather DeLude	Iain Martin
G8 Academy	31779	Girls 8 3/D	4	5	1	0	13	14	19	-5	Florent Martin	Iain Martin
Dynamo	31701	Girls 8 4/F	4	6	0	0	12	21	32	-11	Marc Mauricio	None
G6 Academy	31777	Girls 6 3/F	1	8	1	0	4	11	27	-16	Jack Soucy	Iain Martin
Hawks	31700	Girls 6 4/A 	9	1	0	0	27	32	13	19	Bryan Memmelaar	Adele Haber
Fire	31698	Girls 5 2/B	5	3	2	0	17	29	17	12	Dave Fine	Denis Murphy
G5 Academy	31776	Girls 5 4/A2	3	5	0	0	9	21	26	-5	Iain Martin	None
Lightning	31697	Girls 5 4/C	7	1	2	0	23	34	20	14	Randy Sanborn	Heather Vinci
Junior Storm	31695	Girls 4 2/C	7	2	1	0	22	23	10	13	Matt Tighe	Dave Salerno
Fireworks	31693	Girls 4 4/C	4	2	4	0	16	18	16	2	James Casady	Mark Haranas
G4 Academy	31770	Girls 4 4/D	7	1	2	0	23	36	13	23	Devin Ramos	Iain Martin
Stars	31692	Girls 4 4/G2	1	7	0	0	3	11	37	-26	Mohammad Mahdi Agheli Hajiabadi	Stephen Moorehead
G3 Academy	31769	Girls 3 2/C	3	1	2	0	11	13	7	6	Heather DeLude	Iain Martin
Tornadoes	31691	Girls 3 4/B	3	5	2	0	11	18	23	-5	Netra Srikanth	Miranda Ippolito
Hornets	31690	Girls 3 4/C	2	4	4	0	10	20	26	-6	John Gavula	Marissa Gentile
United	31689	Girls 3 4/C	7	0	3	0	24	37	13	24	Meaghan Alexander	Scott Inglis
Boys High School	32914	Boys 12 2/B	5	2	0	1	14	37	23	14	Amy Mick	None
Hillers	31765	Boys 8 3/A	8	2	0	0	24	29	17	12	Todd Garron	Tom Click
Thunder	31763	Boys 8 4/B	3	5	2	0	11	15	14	1	George Selibas	Eric Wieland
Athletics	31762	Boys 8 4/J	0	10	0	0	0	10	47	-37	David Howell	Steven Jackson
B6 Academy Orange	31790	Boys 6 3/B	6	3	1	0	19	27	24	3	Jack Soucy	Iain Martin
B6 Academy White	31789	Boys 6 4/A 	0	4	1	0	1	5	15	-10	Devin Ramos	Iain Martin
Rovers	31760	Boys 6 4/F	8	2	0	0	24	49	22	27	Jesus Amadori	Masilo Grant
Revolution	31758	Boys 5 4/G	3	5	1	0	10	29	33	-4	Gayl Weinmann	Jitender Kataria
Fury	31757	Boys 4 1/A1	3	2	0	0	9	9	8	1	Keith Gilbreath	Kristin Dykstra
Raptors	31753	Boys 4 3/C	7	1	1	0	22	35	12	23	Peter Fogg	John Murray
B4 Academy	31788	Boys 4 3/F	2	3	0	0	6	12	16	-4	Florent Martin	Iain Martin
Hooligans	31755	Boys 4 4/B	3	6	0	0	9	12	19	-7	Patrick Maiella	Keeley Maiella
Junior Hillers	32766	Boys 4 4/F	0	8	2	1	1	14	30	-16	Ellie Driscoll	Emme Joy
B3 Academy	31782	Boys 3 3/B	5	4	1	0	16	37	36	1	Iain Martin	None
Lions	31750	Boys 3 4/A	3	5	1	0	10	29	31	-2	Carlos Henkle	Bradley Leyshon
Hornets	31752	Boys 3 4/B2	1	2	1	0	4	11	15	-4	Liz Fleming	Kai Wittpennig"""

save_and_import(spring2023_data, 'HOP', 2023, 'Spring')

# Fall 2022
print("\n=== IMPORTING HOP FALL 2022 ===\n")
fall2022_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Breakers	31702	Girls 8 2/D1	2	7	1	0	7	9	30	-21	Frank Fiore	Sarah Hopkins
G8 Academy	31779	Girls 8 3/E2	4	4	2	0	14	18	18	0	Florent Martin	Iain Martin
Dynamo	31701	Girls 8 4/F	2	3	0	0	6	8	11	-3	Marc Mauricio	None
Hawks	31700	Girls 6 3/A	6	2	2	0	20	18	6	12	Bryan Memmelaar	Heather Smith
G6 Academy	31777	Girls 6 4/C	6	2	2	0	20	27	17	10	Cameron Young	Iain Martin
Express	31699	Girls 6 4/G	5	5	0	0	15	19	21	-2	Adele Haber	Ray Fryer
Fire	31698	Girls 5 2/A	3	4	3	0	12	18	18	0	Dave Fine	Gino Spinelli
Lightning	31697	Girls 5 4/A	0	7	1	0	1	16	41	-25	Nate Repucci	Pradeep Veldurthi
G5 Academy	31776	Girls 5 4/A	2	2	0	0	6	12	7	5	Iain Martin	Florent Martin
Power (DROPPED)	31696	Girls 5 4/X	0	0	0	0	0	0	0	0	Adam Feigen	Randy Sanborn
Junior Storm	31695	Girls 4 2/A2	4	2	2	0	14	15	8	7	Matt Tighe	Ryan Jones
Hurricanes (G4)	31694	Girls 4 3/C	1	8	1	0	4	9	32	-23	Dave Salerno	None
G4 Academy	31770	Girls 4 3/H	2	6	2	0	8	11	22	-11	Devin Ramos	Iain Martin
Fireworks	31693	Girls 4 4/D2	0	4	0	0	0	3	11	-8	Mark Haranas	Kaitlyn Mullen
Stars (G4)	31692	Girls 4 4/E	2	4	0	1	5	13	16	-3	Jenn Kirkland	Joseph Mercurio
G3 Academy	31769	Girls 3 2/B2	5	5	0	0	15	25	18	7	Michael Gomes	Iain Martin
Hurricanes (G3)	31691	Girls 3 3/E	4	6	0	0	12	18	25	-7	Leanna Cockburn	Miranda Ippolito
Hornets	31690	Girls 3 3/G	4	4	2	0	13	24	18	6	John Gavula	Marissa Gentile
Stars (G3)	31689	Girls 3 4/B	0	4	1	0	1	7	17	-10	Meaghan Alexander	Jaime Vivian
Hillers	31765	Boys 8 3/B	8	1	1	0	25	37	7	30	Todd Garron	Gino Spinelli
Hurricanes (B8)	31764	Boys 8 3/L	9	1	0	0	27	39	14	25	Eric Wieland	Tom Click
Thunder (B8)	31763	Boys 8 4/D2	3	3	2	0	11	16	15	1	George Selibas	Steven Jackson
Athletics	31762	Boys 8 4/H	2	8	0	0	6	19	48	-29	Aimee Cole	Laney Hammond
Galaxy	31761	Boys 6 2/B	5	2	3	0	18	27	21	6	Patrick Morrissey	Shaun Fitzgibbon
B6 Academy Orange	31790	Boys 6 3/C	4	5	1	1	12	33	22	11	Michael Gomes	Iain Martin
Rovers	31760	Boys 6 4/C	0	4	2	0	2	8	29	-21	Gayla Langlois	None
B6 Academy White	31789	Boys 6 4/C	7	2	1	0	20	30	13	17	Devin Ramos	Iain Martin
United	31759	Boys 5 3/A	5	3	2	0	16	41	21	20	Brian Heaton	Melissa Recos
Revolution	31758	Boys 5 4/B1	1	6	1	0	4	9	25	-16	Greg Gilson	Patrick Tripp
Fury	31757	Boys 4 2/C	8	0	2	0	26	42	12	30	Keith Gilbreath	Jarred Sakakeeny
Hooligans	31755	Boys 4 3/D	4	6	0	0	12	21	30	-9	Patrick Maiella	John Murray
Junior Hillers	31756	Boys 4 3/D	1	6	3	0	6	10	27	-17	Hugh Gregg	Jason Sweet
B4 Academy	31788	Boys 4 3/J	7	2	1	0	22	48	22	26	Florent Martin	Iain Martin
Raptors	31753	Boys 4 3/M	2	7	1	0	7	11	36	-25	Peter Fogg	Dave Holborn
Avengers	31754	Boys 4 3/M	7	3	0	0	21	30	21	9	Michelle Midkiff	Matt Hodges
Thunder (B3)	31751	Boys 3 3/B	1	3	0	0	3	7	16	-9	Heath Guay	Mike DeCandia
B3 Academy	31782	Boys 3 3/B	5	4	1	0	16	41	30	11	Cameron Young	Iain Martin
Hornets	31752	Boys 3 3/E	5	5	0	0	15	29	26	3	Drew Griffin	Tom St.Pierre
Lions	31750	Boys 3 3/G	5	5	0	0	15	29	31	-2	Nate Repucci	Jill Spinale"""

save_and_import(fall2022_data, 'HOP', 2022, 'Fall')

# Spring 2022
print("\n=== IMPORTING HOP SPRING 2022 ===\n")
spring2022_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
GHS Academy	32711	Girls 11 2/A	1	6	0	0	3	7	33	-26	Michael Gomes	Iain Martin
G8 Academy Orange	30336	Girls 8 2/A	0	10	0	0	0	6	32	-26	Iain Martin	None
G8 Academy White	30335	Girls 8 3/G	2	8	0	0	6	4	17	-13	Michael Gomes	Iain Martin
Dynamo (G7/8)	31666	Girls 8 4/D	5	3	2	0	17	11	12	-1	Brad Wilson	Michelle Midkiff
G6 Academy Orange	30333	Girls 6 3/H	2	8	0	0	6	20	34	-14	Florent Martin	Iain Martin
Breakers	30989	Girls 6 4/B	1	9	0	1	2	12	29	-17	Juliana Grontzos	Ana Tomas
Hawks	30988	Girls 5 2/E	4	0	1	0	13	20	8	12	Jarrod Clement	Bryan Memmelaar
Hurricanes (G5)	31665	Girls 5 4/E	1	6	2	0	5	5	21	-16	Emme Joy	Ellie Driscoll
Fire	30978	Girls 4 2/A2	3	2	5	0	14	17	16	1	Denis Murphy	Dave Fine
G4 Academy Orange	30332	Girls 4 3/E	1	2	1	0	4	4	11	-7	Iain Martin	None
Cheetahs	31664	Girls 4 3/G	1	8	1	0	4	5	22	-17	Jennifer Vale	Eric Gangl
Lightning	31663	Girls 4 4/G	0	5	0	0	0	7	25	-18	Randy Sanborn	Terry O'Callaghan
Huskies	31595	Girls 3 3/B	1	9	0	0	3	12	42	-30	Louis Boulanger	Lauren Melton
Hillers (G3)	31596	Girls 3 3/B	4	3	3	0	15	24	19	5	Matt Tighe	Ryan Jones
Orange Crush	31593	Girls 3 3/D	3	4	3	0	12	19	30	-11	Dave Salerno	Marilyn Gibbs
Firebirds	31594	Girls 3 3/D	6	1	3	0	21	29	16	13	Kaitlyn Mullen	Courtney Galvani
BHS Academy	32709	Boys 12 2/A	2	4	1	0	7	20	22	-2	Florent Martin	Iain Martin
Hillers (B8)	31006	Boys 8 3/C	7	0	3	0	24	42	8	34	Todd Garron	Doug Gordon
Athletics	31005	Boys 8 4/B	2	7	1	0	7	16	24	-8	Gary Miloscia	Mark Logan
Thunder (B8)	31004	Boys 8 4/G2	4	1	2	0	14	24	16	8	George Selibas	Stacie Kirkwood
B6 Academy Orange	30339	Boys 6 3/D	6	2	2	1	19	25	8	17	Iain Martin	None
Hurricanes (B6)	31669	Boys 6 3/E	3	5	0	0	9	23	23	0	Jason Pritchard	Eric Wieland
B6 Academy White	30924	Boys 6 4/E2	5	3	2	0	17	17	15	2	Cameron Young	Iain Martin
Rovers	30999	Boys 5 4/C	1	3	2	1	4	13	17	-4	Nate Thomas	Peter Thomas
B4 Academy Orange	30338	Boys 4 3/D	9	0	0	0	27	38	10	28	Florent Martin	Iain Martin
B4 Academy White	30337	Boys 4 3/H	2	2	6	0	12	22	20	2	Michael Gomes	Iain Martin
Revolution	31668	Boys 4 4/A	2	5	2	0	6	27	27	0	Cameron Young	None
United	31667	Boys 4 4/F	0	0	1	0	1	1	1	0	Veronica White	Katrina Provencher
Hooligans	30994	Boys 3 3/A	8	0	2	0	26	43	16	27	Jarred Sakakeeny	Patrick Maiella
Dynamo (B3)	30996	Boys 3 3/A	5	2	3	0	18	24	24	0	Keith Gilbreath	Brad Wilson
Raptors	30995	Boys 3 3/B	6	3	1	0	19	40	32	8	Peter Fogg	Jason Sweet"""

save_and_import(spring2022_data, 'HOP', 2022, 'Spring')

print("\n=== DONE WITH REMAINING HOP SEASONS ===")
print("Still need: Fall 2021, Spring 2021")
