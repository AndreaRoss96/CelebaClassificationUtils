import pandas as pd



def func(s):
  return s.replace("img_align_celeba\\", "")

df = pd.read_csv("D:\\Uni\\deep\\dataframe\\mergeOrientation.csv")

df.Filename = df["Filename"].apply(func)
df.drop(["Predictions_1","Confidence_1","Predictions_2","Confidence_2"],
                        axis = 1,
                        inplace=True)

print(df)
df.to_csv("D:\\Uni\\deep\\CelebaClassificationUtils\\mergeOrientation.csv", encoding='utf-8', index=False)

