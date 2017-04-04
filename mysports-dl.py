import requests

import argparse
import os
import sys

parser = argparse.ArgumentParser(description='TomTom MySports activities mass downloader.')
parser.add_argument('username', help='your username')
parser.add_argument('password', help='your password')
parser.add_argument('format', choices=['tcx', 'gpx', 'fit', 'kml'],
                    help='which format to download')
parser.add_argument('--max-id', type=int, help='download up to this activity id')

args = parser.parse_args(sys.argv[1:])

username = args.username
password = args.password
_format = args.format
max_id = args.max_id

print '## TomTom MySports activities mass downloader ##'
print '. from %s account as %s' % (username, _format)

base = 'https://mysports.tomtom.com'
login = base + '/service/webapi/v2/auth/user/login'
data = base + '/service/webapi/v2/activity'

s = requests.session()

# login
params = {'email': username, 'password': password}
r1 = s.post(login, json=params)

# get data
try:
	r2 = s.get(data)
	activities = r2.json()
except requests.exceptions.RequestException:
	print """
Ops. Seems something went wrong while reaching for TomTom.
Please make sure the website is up, and try in a few minutes.
"""
	raise
except ValueError:
	print """
Ops. Seems something went wrong while getting your activities.
Please report this as an issue at the github repo.
"""
	raise

# check for activities folder
base_path = 'activities/%s'
try:
	os.mkdir('activities')
except OSError:
	if not os.path.isdir('activities'):
		print """
Ops. Seems you have a file called activities in the same folder. 
Please remove it before running this script.
"""
		raise

i = 0
for activity in activities['workouts']:
	i += 1
	if i < 430:
		continue
	if 'formats' not in activity or _format not in activity['formats']:
		print '%s: skipping, format not available' % activity['id']
		continue
	activity_data = s.get(base + activity['links']['self'] + '&format=' + _format)
	filename = activity_data.headers['Content-Disposition'][22:-1]
	print '%s: %s' % (activity['id'], filename)
	with open(base_path % filename, 'w') as f:
		f.writelines(activity_data.text)
	# i += 1
	if activity['id'] == max_id:
		break

print
print '%s activities downloaded.' % i
