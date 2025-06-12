# %% [markdown]
# # Heart Disease Predictor

# %% [markdown]
# * The Heart Disease Predictor Predicts The Possibilty Of The Heart Disease For A Person Based On Their Vitals Entered, The Model Makes It's Prediction Based On Heart Disease Dataset On Which It Is Trained

# %%
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df=pd.read_csv("heart.csv")

# %% [markdown]
# * Understanding The Dataset

# %%
df.info()
df.describe()

# %% [markdown]
# * Knowing How Many Different Values Does Each Categorical Column Have

# %%
print(df["Sex"].unique())
print(df["ChestPainType"].unique())
print(df["RestingECG"].unique())
print(df["ExerciseAngina"].unique())
print(df["ST_Slope"].unique())

# %% [markdown]
# * Dropping Null Rows If Any

# %%
df=df[["Age","Sex","ChestPainType","RestingBP","Cholesterol","FastingBS","RestingECG","MaxHR","ExerciseAngina","Oldpeak","ST_Slope","HeartDisease"]].dropna()

# %% [markdown]
# * Encoding The Categorical Values:

# %%
df["Sex"]=df["Sex"].map({"M":0,"F":1})
df["ChestPainType"]=df["ChestPainType"].map({"ATA":0,"NAP":1,"ASY":2,"TA":3})
df["RestingECG"]=df["RestingECG"].map({"Normal":0,"ST":1,"LVH":2})
df["ExerciseAngina"]=df["ExerciseAngina"].map({"N":0,"Y":1})
df["ST_Slope"]=df["ST_Slope"].map({"Up":0,"Flat":1,"Down":2})

# %% [markdown]
# * Dividing Dataset Into Data And Its Result

# %%
#Data
x=df[["Age","Sex","ChestPainType","RestingBP","Cholesterol","FastingBS","RestingECG","MaxHR","ExerciseAngina","Oldpeak","ST_Slope"]]

#Result
y=df["HeartDisease"]

# %%
model=DecisionTreeClassifier()
model.fit(x,y)

print(".....Heart Disease Predictor.....")
age=int(input("Enter Your Age: "))
sex=input("Enter Your Sex: ")
CPT=input("Describe Your Chest Pain Type ATA/NAP/ASY/TA: ")
RBP=int(input("Enter Your Resting Blood Pressure: "))
CHL=int(input("Enter Your Cholestrol Level: "))
FBS=int(input("Enter Your Fasting Blood Sugar: "))
RECG=input("Enter Your Resting ECG Normal/ST/LVH: ")
MHR=int(input("Enter Your Maximum Heart Rate: "))
EA=input("Does Your Chest Pains While Exercising Yes/No: ")
OP=float(input("Enter Your Old Peak: "))
SS=input("Enter Your ST Slope Up/Flat/Down: ")

# Encoding Categorical Values
sex=0 if sex=="male" else 1

if CPT=="ATA":
    CPT=0
elif CPT=="NAP":
    CPT=1
elif CPT=="ASY":
    CPT=2
else:
    CPT=3

if RECG=="Normal":
    RECG=0
elif RECG=="ST":
    RECG=1
else:
    RECG=2

if EA=="Yes":
    EA=1
else:
    EA=0

if SS=="Up":
    SS=0
elif SS=="Flat":
    SS=1
else:
    SS=2

UserData=pd.DataFrame([[age,sex,CPT,RBP,CHL,FBS,RECG,MHR,EA,OP,SS]],columns=[["Age","Sex","ChestPainType","RestingBP","Cholesterol","FastingBS","RestingECG","MaxHR","ExerciseAngina","Oldpeak","ST_Slope"]])

prediction=model.predict(UserData)

if prediction==0:
    print("You Don't Have Any Heart Disease.")
else:
    print("You Have A Heart Disease!!")


# %%



