import pandas as pd 
import joblib
import sys

def predictRuns(inputfile):
    
    test_case = pd.read_csv(inputfile)
    
    batsmen_list = test_case['batsmen'].values[0].split(',')
    bowler_list = test_case['bowlers'].values[0].split(',')
    over = 6/len(bowler_list)
    n = len(batsmen_list)-2

    
    file = open(r'{0}/regeression_model.joblib'.format(sys.path[0]),'rb')
    regeressor = joblib.load(file)
    file.close()
    file = open(r'{0}/new_regeression_model.joblib'.format(sys.path[0]),'rb')
    new_regeression = joblib.load(file)
    file.close()
    file = open(r'{0}/bowler_regeression_model.joblib'.format(sys.path[0]),'rb')
    bowler_regeression = joblib.load(file)
    file.close()
    file = open(r'{0}/team_encoder.joblib'.format(sys.path[0]),'rb')
    team_encoder = joblib.load(file)
    file.close()    
    file = open(r'{0}/venue_encoder.joblib'.format(sys.path[0]),'rb')
    venue_encoder = joblib.load(file)
    file.close()
    file = open(r'{0}/name_encoder.joblib'.format(sys.path[0]),'rb')
    name_encoder = joblib.load(file)
    file.close()
    file = open(r'{0}/bowler_encoder.joblib'.format(sys.path[0]),'rb')
    bowler_encoder = joblib.load(file)
    file.close()
    
    strike_rate_list = []
    temp = pd.DataFrame({
        'venue' : [test_case['venue'].values[0] for i in range(len(batsmen_list))],
        'striker' : [i for i in batsmen_list],
        'bowling_team' : [test_case['bowling_team'] for i in range(len(batsmen_list))]})

    temp2 = pd.DataFrame({
        
        'bowler' : [i for i in bowler_list],
        'batting_team' : [test_case['batting_team'] for i in range(len(bowler_list))]})

    temp.to_csv(r"{0}/temp.csv".format(sys.path[0]))
    temp = pd.read_csv(r"{0}/temp.csv".format(sys.path[0]))

    temp2.to_csv(r"{0}/temp2.csv".format(sys.path[0]))
    temp2 = pd.read_csv(r"{0}/temp2.csv".format(sys.path[0]))

    temp['venue'] = venue_encoder.transform(temp['venue'])

    test_case['batting_team'] = team_encoder.transform(test_case['batting_team'])
    test_case['bowling_team'] = team_encoder.transform(test_case['bowling_team'])

    data = [[test_case['batting_team'].values[0],test_case['bowling_team'].values[0],n]]

    prediction = round(regeressor.predict(data)[0])

    try:
        temp['striker'] = name_encoder.transform(temp['striker'])
        
        for i in range(0,n+2):
            data=[[temp['venue'].values[0],temp['striker'].values[i],test_case['bowling_team'].values[0]]]
            strike_rate_list.append(round(new_regeression.predict(data)[0]))

        avg_strike_rate = sum(strike_rate_list)/len(strike_rate_list)
        runs = (avg_strike_rate/100)*36
    
    except Exception:
        runs = 0

    try:
        temp2['bowler'] = bowler_encoder.transform(temp2['bowler'])

        ecoruns=0
        for i in range(0,len(bowler_list)):
            data=[[temp2['bowler'].values[i],test_case['batting_team'].values[0],test_case['innings'].values[0]]]
            ecoruns+=(round(bowler_regeression.predict(data)[0])*over)


    except Exception:
        ecoruns = 0

    if runs!=0 and ecoruns!=0:
        prediction = (prediction+runs+ecoruns)/3
    elif runs!=0 and ecoruns==0:
        prediction = (prediction+runs)/2
    elif runs==0 and ecoruns!=0:
        prediction = (prediction+ecoruns)/2
    else:
        pass
    return(prediction)