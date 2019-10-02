import pyodbc
from pulp import *
import string

def IOconfigure(DI24_num, ISODI24_num, DO24_num, DI72_num, ISODI72_num, DO72_num, DI110_num, ISODI110_num, DO110_num, AI_num, ISOAI_num, AO_num):
  conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\williamr\OneDrive - OEM TECHNOLOGY SOLUTIONS PTY LTD\Systems\PC3Configurator\PC3Config.accdb;')
  cursor = conn.cursor()

  # Create list of PCAs
  PCAs = list()

  # Create dictionaries of PCA names and numbers of I/O
  DI24_dict = dict()
  ISODI24_dict = dict()
  DO24_dict = dict()

  DI72_dict = dict()
  ISODI72_dict = dict()
  DO72_dict = dict()

  DI110_dict = dict()
  ISODI110_dict = dict()
  DO110_dict = dict()

  AI_dict = dict()
  ISOAI_dict = dict()
  AO_dict = dict()

  # Get non-isolated from database
  cursor.execute("select * from PC3_IO")

  # Populate lists and dictionaries
  for row in cursor.fetchall():
    PCAs.append(row.PCA_Name)

    DO24_dict[row.PCA_Name] = row.DO_24V

    DO72_dict[row.PCA_Name] = row.DO_72V

    DO110_dict[row.PCA_Name] = row.DO_110V

    AO_dict[row.PCA_Name] = row.AO

    if row.Isolated is True:
      DI24_dict[row.PCA_Name] = 0
      ISODI24_dict[row.PCA_Name] = row.DI_24V

      DI72_dict[row.PCA_Name] = 0
      ISODI72_dict[row.PCA_Name] = row.DI_72V

      DI110_dict[row.PCA_Name] = 0
      ISODI110_dict[row.PCA_Name] = row.DI_110V

      AI_dict[row.PCA_Name] = 0
      ISOAI_dict[row.PCA_Name] = row.AI

    else:
      DI24_dict[row.PCA_Name] = row.DI_24V
      ISODI24_dict[row.PCA_Name] = 0

      DI72_dict[row.PCA_Name] = row.DI_72V
      ISODI72_dict[row.PCA_Name] = 0

      DI110_dict[row.PCA_Name] = row.DI_110V
      ISODI110_dict[row.PCA_Name] = 0

      AI_dict[row.PCA_Name] = row.AI
      ISOAI_dict[row.PCA_Name] = 0


  for row in cursor.fetchall():
    PCAs.append(row.PCA_Name)


  # Create minimisation problem
  prob = LpProblem("PC3", LpMinimize)

  # Dictionary to contain variables with type/category and limits
  PCA_vars = LpVariable.dicts("PCA", PCAs, 0, None, cat="Integer")

  # Objective function to minimise (total number of I/Os)
  prob += lpSum([DI24_dict[i] * PCA_vars[i] +\
                 DO24_dict[i] * PCA_vars[i] +\

                 DI72_dict[i] * PCA_vars[i] +\
                 DO72_dict[i] * PCA_vars[i] +\

                 DI110_dict[i] * PCA_vars[i] +\
                 DO110_dict[i] * PCA_vars[i] +\

                 AI_dict[i] * PCA_vars[i] +\
                 AO_dict[i] * PCA_vars[i] +\

                 ISODI24_dict[i] * PCA_vars[i] +\
                 ISODI72_dict[i] * PCA_vars[i] +\
                 ISODI110_dict[i] * PCA_vars[i] +\
                 ISOAI_dict[i] * PCA_vars[i] for i in PCAs])
  # prob += lpSum([PCA_vars[i] for i in PCAs])

  # Constraints
  prob += lpSum([DI24_dict[i] * PCA_vars[i] for i in PCAs]) >= DI24_num
  prob += lpSum([ISODI24_dict[i] * PCA_vars[i] for i in PCAs]) >= ISODI24_num
  prob += lpSum([DO24_dict[i] * PCA_vars[i] for i in PCAs]) >= DO24_num

  prob += lpSum([DI72_dict[i] * PCA_vars[i] for i in PCAs]) >= DI72_num
  prob += lpSum([ISODI72_dict[i] * PCA_vars[i] for i in PCAs]) >= ISODI72_num
  prob += lpSum([DO72_dict[i] * PCA_vars[i] for i in PCAs]) >= DO72_num

  prob += lpSum([DI110_dict[i] * PCA_vars[i] for i in PCAs]) >= DI110_num
  prob += lpSum([ISODI110_dict[i] * PCA_vars[i] for i in PCAs]) >= ISODI110_num
  prob += lpSum([DO110_dict[i] * PCA_vars[i] for i in PCAs]) >= DO110_num

  prob += lpSum([AI_dict[i] * PCA_vars[i] for i in PCAs]) >= AI_num
  prob += lpSum([ISOAI_dict[i] * PCA_vars[i] for i in PCAs]) >= ISOAI_num
  prob += lpSum([AO_dict[i] * PCA_vars[i] for i in PCAs]) >= AO_num

  # Write to .lp file
  prob.writeLP("PC3_optim.lp")

  # Solve it
  prob.solve()

  # Store the output
  PCA_output = dict()
  numPCAs = 0
  finalIO = dict()

  # Print solution status
  labeltext = str()
  if LpStatus[prob.status] == "Optimal":
    for v in prob.variables():
      if v.name != "__dummy" and v.varValue != 0:
        PCA_output[v.name[4:]] = v.varValue
        # print(v.name, " = ", v.varValue)
        numPCAs += v.varValue

    finalIO["24V DI"] = 0
    finalIO["24V Isolated DI"] = 0
    finalIO["24V DO"] = 0

    finalIO["72V DI"] = 0
    finalIO["72V Isolated DI"] = 0
    finalIO["72V DO"] = 0

    finalIO["110V DI"] = 0
    finalIO["110V Isolated DI"] = 0
    finalIO["110V DO"] = 0

    finalIO["AI"] = 0
    finalIO["Isolated AI"] = 0
    finalIO["AO"] = 0

    for key in PCA_output:

      finalIO["24V DI"] += DI24_dict[key] * PCA_output[key]
      finalIO["24V Isolated DI"] += ISODI24_dict[key] * PCA_output[key]
      finalIO["24V DO"] += DO24_dict[key] * PCA_output[key]

      finalIO["72V DI"] += DI72_dict[key] * PCA_output[key]
      finalIO["72V Isolated DI"] += ISODI72_dict[key] * PCA_output[key]
      finalIO["72V DO"] += DO72_dict[key] * PCA_output[key]

      finalIO["110V DI"] += DI110_dict[key] * PCA_output[key]
      finalIO["110V Isolated DI"] += ISODI110_dict[key] * PCA_output[key]
      finalIO["110V DO"] += DO110_dict[key] * PCA_output[key]

      finalIO["AI"] += AI_dict[key] * PCA_output[key]
      finalIO["Isolated AI"] += ISOAI_dict[key] * PCA_output[key]
      finalIO["AO"] += AO_dict[key] * PCA_output[key]

    labeltext += "PCA list: \n"
    for key in PCA_output:
      labeltext += (key + ": " + str(PCA_output[key]) + "\n")
    labeltext += ("Total number of PCAs: " + str(numPCAs) + "\n\n")
    labeltext += "I/O breakdown of controller: \n"
    for key in finalIO:
      if finalIO[key] != 0:
        labeltext += (key + ": " + str(finalIO[key]) + "\n")
  else:
    labeltext += ("Optimal controller not found, please adjust parameters")
    # return True, PCA_output, numPCAs, finalIO
  return labeltext
    # print("Total number of I/Os = ", value(prob.objective))
    # print("Total number of PCAs = ", numPCAs)
    # input()

  # else:
  #   return False, PCA_output, numPCAs, finalIO
    # print("Solution not found, missing PCA possible cause. Return to the idiot who made this to rectify")
    # input()

def populateComms():
  comms = list()
  conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\williamr\OneDrive - OEM TECHNOLOGY SOLUTIONS PTY LTD\Systems\PC3Configurator\PC3Config.accdb;')
  cursor = conn.cursor()

  for row in cursor.columns(table='PC3_COM'):
    comms.append(row.column_name)

  return comms[1:]

def getComms(commType):
  comms = list()

  conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\williamr\OneDrive - OEM TECHNOLOGY SOLUTIONS PTY LTD\Systems\PC3Configurator\PC3Config.accdb;')
  cursor = conn.cursor()
  # If column has number as first digit, it must be wrapped in quotes else SQL will fail to search
  if commType[0].isdigit():
    commType = '"' + commType + '"'
  # "=-1" because boolean true in SQL is -1
  searchString = "select PCA_Name from PC3_COM where " + commType + "=-1"
  cursor.execute(searchString)

  for row in cursor.fetchall():
    comms.append(row.PCA_Name)
  return comms


if __name__ == '__main__':
  IOconfigure(DI24, DO24, DI72, DO72, DI110, DO110, AI, AO)