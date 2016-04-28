# Import Block
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import time


def main():
  data = pd.read_csv("../train_raw.csv")
  pixels = data.iloc[:,0:data.shape[1]-1].as_matrix()
  targets = data.iloc[:,data.shape[1]-1]

  forest = RandomForestClassifier(n_estimators=150, oob_score=True)
  forest.fit(pixels,targets)

  pickle.dump( pixels, open("pixels.p", "w") )
  pickle.dump( forest, open("forest.p", "w") )

if __name__ == "__main__": main()