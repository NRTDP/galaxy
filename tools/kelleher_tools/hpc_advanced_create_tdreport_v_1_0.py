import xml.etree.ElementTree as ET, sys, subprocess, os, socket, getpass, time, os.path, time
from subprocess import Popen, PIPE


def main():
    db_name = sys.argv[2].split('dataset_')[-1].split('.')[0]
    db_name_with_ext = db_name + ".db"


    regex = '"' + sys.argv[3] + '"'
#    print("regex")
#    print(regex)
#    print("regex")

#    print("sys.argv[4]")
#    print(sys.argv[4])
#    print("sys.argv[4]")

	
    if not sys.argv[3]:
#        print("regex_in_if")
        regex = "none"

#    print("regex")
#    print(regex)
#    print("regex")

	
    parent = os.path.dirname(sys.argv[4])
			
    grandparent = os.path.dirname(parent)
		
    job_id = os.path.basename(os.path.normpath(grandparent))
		
    working_dir = sys.argv[6]
	
    user_email = sys.argv[8]
	
    input_pds = sys.argv[11]
    if sys.argv[12] != "auto":
        input_pds = sys.argv[12]
		
    env_path = "/projects/b1035/shared/" + sys.argv[10];
	
    script_path = env_path + "/GalaxyHPCSearch/";
   # print("script_path")
   # print(script_path)
   # print("script_path")
	
    print("Create Metadata")
#    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + working_dir + " " + sys.argv[9] + " " + user_email)
    os.system("python " + script_path + "hpc_create_metadata.py " + env_path + " " + working_dir + " " + sys.argv[9] + " " + user_email)
    
    #print("Start Monitor")
    running_procs = Popen("python " + script_path + "hpc_monitor.py " + env_path + " " + working_dir + " " + job_id + " " + sys.argv[9] + " " + sys.argv[10], shell=True)

    print("Unzip MzML")
#    os.system("python " + script_path + "hpc_echo_sysargv.py " + sys.argv[1])
    os.system("python " + script_path + "hpc_unzip_mzml.py " + sys.argv[1])

    print("Create Database")
#    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email + " " + input_pds + " " + sys.argv[2])
    os.system("python " + script_path + "hpc_create_database.py " + env_path + " " + sys.argv[2] + " " + db_name + " " + job_id + " " + "false")

    print("Copy Database")               
#    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email + " " + input_pds + " " + sys.argv[2])
    os.system("python " + script_path + "hpc_copy_database.py " + env_path + " " + db_name_with_ext + " " + working_dir + " " + job_id + " " + user_email + " " + input_pds + " " + db_name_with_ext)

#hold over from reg search
#    print("Copy Database")
##    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email + " " + input_pds + " " + sys.argv[2])
#    os.system("python " + script_path + "hpc_copy_database.py " + env_path + " " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email + " " + input_pds + " " + sys.argv[2])

    print("Prepare Files for Search")
#    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + sys.argv[1] + " " + working_dir + " " + job_id + " " + user_email)
    os.system("python " + script_path + "hpc_new_prepare.py " + env_path + " " + sys.argv[1] + " " + working_dir + " " + job_id + " " + user_email)

    if os.system("python " + script_path + "hpc_error_check.py " + working_dir + " PrepareError") != 0:
        raise Exception('Error occurred preparing files for search')



    print("Run Searches")
#    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " 1 " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email)
    os.system("python " + script_path + "hpc_queue_array.py " + env_path + " 1 " + db_name_with_ext + " " + working_dir + " " + job_id + " " + user_email)


#hold over from reg search
#    print("Run Searches")
##    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " 1 " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email)
#    os.system("python " + script_path + "hpc_queue_array.py " + env_path + " 1 " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email)

    if os.system("python " + script_path + "hpc_error_check.py " + working_dir + " SearchError") != 0:
        raise Exception('Error occurred searching files')

    print("Generate TdReport")
#    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " none " + sys.argv[4] + " " + working_dir + " " + job_id + " " + user_email)
    os.system("python " + script_path + "hpc_generate_reports.py " + env_path + " none  " + sys.argv[4] + " " + working_dir + " " + job_id + " " + user_email)

    if os.system("python " + script_path + "hpc_error_check.py " + working_dir + " GenerateReportError") != 0:
        raise Exception('Error occurred generating tdReport')
		
    print("Annotate PFR")
#    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + sys.argv[4] + " " + working_dir + " " + job_id)
    os.system("python " + script_path + "hpc_annotate_pfr.py " + env_path + " " + sys.argv[4] + " " + working_dir + " " + job_id)

    if os.system("python " + script_path + "hpc_error_check.py " + working_dir + " AnnotateError") != 0:
        raise Exception('Error occurred annotating PFR numbers')

   # print("regex")
   # print(regex)
   # print("regex")

    if sys.argv[3]:
        print("Generate SAS Input")
#        os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + regex + " " +  sys.argv[4] + " " + sys.argv[5] + " " + working_dir + " " + job_id + " " + user_email) 
        os.system("python " + script_path + "hpc_generate_sas.py " + env_path + " " + regex + " " +  sys.argv[4] + " " + sys.argv[5] + " " + working_dir + " " + job_id + " " + user_email)

        if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
            raise Exception('Error occurred generating SAS input sheet')
		
if __name__ == "__main__":
    main()

