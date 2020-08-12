import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly

#calculate gpa for a course based on the number of A's, B's, etc...
#input: the row of dataframe, and a keylist with the possible grades
#returns the gpa
def CalculateGPA(course, grades):
    students = 0 #used to track number of students
    grade_gpa = 4.0 #traversing from A+ to F we start with our gpa at 4 and decrease it by 0.33 as we continue
    gpa = 0 #used to store final gpa
    for grade in grades:
        gpa += grade_gpa * course[grade]
        #we don't decrease gpa for A+ to A
        if(grade != 'A+'):
            grade_gpa -= 0.33
        students += course[grade]
    return gpa / students

#condense duplicates of Subjects into one gpa for that Subject
#input: courses, and subjects for the courses to condense
#returns: dataframe of unique subjects with avg gpa
def CondenseSubjects(courses, subjects):
    courseList = [] #stores each unique course to create dataframe at end of function
    for subject in subjects:
        df_temp = courses.loc[courses['Subject'] == subject]
        if(df_temp.size <= 0):
            continue
        avg = df_temp['GPA'].mean()
        df_temp = df_temp.iloc[0]
        df_temp['GPA'] = round(avg,2)
        #df_master.append(df_temp, ignore_index=True)
        courseList.append(df_temp)
    df_master = pd.DataFrame(courseList)
    return df_master

# Yield successive n-sized 
# chunks from l. 
def divide_chunks(l, n): 
    tmp = []
    # looping till length l 
    for i in range(0, len(l), n):  
        tmp.append(list(l[i:i+n]))
        
    return(tmp)

#find the closest square to current number of courses and number of padding needed
#input: number of courses
#output: size of chunks to break into and padding needed

def isPerfect(N): 
    if (sqrt(N) - floor(sqrt(N)) != 0): 
        return False
    return True
  
# Function to find the closest perfect square  
# taking minimum steps to reach from a number  
def getClosestPerfectSquare(N): 
    if (isPerfect(N)):  
        print(N, "0")  
        return
  
    # Variables to store first perfect  
    # square number above and below N  
    aboveN = -1
    belowN = -1
    n1 = 0
  
    # Finding first perfect square  
    # number greater than N  
    n1 = N + 1
    while (True): 
        if (isPerfect(n1)): 
            aboveN = n1  
            break
        else: 
            n1 += 1
  
    # Finding first perfect square  
    # number less than N  
    n1 = N - 1
    while (True):  
        if (isPerfect(n1)):  
            belowN = n1  
            break
        else: 
            n1 -= 1
              
    # Variables to store the differences  
    diff1 = aboveN - N  
    diff2 = N - belowN  
  
    if (diff1 > diff2): 
        return (belowN, diff2)  
    else: 
        return(aboveN, diff1) 

df = pd.read_csv('datasets/gpa/uiuc-gpa-dataset.csv')
grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
subjects = df['Subject'].unique()


gpaList = [] #list of all gpas to add to dataframe
for i in range(len(df)):
    gpaList.append(CalculateGPA(df.iloc[i], grades))
df['GPA'] = gpaList
df_New = df.copy()
df_New = df_New.loc[df_New['Year'] == 2019] #get all 2019 data
subjects = df_New['Subject'].unique()
df = CondenseSubjects(df, subjects) #obtain dataframe for all semesters
df_New = CondenseSubjects(df_New, subjects) #get all 2019 data condensed
df = df.sort_values(by='Subject', ascending=True) #sort by subject number (low to high)

subjects = df_New['Subject'].tolist()
gpa = df['GPA'].tolist()
gpa2 = df_New['GPA'].tolist()
for i in range(3):
    subjects.append('')
    gpa.append(2)
    gpa2.append(2)

# Display course number and gpa on hover
hover=[]
hover2=[]
for i in range(len(gpa)):
    hover.append('Subject: ' + str(subjects[i]) + '<br>' + 'GPA: ' + str(gpa[i]))
    hover2.append('Subject: ' + str(subjects[i]) + '<br>' + 'GPA: ' + str(gpa2[i]))

#split lists into nice format
subjects = divide_chunks(subjects, 11)
gpa = list(divide_chunks(gpa, 11))
gpa2 = list(divide_chunks(gpa2,11))
hover = divide_chunks(hover, 11)
hover2 = divide_chunks(hover2, 11)

#Invert matrices
subjects = subjects[::-1]
gpa = gpa[::-1]
gpa2 = gpa2[::-1]
hover = hover[::-1]
hover2 = hover2[::-1]


# Set Colorscale
colorscale=[[0.0, 'rgb(255,255,255)'], [0.2, 'rgb(235, 72, 63)'],
            [0.4, 'rgb(235, 123, 89)'], [0.6, 'rgb(240, 166, 110)'],
            [0.8, 'rgb(240, 207, 110)'],[1.0, 'rgb(240, 240, 110)']]

#graph heatmap
fig = ff.create_annotated_heatmap(z=gpa, annotation_text=subjects, showscale=True,
    colorscale=colorscale, text=hover, hoverinfo='text')

fig.update_layout(title_text='Subject GPA Heatmap')

#add dropdown
fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list(
            [dict(label = '10 Year Avg',
                  method = 'update',
                  args = [{'z':[gpa], 'text':[hover]},
                        {'visible': [True, False]},
                          {'title': '10 Year',
                           'showlegend':True}]),
             dict(label = '2019',
                  method = 'update',
                  args = [{'z':[gpa2] ,'text':[hover2]},
                          {'visible': [False, True]}, # the index of True aligns with the indices of plot traces
                          {'title': '2019',
                           'showlegend':True}])
                           ])
        )
    ])

fig.show()

