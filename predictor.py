import pandas as pd 
import joblib
import sys

def predictRuns(inputfile):
    
    test_case = pd.read_csv(inputfile)

    n = len(test_case['batsmen'].values[0].split(','))-2
    

    file = open(r'{0}/regeression_model.joblib'.format(sys.path[0]),'rb')
    regeressor = joblib.load(file)
    file.close()
    file = open(r'{0}/team_encoder.joblib'.format(sys.path[0]),'rb')
    team_encoder = joblib.load(file)
    file.close()    


    test_case['batting_team'] = team_encoder.transform(test_case['batting_team'])
    test_case['bowling_team'] = team_encoder.transform(test_case['bowling_team'])

    data = [[test_case['batting_team'].values[0],test_case['bowling_team'].values[0],n]]
    
    prediction = int(regeressor.predict(data)[0])
    
    return prediction

test_case = pd.read_csv('input_test_data.csv')

    n = len(test_case['batsmen'].values[0].split(','))-2
    

    file = open(r'{0}/regeression_bowling_model.joblib'.format(sys.path[0]),'rb')
    regeressor = joblib.load(file)
    file.close()
    file = open(r'{0}/name_encoder.joblib'.format(sys.path[0]),'rb')
    team_encoder = joblib.load(file)
    file.close()    

