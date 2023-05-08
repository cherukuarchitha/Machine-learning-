import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
def show_explore_page():
    st.title("Telco Customer Churn Dataset Exploration")

    st.write(
        """
    ### Visualization using Histogram of Customer Information (each feature individually) vs the Target variable:
    """)
    st.image("pic1.png",width=600)
    st.write("""The number of SeniorCitizen customers is pretty low, And we can observe a near 40% churn of
SeniorCitizen customers. It accounts for a total of 476 customers out of 1142 Senior Citizen customers.
Customers who are housing with a Partner retained more as compared to those not living with a
Partner. And retention is low for the customers that don't have Dependents with them.""")
    st.write("### Visualization using Histogram of Services Subscribed by the Customer vs the Target variable")
    st.image("pic2.png",width=600)
    st.write("""As the services are the direct form of experience to the customer their importance can be seen in the
histogram visualization of the data above very well. A high number of customers have switched their
service provider when it comes to poor services with the above mentioned features. This is a very
important aspect and business strategies should be implemented in this direction.""")
    st.write("### Visualization of Histogram of Payment Information of the Customer vs the Target variable")
    st.image("pic 3.png",width=600)
    st.write("""Customer retention for a Monthly based Contract is quite low. This is due to new customers just trying
the trial period.
The internet service, streaming service and phone service were not consistent.
PaperlessBilling displays a low number of customers retaining. This could be due to payment issues or
receipt issues. Company needs to either drop the Electronic check method or make it user-friendly""")
    st.write("### Visualizations between the Monthly Charges , total charges and the target variable")
    st.image("pic 4.png", width=600)
    st.image("pic6.png", width=600)

    st.write("Clients with higher MonthlyCharges are less likely to retain the service.It seems that there is lower churn when the total charges are higher.")
    
    st.write("### Visualizations between the tenure and the target variable")
    st.image("pic5.png", width=600)
    st.write("Clients who opt for tenure 0 to 20 are more likely to churn and above 20 the churn rate is low.")
    st.write("""### Measures for Increasing Customer Retention and Revenue:

To increase the revenue and also minimize the customer churn following of the implementations can be followed by observing the above model’s evaluation metrics.

Senior citizens, people living with a partner, and people living alone should be targeted as clients.
The number of Senior Citizen consumers is small, but their monthly charge limit is higher than that of other customers. Thus, SeniorCitizen clients are willing to spend top price for exceptional service. Clients with a Partner and customers living alone prefer services with MonthlyCharges under 65.

In order to build a robust customer base, a telecommunications company must provide an accessible and reasonable entry point for their services. For the first six months, it must focus heavily on OnlineSecurity, OnlineBackup, DeviceProtection, and TechSupport, as this is the most critical and unpredictable period for clients. They must reduce the churn tenure of 40 - 50 months for these services.

Once they have established a robust pipeline of customer support services, they must promote the use of MultipleLines and Fiber Optic cables for PhoneService and InternetService, respectively. However, the beginning point of 75+ in MonthlyCharges is a considerable barrier for these two services.
As a result, they must construct combinations of PhoneService and InternetService options with average MonthlyCharges in the range of 100 - 120:
No multiple lines, multiple lines of optical fiber along with DSL
will enhance a user's average income because it eliminates the option of selecting a combination of 
No MultipleLines along with DSL, which has a mean MonthlyCharge of 60 - 70.

It's important to lower the cost of streaming TV and movies while also lowering turnover. All customer types should be catered to in the content of these services. Following this, a simple and hassle-free payment method is required.



Customers become particularly sensitive of their MonthlyCharges whenever the MonthlyCharges for any single service reach the 70 threshold. The standard of service must be maintained.

Both the LightGBM and the XGBoost algorithms are working well, but are predicting based upon different dimensions. It is also worth noting that the predictions are skewed by the imbalance in the dataset but we have used SMOTE technique to balance the data and performed the models again. We have obtained better results after this implementation.""")