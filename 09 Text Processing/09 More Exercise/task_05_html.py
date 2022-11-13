title = input()
content = input()
space = "    "
print("<h1>")
print(f"{space}{title}")
print("</h1>")
print("<article>")
print(f"{space}{content}")
print("</article>")
comment = input()
while comment != "end of comments":
    print("<div>")
    print(f"{space}{comment}")
    print("</div>")
    comment = input()


################################################   Task Description   ################################################
# 5. HTML
# You will receive lines of input:
# • On the first line, you will receive a title of an article
# • On the second line, you will receive the content of that article
# • On the following lines, until you receive "end of comments" you will get the comments about the article
# Print the whole information in html format:
# • The title should be in "h1" tag (<h1></h1>)
# • The content in article tag (<article></article>)
# • Each comment should be in div tag (<div></div>)
