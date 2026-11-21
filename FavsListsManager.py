# This script builds the list pages form the csv files automativally.
# It has to be in the root folder along with Script.js to work.
import os, csv
csvs = []
for i in os.listdir('CSVs'): csvs.append('CSVs/'+i)
htmls = []
for i in os.listdir('Content'):
	if os.path.isdir('Content/'+ i): htmls.append('Content/'+ i +'/index.html')
for c, d in zip(csvs, htmls):
	with open(c, encoding = 'utf8') as f0:
		content = csv.reader(f0)
		header = next(content)
		rows = list(content)
	while [] in rows: rows.remove([])
	rows.sort(key = lambda row: row[0].lower())
	with open(c, mode = 'w', encoding = 'utf8', newline = '') as f0:
		writer = csv.writer(f0)
		writer.writerow(header)
		writer.writerows(rows)
	html = f'''<!DOCTYPE html>
<html>
	<head>
		<title>Good {d[8:-11]}</title>
		<meta charset=UTF-8>
		<meta name='viewport' content='width=device-width, initial-scale=1.0'>
		<link rel='stylesheet' href='/Styles/Mobile.css' media='(max-width: 767px)'>
		<link rel='stylesheet' href='/Styles/Tablet.css' media='(min-width: 768px) and (max-width: 1023px)'>
		<link rel='stylesheet' href='/Styles/Desktop.css' media='(min-width: 1024px)'>
		<link type='image/x-icon' rel='icon' href='/Icon/Favicon.ico'>
	</head>
	<body>
		<div class='item-container'>
'''
	for i in rows: html += f'''			<div class='item'>
				<a href = '{i[1]}' target = '_blank'>{i[0]}</a>
				<button onclick='switchItem(this)'>-</button>
			</div>
'''
	html += '''		</div>
		<p id = 'csvNote'>
			<a href = '/'>Main Page</a>
			/
			<a href = '/Content/CSVs.html'>Download This List</a>
		</p>
	</body>
	<script src='/Script.js'></script>
</html>'''
	with open(d, mode = 'w', encoding = 'utf8') as f1: f1.write(html)
for c in csvs:
	with open(c, encoding = 'utf8') as f0: contents = f0.read().rstrip()
	with open(c, mode = 'w', encoding = 'utf8', newline = '') as f0: f0.write(contents)
print('Done!')