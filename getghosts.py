import urllib.request
import json 
import shutil
import re
import os
import sys
import logging
LOG_FILENAME = 'failures.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

base_url = 'http://tt.chadsoft.co.uk'

# Sets of leaderboards
nintendo_leaderboards = base_url + '/original-track-leaderboards.json'
ctgp_leaderboards = base_url + '/ctgp-leaderboards.json'
nintendo_200cc_leaderboards = base_url + '/original-track-leaderboards-200cc.json'
ctgp_200cc_leaderboards = base_url + '/ctgp-leaderboards-200cc.json'

# Read arguments
if len(sys.argv) == 1:
	leaderboard = nintendo_leaderboards
elif len(sys.argv) == 2:
	if sys.argv[1] in ['150', 'nintendo']:
		leaderboard = nintendo_leaderboards
	elif sys.argv[1] == '200':
		leaderboard = nintendo_200cc_leaderboards
	elif sys.argv[1] == 'ctgp':
		leaderboard = ctgp_leaderboards
	else:
		raise ValueError('Invalid Argument: {}'.format(sys.argv[1]))
elif len(sys.argv) == 3:
	if 'nintendo' in sys.argv:
		if '150' in sys.argv:
			leaderboard = nintendo_leaderboards
		elif '200' in sys.argv:
			leaderboard = nintendo_200cc_leaderboards
		else:
			raise ValueError('Invalid Arguments: {}, {}'.format(sys.argv[1], sys.argv[2]))
	elif 'ctgp' in sys.argv:
		if '150' in sys.argv:
			leaderboard = ctgp_leaderboards
		elif '200' in sys.argv:
			leaderboard = ctgp_200cc_leaderboards
		else:
			raise ValueError('Invalid Arguments: {}, {}'.format(sys.argv[1], sys.argv[2]))
	else:
		raise ValueError('Invalid Arguments: {}, {}'.format(sys.argv[2], sys.argv[2]))
else:
	raise ValueError('Invalid Arguments')

# Pick if you want nintendo/ctgp/200cc nintendo/200cc ctgp ghosts
with urllib.request.urlopen(leaderboard) as url:
    data = json.loads(url.read().decode()[1:])

for course_data in data['leaderboards']:
	# Some errors(?) in database
    if 'name' not in course_data.keys():
        continue
	
    try:
        print('-----------------------')
        print(course_data['name'])
        print('Retrieving course data')
		
		# Data for course (want list of ghosts)
        with urllib.request.urlopen(base_url + course_data['_links']['item']['href']) as url:
            curr_course = json.loads(url.read().decode())
        print('Retrieving best ghost data')
		
		# Get JSON data of ghost
        with urllib.request.urlopen(base_url + curr_course['ghosts'][0]['_links']['item']['href']) as url:
            stuff = json.loads(url.read().decode()[1:])
        print('Generating file name')
        time_components = re.split(':|\.', stuff['finishTime'])
        filename = 'ghosts/'+stuff['trackName']+' SLOT'+("0x%X" % stuff['slotId'])[2:].zfill(2)+'-'+stuff['trackId']+'/'+time_components[0]+'m'+time_components[1]+'s'+time_components[2][:7]+' '+stuff['player']+'.rkg'
        filename = filename.replace('>', '').replace('<', '').replace('*', '').replace(':', '')
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        print('Retrieving ghost file')
		
		# Get ghost file
        with urllib.request.urlopen(base_url + stuff['href']) as response, open(filename, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print()
    except:
        print('Failed. See log file for details.')
        logging.exception('Got exception for {}'.format(course_data['name']))
        with open(LOG_FILENAME, 'a') as f:
            f.write('\n')
print('\n-----------------------\nFinished\n-----------------------')