
import matplotlib.pyplot as plt

path = r"S:\AOU\ML course\w6\smoke_detection_iot.csv"
data = pd.read_csv(path)

Yes_Fire = data[data['Fire_Alarm'] == 1]
No_Fire = data[data['Fire_Alarm'] == 0]


num = [len(Yes_Fire), len(No_Fire)]

plt.pie(num,autopct='%1.1f%%',startangle=192,wedgeprops={'edgecolor' :"black"})
plt.legend(['Yes_Fire','No_Fire'],loc='center right', bbox_to_anchor=(1, 0.5, 0.5, 0.5))
plt.title('fire alatm gragh')
plt.show()
