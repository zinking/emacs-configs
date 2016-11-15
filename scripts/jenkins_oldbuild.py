#!/usr/bin/python
import jenkinsapi
from jenkinsapi.jenkins import Jenkins

if __name__ == '__main__':
    J = Jenkins('http://buildx.hotel.com', 'ewngzen','********')
    job_lastbuild = []
    for jobname,job in J.items():
	job_lastbuildtime = job.get_last_build().get_timestamp()
	job_lastbuild.append( (jobname,job_lastbuildtime))

    sorted(job_lastbuild,key=lambda pair:pair[1])
    print job_lastbuild
