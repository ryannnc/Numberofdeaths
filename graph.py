import data
import json

def get_linedata():
  datas=[{"x":[],"y":[],"name":"all_deaths"},{"x":[],"y":[],"name":"_1_year"},{"x":[],"y":[],"name":"_1_24_years"},{"x":[],"y":[],"name":"_25_44_years"},{"x":[],"y":[],"name":"_54_64_years"},{"x":[],"y":[],"name":"_65_years"}]
  adict=data.load_csv('saved_data.csv')
  for count in range(len(datas)):
    temp=0
    for line in adict:
      if(line[0] not in datas[count]['x']):
        datas[count]['x'].append(line[0])
        datas[count]['y'].append(temp)
        temp=int(line[count+7])
      else:
        temp+=int(line[count+7])
    datas[count]['y'].pop(0)
  return datas


def all():
  overall_death=0
  adict=data.load_csv('saved_data.csv')
  for line in adict:
    overall_death+=int(line[7])
  return overall_death

def get_piedata():
  datas=[{"values":[],"labels":[1,2,3,4,5,6,7,8,9,10,11,12],"type":'pie'}]
  adict=data.load_csv('saved_data.csv')
  for month in range(1,13):
    temp=0
    for line in adict:
      if(int(line[13])==month):
        temp+=int(line[7])
    datas[0]['values'].append((temp/all())*100)
  return datas


def statedata(stateCode):
  datas=[{"x":[],"y":[],"name":"all_deaths"},{"x":[],"y":[],"name":"_1_year"},{"x":[],"y":[],"name":"_1_24_years"},{"x":[],"y":[],"name":"_25_44_years"},{"x":[],"y":[],"name":"_54_64_years"},{"x":[],"y":[],"name":"_65_years"}]
  adict=data.load_csv('saved_data.csv')
  for count in range(len(datas)):
    temp=0
    for line in adict:
      if(line[4]==stateCode):
        if(line[0] not in datas[count]['x']):
          datas[count]['x'].append(line[0])
          datas[count]['y'].append(temp)
          temp=int(line[count+7])
        else:
          temp+=int(line[count+7])
    datas[count]['y'].pop(0)
  return json.dumps(datas)