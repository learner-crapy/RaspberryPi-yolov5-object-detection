from roboflow import Roboflow
rf = Roboflow(api_key="RNCSid3MTAbTkr5p6y6c")
project = rf.workspace("0lu0da0ze0-gmail-com").project("sleep_leaving")
dataset = project.version(1).download("yolov5")