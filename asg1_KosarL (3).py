#!/usr/bin/env python
# coding: utf-8

# In[185]:


'''
Tasks: 
- to read a 5 column csv file 
- summarize the following for each column in a table:
a) max value
b) min value 
c) average 
    note: for a, b, and c, all data within the column has to be numeric - report n/a otherwise
d) standard deviation 
    note: need at least 2 numeric values - report n/a otherwise 
e) mode 
    note: must be calculated for each column. if tie - pick one
f) histogram for each numeric column 

assume: the column names will always be the first row

'''


# In[227]:


# importing csv library to read the input file 
# getting a list of all the columns in the file 

import csv 
import pandas as pd
input_file = input("please enter the file directory: ")

Quizzes = []
Assignments = []
Exercises = []
Projects = []
Total = []

with open (input_file, 'r') as csv_file: #opening the input file in read mode and storing it as csv_file 
    csv_reader = csv.reader(csv_file, delimiter = ',')
    next (csv_reader) #skipping the column headers
    
    course_components = [] # putting each row of input file into a list
    for lines in csv_reader:
        Quizzes.append(lines[0])
        Assignments.append(lines[1])
        Exercises.append(lines[2])
        Projects.append(lines[3])
        Total.append(lines[4])


# In[213]:


# cleaning the lists from non-numeric enteries in each list 

cleaned_quizzes = [x for x in Quizzes if x.isdigit()]
cleaned_assignments = [x for x in Assignments if x.isdigit()]
cleaned_exercises = [x for x in Exercises if x.isdigit()]
cleaned_projects = [x for x in Projects if x.isdigit()]
cleaned_total = [x for x in Total if x.isdigit()]


# casting the enteries in the list to int from str
for i in range(0, len(cleaned_quizzes)):
    cleaned_quizzes[i] = int(cleaned_quizzes[i])
       
for i in range(0, len(cleaned_assignments)):
    cleaned_assignments[i] = int(cleaned_assignments[i])
    
for i in range(0, len(cleaned_exercises)):
    cleaned_exercises[i] = int(cleaned_exercises[i])
    
for i in range(0, len(cleaned_projects)):
    cleaned_projects[i] = int(cleaned_projects[i])
    
for i in range(0, len(cleaned_total)):
    cleaned_total[i] = int(cleaned_total[i])


# In[214]:


# sorting the lists in ascending order 

def selection_sort(L):
    for i in range(len(L)-1):
        initial_index = i # i is the first number on the list (=L) we are using to compare 
        for j in range (i+1, len(L)): # j is the value after i which we are checking to see if smaller or not
            if L[j] < L [initial_index]:
                initial_index = j # if the current index is smaller than the initial index, they get switched 
        L[i], L[initial_index] = L[initial_index], L[i]


# In[215]:


# counting the number of non-numeric values in each original list

columns = [Quizzes, Assignments, Exercises, Projects, Total]
non_numeric_course_components = []
for i in range (len(columns)):
    non_numeric_count = 0 
    for value in columns[i]:
        if not value.isdecimal():
            non_numeric_count += 1
    non_numeric_course_components.append(non_numeric_count) 

non_numeric_quizzes = non_numeric_course_components[0]
non_numeric_assignments = non_numeric_course_components[1]
non_numeric_exercises = non_numeric_course_components[2]    
non_numeric_projects = non_numeric_course_components[3]
non_numeric_total = non_numeric_course_components[4]


# In[216]:


# gives the minimum numeric value in the list, otherwise gives 'n/a'

selection_sort(cleaned_quizzes)
selection_sort(cleaned_assignments)
selection_sort(cleaned_exercises)
selection_sort(cleaned_projects)
selection_sort(cleaned_total)

if non_numeric_quizzes > 0:
    min_quizzes = 'n/a'
else:
    for i in cleaned_quizzes:
        min_quizzes = cleaned_quizzes[0]


        
if non_numeric_assignments > 0:
    min_assignments = 'n/a'
else:
    for i in cleaned_assignments:
        min_assignments = cleaned_assignments[0]
        
        
if non_numeric_exercises > 0:
    min_exercises = 'n/a'
else:
    for i in cleaned_exercises:
        min_exercises = cleaned_exercises[0]
        
        
        
if non_numeric_projects > 0:
    min_projects = 'n/a'
else:
    for i in cleaned_projects:
        min_projects = cleaned_projects[0]
        
        
        
if non_numeric_total > 0:
    min_total = 'n/a'
else:
    for i in cleaned_total:
        min_total = cleaned_total[0]


# In[217]:


# gives the maximum value in the list (if numeric), otherwise gives 'n/a'

selection_sort(cleaned_quizzes)
selection_sort(cleaned_assignments)
selection_sort(cleaned_exercises)
selection_sort(cleaned_projects)
selection_sort(cleaned_total)

if non_numeric_quizzes > 0:
    max_quizzes = 'n/a'
else:
    for i in cleaned_quizzes:
        max_quizzes = cleaned_quizzes[-1]


        
if non_numeric_assignments > 0:
    max_assignments = 'n/a'
else:
    for i in cleaned_assignments:
        max_assignments = cleaned_assignments[-1]
        
        
if non_numeric_exercises > 0:
    max_exercises = 'n/a'
else:
    for i in cleaned_exercises:
        max_exercises = cleaned_exercises[-1]
        
        
        
if non_numeric_projects > 0:
    max_projects = 'n/a'
else:
    for i in cleaned_projects:
        max_projects = cleaned_projects[-1]
        
        
        
if non_numeric_total > 0:
    max_total = 'n/a'
else:
    for i in cleaned_total:
        max_total = cleaned_total[-1]


# In[218]:


# calculating the average of the original list, otherwise gives 'n/a'

if non_numeric_quizzes >0:
    µ_quizzes = 'n/a'
else:
    Sum = 0
    for i in cleaned_quizzes:
        Sum += i 
        i += 1
    µ_quizzes = Sum/len(cleaned_quizzes) 


if non_numeric_assignments >0:
    µ_assignments = 'n/a'
else:
    Sum = 0
    for i in cleaned_assignments:
        Sum += i 
        i += 1
    µ_assignments = Sum/len(cleaned_assignments) 
    
    
if non_numeric_exercises >0:
    µ_exercises = 'n/a'
else:
    Sum = 0
    for i in cleaned_exercises:
        Sum += i 
        i += 1
    µ_exercises = Sum/len(cleaned_exercises) 
    
    
if non_numeric_projects >0:
    µ_projects = 'n/a'
else:
    Sum = 0
    for i in cleaned_projects:
        Sum += i 
        i += 1
    µ_projects = Sum/len(cleaned_projects) 
    
    
if non_numeric_total >0:
    µ_total = 'n/a'
else:
    Sum = 0
    for i in cleaned_total:
        Sum += i 
        i += 1
    µ_total = Sum/len(cleaned_total) 


# In[219]:


# calculating the standard deviation of any list with 2 or more numeric values

if len(Quizzes) - non_numeric_quizzes < 2:
    sd_quizzes = 'n/a'
else:
    Sum = 0
    N = len(cleaned_quizzes)
    µ = sum(cleaned_quizzes)/N
    for i in range (0, N):
        Sum += (cleaned_quizzes[i] - µ)*(cleaned_quizzes[i] - µ) 
        
    ratio = Sum/N
    sd_quizzes = ratio ** 0.5



if len(Assignments) - non_numeric_assignments < 2:
    sd_assignments = 'n/a'
else:
    Sum = 0
    N = len(cleaned_assignments)
    µ = sum(cleaned_assignments)/N
    for i in range (0, N):
        Sum += (cleaned_assignments[i] - µ)*(cleaned_assignments[i] - µ) 
        
    ratio = Sum/N
    sd_assignments = ratio ** 0.5
    
    
    
if len(Exercises) - non_numeric_exercises < 2:
    sd_exercises = 'n/a'
else:
    Sum = 0
    N = len(cleaned_exercises)
    µ = sum(cleaned_exercises)/N
    for i in range (0, N):
        Sum += (cleaned_exercises[i] - µ)*(cleaned_exercises[i] - µ) 
        
    ratio = Sum/N
    sd_exercises = ratio ** 0.5
    
    
if len(Projects) - non_numeric_projects < 2:
    sd_projects = 'n/a'
else:
    Sum = 0
    N = len(cleaned_projects)
    µ = sum(cleaned_projects)/N
    for i in range (0, N):
        Sum += (cleaned_projects[i] - µ)*(cleaned_projects[i] - µ) 
        
    ratio = Sum/N
    sd_projects = ratio ** 0.5
    
if len(Total) - non_numeric_total < 2:
    sd_total = 'n/a'
else:
    Sum = 0
    N = len(cleaned_total)
    µ = sum(cleaned_total)/N
    for i in range (0, N):
        Sum += (cleaned_total[i] - µ)*(cleaned_total[i] - µ) 
        
    ratio = Sum/N
    sd_total = ratio ** 0.5


# In[220]:


# finding the most common value (mode) of each list 

def mode_value (L):
    return max(set(L), key = L.count)

mode_quizzes = mode_value(cleaned_quizzes)
mode_assignments = mode_value(cleaned_assignments)
mode_exercises = mode_value(cleaned_exercises)
mode_projects = mode_value(cleaned_projects)
mode_total = mode_value(cleaned_total)


# In[222]:


# summarizing the data in table format 

import pandas as pd

summary_data = {"Computated values": ['minimum score', 'maximum score', 'mode', 'average score', 'standard deviation'],
       "Quizz": [min_quizzes, max_quizzes, mode_quizzes, µ_quizzes, sd_quizzes], 
       "Assignment": [min_assignments, max_assignments, mode_assignments, µ_assignments, sd_assignments], 
       "Exercises": [min_exercises, max_exercises, mode_exercises, µ_exercises, sd_exercises],
        "Projects": [min_projects, max_projects, mode_projects, µ_projects, sd_projects],
        "Total": [min_total, max_total, mode_total, µ_total, sd_total]}

df = pd.DataFrame(summary_data)
display(df)


# In[207]:


# draw histograms for quiz marks 

from matplotlib import pyplot as plt

plt.hist(cleaned_quizzes)
plt.xlabel("quiz marks")
plt.ylabel("number of students with scores")


# In[225]:


# draw histograms for assignment marks 

plt.hist(cleaned_assignments)
plt.xlabel("assignment marks")
plt.ylabel("number of students with scores")


# In[226]:


# draw histograms for exercise marks 

plt.hist(cleaned_exercises)
plt.xlabel("exercise marks")
plt.ylabel("number of students with scores")


# In[211]:


# draw histograms for project marks 

plt.hist(cleaned_projects)
plt.xlabel("project marks")
plt.ylabel("number of students with scores")


# In[223]:


# draw histograms for total marks 

plt.hist(cleaned_total)
plt.xlabel("final marks")
plt.ylabel("number of students with scores")

