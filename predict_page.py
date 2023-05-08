import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

class_loaded = data["model"]
le_partner=data["le_partner"]
le_dependents = data["le_dependents"]
le_onlinesecurity = data["le_onlinesecurity"]
le_onlinebackup = data["le_onlinebackup"]
le_deviceprotection = data["le_deviceprotection"]
le_techsupport = data["le_techsupport"]
le_contract = data["le_contract"]
le_paperbilling = data["le_paperbilling"]
le_paymentmethod = data["le_paymentmethod"]
#le_monthlycharges= data["le_monthlycharges"]

def show_predict_page():
    
    st.header("Telecom Customer Retention Classification")
    #st.markdown(page_bg_img, unsafe_allow_html=True)
    st.image("https://cdn-bijap.nitrocdn.com/AuMaQmessFRMSicXmZsEecJFLEquAyoT/assets/static/optimized/rev-4b9e7e7/wp-content/uploads/2021/11/telco-trends_1200x375.svg", width=700)
    

    st.write("""### We need some information for prediction""")
    senior=(0,1)
    partner = ("Yes","No")
    dependents=("Yes","No")
    onlinesecurity=("Yes","No", "No internet service")
    onlinebackup=("Yes","No", "No internet service")
    deviceprotection=("Yes","No", "No internet service")
    techsupport=("Yes","No", "No internet service")
    contract=("Month-to-month", "One year", "Two year")
    paperless=("Yes", "No")
    payment=("Electronic check","Mailed check", "Bank transfer (automatic)", "Credit card (automatic)")

    col1, col2, col3 = st.columns(3)

    with col1:
        senior1=st.selectbox("Senior Citizen", senior )
        partner1= st.selectbox("Partner", partner )
        dependents1= st.selectbox("Dependents", dependents )
        onlinesecurity1= st.selectbox("onlinesecurity", onlinesecurity )
        onlinebackup1= st.selectbox('onlinebackup', onlinebackup )
        

    with col2:
        deviceprotection1= st.selectbox("deviceprotection", deviceprotection )
        techsupport1= st.selectbox("techsupport",techsupport )
        contract1= st.selectbox("contract", contract )
        paperless1= st.selectbox("paperless", paperless )
        payment1= st.selectbox("Payment method", payment )

    with col3:
        tenure=st.number_input("Tenure", 0.0, 100.0)
        monthly_charges=st.number_input("monthly charges", 0.0, 200.0)
        total_charges=st.number_input("Total charges", 0.0, 10000.0)
    tenure_min=0
    tenure_max=72
    month_min=18.25
    month_max=118.75
    tot_min=18.8
    tot_max=8684.80
    
    

    

    ok = st.button("Predict")
    if ok:
        X = np.array([[senior1,partner1,dependents1,tenure, onlinesecurity1,onlinebackup1,deviceprotection1,
        techsupport1,contract1,
        paperless1,payment1,monthly_charges, total_charges]])
        X[:, 1] = le_partner.transform(X[:,1])
        X[:, 2] = le_dependents.transform(X[:,2])
        X[:, 3] =np.round_(((float(X[:,3])-tenure_min)/(tenure_max-tenure_min)),decimals=2)
        X[:, 4] = le_onlinesecurity.transform(X[:,4])
        X[:, 5] = le_onlinebackup.transform(X[:,5])
        X[:, 6] = le_deviceprotection.transform(X[:,6])
        X[:, 7] = le_techsupport.transform(X[:,7])
        X[:, 8] = le_contract.transform(X[:,8])
        X[:, 9] = le_paperbilling.transform(X[:,9])
        X[:, 10] = le_paymentmethod.transform(X[:,10])
        X[:, 11] =np.round_( ((float(X[:,11])-month_min)/(month_max-month_min)),decimals=2)
        X[:, 12] = np.round_(((float(X[:,12])-tot_min)/(tot_max-tot_min)),decimals=2)
        X = X.astype(float)

        churn = class_loaded.predict(X)
        if churn==1:
            st.subheader(f"There is a chance that the customer will leave the company")
            st.image("churn1.png", width=250)
            
        else:
            st.subheader(f"The customer wont leave the company")
            st.image("wont.png", width=250)
            
