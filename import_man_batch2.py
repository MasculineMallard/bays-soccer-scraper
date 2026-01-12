#!/usr/bin/env python3
"""Import MAN Fall 2023 through Spring 2021 - Final 7 seasons"""

from universal_import import save_and_import

# Fall 2023
print("\n=== IMPORTING MAN FALL 2023 ===\n")
fall2023_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Hornets I	3155	Girls 8 2/E	8	1	1	0	25	19	2	17	Mark Powers	Doug LaCamera
Hornets II	3159	Girls 8 3/E	7	1	2	0	23	18	3	15	Meg Lanagan	James Morris
Hornets III	3163	Girls 8 3/J2	1	5	2	0	5	5	11	-6	Sergio Martin	Greg DeSista
Hornets IV	3166	Girls 8 4/H	8	2	0	0	24	29	10	19	Traci Mazur	None
Hornets I	3170	Girls 6 2/B1	3	4	3	0	12	15	27	-12	Maggie Gentili	Jeffrey Ward
Hornets II 	3171	Girls 6 3/G	5	1	4	0	19	28	16	12	Chris Joynes	Hank Kurtzman
Hornets I	3175	Girls 5 2/C	7	2	1	0	22	20	13	7	David Kobasa	Jim Stevens
Hornets II	3176	Girls 5 4/C	6	2	2	0	20	33	9	24	Sergio Martin	Paul Miao
Hornets I	3188	Girls 4 2/D	8	1	1	0	25	28	4	24	Dennis Sykes	Robert Faria
Hornets II	3190	Girls 4 3/G	8	1	1	0	25	32	10	22	Traci Mazur	Sarah Joynes
Hornets III	3193	Girls 4 4/B	3	1	0	0	9	14	8	6	Chris Chery	Jamie Mullen
Green Hornets	3216	Girls 3 3/B	8	1	1	0	25	39	13	26	Robert Faria	Meghan Murphy
Hornets	3218	Girls 3 3/B	3	4	3	0	12	30	31	-1	Mike DAmico	Kyle McMorrow
Buzz	3219	Girls 3 4/B	2	7	1	0	7	19	27	-8	Paul Hebard Jr.	Brian Sexton
Hornets I	3222	Boys 8 2/C	6	0	4	0	22	27	11	16	Jessica Grey	Christian Franco
Hornets II	3226	Boys 8 3/C1	5	3	0	0	15	23	9	14	Teri Fleming	Joshua Correia
Hornets III 	4410	Boys 8 3/J	5	5	0	0	15	21	19	2	David Kobasa	Brian Sexton
Hornets - Green	31748	Boys 8 4/K	6	3	1	0	19	36	24	12	Josh Curry	Jerred Campbell
Hornets - White	33179	Boys 8 4/L	3	5	2	0	11	13	22	-9	Rick McMaster	Patrick Curley
Hornets I	3232	Boys 6 1/A	4	3	2	0	14	23	19	4	John McPherson	Daniel Cooper
Hornets II	3233	Boys 6 3/C	1	8	1	0	4	17	42	-25	Jeff Kobs	Jaeson Kawadler
Hornets I	3236	Boys 5 1/A1	4	4	2	0	14	20	21	-1	Jessica Grey	Mohamed Driss
Hornets II	3238	Boys 5 3/C	1	4	0	0	3	7	16	-9	Derek Clinton	Brian Levesque
Hornets III	33183	Boys 5 4/H	2	8	0	0	6	16	29	-13	Joseph Agnello	Derek Power
Hornets I	3239	Boys 4 2/F	0	3	2	0	2	2	8	-6	Danielle Correia	Greg DeSista
Hornets II	3243	Boys 4 3/H	2	7	1	0	7	12	42	-30	Jose Dolores	Keith Kerr
Hornets III	3245	Boys 4 4/K	6	2	2	0	20	31	15	16	Greg Quinn	Nithin Mohan
Green Hornets	3249	Boys 3 3/D	4	2	4	0	16	37	22	15	Jonathan Holmes	Edward Gardner
Hornets	3250	Boys 3 3/D	8	1	1	0	25	38	13	25	George Apazidis	Genevieve Salzsieder
Buzz	33184	Boys 3 4/E	5	4	0	0	15	35	23	12	Derek Power	Carlos Cortejoso"""

save_and_import(fall2023_data, 'MAN', 2023, 'Fall')

# Spring 2023
print("\n=== IMPORTING MAN SPRING 2023 ===\n")
spring2023_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Hornets I	3155	Girls 8 2/A	8	1	1	0	25	30	10	20	Desmond Doyle	Brian Znoj
Hornets II	3159	Girls 8 3/A	2	8	0	0	6	9	21	-12	Chris Joynes	Mark Powers
Hornets III	3163	Girls 8 3/H	1	4	0	0	3	7	12	-5	Sergio Martin	Edward Cosgrove
Hornets IV	3166	Girls 8 4/K	5	3	2	0	17	21	9	12	Will Reynolds	Sahar Forghan
Hornets I	3170	Girls 6 2/A	6	2	2	0	20	16	9	7	Douglas Robinson	Nancy Cremins
Hornets II 	3171	Girls 6 4/D	7	1	2	0	23	30	7	23	Greg DeSista	Brian Levesque
Hornets I	3175	Girls 5 1/AA	2	1	2	0	8	9	7	2	Maggie Gentili	Jeffrey Ward
Hornets II	3176	Girls 5 3/C	1	7	1	1	3	9	25	-16	Matthew Cressy	Dennis Cook
Hornets III	31747	Girls 5 3/F	1	6	3	0	6	19	33	-14	Chris Joynes	Hank Kurtzman
Hornets I	3188	Girls 4 2/B	3	5	2	0	11	13	22	-9	David Kobasa	Ryan Shanahan
Hornets II	3190	Girls 4 3/A	5	2	3	0	18	12	9	3	Chris DiPetrillo	Nicole Mannarino
Hornets III	3193	Girls 4 4/B	2	6	2	0	8	15	19	-4	Sergio Martin	Paul Miao
Green Hornets	3216	Girls 3 3/B	2	8	0	0	6	20	32	-12	Robert Faria	None
Hornets	3218	Girls 3 3/B	4	4	2	0	14	20	22	-2	Traci Mazur	None
Buzz	3219	Girls 3 4/B	6	4	0	0	18	31	23	8	Dennis Sykes	Chris Chery
Hornets I	3222	Boys 8 2/E	6	2	2	0	20	24	15	9	Teri Fleming	Alexander Nosovitski
Hornets II	3226	Boys 8 3/C	3	5	2	0	11	13	25	-12	Paul Miao	None
Hornets III 	4410	Boys 8 3/H	3	5	2	0	11	12	23	-11	David Kobasa	Scott Dunn
Hornets IV	31748	Boys 8 4/J	5	5	0	0	15	36	20	16	Scott O'Connor	Jeff Kobs
Hornets I	3232	Boys 6 2/B2	8	1	1	0	25	27	12	15	Christian Franco	Richard Copp
Hornets II	3233	Boys 6 3/F1	8	1	1	0	25	39	12	27	Christopher Conley	Joshua Correia
Hornets III	5301	Boys 6 4/G	6	3	1	1	18	45	20	25	Patrick Curley	None
Hornets I	3236	Boys 5 1/AA	5	3	2	0	17	23	15	8	John McPherson	Daniel Cooper
Hornets II	3238	Boys 5 3/B	2	7	1	0	7	25	37	-12	Jeff Kobs	Jaeson Kawadler
Hornets I	3239	Boys 4 1/A1	6	2	2	0	20	26	14	12	Jessica Grey	Mohamed Driss
Hornets II	3243	Boys 4 3/K	4	6	0	0	12	27	32	-5	Derek Clinton	Genevieve Salzsieder
Hornets III	3245	Boys 4 4/G	1	9	0	0	3	11	42	-31	Derek Power	Joseph Agnello
Green Hornets	3249	Boys 3 3/C	1	8	1	0	4	20	42	-22	Danielle Correia	Jose Dolores
Hornets	3250	Boys 3 3/C	2	6	1	1	6	14	27	-13	Amanda Waldron	None"""

save_and_import(spring2023_data, 'MAN', 2023, 'Spring')

# Fall 2022
print("\n=== IMPORTING MAN FALL 2022 ===\n")
fall2022_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Hornets I	3155	Girls 8 2/A	6	2	2	0	20	24	12	12	Desmond Doyle	Brian Znoj
Hornets II	3159	Girls 8 3/D	8	1	1	0	25	17	4	13	Chris Joynes	Mark Powers
Hornets III	3163	Girls 8 4/C	9	1	0	0	27	36	14	22	Sergio Martin	Edward Cosgrove
Hornets IV	3166	Girls 8 4/G2	2	1	5	0	11	10	8	2	Will Reynolds	Sahar Forghan
Hornets I	3170	Girls 6 1/A	1	4	0	0	3	5	12	-7	Douglas Robinson	Nancy Cremins
Hornets II 	3171	Girls 6 3/A	1	9	0	0	3	6	30	-24	Greg DeSista	Meg Lanagan
Hornets III 	3173	Girls 6 4/D	2	4	0	0	6	6	11	-5	Brian Levesque	Ed Charlton
Hornets I	3175	Girls 5 1/B	3	2	4	0	13	15	17	-2	Maggie Gentili	Jeffrey Ward
Hornets II	3176	Girls 5 3/C	4	4	1	0	13	17	15	2	Matthew Cressy	Dennis Cook
Hornets III	31747	Girls 5 4/A	8	1	0	0	24	31	12	19	Chris Joynes	Hank Kurtzman
Hornets I	3188	Girls 4 2/D	7	0	3	0	24	30	12	18	David Kobasa	Timothy Eitas
Hornets II	3190	Girls 4 3/D	8	0	2	0	26	27	5	22	Chris DiPetrillo	Nicole Mannarino
Hornets III	3193	Girls 4 4/B	4	5	1	1	12	19	21	-2	Sergio Martin	Paul Miao
Green Hornets	3216	Girls 3 3/B	2	4	4	0	10	17	17	0	Robert Faria	Stephen Brown
Hornets	3218	Girls 3 3/B	3	4	3	0	12	13	17	-4	Traci Mazur	None
Buzz	3219	Girls 3 4/B	3	2	5	0	14	26	22	4	Dennis Sykes	Chris Chery
Hornets I	3222	Boys 8 2/B	1	8	1	0	4	11	34	-23	Teri Fleming	Alexander Nosovitski
Hornets II	3226	Boys 8 3/F	3	4	3	0	12	13	15	-2	Robin O'Brien	Paul Miao
Hornets III 	4410	Boys 8 4/B	6	2	2	0	20	31	17	14	David Kobasa	Scott Dunn
Hornets IV	31748	Boys 8 4/L	1	5	0	0	3	11	18	-7	Dana Cooney	Scott O'Connor
Hornets I	3232	Boys 6 2/B	4	5	1	0	13	13	18	-5	Christian Franco	Richard Copp
Hornets II	3233	Boys 6 3/E	5	1	4	0	19	26	14	12	Christopher Conley	Joshua Correia
Hornets III	5301	Boys 6 4/C	0	9	1	0	1	11	39	-28	Patrick Curley	John Ings
Hornets I	3236	Boys 5 1/A2	5	2	1	0	16	22	16	6	John McPherson	Daniel Cooper
Hornets II	3238	Boys 5 3/A	2	6	2	0	8	17	32	-15	Jeff Kobs	Joseph Andruzzi
Hornets I	3239	Boys 4 1/A2	8	1	1	0	25	27	15	12	Jessica Grey	Mohamed Driss
Hornets II	3243	Boys 4 3/J	0	4	1	0	1	6	19	-13	Derek Clinton	Genevieve Salzsieder
Hornets III	3245	Boys 4 4/E	2	7	1	0	7	11	33	-22	Derek Power	Joseph Agnello
Green Hornets	3249	Boys 3 3/A	2	8	0	1	5	7	26	-19	Danielle Correia	Jose Dolores
Hornets	3250	Boys 3 3/A	4	6	0	0	12	23	32	-9	Dana Cooney	Amanda Waldron
Swarm	30663	Boys 3 4/C	1	8	1	0	4	10	23	-13	Jason Hinton	Marianne Murphy"""

save_and_import(fall2022_data, 'MAN', 2022, 'Fall')

# Spring 2022
print("\n=== IMPORTING MAN SPRING 2022 ===\n")
spring2022_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Hornets I	3155	Girls 8 1/A	7	2	1	0	22	16	5	11	John McPherson	Desmond Doyle
Hornets II	3159	Girls 8 3/A	3	4	3	0	12	21	24	-3	Jon Leman	Brian Znoj
Hornets III	3163	Girls 8 3/F	1	8	0	0	3	3	26	-23	Chris Joynes	Jon Lipsky
Hornets IV	3166	Girls 8 4/G	5	4	1	0	16	18	15	3	Paul Flynn	Sergio Martin
Hornets I	3170	Girls 6 2/A	4	1	5	0	17	16	8	8	Mark Powers	Amanda Waldron
Hornets II 	3171	Girls 6 3/A	3	3	4	0	13	10	11	-1	Tony Troilo	Mark Nappa
Hornets III 	3173	Girls 6 3/H	3	4	3	0	12	8	14	-6	Will Reynolds	Paul Hebard Jr.
Hornets I	3175	Girls 5 2/A	4	3	3	0	15	20	19	1	Douglas Robinson	Doug LaCamera
Hornets II	3176	Girls 5 4/B	7	1	2	0	23	25	10	15	Greg DeSista	Brian Levesque
Hornets I	3188	Girls 4 1/A2	5	4	1	0	16	20	16	4	Jeffrey Ward	Maggie Gentili
Hornets II	3190	Girls 4 3/C	7	2	1	0	22	26	13	13	Mark McGuire	Matthew Cressy
Hornets III	3193	Girls 4 3/F	1	9	0	0	3	7	40	-33	Chris Joynes	Dennis Cook
Green Hornets	3216	Girls 3 2/B	7	2	1	0	22	24	14	10	Chris DiPetrillo	Timothy Eitas
Hornets	3218	Girls 3 2/B	1	7	2	0	5	23	30	-7	David Kobasa	Paul Miao
Buzz	3219	Girls 3 3/F	0	9	1	0	1	6	22	-16	Tim Burgess	None
Hornets	30855	Boys 11 2/A1	5	2	0	1	14	18	10	8	Paul Scholes	Stephen Sheridan
Hornets I	3222	Boys 8 2/F	3	5	2	0	11	16	17	-1	Teri Fleming	Brian DiVasta
Hornets II	3226	Boys 8 3/H	3	4	3	0	12	23	23	0	Giampaolo DiGregorio	John Patrinos
Hornets III 	4410	Boys 8 4/G1	2	4	2	0	8	15	19	-4	Jeff Kobs	Robin O'Brien
Hornets I	3232	Boys 6 2/A	2	5	3	0	9	12	17	-5	Andre Fernandes	Richard Medeiros
Hornets II	3233	Boys 6 3/F	7	1	2	0	23	38	17	21	Teri Fleming	Paul Miao
Hornets III	5301	Boys 6 4/A	1	8	1	0	4	13	43	-30	Josh Curry	Kevin Donovan
Hornets I	3236	Boys 5 2/B	7	2	1	0	22	33	12	21	Richard Copp	Christian Franco
Hornets II	3238	Boys 5 3/A	5	4	1	0	16	25	16	9	Danielle Correia	Joshua Correia
Hornets III	11411	Boys 5 4/E	4	3	1	0	13	24	12	12	Keith Kerr	None
Hornets I	3239	Boys 4 1/A2	7	0	1	0	22	46	15	31	Daniel Cooper	John McPherson
Hornets II	3243	Boys 4 3/A	6	4	0	0	18	27	17	10	Richard Jablonski	Joseph Andruzzi
Hornets III	3245	Boys 4 4/F	6	2	0	0	18	32	15	17	Jeff Kobs	Mark Pozzo
Green Hornets	3249	Boys 3 2/A	1	7	2	0	5	16	39	-23	Jessica Grey	David Parsons
Hornets	3250	Boys 3 2/A	2	6	2	0	8	25	38	-13	Mohamed Driss	Meghan Murphy
Swarm	30663	Boys 3 4/C	6	3	1	0	19	37	17	20	Derek Power	Genevieve Salzsieder"""

save_and_import(spring2022_data, 'MAN', 2022, 'Spring')

# Fall 2021
print("\n=== IMPORTING MAN FALL 2021 ===\n")
fall2021_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Hornets I	3155	Girls 8 1/A	6	2	2	0	20	21	14	7	John McPherson	Desmond Doyle
Hornets II	3159	Girls 8 3/A	3	5	2	0	11	16	15	1	Jon Leman	Matt Zajac
Hornets III	3163	Girls 8 3/J	4	6	0	0	12	9	17	-8	Chris Joynes	None
Hornets IV	3166	Girls 8 4/E	6	4	0	0	18	17	25	-8	Paul Flynn	Sergio Martin
Hornets I	3170	Girls 6 2/C	7	2	1	0	22	27	12	15	Mark Powers	Amanda Waldron
Hornets II 	3171	Girls 6 3/D	5	1	4	0	19	31	16	15	Tony Troilo	Mark Nappa
Hornets III 	3173	Girls 6 4/F	10	0	0	0	30	41	3	38	Will Reynolds	Paul Hebard Jr.
Hornets I	3175	Girls 5 2/C	8	1	1	0	25	32	10	22	Douglas Robinson	Doug LaCamera
Hornets II	3176	Girls 5 3/F	2	8	0	0	6	4	26	-22	Greg DeSista	Brian Levesque
Hornets I	3188	Girls 4 2/B	7	0	3	0	24	35	10	25	Jeffrey Ward	Maggie Gentili
Hornets II	3190	Girls 4 3/F	5	4	1	0	16	15	19	-4	Mark McGuire	Matthew Cressy
Hornets III	3193	Girls 4 4/B	8	1	1	0	25	40	11	29	Chris Joynes	None
Hornets	3218	Girls 3 2/B1	2	2	2	0	8	12	14	-2	David Kobasa	Paul Miao
Green Hornets	3216	Girls 3 3/B	9	1	0	0	27	46	11	35	Chris DiPetrillo	Timothy Eitas
Buzz	3219	Girls 3 4/B	8	2	0	0	24	31	11	20	Tim Burgess	None
Hornets I	3222	Boys 8 2/E	3	4	3	0	12	14	14	0	Teri Fleming	Brian DiVasta
Hornets II	3226	Boys 8 3/G	5	5	0	0	15	22	26	-4	Giampaolo DiGregorio	John Patrinos
Hornets III 	4410	Boys 8 4/J	0	3	1	0	1	2	14	-12	Jeff Kobs	Robin O'Brien
Hornets I	3232	Boys 6 2/C	9	0	1	0	28	25	7	18	Andre Fernandes	Richard Medeiros
Hornets II	3233	Boys 6 3/B	1	7	2	0	5	12	33	-21	Teri Fleming	David Kobasa
Hornets III	5301	Boys 6 4/A	4	3	3	0	15	17	24	-7	Scott Cummings	Josh Curry
Hornets I	3236	Boys 5 2/C	6	2	2	0	20	32	18	14	Richard Copp	Christian Franco
Hornets II	3238	Boys 5 3/D	8	1	1	0	25	30	13	17	Danielle Correia	Joshua Correia
Hornets III	11411	Boys 5 4/D	5	3	2	0	17	30	16	14	Christopher Conley	Keith Kerr
Hornets I	3239	Boys 4 2/C1	3	0	1	0	10	18	8	10	John McPherson	Daniel Cooper
Hornets II	3243	Boys 4 3/A	4	1	1	0	13	17	5	12	Richard Jablonski	Joseph Andruzzi
Hornets III	3245	Boys 4 4/C	2	7	1	0	7	11	28	-17	Jeff Kobs	Deborah Stratton
Green Hornets	3249	Boys 3 2/C	5	0	0	0	15	19	6	13	Jessica Grey	David Parsons
Hornets	3250	Boys 3 3/B	7	2	1	0	22	39	22	17	Mohamed Driss	Meghan Murphy
Swarm	30663	Boys 3 4/A	0	6	1	0	1	8	30	-22	Derek Power	George Apazidis"""

save_and_import(fall2021_data, 'MAN', 2021, 'Fall')

# Spring 2021
print("\n=== IMPORTING MAN SPRING 2021 ===\n")
spring2021_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Hornets I	3155	Girls 8 1/A2	4	2	4	0	16	16	15	1	Richard Hart	Kathy McCann
Hornets II	3159	Girls 8 3/A	5	3	2	0	17	11	11	0
Hornets III	3163	Girls 8 3/E2	2	5	1	0	7	6	16	-10	Matt Zajac	Jon Leman
Hornets IV	3166	Girls 8 4/E	4	6	0	0	12	13	25	-12	Paul Flynn	Mark Deckett
Hornets I	3170	Girls 6 2/A	6	1	3	0	21	28	13	15	Desmond Doyle	Brian Znoj
Hornets II 	3171	Girls 6 3/D	6	1	3	0	21	26	11	15	Jennifer Norige	Chris Joynes
Hornets III 	3173	Girls 6 4/A	2	6	1	0	7	15	23	-8		Richard Jablonski
Hornets I	3175	Girls 5 2/A	4	2	2	0	14	24	15	9	Mark Powers	Tony Troilo
Hornets II	3176	Girls 5 3/B	6	2	2	0	20	25	12	13	Jeffrey Gardini	Chris DiPetrillo
Hornets III	3177	Girls 5 4/A1	8	1	1	0	25	37	7	30	Will Reynolds	Sahar Forghan
Green Hornets 	3188	Girls 4 2/D	9	0	1	0	28	35	7	28	Douglas Robinson	Doug LaCamera
Hornets	3190	Girls 4 3/F	2	7	0	0	6	9	34	-25	Meg Lanagan	Peter Mirabile
Buzz	3193	Girls 4 4/B	1	2	2	0	5	8	12	-4	Brian Levesque	Greg DeSista
Mansfield Hornets	3218	Girls 3 2/B	4	0	1	0	13	18	6	12	Mark McGuire	Brian Roche
Mansfield Green Hornets	3216	Girls 3 3/A	9	0	1	0	28	50	10	40	Maggie Gentili	Jeffrey Ward
Mansfield Buzz	3219	Girls 3 4/A	6	4	0	0	18	30	25	5	Chris Joynes	Dennis Cook
Mansfield Hornets	30854	Boys 12 1/A1	1	4	1	2	2	3	7	-4	Ryan Chambers	None
Mansfield Hornets	30855	Boys 11 2/B	6	1	0	0	18	25	6	19	Stephen Sheridan	None
Hornets I	3222	Boys 8 2/C	10	0	0	0	30	43	5	38	Brian Znoj	Desmond Doyle
Hornets II	3226	Boys 8 3/H1	6	3	1	0	19	35	20	15	Caroline Bruno	Brian DiVasta
Hornets III 	4410	Boys 8 4/B	1	9	0	0	3	14	47	-33	Giampaolo DiGregorio	Christopher Jones
Mansfield Hornets I	3232	Boys 6 2/C	5	4	1	0	16	24	23	1	Alexander Nosovitski	Scott Bertolami
Mansfield Hornets II	3233	Boys 6 3/E	6	1	3	0	21	23	14	9	Dan Bonnyman	None
Mansfield Hornets III	5301	Boys 6 4/E	1	6	3	0	6	16	32	-16	Robin O'Brien	Jeff Kobs
Mansfield Hornets I	3236	Boys 5 2/C	2	3	0	0	6	8	7	1	Jessica Grey	Andre Fernandes
Mansfield Hornets II	3238	Boys 5 3/C	5	4	0	0	15	24	20	4	Teri Fleming	Tom McNeill
Mansfield Hornets III	11411	Boys 5 4/D	4	5	0	0	12	22	28	-6	David Kobasa	Josh Curry
Mansfield Green Hornets 	3239	Boys 4 2/D	6	2	2	0	20	38	15	23	Richard Copp	Christian Franco
Mansfield Hornets 	3243	Boys 4 3/D	7	2	1	0	22	27	11	16	Brian Sexton	Christopher Conley
Mansfield Buzz	3245	Boys 4 4/C	4	5	1	0	13	22	20	2	Danielle Correia	Steve Schoonveld
Mansfield Swarm	11162	Boys 4 4/C	3	6	1	0	10	19	34	-15	Keith Kerr	Elizabeth Quersher
Mansfield Green Hornets	3249	Boys 3 2/C	6	3	1	0	19	33	17	16	Daniel Cooper	Doug LaCamera
Mansfield Hornets	3250	Boys 3 2/C	6	2	2	0	20	24	17	7	John McPherson	Tim Mullin
Mansfield Swarm	30663	Boys 3 4/B	8	0	2	0	26	32	11	21	Jeff Kobs	Richard Jablonski"""

save_and_import(spring2021_data, 'MAN', 2021, 'Spring')

print("\n=== ALL MAN SEASONS COMPLETE ===")
print("Mansfield: 10 seasons imported (Fall 2025 - Spring 2021)")
