# # 打开文件
# with open('C:/Users/user/10856/try1103/20231103.text', 'r') as file:
#     # 跳过标题行（如果有的话）
#     next(file)

#     # 逐行读取文件内容
#     for line in file:
#         # 使用空格或制表符分割每一行
#         fields = line.split()

#         # 确保有足够的字段
#         if len(fields) == 5:  # 假设每行都包含5个字段
#             # 提取 "Similarity" 的值（在这里，它是第3个字段，因为列表从0开始索引）
#             similarity = fields[2]
#             print(f"Similarity: {similarity}")

# 打开文件
with open('C:/Users/user/10856/try1103/20231103.text', 'r') as file:
    # 跳过标题行（如果有的话）
    next(file)

    # 初始化一个空列表来存储 Similarity 值
    similarity_values = []

    # 逐行读取文件内容
    for line in file:
        # 使用空格或制表符分割每一行
        fields = line.split()

        # 确保有足够的字段
        if len(fields) == 5:  # 假设每行都包含5个字段
            # 提取 "Similarity" 的值（在这里，它是第3个字段，因为列表从0开始索引）
            similarity = fields[2]
            similarity_values.append(similarity)

# 生成 HTML 内容
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Similarity 示例</title>
</head>
<body>
    <h1>Similarity 示例</h1>
    <table>
        <tr>
            <th>Similarity</th>
        </tr>
"""

for similarity in similarity_values:
    html_content += f"""
    <tr>
        <td>{similarity}</td>
    </tr>
"""

html_content += """
    </table>
</body>
</html>
"""

# 保存 HTML 内容到一个 HTML 文件
with open("similarity_example.html", "w") as output_file:
    output_file.write(html_content)