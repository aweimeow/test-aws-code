import os

os.system("mkdir public")
s = """<html>
Build complete by aweimeow
</html>"""

with open("public/index.html", "w") as f:
    f.write(s)
