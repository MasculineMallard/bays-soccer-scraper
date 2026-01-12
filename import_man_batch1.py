#!/usr/bin/env python3
"""Import MAN Spring 2025 through Fall 2022"""

from universal_import import save_and_import

# Spring 2025
print("\n=== IMPORTING MAN SPRING 2025 ===\n")
spring2025_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Hornets I	3170	Girls 8 1/B	7	1	2	0	23	21	12	9	Doug LaCamera	Jeffrey Ward
Hornets II 	3171	Girls 8 3/E	4	1	2	0	14	14	6	8	James Morris	Matthew Cressy
Hornets III	3163	Girls 8 4/A	4	3	3	0	15	16	14	2	Greg DeSista	Brian Levesque
Hornets IV	33590	Girls 8 4/K	4	4	1	0	13	13	10	3	Traci Mazur	Chris Joynes
Hornets I	3175	Girls 6 1/B	1	7	2	0	5	13	26	-13	David Kobasa	Nicole Mannarino
Hornets II	3176	Girls 6 3/C	0	10	0	0	0	3	36	-33	Paul Miao	Sergio Martin
Hornets I	3188	Girls 5 2/A	5	5	0	0	15	11	15	-4	Dennis Sykes	Robert Faria
Hornets II	3190	Girls 5 3/D	2	6	0	0	6	11	22	-11	Chris Chery	Jamie Mullen
Hornets I	3216	Girls 4 1/A	2	6	2	0	8	17	31	-14	Jennifer Urso	Robert Faria
Hornets II	3218	Girls 4 3/C	6	3	1	0	19	28	16	12	Stephanie Fennell	Mike DAmico
Hornets III	3219	Girls 4 4/B	2	3	5	0	11	23	23	0	Paul Hebard Jr.	Will Reynolds
Hornets IV	33612	Girls 4 4/H1	1	7	0	0	3	5	22	-17	Erik Woulfe	Rory Flynn
Hornets	33610	Girls 3 3/A	3	6	1	0	10	14	28	-14	Hank Kurtzman	Jen Morse
Green Hornets	33611	Girls 3 3/A	4	3	3	0	15	26	20	6	Bryan Trout	Betsy Bauler
Hornets I	3222	Boys 8 1/A	1	5	4	0	7	17	20	-3	Richard Copp	Christian Franco
Hornets II	3226	Boys 8 3/C2	4	3	1	1	12	20	7	13	Joshua Correia	Danielle Correia
Hornets III 	4410	Boys 8 3/E	3	5	2	0	11	12	19	-7	Rick McMaster	None
Hornets IV	31748	Boys 8 4/K	6	4	0	0	18	26	25	1	Jeff Kobs	Patrick Curley
Hornets I	3236	Boys 6 1/B	4	4	2	0	14	27	24	3	Jessica Grey	Mohamed Driss
Hornets II	3238	Boys 6 4/B	1	7	2	0	5	13	36	-23	Derek Power	Scott Dunn
Hornets I	3239	Boys 5 3/D	8	1	1	0	25	33	17	16	Danielle Correia	Greg DeSista
Hornets II	3243	Boys 5 4/F2	2	4	1	0	7	21	21	0	Dana Cooney	None
Hornets I	3250	Boys 4 2/A	7	3	0	0	21	48	37	11	George Apazidis	Edward Gardner
Hornets II	3249	Boys 4 3/D	4	6	0	0	12	32	34	-2	John Fitts	Graham Wilson
Hornets III	33184	Boys 4 4/F	4	6	0	0	12	25	28	-3	Mohamed Suraij Mohamed Rousdeen	Scott Ames
Hornets	33606	Boys 3 3/A	7	0	3	0	24	35	24	11	Stephen Brown	Andrew Kastanotis
Green Hornets	33607	Boys 3 3/A	2	8	0	0	6	21	35	-14	Chris Karanicolas	Christopher Conley
Buzz	33608	Boys 3 4/C	3	6	1	0	10	18	22	-4	Patrick Mullen	None
Swarm	33609	Boys 3 4/C	2	7	1	0	7	19	35	-16	Philip Quinn	Tina McGrane"""

save_and_import(spring2025_data, 'MAN', 2025, 'Spring')

# Fall 2024
print("\n=== IMPORTING MAN FALL 2024 ===\n")
fall2024_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Hornets I	3170	Girls 8 2/B	7	2	1	0	22	29	14	15	Doug LaCamera	Jeffrey Ward
Hornets II 	3171	Girls 8 3/E	6	1	3	0	21	19	4	15	Meg Lanagan	James Morris
Hornets III	3163	Girls 8 4/C	3	1	0	0	9	11	6	5	Greg DeSista	Brian Levesque
Hornets IV	33590	Girls 8 4/H	5	4	1	0	16	24	13	11	Traci Mazur	Chris Joynes
Hornets I	3175	Girls 6 2/A	6	3	1	0	19	20	13	7	David Kobasa	Nicole Mannarino
Hornets II	3176	Girls 6 3/D	0	7	2	0	2	3	21	-18	Sergio Martin	Paul Miao
Hornets I	3188	Girls 5 2/A	5	4	1	0	16	17	17	0	Dennis Sykes	Robert Faria
Hornets II	3190	Girls 5 3/A	0	9	1	0	1	12	39	-27	Traci Mazur	Jamie Mullen
Hornets I	3216	Girls 4 1/A1	3	4	3	0	12	18	21	-3	Jennifer Urso	Robert Faria
Hornets II	3218	Girls 4 3/C	5	2	3	0	18	31	20	11	Stephanie Fennell	Mike DAmico
Hornets III	3219	Girls 4 4/J	9	1	0	0	27	40	4	36	Paul Hebard Jr.	Mario Harrison
Hornets IV	33612	Girls 4 4/K	2	7	1	0	7	8	24	-16	Michael Reardon	Erik Woulfe
Hornets	33610	Girls 3 3/B	4	5	1	0	13	26	32	-6	Hank Kurtzman	Jennifer Urso
Green Hornets	33611	Girls 3 3/B	3	6	1	0	10	22	39	-17	Bryan Trout	Betsy Bauler
Hornets I	3222	Boys 8 1/B	6	4	0	0	18	21	16	5	Mario Harrison	Richard Copp
Hornets II	3226	Boys 8 3/F	8	1	1	0	25	35	11	24	Joshua Correia	Danielle Correia
Hornets III 	4410	Boys 8 3/M	7	1	2	0	23	32	13	19	Rick McMaster	None
Hornets IV	31748	Boys 8 4/K	8	1	1	0	25	36	18	18	Jeff Kobs	Patrick Curley
Hornets I	3236	Boys 6 1/A	4	5	1	0	13	14	25	-11	Jessica Grey	Mohamed Driss
Hornets II	3238	Boys 6 4/A	6	1	3	0	21	32	20	12	Derek Power	Scott Dunn
Hornets I	3239	Boys 5 3/F	5	5	0	0	15	25	19	6	Danielle Correia	Greg DeSista
Hornets II	3243	Boys 5 4/J	4	5	1	0	13	23	15	8	Greg Quinn	Jim Mackinaw
Hornets I	3250	Boys 4 2/B	6	3	1	0	19	37	27	10	George Apazidis	Edward Gardner
Hornets II	3249	Boys 4 3/F	7	1	2	0	23	37	10	27	Derek Power	Graham Wilson
Hornets III	33184	Boys 4 4/F	4	1	0	0	12	18	10	8	John Fitts	John-David McElderry
Hornets	33606	Boys 3 3/C	8	2	0	0	24	43	20	23	Stephen Brown	Andrew Kastanotis
Green Hornets	33607	Boys 3 3/C	9	1	0	0	27	35	22	13	Chris Karanicolas	Christopher Conley
Buzz	33608	Boys 3 4/D	8	2	0	0	24	35	16	19	Patrick Mullen	Brittany Mangini
Swarm	33609	Boys 3 4/D	6	4	0	0	18	29	24	5	Christina Vargas	Philip Quinn"""

save_and_import(fall2024_data, 'MAN', 2024, 'Fall')

# Spring 2024
print("\n=== IMPORTING MAN SPRING 2024 ===\n")
spring2024_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Hornets I	3155	Girls 8 2/B	9	1	0	0	27	31	6	25	Mark Powers	Doug LaCamera
Hornets II	3159	Girls 8 3/B	1	3	1	0	4	3	15	-12	Meg Lanagan	James Morris
Hornets III	3163	Girls 8 4/G	7	1	2	0	23	18	7	11	Greg DeSista	Will Reynolds
Hornets I	3170	Girls 6 2/B	5	1	4	0	19	23	15	8	Jeffrey Ward	Mark McGuire
Hornets II 	3171	Girls 6 3/H	7	2	1	0	22	24	6	18	Christopher Herrick	Dennis Cook
Hornets III	33590	Girls 6 4/C	5	2	3	0	18	22	20	2	Chris Joynes	Hank Kurtzman
Hornets I	3175	Girls 5 2/A	1	5	4	0	7	8	21	-13	David Kobasa	Jim Stevens
Hornets II	3176	Girls 5 3/G	1	8	0	0	3	5	28	-23	Paul Miao	Jessica Mullett
Hornets I	3188	Girls 4 2/B	2	6	2	0	8	18	23	-5	Dennis Sykes	Robert Faria
Hornets II	3190	Girls 4 3/B	4	4	2	0	14	25	26	-1	Traci Mazur	Sarah Joynes
Hornets III	3193	Girls 4 4/C	8	1	1	0	25	34	10	24	Chris Chery	Jamie Mullen
Green Hornets	3216	Girls 3 2/B	8	1	1	0	25	44	17	27	Robert Faria	Meghan Murphy
Hornets	3218	Girls 3 3/A	6	3	1	0	19	28	19	9	Mike DAmico	Kyle McMorrow
Buzz	3219	Girls 3 4/D	1	6	2	0	5	12	23	-11	Paul Hebard Jr.	Brian Sexton
Hornets I	3222	Boys 8 1/B	3	7	0	1	8	14	18	-4	Jessica Grey	Christian Franco
Hornets II	3226	Boys 8 3/D	2	7	1	0	7	10	28	-18	Joshua Correia	Teri Fleming
Hornets III 	4410	Boys 8 3/K	6	3	1	0	19	16	11	5	David Kobasa	Brian Sexton
Hornets - Green	31748	Boys 8 4/J	1	8	0	0	3	7	42	-35	Josh Curry	Jerred Campbell
Hornets - White	33179	Boys 8 4/K	5	4	1	0	16	26	21	5	Rick McMaster	Patrick Curley
Hornets I	3232	Boys 6 1/A	3	7	0	3	6	21	24	-3	Daniel Cooper	Mohamed Driss
Hornets II	3233	Boys 6 3/D	2	7	1	0	7	18	31	-13	Jeff Kobs	Jaeson Kawadler
Hornets I	3236	Boys 5 1/B	7	3	0	0	21	33	17	16	Jessica Grey	Mohamed Driss
Hornets II	3238	Boys 5 3/B	1	6	3	0	6	14	34	-20	Derek Clinton	Brian Levesque
Hornets III	33183	Boys 5 4/G	5	4	1	0	15	28	25	3	Derek Power	Sanyam Mittal
Hornets I	3239	Boys 4 3/C	1	7	2	0	5	14	23	-9	Danielle Correia	Greg DeSista
Hornets II	3243	Boys 4 4/D	4	2	4	0	13	38	26	12	Greg Quinn	Nithin Mohan
Hornets	3250	Boys 3 2/D	2	4	0	0	6	14	22	-8	George Apazidis	Derek Power
Green Hornets	3249	Boys 3 3/C1	8	1	0	0	24	42	13	29	Jonathan Holmes	Edward Gardner
Buzz	33184	Boys 3 4/C	3	1	1	0	10	16	9	7	Joshua Sweeney	John-David McElderry"""

save_and_import(spring2024_data, 'MAN', 2024, 'Spring')

print("\n=== MAN BATCH 1 COMPLETE (Spring 2025, Fall 2024, Spring 2024) ===")
