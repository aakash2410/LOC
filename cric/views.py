from django.shortcuts import render
import numpy as np
import pandas as pd

# Create your views here.
def home(request):
    return render(request,'cric/HomePage.html')
def calc(request):
    bats = pd.read_csv('bats.csv')
    bowls = pd.read_csv('bowl.csv')
    a = request.GET['n1']
    if a in list(bats['Batsman']):
        df1 = bats[bats['Batsman']==a]
        runs_b =int(df1['Runs'].sum())
        r4s = int(df1['4s'].sum())
        r6s = int(df1['6s'].sum())
        b_sr = df1['SR'].mean()
        bf = int(df1['BF'].sum())
    else:
        runs_b = 'None'
        r4s = 'None'
        r6s = 'None'
        b_sr = 'None'
        bf = 'None'
    mcom = max(list(df1['Opposition']))
    if a in list(bats['Batsman']):
        df2 = bowls[bowls['Bowler']==a]
        ovrs = int(df2['Overs'].sum())
        mdns = int(df2['Mdns'].sum())
        wkts = int(df2['Wkts'].sum())
        ecn = df2['Econ'].mean()
        sr = df2['SR'].mean()
    else:
        ovrs = 'None'
        mdns = 'None'
        wkts = 'None'
        ecn = 'None'
        sr = 'None'
    return render(request ,'cric/PlayerInfo.html',{'a':a,'Bruns':runs_b,'r4s':r4s,'r6s':r6s,'B_sr':b_sr,'Bface':bf,'Ovrs':ovrs,'Mdns':mdns,'Wkts':wkts,'Econ':ecn,'sr':sr,'mcom':mcom})
