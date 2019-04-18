from django.shortcuts import render, render_to_response
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
from app.forms import StateForm, state_const_form

dict = {"Abhanpur": "53", "Ahiwara": "67", "Akaltara": "33", "Arang": "52", "Basna": "40", "Bastar": "85",
        "Beltara": "31", "Bijapur": "89", "Bilha": "29", "Durg City": "64", "AGAR": "166", "ALOTE": "223",
        "AMLA": "130", "ASHTA": "157", "ATER": "9", "BAGLI": "174", "BAIHAR": "108", "BANDA": "42", "BARGI": "96",
        "BETUL": "131", "Aizawl North-i": "10", "Aizawl North-ii": "11", "Aizawl North-iii": "12",
        "Aizawl East-i": "13", "Aizawl East-ii": "14", "Aizawl South-i": "18", "Aizawl South-ii": "19",
        "Aizawl South-iii": "20", "Aizawl West-i": "15", "Aizawl West-ii": "16", "Aizawl West-iii": "17",
        "Ahore": "141", "Amber": "47", "Anta": "193", "Asind": "177", "Bali": "120", "Bagru": "56", "Bansur": "63",
        "Bari": "78", "Bassi": "57", "Bhim": "173", "Alair": "97", "Armur": "11", "Boath": "8", "Chennur": "2",
        "Chevella": "53", "Dubbak": "41", "Gadwal": "79", "Jagtial": "21", "Jukkal": "13", "Mulug": "109"}

dict1={"Alwar Rural":"65" ,"Alwar Urban": "66" ,"Anupgarh": "6" ,"Asind": "177",
       "Aspur": "159" ,"Bagru": "120","Bali": "120","Banswara": "164","Baran-atru": "195","Bari sadri": "171",
       "Baseri":"77","Bayana":"76","Baytu":"136","Beawar":"168",
       "Ahiwara": "67", "Akaltara": "33", "Arang": "52", "Beltara": "31","Bilaigarh":"43","Bilha":"29",
       "Bindranawagarh":"55","Chitrakot":"87","Durg Gramin":"63","Gunderdehi":"61","Jaijaipur":"37",
       "Janjgirchampa":"34","Jashpur":"12","Kanker":"81","Kasdo":"l44",
       "Achampet":"82","Adilabad":"7","Alair":"97","Alampur":"80","Amberpet":"59","Andole":"36",
       "Armur":"11","Asifabad":"5","Aswaraopeta":"118","Bahadurpura":"69","Balkonda":"19","Banswada":"14",
       "Bellampalli": "3", "Bhadrachalam": "119", "Bhongir": "94",
        "AGAR":"166", "ALIRAJPUR": "191", "ALOTE": "223", "AMLA": "130", "ASHOK NAGAR": "32",
        "ATER": "9", "BADNAGAR": "218", "BADNAWAR": "202", "BAGLI": "174", "BAHORIBAND": "94", "BAIHAR": "108",
        "BAMORI": "28", "BANDA": "42", "BANDHAVGARH": "89", "BARGHAT": "114", "BASODA": "145", "BHAINSDEHI": "133",
       "Aizawl South-iii": "20", "Champhai South": "24", "Hachhek": "1", "Hrangturzo": "28","Lawngtlai East": "38",
       "Lawngtlai West": "37", "Lengteng": "21","Lunglei South": "33", "Palak": "40", "Serlui": "6", "Tawi": "9",
       "Thorang": "34"}

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,'app/index.html')

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def partywise(request):
    states={'s26':'Chattisgarh','s29':'Telangana','s12':'MadhyaPradesh','s16':'Mizoram','s20':'Rajasthan'}
    if request.method=="POST":
        form = StateForm(request.POST)
        state = form['dropdown']
        Name = state.data
        ruby="C:/Users/admin/source/repos/ElectionResultsAnalysis/ElectionResultsAnalysis/app/static/scrape_data/"+Name+".csv"
        df = pd.read_csv(ruby,skiprows=2)
        df.plot(kind='bar',x='Party',y='Won',color='blue')
        plt.savefig('C:/Users/admin/source/repos/FlaskElectionDADV/FlaskElectionDADV/FlaskElectionDADV/static/plots/'+Name+".png")
        if(state.data=='Chattisgarh'):
            return render(request,'app/chattisgarh.html')
        elif(state.data=='MadhyaPradesh'):
            return render(request,'app/madhyapradesh.html')
        elif(state.data=='Rajasthan'):
            return render(request,'app/rajasthan.html')
        elif(state.data=='Telangana'):
            return render(request,'app/telangana.html')
        elif(state.data=='Mizoram'):
            return render(request, 'app/mizoram.html')
        else:
            return render(request,'app/party.html')
    else:
        return render(request,'app/party.html')

def trend(request):
    if request.method=="POST":
        form = state_const_form(request.POST)
        Name = form['dropdown'].data
        if(Name=='Chattisgarh'):
            return render(request,'app/chattisgarhtrend.html')
        elif(Name=='MadhyaPradesh'):
            return render(request,'app/madhyapradeshtrend.html')
        elif(Name=='Rajasthan'):
            return render(request,'app/rajasthantrend.html')
        elif(Name=='Telangana'):
            return render(request,'app/telanganatrend.html')
        elif(Name=='Mizoram'):
            return render(request, 'app/mizoramtrend.html')
        else:
            return render(request,'app/party.html')
        #Name4 = form['dropdown1'].data
        #Name1 = dict1[Name4]
        #id=Name1
        #kamesh = str(Name+ ".csv")
        #Name2 = (Name + Name1 + "")
        #Name3 = Name2 + ".png"
        #kk = str("C:/Users/admin/source/repos/ElectionResultsAnalysis/ElectionResultsAnalysis/app/static/data/"+Name+"/"+Name2+".csv")
        #with open(kk, 'r') as f:
            #var = []
            #var = csv.reader(f, delimiter=",");
            #left=[1]
            #tick_label = []
            #margin=[]
            #for i in var:
                #print("Length of i:",len(i))
                #if len(i) is not 0:
                    #tick_label.append(i[1])
                    #margin.append(int(i[2]))
                    #if(len(i)!=3):
                        #tick_label.append(i[1])
                        #margin.append(int(i[2]))
                        #left.append(2)
            #fig = plt.figure()
            #plt.bar(left, margin, tick_label=tick_label,width=0.5 ,color=['red', 'green'])
            #plt.xlabel('Leading party');
            #plt.ylabel('Margin');
            #plt.title('Constituency- wise Trends')
            #plt.show()
            #plt.savefig('C:/Users/admin/source/repos/ElectionResultsAnalysis/ElectionResultsAnalysis/app/static/scrape_data/graph.png');
            #plt.clf()
        return render(request,'app/trend.html')
    else:
        #trendwise_crawling()
        return render(request,'app/trend.html')

def const(request):
    if request.method=="POST":
        dict={"Abhanpur":"53","Ahiwara":"67","Akaltara":"33","Arang":"52","Basna":"40","Bastar":"85","Beltara":"31","Bijapur":"89","Bilha":"29","Durg City":"64","AGAR":"166","ALOTE":"223","AMLA":"130","ASHTA":"157","ATER":"9","BAGLI":"174","BAIHAR":"108","BANDA":"42","BARGI":"96","BETUL":"131","Aizawl North-i":"10","Aizawl North-ii":"11","Aizawl North-iii":"12","Aizawl East-i":"13","Aizawl East-ii":"14","Aizawl South-i":"18","Aizawl South-ii":"19","Aizawl South-iii":"20","Aizawl West-i":"15","Aizawl West-ii":"16","Aizawl West-iii":"17","Ahore":"141","Amber":"47","Anta":"193","Asind":"177","Bali":"120","Bagru":"56","Bansur":"63","Bari":"78","Bassi":"57","Bhim":"173","Alair":"97","Armur":"11","Boath":"8","Chennur":"2","Chevella":"53","Dubbak":"41","Gadwal":"79","Jagtial":"21","Jukkal":"13","Mulug":"109"}
        form = state_const_form(request.POST)
        Name = form['dropdown'].data
        #Name4 = form['dropdown1'].data
        Name1 = dict[Name4]
        Gadzou=str(Name+Name1+".csv")
        Name2=(Name+Name1+"")
        Name3=Name2+".png"
        sana=str("C:/Users/admin/source/repos/Election_Commission/Election_Commission/app/static/app/data/"+Name+"/"+Gadzou)
        with open(sana, 'r') as f:
            var = []
            c_name = []
            p_name = []
            votes = []
            left=[]
            j=0
            tick_label = []
            var = csv.reader(f, delimiter=",");
            for i in var:
                if len(i) is not 0:
                    c_name.append(i[0]);
                    p_name.append(i[1]);
                    votes.append(int(i[2]));
            fig = plt.figure()
            index = np.arange(len(c_name))
            plt.bar(c_name, votes,color=['red', 'yellow', 'blue', 'green', 'black']);
            plt.xlabel('Candidate_name');
            plt.ylabel('Votes polled per canditate');
            plt.xticks(index,c_name, fontsize=5, rotation=70)
            plt.title('Constituency- wise results')
            #plt.show()
            plt.savefig('C:/Users/admin/source/repos/ElectionResultsAnalysis/ElectionResultsAnalysis/app/static/plots/graph.png')
            plt.clf()
            return render(request,'app/constituency.html',{'state':Name,'const':Name4})
    else:
        return render(request,'app/const.html')

def trendwise_crawling():

    link ="http://eciresults.nic.in/statewise{0}.htm"
    state_dict = [
                {'code': 'S26', 'name': 'Chattisgarh', 'pages': 9},
                {'code': 'S12', 'name': 'Madhya Pradesh', 'pages': 23},
                {'code': 'S16', 'name': 'Mizoram', 'pages': 4},
                {'code': 'S20', 'name': 'Rajasthan', 'pages': 20},
                {'code': 'S29', 'name': 'Telangana', 'pages': 12}
            ]
    list_records = []
    for state in state_dict:
        pages = state['pages']
        for i in range(pages):
            page = requests.get(link.format(state['code']+str('' if(i==0) else i)))
            soup = BeautifulSoup(page.content,'html.parser')
            data_tbody = soup.find("tbody", id="ElectionResult")
            for div in data_tbody.find_all("div", {'class':'tooltip'}): 
                div.decompose()
            for span in data_tbody.find_all("span"): 
                span.decompose()
            all_trs = get_first_child(data_tbody, 'tr')
            imp_trs = all_trs[4:]
            for tr in imp_trs:
                all_tds = get_first_child(tr, 'td')
                constituency_dict = {
                        'State': state['name'], 'Constituency':all_tds[0].getText(),
                        'Const.No.': int(all_tds[1].getText()), 'Winner':all_tds[2].getText(),
                        'Winner_Party': all_tds[3].getText(), 'Loser':all_tds[4].getText(),
                        'Loser_Party': all_tds[5].getText(), 'Margin': int(all_tds[6].getText()),
                        'Previous_Winner':all_tds[8].getText(), 'Previous_Winner_Party': all_tds[9].getText(),
                        'Previous_Margin': int(all_tds[10].getText() if(all_tds[10].getText()!='') else 0)
                    }
            # print(constituency_dict)
                list_records.append(constituency_dict)
    dataframe = pd.DataFrame(list_records)
    dataframe.to_csv('C:/Users/admin/source/repos/ElectionResultsAnalysis/ElectionResultsAnalysis/app/static/data/trends2019.csv')

def get_first_child(soup_page, child):
    first_child = soup_page.find(child)
    all_child = [first_child] + first_child.find_next_siblings(child)
    return all_child
