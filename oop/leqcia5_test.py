# სავარჯიშო 1
import sqlite3

def connect_db(db_name):
    return sqlite3.connect(db_name)



def count_by_gender_surv(gender, survived):
    cursor.execute("SELECT count(*) FROM Passengers WHERE sex =? AND Survived =?", (gender,survived))
    return (cursor.fetchone()[0])

def percent():
    pass

male_surv_not = count_by_gender_surv('male',0)

import matplotlib.pyplot as plt
import numpy as np

conn = connect_db("Titanic.sqlite")
cursor = conn.cursor()

total = 891
print('გემზე იმყოფებოდა {} ადამიანი'.format(total))
female_surv = count_by_gender_surv('female',1)
female_surv_not = count_by_gender_surv('female',0)
male_surv = count_by_gender_surv('male',1)




labels = ['გადარჩა', 'ვერ გადარჩა']
men_means = [male_surv, male_surv_not]
women_means = [female_surv, female_surv_not]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()

#
# print('ქალების % რაოდენობა (გადარჩა): {:.0f}%'.format())
# print('ქალების % რაოდენობა (ვერ გადარჩა): {:.0f}%'.format())
# print('კაცების % რაოდენობა (გადარჩა): {:.0f}%'.format())
# print('კაცების % რაოდენობა (ვერ გადარჩა): {:.0f}%'.format())


# სავარჯიშო 2 (pie chart)


# სავარჯიში 3 (Histogram)




# სავარჯიშო 4 (შობადობის სტატისტიკა საქართველოში)
# x_points = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
# y1_total = [52_442, 56_568, 55_230, 51_565, 49_969, 49_657, 60_635, 59_249, 56_569, 53_293, 51_138, 48_296]
#
# y2_boys = [27698, 29660, 28787, 26942, 26138, 25747, 31325,  30902, 28887, 27658, 26538, 24600]
# y3_girls = [24744, 26908, 26443, 24623, 23831, 23910, 29310,  28347, 27682, 25635, 24600, 23267]

