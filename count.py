import urllib2, os
from bs4 import BeautifulSoup

total = 6*[0]
def find_lec(mID):
	_URL = "http://www.timetable.ul.ie/room_res.asp?T1="
	opener = urllib2.build_opener()
	urllib2.install_opener(opener)
	m = 6 * [0]
	i = 0
	soup = BeautifulSoup(urllib2.urlopen(_URL+mID).read(),'html.parser')
	tags = soup.findAll("td",{"align":"justify"})
	for tag in tags:
		s_tag = tag.findAll("font", {"color": "#800000"})
		for _s_tag in s_tag:
			if _s_tag.text.find("LEC") != -1:
				m[i] = m[i]+1
		i=i+1
	total[0] = total[0]+m[0]
	total[1] = total[1]+m[1]
	total[2] = total[2]+m[2]
	total[3] = total[3]+m[3]
	total[4] = total[4]+m[4]
	total[5] = total[5]+m[5]

with open("room") as f:
	content = f.readlines()

for r_id in content:
	find_lec(r_id.strip())

print "(m)"+str(total[0])+" (t)"+str(total[1])+" (w)"+str(total[2])+" (t)"+str(total[3])+" (f)"+str(total[4])
