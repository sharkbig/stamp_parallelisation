#!/usr/bin/python
import os
import sys
import glob
import multiprocessing as mp
import matlab.engine as mat
import os
import time

curdir=os.getcwd()
patch_list=glob.glob(curdir+"/PATCH_*")
options= sys.argv
msglog=open('python_stamps.log','wa')

for op in options:
	if '-j' in op:
		n_core=int(op[2:])
	elif '-s' in op:
		start_step=op[2:]
	elif '-e' in op:
		end_step=op[2:]
	else:
		n_core=1
		start_step='0'
		end_step='8'

if int(end_step) > 5:
	_end_step='5'
else:
	_end_step=end_step


def stamps_by_patch(patch_dir):
	tn= time.time()
	num=patch_dir.split('/')[-1]

	print "Start processing %s"%(num)
	os.chdir(patch_dir)

	# launch matlab engine
	eng = mat.start_matlab('-nodisplay -nodesktop -r "stamps({},{})"'.format(start_step,_end_step))
	dt=time.time()-t0
	print '{} is successfully completed in {}'.format(num,dt)

	msglog.write("Start processing %s\n"%(num))
	# msglog.write('run: matalb -nodisplay -nodesktop -r "stamps({},{})"\n'.format(start_step,_end_step))
	msglog.write('{} is successfully completed in {}\n'.format(num,dt))


t0 = time.time()

# Parallel computation
par= mp.Pool(n_core)
if int(start_step) <= 5:
	print '#############################################'
	print 'parallel processing step 1 - 5 with {} cores'.format(n_core)
	print '#############################################'
	msglog.write('#############################################\n')
	msglog.write('parallel processing step 1 - 5 with {} cores\n'.format(n_core))
	msglog.write('#############################################\n')
	par.map(stamps_by_patch,patch_list)
par.close()
par.join()


os.chdir(curdir)
# mat.ps_merge_patches()
# exec step 6-8
if int(end_step)>= 6:
	print '#############################################\n'
	print 'start processing step 6-{}\n'.format(str(end_step))
	msglog.write('###################################\n')
	msglog.write('start processing step 6-{}'.format(str(end_step)))
	
	eng = mat.start_matlab('-nodisplay -nodesktop -r "stamps(6,{})"'.format(end_step))
dt=time.time()-t0

print '\n Process completed in {}'.format(dt)
msglog.write('\n Process completed in {}\n'.format(dt))
