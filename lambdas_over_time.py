import sys, os
sys.path.append(os.path.join("..", "lib"))
import pymysql

def main(project, conn):
	#foreach =>rawtype, item_types=>fileid
	sql = """ select datetime, r.filename, count, state, container_granularity
		from revisions r, lambda_expressions t where r.project = t.project and r.project = '%(project)s'
		and r.transactionid = t.revision""" % locals()
	print sql

	cursor = conn.cursor()
	cursor.execute(sql)
	timeHash = {}
	for time, filename, state, count, container_granularity in cursor:
		#if container_granularity == "full":
			#continue
		if not timeHash.has_key(time):
			timeHash[time] = []
		timeHash[time].append( (filename, state, count,  "lambda") )
	
	print sql

	times = timeHash.keys()
	times.sort()

	print times

	fd = open(project + "_lambdas_2019_1121.tsv", "w")
	print >> fd, "datetime\tCount"
	files = {}
	for time in times:
		print time
		for file in [x[0] for x in timeHash[time]]:
			files[file] = []
		for filename, state, count, kind  in timeHash[time]:
			if state == 'deleted':
				#print >> fd, "(deleted)state="+state
				pass
			else:
				#print >> fd, "(except)state="+state
				files[filename].append( (count, kind) )
		
		#Raw -> foreach
		#para -> forloop
		totalLambdas = 0

		print files.items();
				
		
		for file, types in files.items():
			for count, kind in types:
				totalLambdas += 1;
					

		print "total Lambdas at time", time, "is", totalLambdas
		print >> fd, str(time)+"\t"+str(totalLambdas)

	
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print >> sys.stderr, "usage: python " + __file__+ " username password "
		print >> sys.stderr, "arguments on the command line"
	#conn = pymysql.connect(host="127.0.0.1",
		#db="csharp_generics", port=3306, user=sys.argv[1], passwd = sys.argv[2])
	#conn = pymysql.connect(host="eb2-2291-fas01.csc.ncsu.edu",
		#db="csharp_generics", port=4747, user=sys.argv[1], passwd = sys.argv[2])
	conn = pymysql.connect(host="127.0.0.1",
		db="generics", port=3306, user=sys.argv[1], passwd = sys.argv[2])
		
	sql = "select distinct project from revisions where project in \
	('guava') order by project "
	#('mono', 'mediaportal3','nasa-exp', 'nhibernate3', 'castle','ccnet', \
	#'beagle', 'monodevelop','lucene.net', 'banshee') order by project "
	
	cursor = conn.cursor()
	cursor.execute(sql)
	projects = []
	for project, in cursor:
		projects.append(project)
	print projects
	for project in projects:
		main(project, conn)
