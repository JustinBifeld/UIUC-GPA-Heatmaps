# UIUC-GPA-Heatmaps
This repository contains scripts to generate Heatmaps representing GPAs of subjects and courses at UIUC.  The data comes from [Wade Fagens github](https://github.com/wadefagen/datasets), specifically using the GPAs of Courses at The University of Illinois, [gpa/uiuc-gpa-dataset.csv](https://github.com/justin02-dev/UIUC-GPA-Heatmaps/blob/master/datasets/gpa/uiuc-gpa-dataset.csv).

This data set contains the the grade distribution for all courses at the University of Illinois over the past 10 years.  I specifically calculate and analyze the GPA from this dataset, obtaining the average GPA for courses within a subject, or the average GPA for an entire subject such as ECE or ECON.  

Using this data the code is capable of generating two interactive heatmaps.  The first, Subject-Heatmap.py, represents the average GPA of every Subject at UIUC, and the second, Course-Heatmap.py displays the average GPA for every course in a department.  Both heatmaps have the option to switch between the 10 year average GPA, and the most recent year's GPA from the data set which is currently 2019.  All tiles in the heatmaps can be hovered over to display the course number or subject depending on the heatmap, and the exact GPA.  These heatmaps can help students visualize and understand the different GPAs between majors or courses, aiding in making decisions.  This can be particularly useful for students who are applying to UIUC, or students in the Division of General Studies when deciding on a major.  While GPA is certainly not the only factor in consideration when choosing courses and curriculum, it is one looked at by most students that carries significant weight.  Hopefully these visualizations can aid students in making tough decisions.  

![Courses Heatmap](https://github.com/justin02-dev/UIUC-GPA-Heatmaps/blob/master/Assets/Course-Heatmap.png)

![Subject Heatmap](https://github.com/justin02-dev/UIUC-GPA-Heatmaps/blob/master/Assets/Subject-Heatmap.png)
