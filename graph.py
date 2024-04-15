# from graphviz import Digraph
# import re

# dot = Digraph()

# # # Add nodes to the graph
# # dot.node('A', 'Node A')
# # dot.node('B', 'Node B')
# # dot.node('C', 'Node C')

# # # Add edges to the graph
# # dot.edge('A', 'B')
# # dot.edge('B', 'C')
# # dot.edge('C', 'A')

# # # Specify the output file format (optional)
# # dot.format = 'png'

# # # Render the graph to a file
# # dot.render('example_graph', view=True)

# # Alternatively, to view the graph without saving it:
# # dot.view()



# level1 = []
# level2 = []
# level3 = []
# level4 = []
# level5 = []
# level6 = []
# level7 = []

# with open("Windows-11-VBox-Logs", "r") as logs:
    
#     pattern = r'\[(.*?)\]'

#     for line in logs.readlines():
#         if "level 1" in line:
#             matches = re.findall(pattern, line)
#             for match in matches:
#                 level1.append(match)
#         elif "level 2" in line:
#             matches = re.findall(pattern, line)
#             for match in matches:
#                 level2.append(match)
#         elif "level 3" in line:
#             matches = re.findall(pattern, line)
#             for match in matches:
#                 level3.append(match)
#         elif "level 4" in line:
#             matches = re.findall(pattern, line)
#             for match in matches:
#                 level4.append(match)
#         elif "level 5" in line:
#             matches = re.findall(pattern, line)
#             for match in matches:
#                 level5.append(match)
#         elif "level 6" in line:
#             matches = re.findall(pattern, line)
#             for match in matches:
#                 level6.append(match)
#         elif "level 7" in line:
#             matches = re.findall(pattern, line)
#             for match in matches:
#                 level7.append(match)

# nodes = level1 + level2 + level3 + level4 + level5 + level6 + level7

# # for node in level2:
# #     print(node)

# for node in level1:
#     dot.edge("/", node)
#     for node2 in level2:
#         if node in node2:
#             dot.edge(node, node2)
#         for node3 in level3:
#             if node2 in node3:
#                 dot.edge(node2, node3)
#             for node4 in level4:
#                 if node3 in node4:
#                     dot.edge(node3, node4)
#                 for node5 in level5:
#                     if node4 in node5:
#                         dot.edge(node4, node5)
#                     for node6 in level6:
#                         if node5 in node6:
#                             dot.edge(node5, node6)
#                         for node7 in level7:
#                             if node6 in node7:
#                                 dot.edge(node6, node7)
                
        

# for node in level2:
#     pass

# # dot.format = 'png'

# # # Render the graph
# dot.render('example_graph', cleanup=True)

# # # Alternatively, to view the graph without saving it:
# # dot.view()


from graphviz import Digraph
import re

dot = Digraph()

level1 = []
level2 = []
level3 = []
level4 = []
level5 = []
level6 = []
level7 = []

with open("Windows-11-VBox-Logs", "r") as logs:
    pattern = r'\[(.*?)\]'
    
    # Populate the levels lists
    for line in logs.readlines():
        if "level 1" in line:
            matches = re.findall(pattern, line)
            level1.extend(matches)
        elif "level 2" in line:
            matches = re.findall(pattern, line)
            level2.extend(matches)
        elif "level 3" in line:
            matches = re.findall(pattern, line)
            level3.extend(matches)
        elif "level 4" in line:
            matches = re.findall(pattern, line)
            level4.extend(matches)
        elif "level 5" in line:
            matches = re.findall(pattern, line)
            level5.extend(matches)
        elif "level 6" in line:
            matches = re.findall(pattern, line)
            level6.extend(matches)
        elif "level 7" in line:
            matches = re.findall(pattern, line)
            level7.extend(matches)

print(len(level1))
print(len(level2))
print(len(level3))
print(len(level4))
print(len(level5))
print(len(level6))
print(len(level7))

# Populate the graph with nodes and edges
for node1 in level1:
    dot.node(node1)
    dot.edge("/", node1)
    for node2 in level2:
        if node1 in node2:
            dot.node(node2)
            dot.edge(node1, node2)
            for node3 in level3:
                if node2 in node3:
                    dot.node(node3)
                    dot.edge(node2, node3)
                    for node4 in level4:
                        if node3 in node4:
                            dot.node(node4)
                            dot.edge(node3, node4)
                            for node5 in level5:
                                if node4 in node5:
                                    dot.node(node5)
                                    dot.edge(node4, node5)
                                    for node6 in level6:
                                        if node5 in node6:
                                            dot.node(node6)
                                            dot.edge(node5, node6)
                                            for node7 in level7:
                                                if node6 in node7:
                                                    dot.node(node7)
                                                    dot.edge(node6, node7)

# dot.graph_attr={'size': '8,12'}
dot.graph_attr['ranksep'] = '5.0'

# Render the graph
dot.render('example_graph', view=False)
