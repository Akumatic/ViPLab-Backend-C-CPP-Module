import os, sys, c, dataObjects

# load exercise and solution data in json format
cur_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
exercise_data_path = os.path.join(cur_dir, "examples", "exercise.json")
solution_data_path = os.path.join(cur_dir, "examples", "solution.json")
exercise_data = dataObjects.readJson(exercise_data_path)
solution_data = dataObjects.readJson(solution_data_path)

# create exercise and solution objects
exercise = dataObjects.Exercise(exercise_data)
solution = dataObjects.Solution(solution_data, exercise)

# optional configuration, e.g. for timeout during running
cfg = {"timelimitInSeconds": 15}

# create C module object, process data and store result data in json format
module = c.C(solution, cfg)
module.processData()
result = module.result.createJson()

print(result)