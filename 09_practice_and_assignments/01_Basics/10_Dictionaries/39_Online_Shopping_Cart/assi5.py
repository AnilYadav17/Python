'''
=========================================
WORD LENGTH GROUPING
====================

A content management system stores article tags.

tags = ["python","java","api","react","html","css"]

Write a program to:

* Group words according to their length.
* Store result in dictionary.

Sample Output:
{
3:['api','css'],
4:['java','html'],
5:['react'],
6:['python']
}
'''

tags = ["python", "java", "api", "react", "html", "css"]
grouped_tags = {}

for tag in tags:
    length = len(tag)
    if length not in grouped_tags:
        grouped_tags[length] = []
    grouped_tags[length].append(tag)

print(grouped_tags)
