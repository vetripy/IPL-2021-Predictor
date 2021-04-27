import sys
from predictor import predictRuns

file_name = sys.argv[1]

runs = predictRuns(r"{0}/{1}".format(sys.path[0],sys.argv[1]))

print(int(runs))

