import re

text = input()
while text:
    pattern = r"((w{3})\.([A-Za-z0-9]+)([A-Za-z0-9\-]+)*(\.[a-z]+)+)"
    matched_links = re.search(pattern, text)
    if matched_links:
        print(matched_links.group())
    text = input()


################################################   Task Description   ################################################
# 6.*Extract the Links
# Write a program that extracts links from a given text.
# The text will come in the form of strings, each representing a sentence.
# You need to extract only the valid links from it. Example:
#           "www.internet.com"
# Sub-Domain 	 Domain name 	 Domain extension
# The Sub-Domain must always be "www".
# The Domain name can consist of English alphabet letters (uppercase and lowercase), digits, and dashes ("–").
# The Domain extension consists of one or more domain blocks,
# a domain block consists of a dot followed by one or more lowercase English alphabet letters,
# a Domain extension must have at least one domain block in order to be valid.
# The Sub-Domain and Domain name must be separated by a single dot.
# Any link that does NOT follow the specified above rules should be treated as invalid.
# The output is all valid links you have found, printed – each on a new line.
