#!/usr/bin/env python3
"""Import WAL Spring 2025, Fall 2024, Spring 2024"""

from universal_import import save_and_import

# Spring 2025
print("\n=== IMPORTING WAL SPRING 2025 ===\n")
spring2025_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Legends 	6529	Girls 12 2/A	5	1	0	0	15	25	10	15	Marty White	Brian Horwitz
Lightning	31936	Girls 8 2/C	4	4	1	0	13	17	15	2	Kathy Martinez	Kate Procaccini
Power	31937	Girls 8 3/H	6	4	0	0	18	15	13	2	David Miles	Mike Porzelt
Courage	31938	Girls 8 4/J	3	5	1	0	10	11	20	-9	Becky McCabe	Josh Singer
Hawks	31940	Girls 6 2/A	4	4	2	0	14	17	14	3	Timothy McElaney	Sarah Madden
Warriors	31941	Girls 6 3/D	8	2	0	0	24	34	16	18	Jamie Hernon	Mike McDonnell
Crush	34116	Girls 6 4/F1	7	2	1	0	21	33	19	14	Anissa Ellis	Patrick Lane
Storm	31944	Girls 5 3/A	9	1	0	0	27	37	9	28	Morgan Miles	Michael Finocchi
Hurricane	31945	Girls 5 3/G	6	3	1	0	19	22	16	6	Nick Sordillo	Margaret Dixon
Thorns	31946	Girls 5 4/E	3	4	3	0	12	16	23	-7	Jon Kopchick	Audrey Grace
Aces	31947	Girls 4 1/B	3	4	3	0	12	18	18	0	Jennifer Gosselin	Kellee Senic
Breakers	31948	Girls 4 3/C	8	1	1	0	25	31	14	17	John Hurley	Carl Kenney
Dash	31949	Girls 4 3/G	2	1	1	0	7	6	6	0	Daniel Olohan	Thomas Neufeld
Trouble	31950	Girls 4 4/H1	3	5	0	0	9	11	17	-6	Colleen Cunningham	Jennifer Dragonetti
FC	6561	Boys 10 2/B	3	4	0	0	7	26	25	1	Kevin Bock	Jonathan Lowe
Warriors	31992	Boys 8 2/A	7	2	1	0	22	42	26	16	Paul Foley	Eric Tjonahen
Legends	32035	Boys 8 4/B	5	3	1	0	16	33	25	8	Horacio Caneja	Keith Jacobsen
Force	32847	Boys 8 4/F	0	9	1	0	1	7	42	-35	Oscar Butragueno	Aaron Price
Thunder	32037	Boys 8 4/N	2	8	0	0	6	16	47	-31	Dan O'Driscoll	Frank Michienzi
Hammers	31998	Boys 6 2/C	2	6	2	0	8	23	28	-5	Muiz Khir	Kristen McPhee
Juventas	32034	Boys 6 3/F	1	7	2	0	5	28	40	-12	Barton Centauro	Isaias Aguiar
Roma	32914	Boys 6 4/J	6	2	1	0	19	47	28	19	Jeff Molles	Minelli Tomaszewski
Revolution	31997	Boys 5 3/A2	3	7	0	0	9	13	31	-18	Patrick Connors	Rob Hollister
Galaxy	31994	Boys 5 4/C	8	1	1	0	24	39	23	16	Meghan Panteleakos	James Desautels
Arsenal	32916	Boys 4 2/B	3	5	2	0	11	18	30	-12	Adam Meszaros	Patrick Murray
Chelsea	33410	Boys 4 3/C	3	4	1	0	10	21	22	-1	Jeff Zammett	Mauro Dellemonache
Milan	32919	Boys 4 3/G	1	7	2	0	5	10	32	-22	Scott Carpenter	Brandon McDowall
Dynamo	34124	Boys 4 4/J	3	5	2	0	11	24	32	-8	Oscar Butragueno	Erin Boyd"""

save_and_import(spring2025_data, 'WAL', 2025, 'Spring')

# Fall 2024
print("\n=== IMPORTING WAL FALL 2024 ===\n")
fall2024_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Lightning	31936	Girls 8 2/B	5	1	4	0	19	17	13	4	Kathy Martinez	Kate Procaccini
Power	31937	Girls 8 3/G	5	2	3	0	18	20	11	9	David Miles	Benjamin Barrett
Courage	31938	Girls 8 4/H	9	0	1	0	28	33	0	33	Mike Porzelt	Michael Susi
Eagles	34115	Girls 8 4/J	3	7	0	0	9	14	18	-4	Becky McCabe	None
Hawks	31940	Girls 6 2/A	6	2	2	0	20	18	12	6	Timothy McElaney	Sarah Madden
Warriors	31941	Girls 6 3/C	7	1	2	0	23	22	9	13	Jamie Hernon	Mike McDonnell
Crush	34116	Girls 6 4/C	7	1	2	1	22	27	8	19	Anissa Ellis	Patrick Lane
Falcons	34117	Girls 6 4/G	6	3	1	0	19	23	17	6	Renee Lamarque	Karen Atkinson
Storm	31944	Girls 5 2/A	1	2	2	0	5	9	13	-4	Keri Moses	Michael Finocchi
Hurricane	31945	Girls 5 3/D	2	7	1	0	7	6	19	-13	Dave Lamb	Glenn Williams
Thorns	31946	Girls 5 4/B	2	2	2	0	7	15	9	6	Nick Sordillo	Jon Kopchick
Dynamo	34119	Girls 5 4/F	4	4	2	0	14	17	16	1	Nicholas O'Leary	Josh Oteri
Aces	31947	Girls 4 2/A	6	4	0	0	18	27	18	9	Jennifer Gosselin	Kellee Senic
Breakers	31948	Girls 4 2/C	0	9	1	0	1	5	36	-31	John Hurley	Carl Kenney
Dash	31949	Girls 4 3/F	3	6	1	0	10	22	31	-9	Deborah Pedersen	Brian Weisman
Trouble	31950	Girls 4 3/G	0	9	1	0	1	6	26	-20	Igor Paliy	Lidia Panfilova
Stars	32995	Girls 4 4/K	3	7	0	0	9	18	30	-12	Eli Smith	Michael Kirby
Warriors	31992	Boys 8 2/D	8	1	1	0	25	40	17	23	Paul Foley	Dana Niles
Legends	32035	Boys 8 3/J	1	6	3	0	6	22	40	-18	Horacio Caneja	Seth Hochberg
Force	32847	Boys 8 4/E	4	1	0	0	12	17	7	10	Keith Jacobsen	Aaron Price
Thunder	32037	Boys 8 4/K	1	4	1	0	4	9	19	-10	Oscar Butragueno	Frank Michienzi
Hammers	31998	Boys 6 2/C	4	5	1	0	13	38	43	-5	Glenn Maffei	Muiz Khir
Juventas	32034	Boys 6 3/J	6	3	1	0	19	36	25	11	Barton Centauro	James Craig Westmoreland
Roma	32914	Boys 6 4/H2	3	5	2	0	11	35	34	1	Jeff Molles	None
Revolution	31997	Boys 5 2/E	2	7	1	0	7	15	25	-10	Patrick Connors	Rob Hollister
Crew	31996	Boys 5 3/H	8	2	0	0	24	41	16	25	Mark Cianci	None
Galaxy	31994	Boys 5 4/E2	0	3	1	0	1	3	12	-9	Meghan Panteleakos	James Desautels
Arsenal	32916	Boys 4 1/B	3	7	0	0	9	19	32	-13	Caitlin Sawyer	Adam Meszaros
Manchester	32918	Boys 4 2/F2	0	4	1	0	1	8	18	-10	David Miles	Mauro Dellemonache
Chelsea	33410	Boys 4 3/B	2	3	1	0	7	7	15	-8	Jeff Zammett	Benjamin Barrett
Milan	32919	Boys 4 3/F	4	6	0	0	12	16	22	-6	Aaron Shepherd	Daniel Nauman
Galaxy	34123	Boys 4 3/H	1	8	1	0	4	17	40	-23	Scott Carpenter	Veronica Marquis
Dynamo	34124	Boys 4 4/J	1	7	0	0	3	11	32	-21	Brandon McDowall	Balraj Senthilkumar"""

save_and_import(fall2024_data, 'WAL', 2024, 'Fall')

# Spring 2024
print("\n=== IMPORTING WAL SPRING 2024 ===\n")
spring2024_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Legends (D1)	6529	Girls 12 1/A	4	2	1	1	12	22	10	12	John Thomsen	Marty White
Lightning	31936	Girls 8 2/B	7	2	1	0	22	24	10	14	Kathy Martinez	Kate Procaccini
Power	31937	Girls 8 4/C	8	1	1	0	25	36	13	23	Jon Paul Sydnor	Terry Doherty
Courage	31938	Girls 8 4/G	3	3	4	0	13	11	10	1	Paul Luongo	Peter Finnerty
Hawks	31940	Girls 6 2/B	2	7	1	0	7	15	25	-10	Robert DeGirolamo	Benjamin Barrett
Warriors	31941	Girls 6 4/F	8	1	0	0	24	34	9	25	Beverly Sprague	Heather Baldassari
Storm	31944	Girls 5 2/B	5	2	3	0	18	20	11	9	Timothy McElaney	Sarah Madden
Hurricanes	31945	Girls 5 3/D	7	0	3	0	24	34	12	22	Maura Beverly	Jamie Hernon
Thorns	31946	Girls 5 4/D	6	2	2	0	18	48	22	26	Anissa Ellis	Renee Lamarque
Aces	31947	Girls 4 2/D	5	3	2	0	17	28	14	14	Keri Moses	Michael Finocchi
Breakers	31948	Girls 4 3/G	4	4	2	0	14	27	25	2	Bill Hamilton	Glenn Williams
Dash	31949	Girls 4 4/A	8	0	2	0	26	31	12	19	Nick Sordillo	Margaret Dixon
Trouble	31950	Girls 4 4/F2	2	4	2	0	8	11	13	-2	Dave Lamb	Jon Kopchick
Stars	32995	Girls 4 4/F2	1	7	0	0	3	4	23	-19	Nick Zozula	Kirsty DiSipio
United	6544	Boys 12 2/B	1	5	0	0	3	11	20	-9	Paul McAndrew	Keith Jacobsen
FC	6561	Boys 10 2/A	0	5	1	0	1	9	32	-23	Kevin Bock	Jim Robertson
Warriors	31992	Boys 8 3/A	6	1	3	0	21	22	14	8	Jonathan Lowe	Paul Foley
Legends	32035	Boys 8 3/F	1	9	0	0	3	20	48	-28	Karen Conway	Ethan Fox
Force	32847	Boys 8 4/F	0	3	1	0	1	6	17	-11	Keith Jacobsen	Brandon McDowall
Thunder	32037	Boys 8 4/L	4	6	0	0	12	22	43	-21	Jim Robertson	Frank Michienzi
Spurs	31998	Boys 6 2/B	10	0	0	0	30	45	15	30	Dana Niles	Michael Finocchi
Barcelona	32034	Boys 6 3/F	3	7	0	0	9	14	32	-18	Oscar Butragueno	Horacio Caneja
City	32914	Boys 6 4/E	3	7	0	0	9	21	36	-15	Aaron Price	Dan O'Driscoll
Hammers	31997	Boys 5 2/A	1	5	0	0	3	19	29	-10	Glenn Maffei	Amy Hall
Juventas	31996	Boys 5 3/E	1	5	0	0	3	12	25	-13	Barton Centauro	Isaias Aguiar
Roma	31994	Boys 5 4/G	0	10	0	0	0	20	62	-42	Valerie Cameron	Minelli Tomaszewski
Revolution	32916	Boys 4 2/F	5	4	1	0	16	21	16	5	Patrick Connors	Caitlin Sawyer
Crew	32918	Boys 4 3/H	4	5	0	0	12	25	25	0	Mark Cianci	John Kluza
Dynamo	32919	Boys 4 4/B1	4	2	2	0	14	30	15	15	Meghan Panteleakos	James Desautels
Galaxy	33410	Boys 4 4/G	1	9	0	0	3	25	48	-23	Jeremy Jarvis	Andrea Bartucca"""

save_and_import(spring2024_data, 'WAL', 2024, 'Spring')

print("\n=== WAL BATCH 1 COMPLETE ===")
