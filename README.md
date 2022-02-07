# IPL-2021-Predictor

## About this Predictor 

This program predicts the score (of first 6 overs) of a team with the previous data.

Contains historic data of T20 matches that have occurred in the past. This dataset may be used by the candidate teams to train an ML model or come up with a data analytics based algorithm that can perform the required prediction as mentioned above.

## Executing the program

**The input for the prediction is in the _input.csv_ file, it has the columns in the order of _(venue,innings,batting team,bowling team,batsmen,bowlers)_. Run the _main.py_ file with the the csv file (above mentioned) as it's _command line argument_.**

*The input.csv should look something like this*
```
venue,innings,batting_team,bowling_team,batsmen,bowlers
Arun Jaitley Stadium,1,Rajasthan Royals,Sunrisers Hyderabad,"YBK Jaiswal, JC Buttler, SV Samson","Sandeep Sharma, B Kumar, KK Ahmed, Rashid Khan"

```
*Run this command (The current dir should contain the main.py )*
```
python main.py input.csv
```

*The result will be printed.*


> *I did not create a front-end for this since at the time of creating this project it was unneccessary. I may develop in the future with some accuracy to the predictions since 2021 IPL was not conducted in India and the data that we trained the ML model had all the matches happening in India.*
