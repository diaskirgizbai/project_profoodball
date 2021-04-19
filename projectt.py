import urllib.request
from bs4 import BeautifulSoup
import csv


# PARSING TABLES
url_epl = 'https://www.skysports.com/premier-league-table'
url_laliga = 'https://www.skysports.com/la-liga-table'
url_seriaA = 'https://www.skysports.com/serie-a-table'
url_ligue1 = 'https://www.skysports.com/ligue-1-table'
url_bundes = 'https://www.skysports.com/bundesliga-table'


def parsing_table(url,league_name):

  result_list = []
  win_list = []
  d_list = []
  l_list = []
  o_list = []
  f_list = []
  a_list = []
  p_list = []
  m_list = []
  r2 = urllib.request.urlopen(url)
  soup2 = BeautifulSoup(r2,'html.parser')
  win = soup2.find_all('td', class_='standing-table__cell')
  a=0
  for y in win:
    if a==0:
      m_list.append(y.text.strip())
    if a==1:
      result_list.append(y.text.strip())
    if a==2:
      o_list.append(y.text.strip())
    if a==3:
      win_list.append(y.text.strip())
    if a==4:
      d_list.append(y.text.strip())
    if a==5:
      l_list.append(y.text.strip())
    if a==6:
      f_list.append(y.text.strip())
    if a==7:
      a_list.append(y.text.strip())
    if a==8:
      pass
    if a==9:
      p_list.append(y.text.strip())
    if a==10:
      pass
    a=a+1
    if a==11:
      a=0


  with open("table_"+league_name+".csv", 'w+', newline='' ) as file:
    column_names=['№','TEAM','PL','W','D','L','F','A','PTS']
    wr = csv.DictWriter(file,fieldnames=column_names)
    wr.writerow({'№':'№','TEAM':'TEAM','PL':'PL','W':'W','D':'D','L':'L','F':'F','A':'A','PTS':'PTS'} ) # column names
    for aa in range (len(m_list)):
      wr.writerow({'№': m_list[aa],'TEAM': result_list[aa],'PL': o_list[aa],'W': win_list[aa],'D': d_list[aa],'L': l_list[aa],'F': f_list[aa],'A': a_list[aa],'PTS': p_list[aa]})
parsing_table(url_bundes, 'bundesliga')
parsing_table(url_seriaA, 'seriaA')
parsing_table(url_ligue1, 'ligue1')
parsing_table(url_epl, 'epl')
parsing_table(url_laliga, 'laliga')


#PARSING TOP SCORERS

url_top_scorers_epl='https://www.bbc.com/sport/football/premier-league/top-scorers'
url_top_scorers_laliga='https://www.bbc.com/sport/football/spanish-la-liga/top-scorers'
url_top_scorers_seriaA='https://www.bbc.com/sport/football/italian-serie-a/top-scorers'
url_top_scorers_bundes='https://www.bbc.com/sport/football/german-bundesliga/top-scorers'
url_top_scorers_ligue1='https://www.bbc.com/sport/football/french-ligue-one/top-scorers'


def parsing_scorers(url,league_name):
  name = []
  goal = []
  game = []
  r = urllib.request.urlopen(url)
  soup2 = BeautifulSoup(r, 'html.parser')
  scorers = soup2.find_all('span', class_='gs-u-vh@l')
  a = 0
  for x in scorers:
    name.append(x.text.strip())
  scorers2 = soup2.find_all('td',class_='gs-o-table__cell gs-o-table__cell--right')
  for y in scorers2:
    if a == 0:
      goal.append(y.text.strip())
    if a == 1:
      pass
    if a == 2:
      game.append(y.text.strip())
    if a == 3:
      pass
    a = a+1
    if a == 4:
      a = 0

  with open("top_scores_" + league_name + ".csv", 'w+', newline='', encoding='utf-8') as file:
    column_names = ['NAME', 'GOAL', 'GAME']
    wr = csv.DictWriter(file, fieldnames=column_names)
    wr.writerow({'NAME': 'NAME', 'GOAL': 'GOAL', 'GAME': 'GAME'})
    for aa in range(len(goal)):
      wr.writerow({'NAME': str(name[aa]), 'GOAL': str(goal[aa]), 'GAME': str(game[aa])})
parsing_scorers(url_top_scorers_epl,'epl')
parsing_scorers(url_top_scorers_laliga,'laliga')
parsing_scorers(url_top_scorers_seriaA,'seriaA')
parsing_scorers(url_top_scorers_bundes,'bundesliga')
parsing_scorers(url_top_scorers_ligue1,'ligue1')



# PARSING CALENDAR
url_calendar_laliga = 'https://www.sport-express.ru/football/L/foreign/spain/laleague/2020-2021/calendar/tours/'
url_calendar_epl = 'https://www.sport-express.ru/football/L/foreign/england/premier/2020-2021/calendar/tours/'
url_calendar_seriaA = 'https://www.sport-express.ru/football/L/foreign/italy/seriaa/2020-2021/calendar/tours/'
url_calendar_bundes = 'https://www.sport-express.ru/football/L/foreign/german/bundes1/2020-2021/calendar/tours/'
url_calendar_ligue1 = 'https://www.sport-express.ru/football/L/foreign/france/league1/2020-2021/calendar/tours/'


def parsing_calendar(url, league_name):
    tur = []
    team1 = []
    team2 = []
    score = []
    a = 0
    r = urllib.request.urlopen(url)
    soup = BeautifulSoup(r, 'html.parser')
    data1 = soup.find_all('span', class_='link-underline')
    for x in data1:
        a = a+1
        if a % 2 == 1:
            team1.append(x.text.strip())
        if a % 2 == 0:
            team2.append(x.text.strip())
    data2 = soup.find_all('p', class_='score_time')
    for x in data2:
        score.append(x.text.strip())
    for x in range(len(team1)-len(score)):
        score.append('---')
    if len(team1) == 306:
        b = ((len(team1))/9)+1
        for x in range(1, int(b)):
            for y in range(9):
                tur.append(x)
    else:
        b = (len(team1)/10)+1
        for x in range(1, int(b)):
            for y in range(10):
                tur.append(x)

    with open("calendar_" + league_name + ".csv", 'w+', newline='') as file:
        column_names = ['TUR', 'TEAM1', 'TEAM2', 'SCORE']
        wr = csv.DictWriter(file, fieldnames=column_names)
        wr.writerow({'TUR': 'TUR', 'TEAM1': 'TEAM1', 'TEAM2': 'TEAM2', 'SCORE': 'SCORE'})
        for aa in range(len(tur)):
            wr.writerow({'TUR': tur[aa], 'TEAM1': str(team1[aa]), 'TEAM2': str(team2[aa]), 'SCORE': str(score[aa])})


parsing_calendar(url_calendar_laliga, 'laliga')
parsing_calendar(url_calendar_seriaA, 'seriaA')
parsing_calendar(url_calendar_epl, 'epl')
parsing_calendar(url_calendar_bundes, 'bundesliga')
parsing_calendar(url_calendar_ligue1, 'ligue1')

# PARSING TOP ASSIST
url_top_assist_epl = 'https://www.bbc.com/sport/football/premier-league/top-scorers/assists'
url_top_assist_laliga = 'https://www.bbc.com/sport/football/spanish-la-liga/top-scorers/assists'
url_top_assist_seriaA = 'https://www.bbc.com/sport/football/italian-serie-a/top-scorers/assists'
url_top_assist_bundes = 'https://www.bbc.com/sport/football/german-bundesliga/top-scorers/assists'
url_top_assist_ligue1 = 'https://www.bbc.com/sport/football/french-ligue-one/top-scorers/assists'


def parsing_top_assist(url, league_name):
    name = []
    assist = []
    game = []
    a = 0
    r = urllib.request.urlopen(url)
    soup = BeautifulSoup(r)
    data1 = soup.find_all('span', class_='gs-u-vh@l')
    for x in data1:
        name.append(x.text.strip())
    data2 = soup.find_all('td', class_='gs-o-table__cell gs-o-table__cell--right')
    for x in data2:
        a = a + 1
        if a == 1:
            assist.append(x.text.strip())
        if a == 2:
            pass
        if a == 3:
            game.append(x.text.strip())
        if a == 3:
            a = 0
    with open("top_assists_" + league_name + ".csv", 'w+', newline='', encoding='utf-8') as file:
        column_names = ['NAME', 'ASSIST', 'GAME']
        wr = csv.DictWriter(file, fieldnames=column_names)
        wr.writerow({'NAME': 'NAME', 'ASSIST': 'ASSIST', 'GAME': 'GAME'})
        for aa in range(len(assist)):
            wr.writerow({'NAME': str(name[aa]), 'ASSIST': str(assist[aa]), 'GAME': str(game[aa])})


parsing_top_assist(url_top_assist_epl, 'epl')
parsing_top_assist(url_top_assist_laliga, 'laliga')
parsing_top_assist(url_top_assist_seriaA, 'seriaA')
parsing_top_assist(url_top_assist_bundes, 'bundesliga')
parsing_top_assist(url_top_assist_ligue1, 'ligue1')
# проверка