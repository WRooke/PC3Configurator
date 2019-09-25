import pyodbc
from pulp import *

conn = pyodbc.connect(
  r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\williamr\OneDrive - OEM TECHNOLOGY SOLUTIONS PTY LTD\Systems\PC3Configurator\PC3Config.accdb;')
cursor = conn.cursor()

DI_num = int(input("DI number: "))
DO_num = int(input("DO number: "))
AI_num = int(input("AI number: "))
AO_num = int(input("AO number: "))

# Create list of PCAs
PCAs = list()

# Create dictionaries of PCA names and numbers of I/O
DI_dict = dict()
DO_dict = dict()
AI_dict = dict()
AO_dict = dict()

# Get from database
cursor.execute("select * from PC3_PCA")

# Populate lists and dictionaries
for row in cursor.fetchall():
  PCAs.append(row.PCA_Name)
  DI_dict[row.PCA_Name] = row.DI
  DO_dict[row.PCA_Name] = row.DO
  AI_dict[row.PCA_Name] = row.AI
  AO_dict[row.PCA_Name] = row.AO

# Create minimisation problem
prob = LpProblem("PC3", LpMinimize)

# Dictionary to contain variables with type/category and limits
PCA_vars = LpVariable.dicts("PCA", PCAs, 0, None, cat="Integer")

# Objective function to minimise
prob += lpSum([DI_dict[i] * PCA_vars[i] + DO_dict[i] * PCA_vars[i] + AI_dict[i] * PCA_vars[i] + AO_dict[i] * PCA_vars[i] for i in PCAs])
# prob += lpSum([PCA_vars[i] for i in PCAs])

# Constraints
prob += lpSum([DI_dict[i] * PCA_vars[i] for i in PCAs]) >= DI_num
prob += lpSum([DO_dict[i] * PCA_vars[i] for i in PCAs]) >= DO_num
prob += lpSum([AI_dict[i] * PCA_vars[i] for i in PCAs]) >= AI_num
prob += lpSum([AO_dict[i] * PCA_vars[i] for i in PCAs]) >= AO_num

# Write to .lp file
prob.writeLP("PC3_optim.lp")

# Solve it
prob.solve()

# Print solution status
print("Status: ",LpStatus[prob.status])

numPCAs = 0
for v in prob.variables():
  print(v.name, " = ", v.varValue)
  numPCAs += v.varValue

# print("Total number of I/Os = ", value(prob.objective))
print("Total number of PCAs = ", numPCAs)