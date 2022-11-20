import os
import dill
from config import basedir
import pandas as pd
import numpy as np
import __main__
__main__.pd = pd
__main__.np = np

def load_model(model_path):
	with open(model_path, 'rb') as f:
		model = dill.load(f)

	return model

heart_failure_path = os.path.join(basedir, 'models', 'heart_failure.dill')
heart_failure = load_model(heart_failure_path)


# if __name__ == '__main__':
# 	heart_failure_path = os.path.join(os.getcwd(), 'models', 'heart_failure.dill')
# 	heart_failure = load_model(heart_failure_path)

# 	age = 27
# 	sex = 'F'
# 	chest_pain = 'ASY'
# 	maxHR = 90
# 	restingBP = 150
# 	exerciseAngina ='N'

# 	X = pd.DataFrame(
# 		[[age, sex, chest_pain, maxHR, restingBP, exerciseAngina]],
#         columns=['Age', 'Sex', 'ChestPainType', 'MaxHR', 'RestingBP', 'ExerciseAngina']
# 	)
# 	print(heart_failure.predict_proba(X))
