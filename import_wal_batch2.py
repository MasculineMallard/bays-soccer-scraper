#!/usr/bin/env python3
"""Import WAL Fall 2023 through Spring 2021 - Final 6 seasons"""

from universal_import import save_and_import

# Fall 2023
print("\n=== IMPORTING WAL FALL 2023 ===\n")
fall2023_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Lightning	31936	Girls 8 2/E	7	1	2	0	23	26	9	17	Kathy Martinez	Kate Procaccini
Power	31937	Girls 8 3/E	2	7	1	0	7	7	20	-13	Jon Paul Sydnor	Heidi Graceffa
Courage	31938	Girls 8 4/A	8	2	0	0	24	27	11	16	Luis Vazquez	Mike Pagnotta
Timberwolves	32987	Girls 8 4/H	5	5	0	0	15	13	11	2	Paul Luongo	Mike Porzelt
Hawks	31940	Girls 6 2/A	6	2	2	0	20	26	22	4	Benjamin Barrett	Robert DeGirolamo
Warriors	31941	Girls 6 3/B	1	6	0	0	3	13	32	-19	Liz Orlando	Jennifer Adams
Eagles	31942	Girls 6 4/B	1	9	0	0	3	16	50	-34	Thomas Dietel	Hardik Raval
Storm	31944	Girls 5 2/C	4	2	4	0	16	15	12	3	Timothy McElaney	Sarah Madden
Hurricanes	31945	Girls 5 3/B2	3	3	2	0	11	21	16	5	Maura Beverly	Jamie Hernon
Thorns	31946	Girls 5 3/E	1	7	2	0	5	6	20	-14	Anissa Ellis	David Lazzaro
Crush	32994	Girls 5 4/C	0	10	0	1	-1	1	47	-46	Karen Atkinson	Renee Lamarque
Aces	31947	Girls 4 2/D	7	3	0	0	21	25	13	12	Keri Moses	Courtney Kelleher
Breakers	31948	Girls 4 3/E	3	4	3	0	12	10	13	-3	Glenn Williams	Bill Hamilton
Dash	31949	Girls 4 4/A	7	3	0	0	21	35	14	21	Nick Sordillo	Margaret Dixon
Trouble	31950	Girls 4 4/C	0	8	2	0	2	5	45	-40	Jon Kopchick	Shannon Findley
Stars	32995	Girls 4 4/G	6	1	1	0	19	19	7	12	Dave Lamb	None
Warriors	31992	Boys 8 2/C	1	9	0	0	3	15	35	-20	Jonathan Lowe	Marc Todisco
Legends	32035	Boys 8 3/C1	3	3	1	0	10	16	27	-11	Karen Conway	Eric Tjonahen
Force	32847	Boys 8 4/D	3	5	2	0	11	24	31	-7	Bill Hamilton	Scott Carpenter
Thunder	32037	Boys 8 4/K	0	10	0	0	0	5	47	-42	Jim Robertson	Keith Jacobsen
Spurs	31998	Boys 6 2/C	5	3	2	0	17	28	28	0	Dana Niles	Michael Finocchi
Barcelona	32034	Boys 6 3/C	3	6	1	0	10	21	32	-11	Oscar Butragueno	Horacio Caneja
City	32914	Boys 6 4/E	4	2	4	0	16	24	20	4	Aaron Price	Dan O'Driscoll
Hammers	31997	Boys 5 3/A	3	6	1	0	10	35	38	-3	James Craig Westmoreland	John Kerin
Juventus	31996	Boys 5 3/C	4	1	0	0	12	15	9	6	Ciaran Martyn	Glenn Maffei
Lightning	32915	Boys 5 4/B	2	7	1	0	7	27	42	-15	Barton Centauro	None
Roma	31994	Boys 5 4/E	1	9	0	1	2	11	49	-38	Valerie Cameron	Holly Montipagni
Revolution	32916	Boys 4 2/C	6	4	0	0	18	29	15	14	Patrick Connors	Caitlin Sawyer
Fire	32917	Boys 4 3/A	2	3	5	0	11	25	32	-7	Mark Cianci	Rob Hollister
Crew	32918	Boys 4 3/L	4	5	1	0	13	31	20	11	Thomas Benoit	John Kluza
Dynamo	32919	Boys 4 4/C	6	4	0	0	18	33	38	-5	David Stanton	James Desautels
Galaxy	33410	Boys 4 4/G1	5	4	1	0	16	30	30	0	Jeremy Jarvis	Saurabh Lele"""

save_and_import(fall2023_data, 'WAL', 2023, 'Fall')

# Spring 2023
print("\n=== IMPORTING WAL SPRING 2023 ===\n")
spring2023_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Legends	32870	Girls 12 1/A2	6	0	1	0	19	43	8	35	Kevin Bock	John Thomsen
Timberwolves (D1)	32871	Girls 10 2/A	4	3	0	0	12	16	8	8	John Thomsen	Marty White
Spirit	31936	Girls 8 2/C	2	6	2	0	8	15	21	-6	Paul Foley	Kathy Martinez
Power	31937	Girls 8 3/D	2	6	1	0	7	10	26	-16	Jon Paul Sydnor	Brian Horwitz
Courage	31938	Girls 8 4/K	8	0	2	0	26	27	4	23	Peter Ellis	Maura Beverly
Hawks	31940	Girls 6 2/D	1	4	5	0	8	18	22	-4	Kate Procaccini	Courtney Kelleher
Warriors	31941	Girls 6 3/F	5	2	3	0	18	13	8	5	Heidi Graceffa	Luis Vazquez
Eagles	31942	Girls 6 4/F	4	5	1	0	13	21	24	-3	Kevin Mason	None
Storm	31944	Girls 5 1/A	0	8	2	0	2	4	16	-12	Kellee Senic	Daniel Blackstock
Hurricanes	31945	Girls 5 3/F	8	0	2	0	26	29	10	19	Robert DeGirolamo	Jennifer Adams
Thorns	31946	Girls 5 4/E	4	3	3	0	15	24	27	-3	Thomas Dietel	CJ Vasani
Aces	31947	Girls 4 2/B	4	6	0	0	12	14	22	-8	Timothy McElaney	Colleen Campbell
Breakers	31948	Girls 4 3/B	4	5	1	0	13	13	15	-2	Jamie Hernon	Sarah Madden
Dash	31949	Girls 4 4/E	8	1	0	0	24	37	12	25	Anissa Ellis	David Lazzaro
Pride	31950	Girls 4 4/G1	7	0	0	0	21	32	9	23	Andrew Ferguson	None
United	32872	Boys 12 1/A	0	6	0	0	0	2	27	-25	Paul McAndrew	Al Lessard
FC	32873	Boys 10 2/A	1	5	1	0	4	10	33	-23	Keith Jacobsen	Jim Robertson
Warriors	31992	Boys 8 2/E	5	3	2	0	17	19	13	6	Kevin Bock	Nicole Bock
Legends	32035	Boys 8 3/H	7	3	0	0	21	36	22	14	Alex Danesco	Doug Kennedy
Force	32847	Boys 8 4/A	6	3	1	0	19	34	17	17	Karen Conway	Marc Todisco
Thunder	32037	Boys 8 4/J	8	1	1	0	25	27	12	15	Paul Hession	Brandon McDowall
United	32001	Boys 6 2/B2	2	8	0	0	6	20	34	-14	John Hurley	Paul Foley
Blackpool	32790	Boys 6 3/E	0	6	4	0	4	15	35	-20	Bill Hamilton	Keith Jacobsen
Crew	31999	Boys 6 4/G	3	6	1	0	10	16	34	-18	Jim Robertson	Frank Michienzi
Spurs	31998	Boys 5 2/E	6	4	0	0	18	31	21	10	Dana Niles	Patrick Penza
Barcelona	32034	Boys 5 3/F	3	7	0	0	9	16	36	-20	Oscar Butragueno	Horacio Caneja
Hammers	31997	Boys 4 3/B	6	1	3	0	21	31	19	12	Muiz Khir	None
Juventus	31996	Boys 4 3/K	5	3	2	0	17	28	24	4	James Craig Westmoreland	Khalil Samara
Roma	31994	Boys 4 4/D	1	9	0	0	3	13	57	-44	Barton Centauro	Erin Athens
Arsenal	32850	Boys 4 4/E	5	0	1	0	16	32	15	17	Valerie Cameron	None"""

save_and_import(spring2023_data, 'WAL', 2023, 'Spring')

# Fall 2022
print("\n=== IMPORTING WAL FALL 2022 ===\n")
fall2022_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Spirit	31936	Girls 8 2/D2	7	2	1	0	22	23	14	9	Paul Foley	Kathy Martinez
Power	31937	Girls 8 3/L	8	2	0	0	24	32	13	19	Jon Paul Sydnor	Wayan Suwena
Courage	31938	Girls 8 4/C	4	3	3	0	15	22	14	8	Brian Horwitz	Terry Doherty
Reign	31939	Girls 8 4/G2	1	2	5	0	8	7	15	-8	Peter Ellis	Darwin Cevallos
Hawks	31940	Girls 6 2/B	0	8	2	0	2	9	37	-28	Kate Procaccini	Courtney Kelleher
Warriors	31941	Girls 6 3/F	6	3	1	0	19	28	15	13	Heidi Graceffa	David Miles
Eagles	31942	Girls 6 4/C	6	1	3	1	20	22	10	12	Mike Pagnotta	Jeannette Wehrenberg
Cyclones	31943	Girls 6 4/J	1	9	0	0	3	6	54	-48	Bernie Smith	Thomas Dietel
Storm	31944	Girls 5 1/B	2	5	2	0	8	12	20	-8	Kellee Senic	Daniel Blackstock
Hurricanes	31945	Girls 5 3/E	3	4	2	0	11	13	15	-2	Robert DeGirolamo	Jennifer Adams
Thorns	31946	Girls 5 4/A	2	6	1	0	7	14	34	-20	Brian Flynn	CJ Vasani
Aces	31947	Girls 4 2/A2	3	4	1	0	10	19	21	-2	Timothy McElaney	Colleen Campbell
Breakers	31948	Girls 4 2/A2	0	8	0	0	0	4	24	-20	Jamie Hernon	Sarah Madden
Dash	31949	Girls 4 3/F	4	2	4	0	16	19	11	8	Maura Beverly	Stephanie Ellard
Pride	31950	Girls 4 4/D2	3	4	1	0	10	10	19	-9	Anissa Ellis	Melody Hugo
Wave	31951	Girls 4 4/D2	4	2	2	0	14	20	14	6	Kevin Teller	None
Warriors	31992	Boys 8 2/D	2	2	1	0	7	8	10	-2	Kevin Bock	Seth Hochberg
Legends	32035	Boys 8 3/F	2	6	2	0	8	15	21	-6	Alex Danesco	None
Force	32036	Boys 8 4/B	6	0	4	0	22	39	23	16	Karen Conway	Marc Todisco
Thunder	32037	Boys 8 4/D2	4	1	3	0	15	22	18	4	Robert Grabowy	None
United	32001	Boys 6 2/A	1	8	1	0	4	13	31	-18	John Hurley	Nicholas Kakas
Blues	32000	Boys 6 3/H	6	3	1	0	19	30	19	11	Bill Hamilton	Keith Jacobsen
Crew	31999	Boys 6 4/G	0	9	1	0	1	11	46	-35	Jim Robertson	Frank Michienzi
Spurs	31998	Boys 5 2/B	1	7	2	0	5	16	34	-18	Dana Niles	Michael Finocchi
Barcelona	32034	Boys 5 3/D	6	2	2	0	20	31	24	7	Oscar Butragueno	Horacio Caneja
City	32033	Boys 5 4/C	4	5	0	0	12	26	23	3	Aaron Price	Dan O'Driscoll
Hammers	31997	Boys 4 2/D	5	3	2	0	17	28	15	13	Muiz Khir	None
Milan	31995	Boys 4 3/L	0	10	0	0	0	6	35	-29	None	None
Juventus	31996	Boys 4 3/L	6	3	1	0	19	29	14	15	James Craig Westmoreland	Khalil Samara
Roma	31994	Boys 4 4/G	7	2	1	0	22	36	17	19	Barton Centauro	None"""

save_and_import(fall2022_data, 'WAL', 2022, 'Fall')

# Spring 2022
print("\n=== IMPORTING WAL SPRING 2022 ===\n")
spring2022_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Timberwolves D1	30858	Girls 12 2/A	7	0	0	0	21	38	7	31	Kevin Bock	John Thomsen
Wolfpack D1	30859	Girls 11 2/A	6	1	0	0	18	26	6	20	Michael St. George	John Thomsen
Trouble	31037	Girls 8 2/A	7	1	2	0	23	27	13	14	Joe Marerro	Marty White
Spirit	31034	Girls 8 3/K	3	4	3	0	12	18	20	-2	David Miles	Patrick Connors
Courage	31035	Girls 8 4/A	5	3	2	0	17	21	16	5	Sean Ahern	David Corbett
Reign	31036	Girls 8 4/E	6	3	1	0	19	23	8	15	Peter Ellis	Darwin Cevallos
Lightning	31038	Girls 6 2/C	8	0	2	0	26	38	15	23	Kathy Martinez	Wayan Suwena
Power	31039	Girls 6 3/D	4	6	0	0	12	20	27	-7	Brian Horwitz	Maura Beverly
Pride	31040	Girls 6 4/C	5	2	1	0	16	20	14	6	Brad Hickey	Terry Doherty
Hawks	31041	Girls 5 2/B	0	4	0	0	0	5	13	-8	Kate Procaccini	None
Warriors	31042	Girls 5 3/G	4	0	0	0	12	11	3	8	Heidi Graceffa	Brooke McMillan
Eagles	31043	Girls 5 4/B	4	3	2	0	14	15	13	2	Bernie Smith	Matt Feener
Fire	31044	Girls 4 2/C	6	2	2	0	20	28	19	9	Darwin Cevallos	Daniel Blackstock
Storm	31045	Girls 4 2/C	6	1	3	0	21	28	16	12	Kellee Senic	Robert DeGirolamo
Hurricanes	31047	Girls 4 4/A	3	7	0	0	9	15	39	-24	Jennifer Adams	Jim Bunt
Thorns	31046	Girls 4 4/F	3	6	1	0	10	16	17	-1	Beverly Sprague	Thomas Dietel
United D1	30860	Boys 11 1/A1	1	5	1	0	4	7	19	-12	Al Lessard	Toar Winter
Timberwolves D2	30861	Boys 11 2/C1	0	7	0	0	0	2	28	-26	Paul McAndrew	Daniel OConnell
Warriors	31283	Boys 8 2/E	7	0	3	0	24	24	4	20	Will Graceffa	Seth Hochberg
Hawks	31284	Boys 8 3/H	5	4	1	0	16	29	19	10	Kevin Bock	Nicole Bock
Coyotes	31285	Boys 8 4/B	6	1	3	0	21	17	8	9	Jim Robertson	Keith Jacobsen
Force	31288	Boys 8 4/E	3	6	1	0	10	10	19	-9	Alex Danesco	Jim Keller
Legends	30793	Boys 6 2/C	4	4	2	0	14	22	26	-4	Jonathan Lowe	Doug Kennedy
Thunder	31286	Boys 6 4/D	3	7	0	0	9	21	45	-24	Karen Conway	Marc Todisco
United	31289	Boys 5 2/C	8	1	1	0	25	37	20	17	John Hurley	Paul Foley
Blues	31290	Boys 5 4/A	7	3	0	0	21	31	20	11	Bill Hamilton	Eric Tjonahen
Crew	31291	Boys 5 4/F	0	8	2	0	2	11	35	-24	Keith Jacobsen	Jim Robertson
Spurs	31292	Boys 4 2/D	2	5	3	0	9	20	34	-14	Dana Niles	Michael Finocchi
Barcelona	31293	Boys 4 3/D	1	3	1	0	4	13	11	2	Patrick Penza	Yathu Gopinath
City	31295	Boys 4 4/E	7	3	0	0	21	40	22	18	Oscar Butragueno	None"""

save_and_import(spring2022_data, 'WAL', 2022, 'Spring')

# Fall 2021
print("\n=== IMPORTING WAL FALL 2021 ===\n")
fall2021_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Trouble	31037	Girls 8 2/A	6	2	2	0	20	25	15	10	Joe Marerro	Marty White
Spirit	31034	Girls 8 3/C	1	7	2	0	5	15	24	-9	David Miles	Patrick Connors
Courage	31035	Girls 8 4/A	4	3	3	0	15	23	19	4	Sean Ahern	David Corbett
Reign	31036	Girls 8 4/J	7	2	1	0	22	23	5	18	Peter Ellis	Darwin Cevallos
Lightning	31038	Girls 6 2/E	5	4	1	0	16	24	18	6	Kathy Martinez	Wayan Suwena
Power	31039	Girls 6 3/E	5	2	1	0	16	15	14	1	Brian Horwitz	Maura Beverly
Pride	31040	Girls 6 4/D1	5	2	1	0	16	27	14	13	Brad Hickey	Terry Doherty
Hawks	31041	Girls 5 2/E	3	5	2	0	11	20	32	-12	Kate Procaccini	David Miles
Warriors	31042	Girls 5 3/F	6	2	2	0	20	29	10	19	Heidi Graceffa	Brooke McMillan
Eagles	31043	Girls 5 4/D	4	3	3	0	15	20	19	1	Bernie Smith	Amritha Farswani
Fire	31044	Girls 4 2/B	3	5	2	0	11	16	25	-9	Darwin Cevallos	Daniel Blackstock
Storm	31045	Girls 4 2/B	4	3	2	0	14	22	18	4	Kellee Senic	Lauren Trotta
Thorns	31046	Girls 4 4/F	2	5	3	0	9	13	30	-17	Beverly Sprague	Thomas Dietel
Dash	31047	Girls 4 4/F	7	1	2	0	23	32	10	22	Jennifer Adams	None
Warriors	31283	Boys 8 2/E	6	2	2	0	20	23	11	12	Will Graceffa	Jonathan Tillinghast
Hawks	31284	Boys 8 3/G	4	6	0	0	12	20	15	5	Todd Zahurak	Kevin Bock
Coyotes	31285	Boys 8 4/F	5	0	0	0	15	21	1	20	Jim Robertson	Keith Jacobsen
Force	31288	Boys 8 4/J	7	2	1	0	22	31	19	12	Alex Danesco	Jim Keller
Legends	30793	Boys 6 2/C	6	3	1	0	19	24	20	4	Jonathan Lowe	Doug Kennedy
Thunder	31286	Boys 6 4/A	4	1	0	0	12	22	9	13	Karen Conway	None
Timberwolves	31287	Boys 6 4/G	0	9	0	0	0	7	56	-49	Robert Grabowy	None
United	31289	Boys 5 2/C	2	8	0	0	6	29	37	-8	John Hurley	Mathew Roberts
Blues	31290	Boys 5 3/D	0	9	1	0	1	16	43	-27	Bill Hamilton	Eric Tjonahen
Crew	31291	Boys 5 4/H	5	5	0	0	15	21	24	-3	Keith Jacobsen	Jim Robertson
Spurs	31292	Boys 4 2/C1	4	3	1	0	13	20	18	2	Dana Niles	Michael Finocchi
Barcelona	31293	Boys 4 3/B	1	7	2	0	5	13	31	-18	Horacio Caneja	Seth Hochberg
Chelsea	31294	Boys 4 4/C	4	3	3	0	15	18	19	-1	Sean Whelan	Richard Mccolgan
Celtic	31295	Boys 4 4/C	3	5	2	0	11	20	26	-6	Patrick Penza	Yathu Gopinath
City	31297	Boys 4 4/C	4	5	1	0	13	28	31	-3	Oscar Butragueno	None"""

save_and_import(fall2021_data, 'WAL', 2021, 'Fall')

# Spring 2021
print("\n=== IMPORTING WAL SPRING 2021 ===\n")
spring2021_data = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Walpole U18 Girls	30858	Girls 12 1/A1	6	0	0	0	18	30	2	28	Kevin Bock	John Thomsen
Walpole U16 Girls	30859	Girls 12 2/A	6	0	1	0	19	25	2	23	Michael St. George	Paul English
United	30774	Girls 8 1/A1	3	5	2	0	11	11	25	-14	Marc Schultz	John Thomsen
Trouble	30775	Girls 8 2/C	5	2	3	0	18	23	19	4	Joe Marerro	Marty White
Crush	30776	Girls 8 3/C	1	7	0	0	3	13	36	-23	Sandra DAvignon	Paul Connelly
Twisters	30778	Girls 8 4/B	3	6	1	0	10	9	23	-14	Rita Tyszka	Heather Towery
Crusaders	30777	Girls 8 4/E	3	1	1	0	10	9	5	4	David Miles	Patrick Connors
Bandits	30779	Girls 6 2/B	6	4	0	0	18	14	14	0	Paul Foley	Mike McDonnell
Fire	30780	Girls 6 3/F2	4	3	1	0	13	18	12	6	Sean Ahern	Peter Ellis
Legends	30781	Girls 6 4/E	6	2	2	0	20	25	14	11	Darwin Cevallos	Maura Beverly
Power	30782	Girls 5 3/B	2	5	3	0	9	22	31	-9	Jon Paul Sydnor	Brian Horwitz
Lightning	30783	Girls 5 3/B	4	4	2	0	14	18	20	-2	Kathy Martinez	Terry Doherty
Hawks	30784	Girls 4 2/E	3	4	3	0	12	12	14	-2	Kate Procaccini	David Miles
Warriors	30785	Girls 4 3/E	5	5	0	0	15	22	14	8	Heidi Graceffa	Brooke McMillan
Eagles	30786	Girls 4 4/A1	2	3	3	0	9	10	9	1	Bernie Smith	Amritha Farswani
Walpole U18 Boys	30860	Boys 12 1/B1	2	3	2	0	8	17	18	-1	Al Lessard
Walpole U16 Boys	30861	Boys 11 2/B	4	3	0	1	11	17	10	7	Eoin Walsh	John Kerin
Wildcats	30787	Boys 8 2/A	3	5	2	0	11	18	21	-3	Matt Feener	Mathew Roberts
Hawks	30788	Boys 8 3/H1	5	4	1	0	16	30	21	9	Daniel OConnell	Todd Zahurak
Coyotes	30789	Boys 8 4/D	3	7	0	0	9	19	31	-12	Jim Robertson	Keith Jacobsen
Patriots	30790	Boys 6 2/C	5	4	0	0	15	27	26	1	Will Graceffa	Seth Hochberg
Warriors	30791	Boys 6 3/C	2	6	2	0	8	20	40	-20	Dana Niles	Kevin Bock
Force	30792	Boys 6 4/B	5	4	1	0	16	18	20	-2	Alex Danesco	Jim Keller
Legends	30793	Boys 5 2/B	2	6	2	0	8	13	30	-17	Jonathan Lowe	Manak Ahluwalia
Thunder	30794	Boys 5 4/A1	0	8	0	0	0	1	44	-43	Karen Conway	Byron Olson
United	30795	Boys 4 2/C	1	5	3	0	6	21	34	-13	John Hurley	Nicholas Kakas
Revolution	30796	Boys 4 2/C	2	6	1	0	7	21	38	-17	Paul Foley	Brian Bingham
Bobcats	30797	Boys 4 3/G	1	7	1	0	4	15	40	-25	Keith Jacobsen	Morgan Miles
Arsenal	30798	Boys 4 4/B	3	6	1	0	10	22	26	-4	Bill Hamilton	Eric Tjonahen"""

save_and_import(spring2021_data, 'WAL', 2021, 'Spring')

print("\n=== ALL WAL SEASONS COMPLETE ===")
print("Walpole: 10 seasons imported (Fall 2025 - Spring 2021)")
