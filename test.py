import dbUtils

print('looking for the set name')

x = dbutils.jobs.taskValues.get(taskKey = "fetchRasterData", key = "name")

print(x)