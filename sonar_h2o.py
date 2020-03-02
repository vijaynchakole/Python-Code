
import h2o
h2o.init()

df = h2o.import_file("C:/Users/hp/PycharmProjects/Project/Sonar.csv")

print(df)

print(df.col_names)
df['Class'] = df['Class'].asfactor()

print(type(df['Class']))
col_class = df['Class']
print(df['Class'].levels())

print(col_class)

#df[col_class == 'R'] = 1

print(df['Class'])

help(h2o.estimators.glm.H2OGeneralizedLinearEstimator)