import pandas as pd

input = """15-60,14-59
32-80,17-79
47-80,79-80
64-64,12-63
93-93,8-92
35-41,34-41
7-52,7-8
28-95,28-94
43-99,2-43
74-77,75-78
44-98,55-69
2-52,53-53
71-73,71-72
35-49,48-49
84-85,22-85
88-90,7-89
18-85,5-85
4-4,3-82
22-79,21-79
6-6,6-84
61-84,61-84
66-95,16-94
12-46,47-47
93-93,55-93
23-95,22-99
16-16,16-58
67-81,65-80
58-66,24-66
39-46,47-79
9-9,9-89
18-89,19-68
4-89,10-47
5-79,3-5
12-90,20-91
78-83,79-89
6-80,5-81
37-98,37-38
33-98,32-97
42-78,41-43
31-97,2-98
24-72,23-73
6-88,5-29
80-93,81-94
5-85,4-84
21-81,4-89
45-84,22-44
57-80,81-81
46-76,47-77
22-32,21-72
5-29,4-29
11-78,10-78
61-62,61-92
17-24,18-24
57-93,56-97
1-98,4-50
5-5,5-42
10-92,10-11
8-86,22-87
10-52,9-9
3-13,10-14
1-46,3-56
85-85,7-84
88-89,88-96
1-93,1-93
58-71,53-60
79-96,30-79
5-56,5-57
42-98,41-99
3-97,96-97
55-65,54-56
73-93,93-94
18-98,99-99
2-57,1-69
41-42,41-77
10-51,50-52
73-73,73-89
31-91,31-31
6-27,6-61
1-1,1-84
21-56,57-57
30-31,30-31
24-72,16-72
59-65,56-65
18-18,17-99
87-87,32-88
30-30,30-60
12-95,13-95
29-66,6-65
2-52,2-53
93-93,2-93
2-98,3-3
19-90,15-18
12-83,3-13
21-99,22-22
5-54,5-54
43-73,44-73
15-26,7-25
52-94,53-95
67-68,2-67
2-92,91-92
72-91,73-78
20-87,21-87
27-56,10-56
20-88,89-89
5-90,10-90
11-20,12-21
4-86,4-86
44-46,45-98
10-11,10-63
8-9,13-98
23-46,23-61
71-87,15-86
33-40,19-39
7-93,8-93
18-18,17-76
3-58,8-59
42-94,42-42
12-86,44-87
20-93,93-96
12-54,13-36
41-77,41-76
20-20,19-96
13-91,12-90
3-98,4-4
6-67,6-66
25-61,30-54
61-61,15-61
24-81,24-24
45-69,46-68
56-66,52-98
50-67,59-68
2-97,3-72
33-79,34-51
56-92,55-91
3-69,1-68
34-34,33-34
93-93,48-92
22-69,21-30
2-7,16-83
87-95,19-88
93-98,94-97
42-95,43-95
6-7,6-83
23-95,19-86
30-94,19-98
59-94,14-95
24-84,24-83
31-36,32-35
20-57,21-57
2-46,2-2
9-44,6-9
25-64,26-65
21-96,43-97
1-5,4-50
58-72,57-59
96-97,22-96
3-63,31-64
18-67,16-16
38-42,37-43
9-18,18-82
53-59,52-52
6-99,6-6
56-89,89-97
88-90,13-89
24-26,25-85
46-87,30-45
63-64,18-64
12-94,9-13
51-98,50-50
8-18,7-17
25-25,25-32
5-39,39-40
7-18,7-7
23-65,65-94
17-43,16-44
32-91,90-90
3-5,2-5
28-39,27-42
12-13,12-65
2-91,48-92
93-98,72-87
31-43,31-42
12-69,12-59
2-14,14-81
17-89,17-90
20-37,38-62
6-36,3-22
6-97,5-7
71-81,8-77
18-61,61-84
86-86,22-85
9-27,12-79
1-46,8-47
12-85,85-98
57-66,58-65
62-97,3-99
5-80,6-20
39-88,38-88
54-63,13-64
17-40,39-57
9-99,10-82
24-37,24-24
64-81,65-81
2-47,48-48
5-6,6-6
26-42,38-91
17-81,80-81
4-7,5-8
23-43,23-34
98-99,3-97
43-75,74-75
58-78,18-78
60-78,60-78
10-95,88-96
77-78,20-78
36-70,36-57
19-65,20-66
1-3,3-15
1-5,5-47
23-80,22-22
38-73,29-38
41-41,40-57
8-96,9-89
28-28,29-96
22-85,85-97
20-92,21-92
35-53,54-54
45-49,47-48
20-90,82-91
38-92,37-93
1-64,55-62
56-75,32-55
13-98,14-92
4-16,3-16
52-75,52-74
1-86,1-87
12-81,12-82
35-36,35-97
9-67,67-68
14-97,13-14
6-6,5-69
73-90,48-95
24-27,26-28
25-52,26-50
75-75,75-98
22-96,7-18
60-88,60-89
47-49,8-48
19-44,36-67
4-5,9-96
30-74,75-75
10-10,11-77
47-79,80-80
12-68,12-69
38-79,52-91
29-30,4-29
40-88,40-49
4-39,4-39
15-83,82-84
69-96,4-96
5-93,2-94
49-50,48-48
68-84,68-84
16-74,74-86
7-86,6-8
47-80,48-74
3-69,69-71
49-58,60-78
31-59,32-60
4-64,4-64
59-91,91-91
90-90,9-89
70-85,44-86
24-62,62-85
1-11,2-94
15-99,19-95
12-32,31-32
56-61,56-72
7-44,1-7
1-70,3-71
29-62,1-61
7-97,8-97
90-92,48-91
54-75,53-74
2-98,98-98
2-69,70-70
45-88,64-89
28-60,28-28
10-94,27-98
32-32,32-49
63-64,31-62
15-69,16-70
16-23,13-16
20-66,66-67
16-99,17-93
62-64,7-63
97-97,41-78
41-75,27-39
2-38,37-37
13-96,95-96
7-35,42-75
39-40,3-40
4-89,2-5
22-35,35-36
6-59,58-59
23-29,9-28
77-77,76-76
12-48,11-96
57-85,56-84
90-92,68-91
97-98,62-98
23-69,22-69
4-85,3-95
50-87,33-88
33-74,32-74
20-67,21-47
5-90,6-91
50-98,50-98
4-94,1-26
4-38,39-78
91-91,11-90
54-99,55-99
80-84,84-85
33-91,16-33
62-83,29-61
23-67,23-68
26-94,29-91
21-84,32-84
48-61,28-48
15-15,15-76
20-26,58-79
75-75,47-74
30-63,31-63
16-95,55-96
45-92,44-66
59-95,58-99
19-19,18-19
30-36,34-36
5-8,3-9
6-62,6-6
90-90,67-89
31-79,31-84
20-24,19-23
33-72,33-86
59-95,1-59
4-91,4-97
92-93,75-92
42-95,18-99
95-96,20-95
23-23,22-50
5-99,5-6
16-76,17-17
48-59,49-76
51-91,13-91
10-11,5-10
19-95,18-18
41-41,1-41
40-64,40-78
56-84,12-83
17-63,16-84
15-49,15-15
31-91,90-92
38-40,8-85
46-96,46-79
54-72,54-54
2-96,8-97
2-96,1-98
15-86,16-44
10-65,9-65
79-79,9-78
18-70,17-70
68-83,14-68
28-68,26-29
18-54,17-21
61-82,20-60
47-76,47-93
6-79,79-85
13-13,13-91
40-40,40-92
9-76,18-83
17-40,18-98
45-60,10-54
26-48,48-63
15-58,14-92
69-70,22-69
5-88,5-89
42-44,46-89
38-76,44-77
1-73,2-79
52-98,49-82
5-94,29-99
13-63,13-94
72-87,71-86
27-94,93-94
35-94,1-93
43-49,42-48
72-94,72-72
43-86,42-85
1-3,3-94
42-80,30-92
22-85,23-84
39-43,44-44
36-36,28-35
12-46,13-78
14-98,14-98
69-78,73-79
91-98,74-91
10-11,10-96
32-40,25-39
50-81,12-80
88-89,6-88
48-69,7-48
4-8,9-93
74-84,74-75
27-82,27-82
1-97,1-1
43-69,43-68
13-27,14-27
9-27,32-78
22-78,22-23
47-58,46-46
19-98,3-98
27-78,27-78
74-90,4-74
44-46,31-45
35-81,6-55
6-60,6-59
10-32,32-33
23-23,23-53
4-87,4-86
96-96,6-95
1-37,2-38
77-88,74-87
3-92,5-93
15-96,16-92
37-58,34-36
40-75,38-74
2-62,55-62
43-93,43-43
77-93,70-77
56-76,56-77
2-2,3-88
2-53,53-60
30-31,29-36
30-30,29-88
42-79,41-80
75-75,28-74
18-88,8-87
13-63,64-64
3-48,46-49
12-30,12-12
3-99,4-94
3-3,4-64
30-76,29-29
12-60,11-54
9-95,9-95
66-73,61-73
10-11,10-11
42-72,42-44
8-89,10-89
25-74,75-75
33-44,34-45
28-78,27-77
48-97,37-93
46-65,10-64
17-97,68-96
50-93,93-95
22-96,23-97
2-20,1-86
6-60,60-80
33-65,66-66
23-23,16-22
41-89,40-62
17-96,97-97
70-71,9-70
11-24,11-35
8-48,49-49
78-92,75-91
21-98,99-99
12-45,12-13
36-36,35-58
9-15,15-98
43-61,61-89
52-53,52-74
2-51,1-5
29-29,28-75
1-45,3-47
5-13,12-13
17-86,17-17
4-99,5-99
77-88,76-90
50-70,50-51
3-88,2-87
4-55,4-75
8-22,8-8
76-99,77-96
14-72,13-90
1-62,63-94
11-74,5-10
37-65,65-65
10-73,11-91
34-78,21-34
47-61,46-62
11-86,8-10
14-39,14-40
8-81,82-89
85-86,18-85
14-91,66-97
20-51,19-43
1-57,3-57
14-52,45-53
37-92,36-99
84-84,32-83
45-88,44-81
30-80,80-92
6-82,6-6
9-9,9-87
26-28,21-27
1-92,7-93
32-90,33-33
26-44,44-66
24-86,23-86
19-83,84-99
28-40,28-30
18-88,17-87
62-70,71-71
3-86,3-3
20-20,19-90
7-18,4-17
29-41,41-42
24-57,40-58
15-15,15-54
19-47,19-20
63-64,21-63
29-30,21-30
61-62,16-61
16-78,8-15
63-74,63-63
68-69,31-69
3-99,4-99
28-28,29-39
72-85,3-67
64-67,68-68
75-97,74-74
11-99,80-88
10-93,24-79
93-94,2-94
1-98,1-99
2-95,2-2
20-75,21-75
26-85,2-26
9-96,9-99
85-85,85-85
59-70,59-70
22-27,23-23
41-42,41-52
2-17,1-16
41-54,55-55
8-89,7-9
13-98,9-13
10-84,3-84
40-90,39-39
12-93,2-93
5-99,4-99
30-81,30-88
1-43,2-54
72-84,81-85
2-34,4-35
7-88,6-88
66-98,65-99
93-94,36-94
66-76,67-77
15-97,15-98
53-60,53-54
1-81,81-86
51-65,17-50
11-51,4-50
16-16,17-82
44-80,45-81
32-39,9-38
51-76,51-75
58-98,59-79
60-61,60-61
7-8,7-87
32-33,32-32
35-85,79-97
20-65,20-66
5-73,6-74
15-76,14-82
43-91,43-99
8-94,42-95
19-92,92-94
2-99,2-2
91-96,5-92
7-94,7-7
82-82,33-82
1-5,1-2
87-88,48-87
88-88,40-88
24-32,10-31
15-82,14-81
18-34,18-33
40-46,39-73
40-64,46-65
3-94,93-95
41-56,57-85
48-56,2-48
79-93,80-94
45-78,44-66
49-77,77-89
29-67,28-28
53-96,95-97
6-44,24-99
7-68,28-84
6-77,76-78
3-99,98-99
11-85,11-85
24-24,25-96
44-51,52-64
88-90,89-98
2-97,3-97
15-16,15-58
5-96,6-92
2-22,5-21
11-11,10-87
95-98,75-96
8-69,3-7
25-81,26-74
25-99,24-68
92-93,17-92
2-73,2-2
87-95,11-87
20-93,15-97
7-98,49-98
4-79,4-31
50-57,50-57
67-68,34-68
57-68,72-90
3-33,10-34
26-27,26-80
8-8,8-82
93-93,2-93
12-86,1-12
4-8,8-89
14-49,15-50
5-35,33-33
92-93,6-93
28-76,76-93
47-48,47-85
7-94,2-43
43-85,22-43
71-91,90-91
14-92,14-91
5-8,9-78
13-33,33-33
32-93,37-86
37-89,37-90
51-53,11-52
11-38,37-37
4-85,4-89
6-10,7-14
21-33,20-91
9-92,92-92
29-96,97-97
13-94,12-98
11-96,12-97
35-39,39-70
31-60,31-95
18-84,17-83
5-6,5-89
63-64,40-63
89-90,6-90
88-89,89-90
69-83,76-83
16-82,81-82
5-50,49-80
9-98,9-99
75-76,18-75
1-46,16-46
45-52,46-52
18-43,17-19
8-80,19-81
11-11,11-86
20-49,19-49
54-89,53-90
9-9,9-95
21-86,17-21
57-95,33-94
13-14,13-53
7-21,8-21
3-24,12-25
89-91,45-90
82-83,22-82
57-63,64-72
6-7,6-70
19-97,18-18
30-56,30-31
24-96,25-98
1-74,7-99
24-90,25-63
44-57,43-58
62-85,86-86
15-49,20-50
20-69,20-69
38-66,67-77
8-27,7-91
8-21,15-51
19-83,9-10
23-23,20-22
19-19,19-88
4-9,1-8
15-69,16-16
20-42,42-69
43-47,7-46
5-93,6-94
10-55,9-54
8-91,9-27
42-97,43-98
20-82,14-81
19-31,19-70
7-93,7-8
28-66,17-28
65-96,17-95
40-78,77-79
51-97,53-96
25-40,11-25
19-97,20-96
23-88,40-88
81-81,35-80
71-86,34-86
13-88,14-89
63-84,64-85
56-98,7-97
31-82,30-81
58-98,58-99
36-47,46-46
80-80,20-79
59-92,19-91
19-66,63-84
70-70,4-70
66-74,65-79
5-68,1-4
17-52,11-17
6-77,78-78
10-11,10-25
13-96,22-61
5-20,6-31
18-61,19-50
6-35,6-34
12-91,11-90
1-1,2-21
2-98,1-99
28-98,25-38
34-63,35-76
20-85,84-85
11-13,13-31
72-74,2-73
3-10,6-25
46-46,46-88
34-59,32-60
77-77,23-77
11-12,11-83
4-83,5-84
10-89,9-88
82-90,79-83
1-60,4-61
29-93,28-92
1-47,36-48
51-94,45-93
30-62,30-33
3-96,4-97
57-96,56-96
44-44,44-94
44-58,44-45
3-16,26-84
31-32,31-78
41-96,42-96
34-63,62-90
20-22,16-23
61-99,60-98
3-3,4-21
2-46,11-47
7-8,7-64
7-47,47-70
49-87,50-89
22-95,21-77
87-87,18-86
30-30,30-99
54-66,65-66
77-77,37-76
11-32,13-32
93-95,19-93
3-93,1-92
37-46,36-55
12-76,76-85
18-94,23-74
10-99,98-99
23-23,24-31
4-6,9-96
42-56,9-45
9-50,14-51
22-82,23-83
21-56,56-92
1-7,1-1
96-96,1-96
61-70,27-70
2-38,9-37
19-20,20-56
61-66,1-67
42-44,2-43
6-6,6-90
40-89,4-14
96-96,11-96
54-77,77-88
29-81,29-81
12-77,5-76
4-86,3-86
57-58,20-57
18-18,19-62
9-56,10-57
26-91,35-92
6-56,7-81
1-78,1-61
76-79,43-76
96-99,32-97
27-30,28-31
94-95,21-94
22-25,18-24
40-89,39-41
20-26,20-20
28-77,77-88
2-79,14-80
17-34,20-33
26-89,25-88
5-29,20-73
9-78,9-77
11-12,11-79
25-62,24-26
1-94,1-2
90-91,51-90
8-96,9-97
6-20,17-40
42-82,24-42
10-77,10-76
32-88,33-87
58-63,62-62
64-70,64-71
34-54,55-55
88-90,19-88
77-86,77-78
3-88,88-89
42-45,31-44
99-99,88-97
81-99,18-81
7-95,11-88
4-72,2-92
7-7,7-26
10-90,9-89
2-2,3-65
7-49,8-49
51-98,52-92
27-70,2-67
65-73,37-69
81-83,81-82
40-55,41-54
4-38,29-90
53-57,36-57
79-79,13-78
18-83,19-84
11-91,10-93
7-79,8-80
18-56,18-18
80-80,32-79
2-44,34-63
6-73,73-74
12-70,13-71
25-57,15-56
40-95,40-41
1-63,1-2
7-7,8-71
23-94,23-23
51-89,46-88
67-67,8-66
24-91,21-25
67-72,9-71
8-97,9-97
50-60,36-60
1-56,27-32
2-6,6-91
67-73,68-74
30-30,30-37
4-69,5-68
94-95,10-95
30-77,77-78
10-95,10-60
37-93,2-32
8-99,7-7
57-89,58-99
1-30,13-54
31-97,32-32
82-82,18-82
10-17,15-18
74-87,75-88
21-84,82-86
11-90,12-17
26-98,97-99
35-95,35-95
2-4,3-75
3-23,24-60
85-94,85-95
1-3,3-22
53-78,53-79
1-41,3-40
54-87,54-65
3-91,17-90
41-75,40-74
44-78,43-77
75-80,41-74
43-58,36-47
61-63,62-64
16-88,16-87
4-93,5-94
56-93,93-98
27-66,27-27
51-75,35-74
50-77,38-76
51-78,29-77
12-19,20-86
4-90,1-71
13-15,14-25
75-84,74-74
7-90,6-65
56-73,72-74
20-21,20-83
7-35,3-35
1-5,5-46
30-90,46-90
10-78,3-87
25-87,25-25
5-7,6-92
24-85,25-84
14-87,16-87
3-87,4-88
53-64,52-52
71-73,72-73
19-33,32-43
3-68,24-69
4-43,9-44
62-62,62-69
32-38,37-38
14-68,68-70
64-88,88-95
27-81,81-84
2-24,24-24
52-52,52-90
1-97,11-95
9-94,4-93
5-33,4-24
37-37,36-76
1-2,3-64
85-93,10-85
39-85,38-84
47-48,16-47
30-49,31-50
46-85,45-45
7-86,4-85
23-66,66-67
54-95,16-27
2-3,7-59
57-57,35-56
20-21,20-90
35-58,34-54
14-91,91-93
9-99,16-97
24-50,25-50
18-27,19-86
78-92,79-79
23-90,53-91
27-73,69-70
90-94,25-90
8-68,1-67
50-87,5-50
25-67,24-67
3-98,8-97
85-99,57-98
34-34,17-35
8-80,81-81
14-98,15-99
1-2,1-99
24-49,23-43
36-39,35-39
1-25,11-26
2-51,6-97
33-58,23-57
25-80,24-26
26-82,25-25
44-95,43-94
61-68,9-62
27-55,28-48
22-88,20-23"""

# Load Data

# df = pd.read_csv("fileinput.txt", header=None)
df = pd.DataFrame([x.split(",") for x in input.split("\n")]).astype("string")
df.rename(columns={0: "S1", 1: "S2"}, inplace=True)

# Setting constants
count = 0

# iterating through rows
for index, row in df.iterrows():
    S1l = int((row["S1"].split("-"))[0])
    print("S1l", S1l)
    S1h = int((row["S1"].split("-"))[1])
    print("S1h", S1h)
    S2l = int((row["S2"].split("-"))[0])
    print("S2l", S2l)
    S2h = int((row["S2"].split("-"))[1])
    print("S2h", S2h)

    print(S1l <= S2l)
    print(S1h >= S2h)

    if S1l <= S2l and S1h >= S2h:
        print("S1 contains S2", index, "\n", row)
        count += 1

    elif S2l <= S1l and S2h >= S1h:
        print("S2 contains S1", index, "\n", row)
        count += 1


print("Count ->", count)
print(df)

# total = 0

# with open("fileinput.txt") as file:
#     for line in file:
#         contents = line.split(",")
#         elf1 = contents[0]
#         elf2 = contents[1]
#         elf1_start, elf1_stop = elf1.split("-")[0], elf1.split("-")[1]
#         elf2_start, elf2_stop = elf2.split("-")[0], elf2.split("-")[1]
#         elf1_range = range(int(elf1_start), int(elf1_stop) + 1)
#         elf2_range = range(int(elf2_start), int(elf2_stop) + 1)

#         counter = 0

#         for item in range(int(elf1_start), int(elf1_stop) + 1):
#             if item in range(int(elf2_start), int(elf2_stop) + 1):
#                 counter += 1
#             if counter == len(elf1_range) or counter == len(elf2_range):
#                 total += 1
#                 break

# print(total)
