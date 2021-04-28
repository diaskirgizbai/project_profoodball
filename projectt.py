import urllib.request
from bs4 import BeautifulSoup
import csv
import pandas as pd
from tkinter import *
from tkinter import ttk

print('Выполняется обнавление данных. Подаждите')
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


  with open("table_"+league_name+".csv", 'w+', newline='', encoding='utf-8' ) as file:
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

    with open("calendar_" + league_name + ".csv", 'w+', newline='', encoding='utf-8') as file:
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
    soup = BeautifulSoup(r, 'html.parser')
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


def start():
    btn_table.place_forget()
    btn_match.place_forget()
    btn_statistic.place_forget()
    btn_back.place_forget()
    btn_start_laliga.place(x=290, y=115)
    btn_start_seriaA.place(x=290, y=195)
    btn_start_epl.place(x=290, y=275)
    btn_start_ligue1.place(x=290, y=355)
    btn_start_bundesliga.place(x=290, y=435)
def laliga():
    league = 'laliga'
    ProFootball(league).opiration()
def seriaA():
    league = 'seriaA'
    ProFootball(league).opiration()
def epl():
    league = 'epl'
    ProFootball(league).opiration()
def ligue1():
    league = 'ligue1'
    ProFootball(league).opiration()
def bundesliga():
    league = 'bundesliga'
    ProFootball(league).opiration()

class ProFootball:
    def __init__(self, league):
        self.league = league

    def opiration(self):
        btn_start_laliga.place_forget()
        btn_start_seriaA.place_forget()
        btn_start_epl.place_forget()
        btn_start_ligue1.place_forget()
        btn_start_bundesliga.place_forget()
        btn_table.place(x=290, y=120)
        btn_match.place(x=290, y=210)
        btn_statistic.place(x=290, y=300)
        btn_statistic.config(command=self.statistic)
        btn_back.place(x=290, y=390)

    def back(self):
        lbl_statistic1.place_forget()
        lbl_statistic2.place_forget()
        btn_back_2.place_forget()
        tv2.place_forget()
        tv.place_forget()
        self.opiration()
        tv.delete(*tv.get_children())
        tv2.delete(*tv2.get_children())

    def statistic(self):
        a=0
        btn_table.place_forget()
        btn_match.place_forget()
        btn_statistic.place_forget()
        btn_back.place_forget()
        lbl_statistic1.place(x=350, y=280)
        lbl_statistic2.place(x=365, y=10)
        btn_back_2.place(x=10, y=10)
        with open('top_assists_'+self.league+'.csv') as file1:
            for x in csv.reader(file1):
                a = a+1
                if a > 1:
                    tv.insert('', 'end', values=x)
        with open('top_scores_'+self.league+'.csv') as file2:
            for x in csv.reader(file2):
                a = a + 1
                if a > 1:
                    tv2.insert('', 'end', values=x)

        tv2.place(x=100, y=320)
        tv.place(x=100, y=40)
        btn_back_2.config(command=self.back)

window = Tk()
window.geometry('800x600')
window.title('ProFootball')
window['bg'] = 'gray'

btn_start_laliga = Button(window, text='LA LIGA', width=30, height=3, command=laliga)
btn_start_seriaA = Button(window, text='SERIA A', width=30, height=3, command=seriaA)
btn_start_epl = Button(window, text='EPL', width=30, height=3, command=epl)
btn_start_ligue1 = Button(window, text='LIGUE 1', width=30, height=3, command=ligue1)
btn_start_bundesliga = Button(window, text='BUNDESLIGA', width=30, height=3, command=bundesliga)
btn_table = Button(window,text='TABLE', width=30, height=3, command='')
btn_match = Button(window,text='MATCH', width=30, height=3, command='')
btn_statistic = Button(window,text='STATISTIC', width=30, height=3, command='')
btn_back = Button(window,text='BACK', width=30, height=3, command=start)
btn_back_2 = Button(window,text='BACK', width=10, command='')

lbl_table = Label(window, text='')
lbl_statistic2 = Label(window, text='TOP ASSISTS')
lbl_statistic1 = Label(window, text='TOP BOMBARDIER')
lbl_match = Label(window, text='')

start()
tv = ttk.Treeview(window, columns=(1, 2, 3), show='headings', height='10')
tv2 = ttk.Treeview(window, columns=(1, 2, 3), show='headings', height='10')
tv.heading(1, text='NAME')
tv2.heading(1, text='NAME')
tv.heading(2, text='ASSIST')
tv2.heading(2, text='GOAL')
tv.heading(3, text='GAME')
tv2.heading(3, text='GAME')
window.mainloop()