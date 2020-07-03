import csv
import pandas as pd
from portfolios.models import Skill
with open("C:/semi/Application&Data.csv","r") as f:
    dr = csv.DictReader(f)
    s = pd.DataFrame(dr)
ss = []
for i in range(len(s)):
    st = (s["skill_kind"][i], s["skill_name"][i], s["skill_img"][i])
    ss.append(st)
for i in range(len(s)):
    Skill.objects.create(skill_kind=ss[i][0], skill_name=ss[i][1], skill_img=ss[i][2])
