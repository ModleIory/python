import re
string = '''<h1 style="font-weight:bold; font-size:20px; line-height:22px; height:22px; margin-bottom:10px;">
里仁篇
<a id="leftbtn22" style=" float:right;line-height:20px; height:20px; width:40px; border:1px solid #999999; color:#999999; text-align:center;font-size:14px;-moz-border-radius:5px;-webkit-border-radius:5px;border-radius:5px;" href="javascript:ShowYizhu(22)">译注</a>
</h1>'''
e = r'<h1.+?>\n(.+?)\n<a'

print(re.findall(e,string,re.S|re.M))