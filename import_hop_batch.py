#!/usr/bin/env python3
"""Import HOP Fall 2025, Spring 2025, Fall 2024"""

from universal_import import save_and_import

# Fall 2025
print("\n=== IMPORTING HOP FALL 2025 ===\n")
with open('data/pastes/HOP_Fall2025_raw.txt', 'r', encoding='utf-8') as f:
    save_and_import(f.read(), 'HOP', 2025, 'Fall')

# Spring 2025
print("\n=== IMPORTING HOP SPRING 2025 ===\n")
spring2025_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Lady Hillers	34250	Girls 912 3/B1	2	3	1	0	7	10	10	0	Edward Lucy	Michelle Midkiff
Fire	33674	Girls 8 2/B	4	3	3	2	13	10	12	-2	Dave Fine	Denis Murphy
G8 Academy	33701	Girls 8 4/A	6	2	2	0	20	28	10	18	Devin Ramos	Florent Martin
Lightning	33673	Girls 8 4/H	2	5	2	0	8	22	37	-15	Michael Twardowski	Gino Spinelli
Reign	33670	Girls 6 2/C	4	3	3	0	15	25	21	4	Ryan Jones	Mark Haranas
G6 Academy	33700	Girls 6 3/F	6	2	2	0	20	36	22	14	Davi Dias	Florent Martin
Blaze	33669	Girls 6 4/E	2	5	3	0	9	13	30	-17	David Kubiak	None
United	33668	Girls 5 2/A	1	8	1	1	3	8	22	-14	Bryan Memmelaar	Heather Smith
G5 Academy	33699	Girls 5 2/D	3	4	3	0	12	21	23	-2	Iain Martin	Florent Martin
Strikers	33667	Girls 5 3/G	0	9	1	1	0	9	33	-24	Ken O'Toole	Amy Steppacher
Hawks	33666	Girls 5 4/E	0	9	1	1	0	9	36	-27	Lindsey Baumer	Tim French
Kicks	33663	Girls 4 3/C	2	8	0	0	6	16	35	-19	Kristin Dykstra	Gayl Weinmann
Blizzards	33665	Girls 4 3/D	3	6	0	0	9	15	36	-21	Dave Salerno	Mark Gordon
G4 Academy	33698	Girls 4 3/E	2	1	1	0	7	11	6	5	Florent Martin	Devin Ramos
G3 Academy	33697	Girls 3 3/E	9	1	0	0	27	41	17	24	Gabriel Cumplido	Florent Martin
Hillers	33661	Girls 3 4/B	1	6	1	0	4	7	22	-15	John Roach	Liz Roach
Hyenas	33662	Girls 3 4/B	5	5	0	0	15	37	36	1	Jamas LaFreniere 	Margot LaFreniere
Hillers	64	Boys 10 2/A	3	4	0	0	9	15	17	-2	Todd Garron	Patrick Morrissey
Galaxy	34088	Boys 8 3/G	3	3	0	0	9	15	18	-3	Patrick Morrissey	Shaun Fitzgibbon
B8 Academy	33711	Boys 8 4/A	6	4	0	0	18	30	24	6	David Samson	Florent Martin
United	33696	Boys 6 3/A	6	2	2	0	20	25	18	7	Kristin Dykstra	None
B6 Academy	33710	Boys 6 3/F	4	6	0	0	12	31	32	-1	Gabriel Cumplido	Florent Martin
Avengers	33694	Boys 6 4/C	3	6	1	0	10	25	42	-17	Ambikesh Khiriya	Heather Wellington
B5 Academy	33709	Boys 5 3/C	2	1	1	0	7	17	14	3	Davi Dias	Florent Martin
Hooligans	34180	Boys 5 4/A	6	3	1	1	18	34	16	18	Raymond Shehata	None
Revolution	33690	Boys 5 4/F1	6	2	0	0	18	30	17	13	Suraj Saraswat	Amar Prabhu
B4 Academy	33708	Boys 4 3/E1	3	0	1	0	10	19	7	12	Devin Ramos	Florent Martin
Rebels	34181	Boys 4 4/A2	5	2	0	0	15	24	16	8	Jose Laguarta 	None
Breakers	33692	Boys 4 4/B	6	4	0	0	18	36	31	5	David Weibe	None
Avengers	33685	Boys 4 4/B	4	6	0	0	12	41	38	3	Michelle Midkiff	Steven Gargolinski
B3 Academy	33707	Boys 3 2/C	1	2	1	0	4	7	10	-3	Florent Martin	Devin Ramos
Ajax	33679	Boys 3 3/F	1	8	1	0	4	17	37	-20	Grant Van Ranst	Patrick Davis
Bay State Warriors	33678	Boys 3 3/G	7	2	1	0	21	49	27	22	Mark Haranas	Tim Damianidis
FC Orange Crush	33680	Boys 3 3/G	2	6	1	0	7	15	27	-12	Sal Mangano	None"""

save_and_import(spring2025_data, 'HOP', 2025, 'Spring')

# Fall 2024
print("\n=== IMPORTING HOP FALL 2024 ===\n")
fall2024_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Fire	33674	Girls 8 1/B	8	1	0	0	24	42	14	28	Dave Fine	Denis Murphy
Lightning	33673	Girls 8 3/E	0	3	1	0	1	1	9	-8	Gino Spinelli	Derek Pszybysz
G8 Academy	33701	Girls 8 4/C	7	1	2	0	23	27	10	17	Devin Ramos	Iain Martin
Cyclones	33671	Girls 8 4/L	0	4	0	0	0	3	19	-16	Michael Twardowski	None
Reign	33670	Girls 6 2/C	5	4	1	0	16	17	13	4	Ryan Jones	Marilyn Gibbs
G6 Academy	33700	Girls 6 4/A	5	0	0	0	15	20	5	15	David Samson	Iain Martin
Blaze	33669	Girls 6 4/E	1	3	1	0	4	6	9	-3	David Kubiak	Courtney Galvani
G5 Academy	33699	Girls 5 2/C	2	8	0	0	6	10	30	-20	Iain Martin	Florent Martin
United	33668	Girls 5 2/D	3	4	3	0	12	17	15	2	Heather Smith	Bryan Memmelaar
Strikers	33667	Girls 5 3/E	1	8	1	0	4	12	35	-23	Ken O'Toole	Amy Steppacher
Hawks	33666	Girls 5 4/F	0	10	0	0	0	3	46	-43	Gayla Langlois	Lindsey Baumer
G4 Academy	33698	Girls 4 3/C	4	6	0	0	12	20	37	-17	Florent Martin	Iain Martin
Hurricanes	33664	Girls 4 3/F	2	8	0	0	6	14	34	-20	Peter Fogg	Dan Gyllstrom
Amber Aces	33665	Girls 4 3/F	7	2	1	0	22	36	20	16	John Jannino	Dave Salerno
Kicks	33663	Girls 4 3/G	10	0	0	0	30	27	5	22	Kristin Dykstra	Gayl Weinmann
G3 Academy	33697	Girls 3 3/E	5	4	1	0	16	33	27	6	Gabriel Cumplido	Iain Martin
Hillers	33661	Girls 3 4/A1	6	4	0	0	18	17	9	8	John Roach	Liz Roach
Solar Sparks	33662	Girls 3 4/A1	3	5	2	0	11	30	30	0	John Jannino	Fredy Huezo
Hillers	34170	Boys 912 3/C	3	4	0	0	7	34	32	2	Stacie Kirkwood	Steven Jackson
Galaxy	34088	Boys 8 2/D	3	7	0	0	9	14	26	-12	Patrick Morrissey	Steve Quinn
Revolution	34087	Boys 8 3/M	1	5	0	0	3	7	27	-20	Gary Miloscia	TJ Paparazzo
B8 Academy	33711	Boys 8 4/C2	5	3	0	0	15	19	8	11	David Samson	Iain Martin
United	34086	Boys 8 4/K	2	5	3	0	9	18	30	-12	Raymond Shehata	None
United	33696	Boys 6 2/A	5	4	1	0	16	33	20	13	Brad Wilson	Kristin Dykstra
Raptors	33695	Boys 6 3/D	4	6	0	0	12	19	34	-15	Peter Fogg	Matt Hodges
B6 Academy	33710	Boys 6 3/H	4	2	3	0	15	32	22	10	Gabriel Cumplido	Iain Martin
Avengers	33694	Boys 6 4/H1	6	2	2	0	20	44	22	22	Ambikesh Khiriya	Kailey Mulvihill
B5 Academy	33709	Boys 5 2/E	2	7	1	0	7	16	43	-27	Iain Martin	Florent Martin
Hurricanes	33693	Boys 5 3/E	7	0	1	0	22	31	17	14	Drew Griffin	Liz Fleming
Dynamo	33691	Boys 5 4/E2	2	3	0	1	5	6	10	-4	Jeff Bucci	Sami Chogle
Revolution	33690	Boys 5 4/F	1	8	1	0	4	15	38	-23	Suraj Saraswat	Amar Prabhu
B4 Academy	33708	Boys 4 3/A	1	7	2	0	5	27	41	-14	Devin Ramos	Iain Martin
Lightning	33689	Boys 4 3/J	7	1	2	0	23	35	15	20	Marilyn Gibbs	Steven Gargolinski
Breakers	33692	Boys 4 3/J	3	5	2	0	11	36	38	-2	David Weibe	Josh Burton
Hurricanes	33688	Boys 4 3/K	5	2	3	0	18	29	17	12	Leigh Murray	Sara Labrecque
Avengers	33685	Boys 4 4/A	2	2	1	0	7	19	17	2	Michelle Midkiff	Dana Passante
B3 Academy	33707	Boys 3 3/A	2	1	1	0	7	14	11	3	Florent Martin	Iain Martin
United	33677	Boys 3 3/F	5	5	0	0	15	39	38	1	Erik Wolf	Steve Quinn
Ajax	33679	Boys 3 3/F	6	2	2	0	20	33	27	6	Grant Van Ranst	Patrick Davis
Bay State Warriors	33678	Boys 3 3/G	8	2	0	0	24	32	16	16	Tim Wilson	Daniel Hausermann
FC Orange Crush	33680	Boys 3 3/G	1	8	1	0	4	17	44	-27	Sal Mangano	Mark Haranas"""

save_and_import(fall2024_data, 'HOP', 2024, 'Fall')

print("\n=== DONE ===")
print("HOP Fall 2025, Spring 2025, Fall 2024 imported!")
