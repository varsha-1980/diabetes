import streamlit as st
import seaborn as sns
import pandas as pd
from PIL import Image
import pickle
st.title("DIABETES CHECKUP")
img = Image.open("C:\\Users\\DELL\\Downloads\\diabetes1.jpg")
st.image(img,width=500,caption="diabetes")
st.write("diabetes is one of the major health issue")
st.markdown("""people need to eat less sweets to get rid from
            the dangeorus disease called diabetes""")
df=pd.read_csv("C:\\Users\\DELL\\Downloads\\diabetes.csv")
st.write(df.head())
p = st.number_input("enter the pregnancy:")
g = st.number_input("enter the glucose:")
bp= st.number_input("enter the bloodpressure:")
sti= st.number_input("enter the skinthickness:")
ins = st.number_input("enter the insulin:")
bmi= st.number_input("enter the bmi:")
dpf = st.number_input("enter the diabetespedigreefunction:")
a= st.number_input("enter the age:")
output=[]
lst=[p,g,bp,sti,ins,bmi,dpf,a]
output.append(lst)
with open("C:\\Users\\DELL\\Downloads\\model1","rb")as f:
    model=pickle.load(f)
button=st.button("predict")
if button:
    outcome=model.predict(output)
    st.write(outcome)
    st.write()
    if(outcome==1):
        st.write("diabetic")
    else:
        st.write("non-diabetic")

if st.checkbox("correlation"):
    st.write(sns.heatmap(df.corr()))
    st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)
    









