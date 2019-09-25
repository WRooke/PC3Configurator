import pyodbc
from pulp import *

conn = pyodbc.connect(
  r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\williamr\OneDrive - OEM TECHNOLOGY SOLUTIONS PTY LTD\Systems\PC3Configurator\PC3Config.accdb;')
cursor = conn.cursor()

DI24_num = int(input("24V DI number: "))
DO24_num = int(input("24V DO number: "))
DI72_num = int(input("72V DI number: "))
DO72_num = int(input("72V DO number: "))
DI110_num = int(input("110V DI number: "))
DO110_num = int(input("110V DO number: "))
AI_num = int(input("AI number: "))
AO_num = int(input("AO number: "))

# Create list of PCAs
PCAs = list()

# Create dictionaries of PCA names and numbers of I/O
DI24_dict = dict()
DO24_dict = dict()

DI72_dict = dict()
DO72_dict = dict()

DI110_dict = dict()
DO110_dict = dict()

AI_dict = dict()
AO_dict = dict()

# Get from database
cursor.execute("select * from PC3_PCA")

# Populate lists and dictionaries
for row in cursor.fetchall():
  PCAs.append(row.PCA_Name)

  DI24_dict[row.PCA_Name] = row.DI_24V
  DO24_dict[row.PCA_Name] = row.DO_24V

  DI72_dict[row.PCA_Name] = row.DI_72V
  DO72_dict[row.PCA_Name] = row.DO_72V

  DI110_dict[row.PCA_Name] = row.DI_110V
  DO110_dict[row.PCA_Name] = row.DO_110V

  AI_dict[row.PCA_Name] = row.AI
  AO_dict[row.PCA_Name] = row.AO

# Create minimisation problem
prob = LpProblem("PC3", LpMinimize)

# Dictionary to contain variables with type/category and limits
PCA_vars = LpVariable.dicts("PCA", PCAs, 0, None, cat="Integer")

# Objective function to minimise (total number of I/Os)
prob += lpSum([DI24_dict[i] * PCA_vars[i] + DO24_dict[i] * PCA_vars[i] +\
               DI72_dict[i] * PCA_vars[i] + DO72_dict[i] * PCA_vars[i] +\
               DI110_dict[i] * PCA_vars[i] + DO110_dict[i] * PCA_vars[i] +\
               AI_dict[i] * PCA_vars[i] + AO_dict[i] * PCA_vars[i] for i in PCAs])
# prob += lpSum([PCA_vars[i] for i in PCAs])

# Constraints
prob += lpSum([DI24_dict[i] * PCA_vars[i] for i in PCAs]) >= DI24_num
prob += lpSum([DO24_dict[i] * PCA_vars[i] for i in PCAs]) >= DO24_num

prob += lpSum([DI72_dict[i] * PCA_vars[i] for i in PCAs]) >= DI72_num
prob += lpSum([DO72_dict[i] * PCA_vars[i] for i in PCAs]) >= DO72_num

prob += lpSum([DI110_dict[i] * PCA_vars[i] for i in PCAs]) >= DI110_num
prob += lpSum([DO110_dict[i] * PCA_vars[i] for i in PCAs]) >= DO110_num

prob += lpSum([AI_dict[i] * PCA_vars[i] for i in PCAs]) >= AI_num
prob += lpSum([AO_dict[i] * PCA_vars[i] for i in PCAs]) >= AO_num

# Write to .lp file
prob.writeLP("PC3_optim.lp")

# Solve it
prob.solve()

# Print solution status
print("Status: ", LpStatus[prob.status])

numPCAs = 0
for v in prob.variables():
  if v.name != "__dummy":
    print(v.name, " = ", v.varValue)
    numPCAs += v.varValue

# print("Total number of I/Os = ", value(prob.objective))
print("Total number of PCAs = ", numPCAs)