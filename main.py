import sys
from predictor import predictRuns

file_name = sys.argv[1]

runs = predictRuns(r'{0}/csv/{1}'.format(sys.path,file_name))

print("Predicted run: ",runs)