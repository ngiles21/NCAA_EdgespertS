# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:50:20 2023

@author: noahg
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import streamlit as st
#from collections import namedtuple
#import altair as alt
import math
import pandas as pd
#from pybaseball import *
import pandas as pd


def main():

   

    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import time 
    def scrape_website(url):
        # Send a GET request to the website
        response = requests.get(url)
    
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
    
            # Example: Extract data from tables
            data = []
            for table in soup.find_all('table'):
                rows = table.find_all('tr')
                for row in rows:
                    columns = row.find_all(['th', 'td'])
                    data.append([column.text.strip() for column in columns])
    
            # Create a DataFrame from the extracted data
            df = pd.DataFrame(data)
    
            # Print the DataFrame
            return df
    
      
    
    #dataurl=pd.read_excel('sportsref_download.xlsx')
    
    
    
   



   
    st.title("Edge Sports App")
    st.write("This app is designed to let you enter the matchup you want a prediction from.")
    
    
    
    col1, col2 = st.columns(2)
    with col1:
        optionHome = st.selectbox(
    'Select the Home Team',
    ('Abilene Christian',
     'Air Force',
     'Akron',
     'Alabama',
     'Alabama A&M',
     'Alabama State',
     'Albany (NY)',
     'Alcorn State',
     'Allegheny Gators',
     'American',
     'Amherst Lord Jeffs',
     'Appalachian State',
     'Arizona',
     'Arizona State',
     'Arkansas',
     'Arkansas State',
     'Arkansas-Pine Bluff',
     'Armstrong Pirates',
     'Army',
     'Auburn',
     'Augusta State Jaguars',
     'Augustana (IL) Vikings',
     'Austin Peay',
     'Baker University Wildcats',
     'Baldwin-Wallace Yellow Jackets',
     'Ball State',
     'Baltimore Super Bees',
     'Baylor',
     'Bellarmine',
     'Belmont',
     'Beloit Buccaneers',
     'Bethune-Cookman',
     'Binghamton',
     'Birmingham-Southern Panthers',
     'Bloomsburg Huskies',
     'Boise State',
     'Boston College',
     'Boston University',
     'Bowling Green State',
     'Bradley',
     'Brigham Young',
     'Brigham Young College',
     'Brooklyn Bulldogs',
     'Brown',
     'Bryant',
     'Bucknell',
     'Buffalo',
     'Butler',
     'Cal Poly',
     'Cal State Bakersfield',
     'Cal State Fullerton',
     'Cal State Los Angeles Golden Eagles',
     'Cal State Northridge',
     'California',
     'California Baptist',
     'Campbell',
     'Canisius',
     'Canterbury College',
     'Carleton College Knights',
     'Carnegie Mellon Tartans',
     'Case Western Reserve Spartans',
     'Catholic Cardinals',
     'Centenary (LA) Gents',
     'Central Arkansas',
     'Central Connecticut State',
     'Central Florida',
     'Central Michigan',
     'Central Missouri Mules',
     'Central Pennsylvania College Knights',
     'Centre (KY) Colonels',
     'Charleston Southern',
     'Charlotte',
     'Chattanooga',
     'Cheyenne Business College',
     'Chicago Maroons',
     'Chicago State',
     'Cincinnati',
     'City College of New York Beavers',
     'Clemson',
     'Cleveland State',
     'Coastal Carolina',
     'Colgate',
     'College of Charleston',
     'College of New Jersey Lions',
     'Colorado',
     'Colorado College Tigers',
     'Colorado School of Mines Orediggers',
     'Colorado State',
     'Columbia',
     'Concordia Seminary Preachers',
     'Connecticut',
     'Coppin State',
     'Cornell',
     'Cotner College',
     'Creighton',
     'Cumberland',
     'Dakota Wesleyan Tigers',
     'Dartmouth',
     'Davidson',
     'Dayton',
     'Delaware',
     'Delaware State',
     'Denison Big Red',
     'Denver',
     'DePaul',
     'DePauw Tigers',
     'Detroit Mercy',
     'Dickinson College Red Devils',
     'Drake',
     'Drexel',
     'Duke',
     'Duquesne',
     'East Carolina',
     'East Central Tigers',
     'East Tennessee State',
     'Eastern Illinois',
     'Eastern Kentucky',
     'Eastern Michigan',
     'Eastern Washington',
     'Elon',
     'Emporia State Hornets',
     'Ensign College',
     'Evansville',
     'Fairfield',
     'Fairleigh Dickinson',
     'Florida',
     'Florida A&M',
     'Florida Atlantic',
     'Florida Gulf Coast',
     'Florida International',
     'Florida State',
     'Fordham',
     'Franklin Grizzlies',
     'Fresno State',
     'Furman',
     'Gardner-Webb',
     'Geneva Golden Tornadoes',
     'George Mason',
     'George Washington',
     'Georgetown',
     'Georgia',
     'Georgia Southern',
     'Georgia State',
     'Georgia Tech',
     'Gettysburg Bullets',
     'Gonzaga',
     'Grambling',
     'Grand Canyon',
     'Green Bay',
     'Grinnell Pioneers',
     'Grove City Wolverines',
     'Hamline Pipers',
     'Hampton',
     'Hardin-Simmons Cowboys',
     'Hartford Hawks',
     'Harvard',
     'Haskell (KS) Fighting Indians',
     'Hawaii',
     'High Point',
     'Hiram Terriers',
     'Hofstra',
     'Holy Cross',
     'Hope Flying Dutchmen',
     'Houston',
     'Houston Christian',
     'Howard',
     'Idaho',
     'Idaho State',
     'Illinois',
     'Illinois State',
     'Illinois Wesleyan Titans',
     'Illinois-Chicago',
     'Incarnate Word',
     'Indiana',
     'Indiana State',
     'Iona',
     'Iowa',
     'Iowa State',
     'IUPUI',
     'Jackson State',
     'Jacksonville',
     'Jacksonville State',
     'James Madison',
     'John Carroll Blue Streaks',
     'Kalamazoo Hornets',
     'Kansas',
     'Kansas City',
     'Kansas State',
     'Kennesaw State',
     'Kent State',
     'Kentucky',
     'Kentucky Wesleyan Panthers',
     'La Salle',
     'Lafayette',
     'Lake Forest Foresters',
     'Lamar',
     'Lawrence Vikings',
     'Le Moyne',
     'Lehigh',
     'Lewis Flyers',
     'Liberty',
     'Lindenwood',
     'Lipscomb',
     'Little Rock',
     'Long Beach State',
     'Long Island University',
     'Longwood',
     'Louisiana',
     'Louisiana State',
     'Louisiana Tech',
     'Louisiana-Monroe',
     'Louisville',
     'Loyola (IL)',
     'Loyola (LA) Wolfpack',
     'Loyola (MD)',
     'Loyola Marymount',
     'Macalester Scots',
     'Maine',
     'Manchester Spartans',
     'Manhattan',
     'Marietta Pioneers',
     'Marist',
     'Marquette',
     'Marshall',
     'Maryland',
     'Maryland-Baltimore County',
     'Maryland-Eastern Shore',
     'Massachusetts',
     'Massachusetts Institute of Technology Engineers',
     'Massachusetts-Lowell',
     'McNeese State',
     'Memphis',
     'Mercer',
     'Merchant Marine Mariners',
     'Merrimack',
     'Miami (FL)',
     'Miami (OH)',
     'Michigan',
     'Michigan State',
     'Middle Tennessee',
     'Millikin Big Blue',
     'Millsaps Majors',
     'Milwaukee',
     'Minnesota',
     'Minnesota A&M Aggies',
     'Mississippi',
     'Mississippi State',
     'Mississippi Valley State',
     'Missouri',
     'Missouri State',
     'Monmouth',
     'Montana',
     'Montana State',
     'Morehead State',
     'Morgan State',
     'Morris Brown Wolverines',
     "Mount St. Mary's",
     'Mount Union Purple Raiders',
     'Muhlenberg Mules',
     'Murray State',
     'Muskingum Fighting Muskies',
     'Navy',
     'NC State',
     'Nebraska',
     'Nebraska Wesleyan Prairie Wolves',
     'Nevada',
     'Nevada-Las Vegas',
     'New Hampshire',
     'New Mexico',
     'New Mexico State',
     'New Orleans',
     'New York University Violets',
     'Newberry Wolves',
     'Niagara',
     'Nicholls State',
     'NJIT',
     'Norfolk State',
     'North Alabama',
     'North Carolina',
     'North Carolina A&T',
     'North Carolina Central',
     'North Central Cardinals',
     'North Dakota',
     'North Dakota State',
     'North Florida',
     'North Texas',
     'Northeastern',
     'Northeastern Illinois Golden Eagles',
     'Northern Arizona',
     'Northern Colorado',
     'Northern Illinois',
     'Northern Iowa',
     'Northern Kentucky',
     'Northwest Missouri State Bearcats',
     'Northwestern',
     'Northwestern State',
     'Notre Dame',
     'Oakland',
     'Oberlin Yeomen',
     'Ohio',
     'Ohio State',
     'Ohio Wesleyan Battling Bishops',
     'Oklahoma',
     'Oklahoma City Chiefs',
     'Oklahoma State',
     'Old Dominion',
     'Omaha',
     'Oral Roberts',
     'Oregon',
     'Oregon State',
     'Pacific',
     'Penn State',
     'Pennsylvania',
     'Pepperdine',
     'Phillips Haymakers',
     'Pittsburg State Gorillas',
     'Pittsburgh',
     'Portland',
     'Portland State',
     'Prairie View',
     'Pratt Institute Cannoneers',
     'Presbyterian',
     'Princeton',
     'Providence',
     'Purdue',
     'Purdue Fort Wayne',
     'Queens (NC)',
     'Quinnipiac',
     'Radford',
     'Regis (CO) Rangers',
     'Rensselaer Engineers',
     'Rhode Island',
     'Rice',
     'Richmond',
     'Rider',
     'Ripon Red Hawks',
     'Roanoke Maroons',
     'Robert Morris',
     'Rochester (NY) Yellowjackets',
     "Rose-Hulman Fightin' Engineers",
     'Rutgers',
     'Sacramento State',
     'Sacred Heart',
     'Saint Francis (PA)',
     "Saint Joseph's",
     'Saint Louis',
     "Saint Mary's (CA)",
     "Saint Peter's",
     'Sam Houston',
     'Samford',
     'San Diego',
     'San Diego State',
     'San Francisco',
     'San Jose State',
     'Santa Clara',
     'Savage School of Physical Education',
     'Savannah State Tigers',
     'Scranton Royals',
     'Seattle',
     'Seton Hall',
     'Sewanee Tigers',
     'Siena',
     'South Alabama',
     'South Carolina',
     'South Carolina State',
     'South Carolina Upstate',
     'South Dakota',
     'South Dakota State',
     'South Florida',
     'Southeast Missouri State',
     'Southeastern Louisiana',
     'Southern',
     'Southern California',
     'Southern Illinois',
     'Southern Illinois-Edwardsville',
     'Southern Indiana',
     'Southern Methodist',
     'Southern Mississippi',
     'Southern Utah',
     'Southwestern (KS) Moundbuilders',
     'Southwestern (TX) Pirates',
     'Springfield Pride',
     'St. Bonaventure',
     'St. Francis (NY)',
     "St. John's (NY)",
     "St. John's College (OH)",
     'St. Lawrence Saints',
     'St. Thomas',
     'Stanford',
     'Stephen F. Austin',
     'Stetson',
     'Stevens Institute Ducks',
     'Stonehill',
     'Stony Brook',
     'SUNY-Potsdam Bears',
     'Swarthmore Garnet',
     'Syracuse',
     'Tarleton State',
     'TCU',
     'Temple',
     'Tennessee',
     'Tennessee State',
     'Tennessee Tech',
     'Tennessee-Martin',
     'Texas',
     'Texas A&M',
     'Texas A&M-Commerce',
     'Texas A&M-Corpus Christi',
     'Texas Southern',
     'Texas State',
     'Texas Tech',
     'Texas Wesleyan Rams',
     'Texas-Rio Grande Valley',
     'The Citadel',
     'Toledo',
     'Towson',
     'Trinity (CT) Bantams',
     'Trinity (TX) Tigers',
     'Troy',
     'Tulane',
     'Tulsa',
     'U.S. International Gulls',
     'UAB',
     'UC Davis',
     'UC Irvine',
     'UC Riverside',
     'UC San Diego',
     'UC Santa Barbara',
     'UCLA',
     'UNC Asheville',
     'UNC Greensboro',
     'UNC Wilmington',
     'Union (NY) Dutchmen',
     'UT Arlington',
     'Utah',
     'Utah State',
     'Utah Tech',
     'Utah Valley',
     'UTEP',
     'Utica Pioneers',
     'UTSA',
     'Valparaiso',
     'Vanderbilt',
     'Vermont',
     'Villanova',
     'Virginia',
     'Virginia Commonwealth',
     'Virginia Military Institute',
     'Virginia Tech',
     'Wabash Little Giants',
     'Wagner',
     'Wake Forest',
     'Washburn Ichabods',
     'Washington',
     'Washington & Jefferson Presidents',
     'Washington & Lee Generals',
     'Washington (MO) Bears',
     'Washington College Shoremen',
     'Washington State',
     'Wayne State (MI) Warriors',
     'Weber State',
     'Wesleyan (CT) Cardinals',
     'West Chester Golden Rams',
     'West Texas A&M Buffaloes',
     'West Virginia',
     'Western Carolina',
     'Western Colorado Mountaineers',
     'Western Illinois',
     'Western Kentucky',
     'Western Michigan',
     'Westminster (MO) Blue Jays',
     'Westminster (PA) Titans',
     'Wheaton (IL) Thunder',
     'Whittier Poets',
     'Wichita State',
     'Widener Pride',
     'William & Mary',
     'Williams Ephs',
     'Winthrop',
     'Wisconsin',
     'Wisconsin-Stevens Point Pointers',
     'Wisconsin-Superior Yellowjackets',
     'Wittenberg Tigers',
     'Wofford',
     'Wooster Fighting Scots',
     'WPI Engineers',
     'Wright State',
     'Wyoming',
     'Xavier',
     'Yale',
     'Youngstown State'),key='HomeBox')
      
    with col2:
        optionAway = st.selectbox(
    'Select the Away Team',
    ('Abilene Christian',
     'Air Force',
     'Akron',
     'Alabama',
     'Alabama A&M',
     'Alabama State',
     'Albany (NY)',
     'Alcorn State',
     'Allegheny Gators',
     'American',
     'Amherst Lord Jeffs',
     'Appalachian State',
     'Arizona',
     'Arizona State',
     'Arkansas',
     'Arkansas State',
     'Arkansas-Pine Bluff',
     'Armstrong Pirates',
     'Army',
     'Auburn',
     'Augusta State Jaguars',
     'Augustana (IL) Vikings',
     'Austin Peay',
     'Baker University Wildcats',
     'Baldwin-Wallace Yellow Jackets',
     'Ball State',
     'Baltimore Super Bees',
     'Baylor',
     'Bellarmine',
     'Belmont',
     'Beloit Buccaneers',
     'Bethune-Cookman',
     'Binghamton',
     'Birmingham-Southern Panthers',
     'Bloomsburg Huskies',
     'Boise State',
     'Boston College',
     'Boston University',
     'Bowling Green State',
     'Bradley',
     'Brigham Young',
     'Brigham Young College',
     'Brooklyn Bulldogs',
     'Brown',
     'Bryant',
     'Bucknell',
     'Buffalo',
     'Butler',
     'Cal Poly',
     'Cal State Bakersfield',
     'Cal State Fullerton',
     'Cal State Los Angeles Golden Eagles',
     'Cal State Northridge',
     'California',
     'California Baptist',
     'Campbell',
     'Canisius',
     'Canterbury College',
     'Carleton College Knights',
     'Carnegie Mellon Tartans',
     'Case Western Reserve Spartans',
     'Catholic Cardinals',
     'Centenary (LA) Gents',
     'Central Arkansas',
     'Central Connecticut State',
     'Central Florida',
     'Central Michigan',
     'Central Missouri Mules',
     'Central Pennsylvania College Knights',
     'Centre (KY) Colonels',
     'Charleston Southern',
     'Charlotte',
     'Chattanooga',
     'Cheyenne Business College',
     'Chicago Maroons',
     'Chicago State',
     'Cincinnati',
     'City College of New York Beavers',
     'Clemson',
     'Cleveland State',
     'Coastal Carolina',
     'Colgate',
     'College of Charleston',
     'College of New Jersey Lions',
     'Colorado',
     'Colorado College Tigers',
     'Colorado School of Mines Orediggers',
     'Colorado State',
     'Columbia',
     'Concordia Seminary Preachers',
     'Connecticut',
     'Coppin State',
     'Cornell',
     'Cotner College',
     'Creighton',
     'Cumberland',
     'Dakota Wesleyan Tigers',
     'Dartmouth',
     'Davidson',
     'Dayton',
     'Delaware',
     'Delaware State',
     'Denison Big Red',
     'Denver',
     'DePaul',
     'DePauw Tigers',
     'Detroit Mercy',
     'Dickinson College Red Devils',
     'Drake',
     'Drexel',
     'Duke',
     'Duquesne',
     'East Carolina',
     'East Central Tigers',
     'East Tennessee State',
     'Eastern Illinois',
     'Eastern Kentucky',
     'Eastern Michigan',
     'Eastern Washington',
     'Elon',
     'Emporia State Hornets',
     'Ensign College',
     'Evansville',
     'Fairfield',
     'Fairleigh Dickinson',
     'Florida',
     'Florida A&M',
     'Florida Atlantic',
     'Florida Gulf Coast',
     'Florida International',
     'Florida State',
     'Fordham',
     'Franklin Grizzlies',
     'Fresno State',
     'Furman',
     'Gardner-Webb',
     'Geneva Golden Tornadoes',
     'George Mason',
     'George Washington',
     'Georgetown',
     'Georgia',
     'Georgia Southern',
     'Georgia State',
     'Georgia Tech',
     'Gettysburg Bullets',
     'Gonzaga',
     'Grambling',
     'Grand Canyon',
     'Green Bay',
     'Grinnell Pioneers',
     'Grove City Wolverines',
     'Hamline Pipers',
     'Hampton',
     'Hardin-Simmons Cowboys',
     'Hartford Hawks',
     'Harvard',
     'Haskell (KS) Fighting Indians',
     'Hawaii',
     'High Point',
     'Hiram Terriers',
     'Hofstra',
     'Holy Cross',
     'Hope Flying Dutchmen',
     'Houston',
     'Houston Christian',
     'Howard',
     'Idaho',
     'Idaho State',
     'Illinois',
     'Illinois State',
     'Illinois Wesleyan Titans',
     'Illinois-Chicago',
     'Incarnate Word',
     'Indiana',
     'Indiana State',
     'Iona',
     'Iowa',
     'Iowa State',
     'IUPUI',
     'Jackson State',
     'Jacksonville',
     'Jacksonville State',
     'James Madison',
     'John Carroll Blue Streaks',
     'Kalamazoo Hornets',
     'Kansas',
     'Kansas City',
     'Kansas State',
     'Kennesaw State',
     'Kent State',
     'Kentucky',
     'Kentucky Wesleyan Panthers',
     'La Salle',
     'Lafayette',
     'Lake Forest Foresters',
     'Lamar',
     'Lawrence Vikings',
     'Le Moyne',
     'Lehigh',
     'Lewis Flyers',
     'Liberty',
     'Lindenwood',
     'Lipscomb',
     'Little Rock',
     'Long Beach State',
     'Long Island University',
     'Longwood',
     'Louisiana',
     'Louisiana State',
     'Louisiana Tech',
     'Louisiana-Monroe',
     'Louisville',
     'Loyola (IL)',
     'Loyola (LA) Wolfpack',
     'Loyola (MD)',
     'Loyola Marymount',
     'Macalester Scots',
     'Maine',
     'Manchester Spartans',
     'Manhattan',
     'Marietta Pioneers',
     'Marist',
     'Marquette',
     'Marshall',
     'Maryland',
     'Maryland-Baltimore County',
     'Maryland-Eastern Shore',
     'Massachusetts',
     'Massachusetts Institute of Technology Engineers',
     'Massachusetts-Lowell',
     'McNeese State',
     'Memphis',
     'Mercer',
     'Merchant Marine Mariners',
     'Merrimack',
     'Miami (FL)',
     'Miami (OH)',
     'Michigan',
     'Michigan State',
     'Middle Tennessee',
     'Millikin Big Blue',
     'Millsaps Majors',
     'Milwaukee',
     'Minnesota',
     'Minnesota A&M Aggies',
     'Mississippi',
     'Mississippi State',
     'Mississippi Valley State',
     'Missouri',
     'Missouri State',
     'Monmouth',
     'Montana',
     'Montana State',
     'Morehead State',
     'Morgan State',
     'Morris Brown Wolverines',
     "Mount St. Mary's",
     'Mount Union Purple Raiders',
     'Muhlenberg Mules',
     'Murray State',
     'Muskingum Fighting Muskies',
     'Navy',
     'NC State',
     'Nebraska',
     'Nebraska Wesleyan Prairie Wolves',
     'Nevada',
     'Nevada-Las Vegas',
     'New Hampshire',
     'New Mexico',
     'New Mexico State',
     'New Orleans',
     'New York University Violets',
     'Newberry Wolves',
     'Niagara',
     'Nicholls State',
     'NJIT',
     'Norfolk State',
     'North Alabama',
     'North Carolina',
     'North Carolina A&T',
     'North Carolina Central',
     'North Central Cardinals',
     'North Dakota',
     'North Dakota State',
     'North Florida',
     'North Texas',
     'Northeastern',
     'Northeastern Illinois Golden Eagles',
     'Northern Arizona',
     'Northern Colorado',
     'Northern Illinois',
     'Northern Iowa',
     'Northern Kentucky',
     'Northwest Missouri State Bearcats',
     'Northwestern',
     'Northwestern State',
     'Notre Dame',
     'Oakland',
     'Oberlin Yeomen',
     'Ohio',
     'Ohio State',
     'Ohio Wesleyan Battling Bishops',
     'Oklahoma',
     'Oklahoma City Chiefs',
     'Oklahoma State',
     'Old Dominion',
     'Omaha',
     'Oral Roberts',
     'Oregon',
     'Oregon State',
     'Pacific',
     'Penn State',
     'Pennsylvania',
     'Pepperdine',
     'Phillips Haymakers',
     'Pittsburg State Gorillas',
     'Pittsburgh',
     'Portland',
     'Portland State',
     'Prairie View',
     'Pratt Institute Cannoneers',
     'Presbyterian',
     'Princeton',
     'Providence',
     'Purdue',
     'Purdue Fort Wayne',
     'Queens (NC)',
     'Quinnipiac',
     'Radford',
     'Regis (CO) Rangers',
     'Rensselaer Engineers',
     'Rhode Island',
     'Rice',
     'Richmond',
     'Rider',
     'Ripon Red Hawks',
     'Roanoke Maroons',
     'Robert Morris',
     'Rochester (NY) Yellowjackets',
     "Rose-Hulman Fightin' Engineers",
     'Rutgers',
     'Sacramento State',
     'Sacred Heart',
     'Saint Francis (PA)',
     "Saint Joseph's",
     'Saint Louis',
     "Saint Mary's (CA)",
     "Saint Peter's",
     'Sam Houston',
     'Samford',
     'San Diego',
     'San Diego State',
     'San Francisco',
     'San Jose State',
     'Santa Clara',
     'Savage School of Physical Education',
     'Savannah State Tigers',
     'Scranton Royals',
     'Seattle',
     'Seton Hall',
     'Sewanee Tigers',
     'Siena',
     'South Alabama',
     'South Carolina',
     'South Carolina State',
     'South Carolina Upstate',
     'South Dakota',
     'South Dakota State',
     'South Florida',
     'Southeast Missouri State',
     'Southeastern Louisiana',
     'Southern',
     'Southern California',
     'Southern Illinois',
     'Southern Illinois-Edwardsville',
     'Southern Indiana',
     'Southern Methodist',
     'Southern Mississippi',
     'Southern Utah',
     'Southwestern (KS) Moundbuilders',
     'Southwestern (TX) Pirates',
     'Springfield Pride',
     'St. Bonaventure',
     'St. Francis (NY)',
     "St. John's (NY)",
     "St. John's College (OH)",
     'St. Lawrence Saints',
     'St. Thomas',
     'Stanford',
     'Stephen F. Austin',
     'Stetson',
     'Stevens Institute Ducks',
     'Stonehill',
     'Stony Brook',
     'SUNY-Potsdam Bears',
     'Swarthmore Garnet',
     'Syracuse',
     'Tarleton State',
     'TCU',
     'Temple',
     'Tennessee',
     'Tennessee State',
     'Tennessee Tech',
     'Tennessee-Martin',
     'Texas',
     'Texas A&M',
     'Texas A&M-Commerce',
     'Texas A&M-Corpus Christi',
     'Texas Southern',
     'Texas State',
     'Texas Tech',
     'Texas Wesleyan Rams',
     'Texas-Rio Grande Valley',
     'The Citadel',
     'Toledo',
     'Towson',
     'Trinity (CT) Bantams',
     'Trinity (TX) Tigers',
     'Troy',
     'Tulane',
     'Tulsa',
     'U.S. International Gulls',
     'UAB',
     'UC Davis',
     'UC Irvine',
     'UC Riverside',
     'UC San Diego',
     'UC Santa Barbara',
     'UCLA',
     'UNC Asheville',
     'UNC Greensboro',
     'UNC Wilmington',
     'Union (NY) Dutchmen',
     'UT Arlington',
     'Utah',
     'Utah State',
     'Utah Tech',
     'Utah Valley',
     'UTEP',
     'Utica Pioneers',
     'UTSA',
     'Valparaiso',
     'Vanderbilt',
     'Vermont',
     'Villanova',
     'Virginia',
     'Virginia Commonwealth',
     'Virginia Military Institute',
     'Virginia Tech',
     'Wabash Little Giants',
     'Wagner',
     'Wake Forest',
     'Washburn Ichabods',
     'Washington',
     'Washington & Jefferson Presidents',
     'Washington & Lee Generals',
     'Washington (MO) Bears',
     'Washington College Shoremen',
     'Washington State',
     'Wayne State (MI) Warriors',
     'Weber State',
     'Wesleyan (CT) Cardinals',
     'West Chester Golden Rams',
     'West Texas A&M Buffaloes',
     'West Virginia',
     'Western Carolina',
     'Western Colorado Mountaineers',
     'Western Illinois',
     'Western Kentucky',
     'Western Michigan',
     'Westminster (MO) Blue Jays',
     'Westminster (PA) Titans',
     'Wheaton (IL) Thunder',
     'Whittier Poets',
     'Wichita State',
     'Widener Pride',
     'William & Mary',
     'Williams Ephs',
     'Winthrop',
     'Wisconsin',
     'Wisconsin-Stevens Point Pointers',
     'Wisconsin-Superior Yellowjackets',
     'Wittenberg Tigers',
     'Wofford',
     'Wooster Fighting Scots',
     'WPI Engineers',
     'Wright State',
     'Wyoming',
     'Xavier',
     'Yale',
     'Youngstown State'),key='AwayBox')
      
    if st.button('Click to Submit'):
        schoollist1=[optionHome,optionAway]
        schoollist1.sort()
        schoollist=[]
        for x in schoollist1:
            x= x.replace('&','').replace('(','').replace(')','')
            
            if '-' in x:
                x= x.lower().split(' ')[0]
            else:
                x=x.lower().split(' ')[0:2]
                x='-'.join(x)
            schoollist.append(x)
        
        tempx=pd.DataFrame()
        for school in schoollist:
            
            url = "https://www.sports-reference.com/cbb/schools/{}/men/2024-gamelogs-advanced.html".format(school)
            df2=scrape_website(url)
       
            time.sleep(3.5)
            df2.iloc[1].tolist()
    
            df2.columns = ['G',
             'Date',
             'nocolumn',
             'Opp',
             'W/L',
             'Tm',
             'Oppscore',
             'ORtg',
             'DRtg',
             'Pace',
             'FTr',
             '3PAr',
             'TS%',
             'TRB%',
             'AST%',
             'STL%',
             'BLK%',
             'nocolumn2',
             'eFG%_off',
             'TOV%_off',
             'ORB%_off',
             'FT/FGA_off',
             'nocolumn3',
             'eFG%_def',
             'TOV%_def',
             'DRB%_def',
             'FT/FGA_def']
    
            df2=df2[['G',
             'Date',
    
             'Opp',
             'W/L',
             'Tm',
             'Oppscore',
             'ORtg',
             'DRtg',
             'Pace',
             'FTr',
             '3PAr',
             'TS%',
             'TRB%',
             'AST%',
             'STL%',
             'BLK%',
    
             'eFG%_off',
             'TOV%_off',
             'ORB%_off',
             'FT/FGA_off',
    
             'eFG%_def',
             'TOV%_def',
             'DRB%_def',
             'FT/FGA_def']].iloc[2:]
    
            df2['Tm']=pd.to_numeric(df2['Tm'],errors='coerce')
            df2=df2.dropna(subset='Tm')
            df2['Team']=school
            tempx=pd.concat([tempx,df2])
                
        df3= pd.DataFrame()
        i=0
        for team in tempx['Team'].unique():
            
            temp = tempx.loc[tempx['Team'] == team]
            if len(temp['G']) > 5:
                avg1 =pd.DataFrame(temp[['Tm', 'Oppscore','ORtg', 'DRtg',
                   'Pace', 'FTr', '3PAr', 'TS%', 'TRB%', 'AST%', 'STL%', 'BLK%',
                   'eFG%_off', 'TOV%_off', 'ORB%_off', 'FT/FGA_off', 'eFG%_def',
                   'TOV%_def', 'DRB%_def', 'FT/FGA_def']].iloc[len(temp['G'])-4:len(temp['G'])-1].astype(float).mean()).T
                #avg1['Date'] = temp.iloc[len(temp['G'])-2].Date
                avg1['Team'] = team
                avg1['consitencyscoreoff'] = ((1-abs((temp[['Tm']].iloc[len(temp['G'])-4:len(temp['G'])-1]-avg1['Tm'].iloc[0]) / avg1['Tm'].iloc[0]) ).mean() * 100)[0]
                avg1['consitencyscoredef'] = ((1-abs((temp[['Oppscore']].astype(float).iloc[len(temp['G'])-4:len(temp['G'])-1]-avg1['Oppscore'].astype(float).iloc[0]) / avg1['Oppscore'].astype(float).iloc[0]) ).mean() * 100)[0]
        
                if i == 0:
                    constoff = avg1['consitencyscoreoff'].iloc[0]
                    constdef = avg1['consitencyscoredef'].iloc[0]
                    i=i+1
                else:
                    constoff2 = avg1['consitencyscoreoff'].iloc[0]
                    constdef2 = avg1['consitencyscoredef'].iloc[0]
                #temp2=pd.concat([avg1,avg2])
                df3=pd.concat([df3,avg1])
                df3['index']='0'
    
        #st.header('_'.join(list(temp['Team'].unique())))
        st.header('Team Metrics')
        st.dataframe(df3) 
        data_t=pd.merge(df3.iloc[[0]],df3.iloc[[1]],left_on=['index'],right_on=['index'],
                  suffixes=('','Opp_metrics'))


        
        Xdata=data_t[['ORtg',
       'DRtg', 'Pace', 'FTr', '3PAr', 'TS%', 'TRB%', 'AST%', 'STL%', 'BLK%',
       'eFG%_off', 'TOV%_off', 'ORB%_off', 'FT/FGA_off', 'eFG%_def',
       'TOV%_def', 'DRB%_def', 'FT/FGA_def', 'consitencyscoreoff',
       'consitencyscoredef', 'TmOpp_metrics', 'OppscoreOpp_metrics',
       'ORtgOpp_metrics', 'DRtgOpp_metrics', 'PaceOpp_metrics',
       'FTrOpp_metrics', '3PArOpp_metrics', 'TS%Opp_metrics',
       'TRB%Opp_metrics', 'AST%Opp_metrics', 'STL%Opp_metrics',
       'BLK%Opp_metrics', 'eFG%_offOpp_metrics', 'TOV%_offOpp_metrics',
       'ORB%_offOpp_metrics', 'FT/FGA_offOpp_metrics', 'eFG%_defOpp_metrics',
       'TOV%_defOpp_metrics', 'DRB%_defOpp_metrics', 'FT/FGA_defOpp_metrics',
        'consitencyscoreoffOpp_metrics',
       'consitencyscoredefOpp_metrics']].fillna(0)
        import pickle
        # save the model to disk
        filename = 'edge_ncaamodel1.sav'


        # load the model from disk
        regressor = pickle.load(open(filename, 'rb'))
        y_pred = regressor.predict(Xdata)[0]
        #y_pred=142


        st.header('{} Stats >> Offensive Consistency : {}   Defensive Consistency : {} '.format(optionHome,round(constoff,2),round(constdef,2)))
       
        st.markdown("***")

        st.header('{} Stats >> Offensive Consistency : {}   Defensive Consistency : {} '.format(optionAway,round(constoff2,2),round(constdef2,2)))
       
        st.markdown("***")
        
        st.header('{} Total Points'.format(round(y_pred+7,0)))
    # Add your Streamlit app code here

if __name__ == "__main__":
    main()
