#!/usr/bin/env python3
"""Import final 2 HOP seasons: Fall 2021, Spring 2021"""

from universal_import import save_and_import

# Fall 2021
print("\n=== IMPORTING HOP FALL 2021 ===\n")
fall2021_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
G8 Academy Orange	30336	Girls 8 2/C	4	4	2	0	14	15	16	-1	Iain Martin	Michael Gomes
United (G8)	30992	Girls 8 3/J	7	2	0	0	21	22	10	12	Brad Wilson	Mark Valutkevich
G8 Academy White	30335	Girls 8 4/A	9	0	1	0	28	26	6	20	Michael Gomes	Iain Martin
Thunder (G8)	30991	Girls 8 4/H	1	7	2	0	5	10	31	-21	Michelle Midkiff	None
Hurricanes (G6)	30990	Girls 6 3/B	10	0	0	0	30	31	1	30	Ken Abrahamsen	Martha Godfroy
G6 Academy Orange	30333	Girls 6 3/F	1	8	0	0	3	16	31	-15	Florent Martin	Iain Martin
Breakers	30989	Girls 6 4/A	4	4	1	0	13	19	27	-8	Brian Skaff	Tess Hanson
Hawks	30988	Girls 5 2/C	0	8	2	0	2	8	27	-19	Heather Smith	Eric Gangl
FC Hillers	30987	Girls 5 4/A1	2	6	2	0	8	15	25	-10	Bryan Memmelaar	Joey Fonseca
Express	30981	Girls 5 4/E1	0	9	0	0	0	2	25	-23	Carly Seidewand	Jennifer Carter
Fire	30978	Girls 4 2/D	8	1	1	0	25	28	14	14	Dave Fine	Gino Spinelli
G4 Academy Orange	30332	Girls 4 3/H	8	0	2	0	26	42	22	20	Steve Patino	Iain Martin
Honey Badgers	30976	Girls 4 4/A	0	5	1	0	1	11	41	-30	Jennifer Vale	Keith Gilbreath
Lightning	30977	Girls 4 4/A	3	3	0	0	9	19	14	5	Randy Sanborn	Eric Benson
Junior Storm	30975	Girls 3 2/A	0	4	2	0	2	4	19	-15	Matt Tighe	Dave Salerno
Fireworks	30973	Girls 3 3/E	5	0	0	0	15	16	6	10	Dawn McNerney	Marilyn Gibbs
Stars	30972	Girls 3 3/G	5	5	0	0	15	32	34	-2	Kaitlyn Mullen	Courtney Galvani
Hurricanes (G3)	30974	Girls 3 3/G	3	6	0	0	9	27	22	5	Louis Boulanger	None
Hillers (B8)	31006	Boys 8 3/A	5	3	2	0	17	24	22	2	Doug Gordon	Todd Garron
Athletics	31005	Boys 8 3/H	3	5	2	0	11	27	27	0	Gary Miloscia	Jessica Bruce
United (B8)	31003	Boys 8 4/A2	1	9	0	0	3	12	49	-37	Nate Repucci	Kevin Stacey
Thunder (B8)	31004	Boys 8 4/H	1	4	0	0	3	6	12	-6	George Selibas	Stacie Kirkwood
Hillers (B6)	31002	Boys 6 2/F	7	1	2	0	23	32	14	18	Dave Fine	Jason Pritchard
B6 Academy Orange	30339	Boys 6 3/E	6	2	2	0	20	32	13	19	Steve Patino	Iain Martin
B6 Academy White	30924	Boys 6 3/G2	0	8	1	0	1	3	35	-32	Cameron Mullins	Iain Martin
Revolution (B6)	31001	Boys 6 4/C	1	3	1	0	4	9	15	-6	Anthony Gonzalez	Rob Benson
Galaxy	31000	Boys 5 2/A	2	5	3	0	9	19	28	-9	Patrick Morrissey	Shaun Fitzgibbon
Rovers	30999	Boys 5 4/H	3	2	0	0	9	12	7	5	Gayla Langlois	Ted Behrens
B4 Academy Orange	30338	Boys 4 2/D	2	8	0	0	6	21	43	-22	Florent Martin	Iain Martin
B4 Academy White	30337	Boys 4 3/J	5	1	0	0	15	18	9	9	Michael Gomes	Iain Martin
United (B4)	30998	Boys 4 3/J	8	2	0	1	23	39	10	29	Brian Heaton	Matt Colleran
Revolution (B4)	30997	Boys 4 4/D	0	5	0	0	0	2	24	-22	Greg Gilson	None
Raptors	30994	Boys 3 3/C	9	0	1	0	28	40	7	33	Peter Fogg	Aico Van Nunen
Hooligans	30995	Boys 3 3/C	7	3	0	0	21	34	13	21	Jarred Sakakeeny	Hugh Gregg
Dynamo	30996	Boys 3 3/C	6	3	1	1	18	25	12	13	Keith Gilbreath	Ed O'Donnell
Avengers	30993	Boys 3 3/H	5	0	0	0	15	12	2	10	Michelle Midkiff	Krystal Avila"""

save_and_import(fall2021_data, 'HOP', 2021, 'Fall')

# Spring 2021
print("\n=== IMPORTING HOP SPRING 2021 ===\n")
spring2021_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
G8 Academy Orange	30336	Girls 8 2/E	3	3	4	0	13	11	14	-3	Michael Gomes	Kevin Friel
United (G7/8)	30313	Girls 8 3/D	1	6	2	0	5	5	20	-15	Chris Michaud	Brad Wilson
G8 Academy White	30335	Girls 8 3/H	1	9	0	0	3	8	30	-22	Steve Patino	Kevin Friel
Cheetahs	30312	Girls 8 4/E	0	7	3	0	3	3	20	-17	Jamie Devlin	Paul McCarthy
G6 Academy Orange	30334	Girls 6 2/E	2	5	2	0	8	19	29	-10	Kevin Friel	Florent Martin
G6 Academy White	30333	Girls 6 3/F1	3	3	2	0	11	21	19	2	Florent Martin	Kevin Friel
Junior Hillers	30311	Girls 6 4/E	3	6	1	0	10	27	35	-8	Kylie Davis	None
Hawks	30309	Girls 4 3/A	2	7	1	0	7	20	35	-15	Jimmy Odierna	Heather Smith
G4 Academy Orange	30332	Girls 4 3/F	1	6	0	0	3	15	30	-15	Joel Cordeiro	Kevin Friel
FC Hillers	30308	Girls 4 3/G1	1	6	1	0	4	3	29	-26	Alexis Viehl	Amanda Normandeau
Orange Crush	30305	Girls 3 3/C1	2	5	1	0	7	16	27	-11	Denis Murphy	Kelly Toomer
Fire	30306	Girls 3 3/C1	5	0	3	0	18	29	7	22	Dave Fine	Gino Spinelli
BHS Academy	30840	Boys 12 1/B2	1	5	1	1	3	13	22	-9	Steve Patino	Kevin Friel
Athletics	30331	Boys 8 3/D	9	0	1	0	28	49	19	30	Todd Garron	Doug Gordon
B8 Academy Orange	30340	Boys 8 3/G	2	5	3	0	9	21	29	-8	Florent Martin	Kevin Friel
B6 Academy Orange	30339	Boys 6 3/E	4	4	1	0	13	17	18	-1	Joel Cordeiro	Kevin Friel
Thunder	30330	Boys 6 4/A	6	4	0	0	18	22	16	6	Todd Garron	George Selibas
Revolution	30325	Boys 5 3/D	4	6	0	0	12	23	28	-5	Rob Benson	Jason Pritchard
B4 Academy Orange	30338	Boys 4 2/D	1	7	1	0	4	11	36	-25	Steve Patino	Kevin Friel
Rovers	30315	Boys 4 3/D	1	2	0	0	3	3	11	-8	Hugh Gregg	Steven Levandosky
B3 Academy White	30337	Boys 3 3/E	7	1	2	1	22	33	11	22	Michael Gomes	Kevin Friel
United (B3)	30314	Boys 3 3/F	5	4	1	1	15	41	26	15	Brian Heaton	Matt Colleran"""

save_and_import(spring2021_data, 'HOP', 2021, 'Spring')

print("\n=== ALL HOP SEASONS COMPLETE ===")
print("Hopkinton: 10 seasons imported (Fall 2025 - Spring 2021)")
