import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/tickets.csv")

plt.figure(figsize=(10, 6))
data['category'].value_counts().plot(kind='bar')
plt.title('Ticket Categories')
plt.savefig('reports/ticket_report.png')
