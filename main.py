import bottle
import json
import data
import os.path
import process
import graph


@bottle.route('/')
def index():
  return bottle.static_file("index.html", root=".")

@bottle.route('/graph.js')
def static():
  return bottle.static_file("graph.js", root=".")

@bottle.route('/ajax.js')
def ajax():
  return bottle.static_file("ajax.js", root=".")

@bottle.get('/line')
def send_linedata():
  linedatas=graph.get_linedata()
  return json.dumps(linedatas)

@bottle.post('/send')
def receive_state():
  content=bottle.request.body.read().decode()
  content=json.loads(content)
  return graph.statedata(content['state'])

@bottle.get('/state')
def stateData():
  datas=graph.get_statedata()
  return json.dumps(datas)


@bottle.get('/pie')
def send_piedata():
  piedatas=graph.get_piedata()
  return json.dumps(piedatas)

def sortY(x):
  return x['year']

def get_data():
  csv_file = 'saved_data.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.cdc.gov/resource/mr8w-325u.json?$limit=50000'
    info = data.grab_json(url)
    data.separate_dates(info, "week_ending_date")
    heads = ['year', 'week', 'week_ending_date', 'region', 'state', 'city',
    'pneumonia_and_influenza_deaths', 'all_deaths', '_1_year', '_1_24_years',
    '_25_44_years', '_54_64_years', '_65_years', 'month', 'day']
    info.sort(key=sortY)
    data.write_csv(info, csv_file,heads)
get_data()

bottle.run(host="0.0.0.0",port=8080)