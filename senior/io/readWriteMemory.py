from io import BytesIO
from io import StringIO

fStr = StringIO()
fStr.write("This is string io")

fByte = BytesIO()
fByte.write(b"I am byte io")

print(fStr.getvalue())
print(fByte.getvalue())