import xml.etree.ElementTree as ET, sys, subprocess, os, socket, getpass, time, os.path, time
from subprocess import Popen, PIPE

def main():
    db_name = sys.argv[2].split('dataset_')[-1].split('.')[0]
    db_name_with_ext = db_name + ".db"

    print(sys.argv[1:])

    regex = '"' + sys.argv[3] + '"'
    print("regex")
    print(regex)
    print("regex")

    print("sys.argv[4]")
    print(sys.argv[4])
    print("sys.argv[4]")


    regex = sys.argv[3]
	
    if not sys.argv[3]:
        print("regex_in_if")
        regex = "none"

    print("regex")
    print(regex)
    print("regex")

	
    parent = os.path.dirname(sys.argv[4])
			
    grandparent = os.path.dirname(parent)
		
    job_id = os.path.basename(os.path.normpath(grandparent))
		
    working_dir = sys.argv[6]
    base_dir = os.path.dirname(working_dir)
    stdout_path = base_dir + "/stdout"
    stderr_path = base_dir + "/stderr"

    user_email = sys.argv[8]
	
    env_path = "/projects/b1035/shared/" + sys.argv[10];

#    if sys.argv[13] == "None" and sys.argv[10] == "standard_2_0":
#        raise Exception('Required parameters file not included.')
    includes_params_file = sys.argv[13] != "None"
#    includes_params_file = True


    if includes_params_file:
        parameters = sys.argv[13]
    else:
        parameters = env_path + "/AllFolderBase/parameters_final_noThreadCrawler.json"

    print("parameters")
    print(parameters)
    print("parameters")

    script_path = env_path + "/GalaxyHPCSearch/";


    if sys.argv[10] == "standard_2_1":
        if sys.argv[3] == "True" and sys.argv[14] == "False":
            sys.exit("Cannot perform Quant without FDR. Please check input parameters.")
        print ("validate")
        print ("python " + script_path + "hpc_validate.py " + env_path + " " + parameters + " " + sys.argv[3])
        print ("validate")
        if os.system("python " + script_path + "hpc_validate.py " + env_path + " " + parameters + " " + sys.argv[3]) != 0:
            raise Exception('Error occurred validating files for search')
            sys.exit("21.")
        stdout_open = open(stdout_path, "r")
        for line in stdout_open:
            if line.startswith('Error:'):
                sys.exit(line)


#    sys.exit()
    


	


#    print("includes_params_file")
#    print(sys.argv[13])
#    print(includes_params_file)
#    print("includes_params_file")

    input_pds = "search.pds"

    print("Create Metadata")
    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + working_dir + " " + sys.argv[9] + " " + user_email)
    os.system("python " + script_path + "hpc_create_metadata.py " + env_path + " " + working_dir + " " + sys.argv[9] + " " + user_email)
    
    print("Start Monitor")
    #os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + working_dir + " " + job_id + " " + sys.argv[9] + " " + sys.argv[10])

    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + working_dir + " " + job_id + " " + sys.argv[9] + " " + sys.argv[10])
    running_procs = Popen("python " + script_path + "hpc_monitor.py " + env_path + " " + working_dir + " " + job_id + " " + sys.argv[9] + " " + sys.argv[10], shell=True)

    print("Create Database")
    print("Create Database")
    print("Create Database")
    print("Create Database")
    print("Create Database")
    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email + " " + input_pds + " " + sys.argv[2])
    print("python " + script_path + "hpc_create_database.py " + env_path + " " + sys.argv[2] + " " + db_name + " " + job_id + " " + "false")
    print("Create Database")
    print("Create Database")
    print("Create Database")



    os.system("python " + script_path + "hpc_create_database.py " + env_path + " " + sys.argv[2] + " " + db_name + " " + job_id + " " + "false")

    #sys.exit("after db creation")


    print("Copy Database")
    os.system("python " + script_path + "hpc_copy_database.py " + env_path + " " + db_name_with_ext + " " + working_dir + " " + job_id + " " + user_email + " " + input_pds + " " + db_name_with_ext + " " + parameters)
#    os.system("python " + script_path + "hpc_copy_database.py " + env_path + " " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email + " " + input_pds + " " + sys.argv[2] + " " + parameters)

    folder_base_dir = os.getcwd() + "/FolderBase/"
#    parameters = folder_base_dir + "parameters_final_noThreadCrawler.json"

    if sys.argv[10] == "standard_2_1":
        print "standard 2.1"
        if sys.argv[14] == "False":
            print "standard 2.1 + false"
            if includes_params_file:
                print "standard 2.1 + false + includes file"
                set_parameters_path = "/projects/b1035/shared/scripts/set_fragmentation_method.py"
                print("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "UVPD")
                os.system("python " + set_parameters_path + " " + parameters + " " + "FdrCutoff" + " " + "1000000")

    if sys.argv[12] != "auto":
        if includes_params_file:
            set_parameters_path = "/projects/b1035/shared/scripts/set_fragmentation_method.py"
            print("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "UVPD")
            os.system("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "UVPD")

    if sys.argv[11] != "hi_res_default_search_tree.pds":
        if includes_params_file:
            set_parameters_path = "/projects/b1035/shared/scripts/set_fragmentation_method.py"
            print("python " + set_parameters_path + " " + parameters + " " + "BioMarker" + " " + "Delete")
            os.system("python " + set_parameters_path + " " + parameters + " " + "BioMarker" + " " + "Delete")



    print("Prepare Files for Search")
    os.system("python " + script_path + "hpc_prepare.py")

    if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
        raise Exception('Error occurred preparing files for search')

    print("Run Searches")
    print("Run Searches")
    print("Run Searches")
    print("Run Searches")
    print("Run Searches")
    print("Run Searches")
    print("Run Searches")
    print("Run Searches")
#    os.system("python " + script_path + "hpc_queue_array.py " + env_path + " 1 " + db_name_with_ext + " " + working_dir + " " + job_id + " " + user_email)
    if includes_params_file:
        print("params included")
        print("python " + script_path + "hpc_queue_array.py " + env_path + " 1 " + db_name_with_ext + " " + working_dir + " " + job_id + " " + user_email + " " + parameters)
        os.system("python " + script_path + "hpc_queue_array.py " + env_path + " 1 " + db_name_with_ext + " " + working_dir + " " + job_id + " " + user_email + " " + parameters)
    else:
        print("params not included")
        os.system("python " + script_path + "hpc_queue_array.py " + env_path + " 1 " + db_name_with_ext + " " + working_dir + " " + job_id + " " + user_email)
    print("Run Searches")
    print("Run Searches")
    print("Run Searches")
    print("Run Searches")
    print("Run Searches")
    print("Run Searches")
    print("Run Searches")

    print(os.system("python " + script_path + "hpc_error_check.py " + working_dir))

    if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
        raise Exception('Error occurred searching files')

    print("Generate TdReport")
    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " none " + sys.argv[4] + " " + working_dir + " " + job_id + " " + user_email)
    if includes_params_file:
        os.system("python " + script_path + "hpc_generate_reports.py " + env_path + " none  " + sys.argv[4] + " " + working_dir + " " + job_id + " " + user_email + " " + parameters)
    else:
        os.system("python " + script_path + "hpc_generate_reports.py " + env_path + " none  " + sys.argv[4] + " " + working_dir + " " + job_id + " " + user_email)

    print(os.system("python " + script_path + "hpc_error_check.py " + working_dir))


    if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
        raise Exception('Error occurred generating tdReport')
		
    print("Annotate PFR")
    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + sys.argv[4] + " " + working_dir + " " + job_id)
    os.system("python " + script_path + "hpc_annotate_pfr.py " + env_path + " " + sys.argv[4] + " " + working_dir + " " + job_id)

    if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
        raise Exception('Error occurred annotating PFR numbers')

    if sys.argv[3] == "True":
        print("Generate SAS Input")
        os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + regex + " " +  sys.argv[4] + " " + sys.argv[5] + " " + working_dir + " " + job_id + " " + user_email) 
        if includes_params_file:
            os.system("python " + script_path + "hpc_generate_sas.py " + env_path + " " + regex + " " +  sys.argv[4] + " " + sys.argv[5] + " " + working_dir + " " + job_id + " " + user_email + " " + parameters)
        else:
            os.system("python " + script_path + "hpc_generate_sas.py " + env_path + " " + regex + " " +  sys.argv[4] + " " + sys.argv[5] + " " + working_dir + " " + job_id + " " + user_email)

        if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
            raise Exception('Error occurred generating SAS input sheet')
		
if __name__ == "__main__":
    main()

