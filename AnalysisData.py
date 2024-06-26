import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
from matplotlib.patches import ConnectionPatch
import numpy as np

def plot_churn_pie(dataset):
    churn_counts = dataset['Churn'].value_counts()
    churn_percentages = churn_counts * 100.0 / len(dataset)
    explode = [0, 0.05]
    churn_percentages.plot.pie(autopct='%.2f%%', explode=explode)
    plt.title('Churn Analysis')
    plt.ylabel('')
    plt.savefig('churn_analysis.png')  # Save the figure
    plt.show()

def plot_gender_histogram(dataset):
    plt.hist(dataset['gender'])
    plt.title('Gender Analysis')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.savefig('gender_histogram.png')  # Save the figure
    plt.show()

def plot_gender_pie(dataset):
    gender_counts = dataset['gender'].value_counts()
    gender_percentages = gender_counts * 100.0 / len(dataset)
    explode = [0, 0.03]
    gender_percentages.plot.pie(autopct='%.2f%%', explode=explode)
    plt.title('Gender Analysis')
    plt.ylabel('')
    plt.savefig('gender_pie.png')  # Save the figure
    plt.show()

def plot_monthly_total_charges(dataset):
    sea.scatterplot(x='MonthlyCharges', y='TotalCharges', data=dataset, hue="Churn")
    plt.xlabel('Monthly Charges')
    plt.ylabel('Total Charges')
    plt.title('Relationship between MonthlyCharges, TotalCharges, and Churn')
    plt.savefig('monthly_total_charges.png')  # Save the figure
    plt.show()

def plot_contract_churn_relationship(dataset):
    sea.countplot(x='Contract', hue='Churn', data=dataset)
    plt.title('Contract vs Churn')
    plt.xlabel('Contract')
    plt.ylabel('Number of Customers')
    plt.savefig('contract_churn_relationship.png')  # Save the figure
    plt.show()

def plot_online_security_analysis(dataset):
    # Your existing code here
    plt.savefig('online_security_analysis.png')  # Save the figure
    plt.show()

def plot_services_pie(dataset):
    services = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
    service_counts = dataset[services].apply(pd.value_counts)
    service_counts.plot(kind='pie', subplots=True, figsize=(20, 15), layout=(3, 3), autopct='%.1f%%', colors=['orange', 'purple', 'gray', 'lightblue'])
    plt.savefig('services_pie.png')  # Save the figure
    plt.show()
