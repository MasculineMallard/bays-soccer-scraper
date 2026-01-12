"""
Batch import all Foxborough seasons
"""

import sys
sys.path.append('.')
from universal_import import save_and_import

# Spring 2023
spring2023 = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Warriors 7/8G-Blue	6345	Girls 8 2/A	3	6	1	0	10	12	19	-7	Melissa Maling
Warriors 7/8G-Gold	10411	Girls 8 3/D	1	7	1	0	4	3	19	-16	John Grace	None
Warriors 6G-Blue	10033	Girls 6 2/C	4	5	0	0	12	20	19	1	Matthew Quin	Matthew Monahan
Warriors 6G-Gold	6264	Girls 6 4/E2	1	3	1	0	4	5	9	-4	David Del Pizzo	Don Kelloway
Warriors 4G-Blue	6255	Girls 4 3/E	2	7	1	0	7	18	37	-19	Matthew Quin	Khaled Alshara
Warriors 3G-Blue	11129	Girls 3 3/D	3	5	1	0	10	16	26	-10	Brian Compter	David Del Pizzo
Warriors High School(1)	32920	Boys 912 3/A	1	4	1	1	3	11	13	-2	Isaac Sham	Shane Palmer
Warriors High School(2)	32921	Boys 912 3/A	0	6	1	5	-4	1	13	-12	Danielle Riley	Jennifer Keen
Warriors 7/8B-Blue	6154	Boys 8 3/C	1	8	1	0	4	15	33	-18	Brent Ruter	John Devine
Warriors 6B-Blue	31800	Boys 6 3/G	0	4	1	0	1	5	20	-15	Matt Griffin	None
Warriors 4B-Blue	31011	Boys 4 2/D	3	4	3	0	12	20	27	-7	Fabio Felix	Gary Luck
Warriors 4B-Gold	31012	Boys 4 4/A	2	8	0	0	6	15	27	-12	Bryan Rose	David Blair
Warriors 3B-Blue	31797	Boys 3 2/C	3	5	2	0	11	20	24	-4	James Miller	John Greenhalgh
Warriors 3B-Gold	31798	Boys 3 4/B1	0	6	1	0	1	10	28	-18	Matthew Houston 	Andrew Woodward"""

# Fall 2022
fall2022 = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Warriors 7/8G-1	6345	Girls 8 2/B2	6	2	2	0	20	20	9	11	Melissa Maling	Denise Casey
Warriors 7/8G-2A	10411	Girls 8 3/D	3	6	0	1	8	14	17	-3	Shane Palmer	Richard Pham
Warriors 7/8G-2B	31927	Girls 8 4/B	0	4	1	0	1	9	19	-10	Kristine McWilliams	Jill Lamson
Warriors 6G-1	10033	Girls 6 2/C2	5	2	3	0	18	27	18	9	Samantha Smith	Matthew Monahan
Warriors 6G-2	31306	Girls 6 3/F	1	8	1	0	4	10	33	-23	Aaron Cyr	Don Kelloway
Warriors 5G-1	6264	Girls 5 2/D	4	4	2	0	14	18	17	1	Shawn Higgins	Kathleen Courtney
Warriors 5G-2 (DROPPED)	10032	Girls 5 3/X	0	0	0	0	0	0	0	0	None	None
Warriors 4G-1	6255	Girls 4 3/D	5	4	1	0	16	30	18	12	Matthew Quin	Mike James
Warriors 4G-2	31928	Girls 4 4/B	0	4	1	0	1	6	18	-12	Hector Garcia	None
Warriors 3G-1	11129	Girls 3 3/B	2	4	3	0	9	11	24	-13	Joe Depasquale 	James Mosesso
Warriors 3G-2	10376	Girls 3 3/F	3	3	4	0	13	24	21	3	Dianna Walker	James McVeigh
Warriors 3G-3	31929	Girls 3 4/B	4	4	2	0	14	21	19	2	Mark Whitehouse
Warriors 7/8B-1	6193	Boys 8 2/D	1	7	2	0	5	15	37	-22	Ian Christianson	Brent Ruter
Warriors 7/8B-2	6154	Boys 8 4/B	1	5	0	0	3	12	25	-13	John Devine	None
Warriors 6B-1	31800	Boys 6 3/H	4	1	1	0	13	18	9	9	Matt Griffin	Kevin Atkinson
Warriors 6B-2 - DROPPED	32164	Boys 6 4/X	0	0	0	0	0	0	0	0	None	None
Warriors 5B-1	6140	Boys 5 3/G	6	2	2	0	20	48	25	23	Ryan Sylvia	Stephen Toland
Warriors 4B-1	31011	Boys 4 3/B	6	0	3	0	21	34	12	22	Matthew Monahan	Gary Luck
Warriors 4B-2	31012	Boys 4 4/D	4	4	2	0	14	30	24	6	Bryan Rose	David Blair
Warriors 3B-1	31797	Boys 3 2/C	7	3	0	0	20	43	19	24	James Miller	John Greenhalgh
Warriors 3B-2	31798	Boys 3 3/H	5	5	0	0	15	20	23	-3	Aaron Coby	AJ Dooley
Warriors 3B-3	31799	Boys 3 4/C	6	1	3	0	21	23	9	14	Matthew Houston 	Andrew Woodward"""

# Spring 2022
spring2022 = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Warriors 7/8G-1	6345	Girls 8 2/C	2	4	3	0	9	15	19	-4	Danielle Riley	Danielle Goldstein
Warriors 7/8G-2	10411	Girls 8 3/F	3	3	4	0	13	11	12	-1	Jeff D'Arcy	Kevin McAuliffe
Warriors 6G-1	10033	Girls 6 2/D	7	1	2	0	23	25	11	14	Shane Palmer	Melanie McElroy
Warriors 6G-2	31306	Girls 6 3/F	3	3	4	0	13	20	18	2	Kristine McWilliams	None
Warriors 5G-1	6264	Girls 5 3/E	7	1	1	0	22	28	11	17	Matthew Monahan	Matthew Quin
Warriors 5G-2	10032	Girls 5 4/B	4	3	3	0	15	17	15	2	Don Kelloway	Aaron Cyr
Warriors 4G-1	6255	Girls 4 3/A1	1	5	2	0	5	9	17	-8	Shawn Higgins	AJ Dooley
Warriors 3G-1	11129	Girls 3 3/A	1	1	0	0	3	4	5	-1	Matthew Quin	Vincent Zabbo
Warriors 3G-2	10376	Girls 3 3/D	0	9	1	1	0	5	45	-40	Sam Toma	Khaled Alshara
Warriors HS	32734	Boys 912 3/A	4	2	1	0	13	28	19	9	Isaac Sham
Warriors 7/8B-1	6193	Boys 8 2/F	2	6	2	0	8	12	22	-10	Jennifer Keen	Shawn Higgins
Warriors 6B-1	6154	Boys 6 3/B	2	6	2	0	8	16	28	-12	Brent Ruter	Ian Christianson
Warriors 5B-1	30833	Boys 5 3/F	3	4	3	0	12	23	30	-7	Matt Griffin	Jackie D'Andrea
Warriors 4B-1	6140	Boys 4 4/E	4	0	0	0	12	18	6	12	Ryan Sylvia	None
Warriors 3B-1	31011	Boys 3 3/A	2	5	3	0	9	16	26	-10	Gary Luck	Matthew Monahan
Warriors 3B-2	31012	Boys 3 3/H1	8	0	2	0	26	40	14	26	Bryan Rose	None
Warriors 3B-3	31013	Boys 3 3/H1	0	9	0	0	0	6	37	-31	Khaled Alshara	David Blair"""

# Fall 2021
fall2021 = """Team	Team#	GADS	W	L	T	F	PTS	GF	GA	+/-	Coach	A. Coach
Warriors 7/8G-1	6345	Girls 8 2/E	6	4	0	0	18	19	11	8	Danielle Riley	Danielle Goldstein
Warriors 7/8G-2a	10411	Girls 8 3/F	2	4	4	0	10	15	13	2	Jennifer Jaworski	Jake Picard
Warriors 7/8G-2b	31304	Girls 8 3/L	3	2	1	0	10	11	8	3	Sarah Behn	Kevin McAuliffe
Warriors 6G-1	10033	Girls 6 2/B	2	5	3	0	9	15	20	-5	Shane Palmer	John Grace
Warriors 6G-2	31306	Girls 6 3/G	6	4	0	0	18	25	16	9	Jill Lamson	Kristine McWilliams
Warriors 5G-1	6264	Girls 5 2/C	5	4	1	0	16	23	19	4	Samantha Smith	Matthew Monahan
Warriors 5G-2	10032	Girls 5 3/F	0	10	0	0	0	5	33	-28	Dan Davis	Tarick Elsadig
Warriors 4G-1	6255	Girls 4 2/B	4	3	2	0	14	12	15	-3	Kathleen Courtney	AJ Dooley
Warriors 4G-2	11631	Girls 4 4/B	2	7	1	1	6	8	21	-13	Emmerson Phillips	Vincent Calio
Warriors 3G-1	11129	Girls 3 2/A	2	7	1	1	6	14	22	-8	William Curry	Jason McAuliffe
Warriors 3G-2	10376	Girls 3 3/D	2	6	2	0	8	10	21	-11	Robert Augusta	Khaled Alshara
Warriors 3G-3	31309	Girls 3 4/B	1	7	2	0	5	16	35	-19	Sam Toma	Jess Sallie
Warriors 7/8B-1	6193	Boys 8 2/E	0	4	1	0	1	5	16	-11	Jennifer Keen	Edward Lavallee
Warriors 7/8B-2	31017	Boys 8 3/G	0	4	1	0	1	3	16	-13	Matt Griffin	Mark Hannon
Warriors 6B-1	6154	Boys 6 2/C	2	7	1	0	7	18	25	-7	Brent Ruter	Ian Christianson
Warriors 6B-2	31016	Boys 6 3/E	2	7	1	0	7	16	31	-15	John Devine	Mark Truss
Warriors 5B-1	30833	Boys 5 3/D	3	6	1	0	10	31	34	-3	Salvatore Napoli	Jeffrey Messier
Warriors 5B-2	31015	Boys 5 4/A	1	0	3	0	6	9	6	3	Kevin Atkinson	Sam Toma
Warriors 4B-1	6140	Boys 4 3/B	2	7	1	0	7	15	36	-21	Ryan Sylvia	Stephen Toland
Warriors 4B-2	31014	Boys 4 3/J	1	7	2	0	5	16	39	-23	Dave Palmer	None
Warriors 3B-1	31011	Boys 3 2/C	5	4	1	0	16	24	18	6	Matthew Monahan	Fabio Felix
Warriors 3B-2	31012	Boys 3 3/E	1	3	0	0	3	6	20	-14	Khaled Alshara	David Blair
Warriors 3B-3	31013	Boys 3 3/G	8	2	0	0	24	29	17	12	Bryan Rose	Daniel Sexton"""

print("=" * 60)
print("BATCH IMPORTING ALL FOXBOROUGH SEASONS")
print("=" * 60)
print()

seasons = [
    (spring2023, 'FOX', 2023, 'Spring'),
    (fall2022, 'FOX', 2022, 'Fall'),
    (spring2022, 'FOX', 2022, 'Spring'),
    (fall2021, 'FOX', 2021, 'Fall'),
]

total_added = 0
for data, town, year, period in seasons:
    print(f"\n{'='*60}")
    print(f"IMPORTING {town} {period} {year}")
    print('='*60)
    added, skipped = save_and_import(data, town, year, period)
    total_added += added

print()
print("=" * 60)
print(f"BATCH IMPORT COMPLETE: {total_added} total teams added")
print("=" * 60)
