import xml.etree.ElementTree as ET, sys, subprocess, os, socket, getpass, time, os.path, time, re
from subprocess import Popen, PIPE
from shutil import copyfile

def main():
    env_path = "/projects/b1035/shared/" + sys.argv[11];

    base_dir = os.path.dirname(os.getcwd())
    inputs_dir = base_dir + "/inputs/"
    print("inputs")
    print(inputs_dir)

    if "FTP" in sys.argv[17]:
        if "old" in sys.argv[17]:
            dataset_folder = "/share/PCEitAdmin/Galaxy/external_users/" + sys.argv[17].split()[1] + "/" + sys.argv[18]
            for file in sys.argv[19].split(','):
                copyfile(dataset_folder + "/" + file, inputs_dir + "/" + file)
                print(dataset_folder + "/" + file)
        if "new" in sys.argv[17]:
            dataset_folder = "/share/NU-PCEDATA/external_users/" + sys.argv[17].split()[1] + "/" + sys.argv[18]
            for file in sys.argv[19].split(','):
                copyfile(dataset_folder + "/" + file, inputs_dir + "/" + file)
                print(dataset_folder + "/" + file)
    else:
        dataset_folder = "/share/krgData/Projects/" + sys.argv[17] + "/" +  sys.argv[18] + "/Samples"
        for file in sys.argv[19].split(','):
            copyfile(dataset_folder + "/" + file, inputs_dir + "/" + file)




    print(sys.argv[1:])
    print("1")
    print(sys.argv[1])

    print("2")

    print(sys.argv[2])
    print("3")

    print(sys.argv[3])
    print("4")

    print(sys.argv[4])
    print("5")

    print(sys.argv[5])
    print("6")

    print(sys.argv[6])
    print("7")

    print(sys.argv[7])
    
#    sys.exit(sys.argv[1])


    regex = '"' + sys.argv[4] + '"'
    regex = sys.argv[4]
	
    if not sys.argv[4]:
        regex = "none"
	
    parent = os.path.dirname(sys.argv[5])
			
    grandparent = os.path.dirname(parent)
		
    job_id = os.path.basename(os.path.normpath(grandparent))
		
    working_dir = sys.argv[7]
    base_dir = os.path.dirname(working_dir)
    stdout_path = base_dir + "/stdout"	
    stderr_path = base_dir + "/stderr"	
    user_email = sys.argv[9]
	
    includes_params_file = True

    script_path = env_path + "/GalaxyHPCSearch/";
	
#    input_pds = "search.pds"
    input_pds = "hi_res_default_search_tree_new.pds"

    if sys.argv[14] == "None":
        parameters = env_path + "/AllFolderBase/parameters_final_noThreadCrawler.json"
    else:
        parameters = sys.argv[14]    

    if sys.argv[11] == "standard_2_1":
        if sys.argv[4] == "True" and sys.argv[15] == "False":
            sys.exit("Cannot perform Quant without FDR. Please check input parameters.")
        if os.system("python " + script_path + "hpc_validate.py " + env_path + " " + parameters + " " + sys.argv[4]) != 0:
            raise Exception('Error occurred preparing files for search')
            sys.exit("21.")
        stdout_open = open(stdout_path, "r")
        for line in stdout_open:
            if line.startswith('Error:'):
                sys.exit(line)

    print("Create Metadata")
    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + working_dir + " " + sys.argv[10] + " " + user_email)
    os.system("python " + script_path + "hpc_create_metadata.py " + env_path + " " + working_dir + " " + sys.argv[10] + " " + user_email)
    
    print("Start Monitor")
    #os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + working_dir + " " + job_id + " " + sys.argv[10] + " " + sys.argv[11])

    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + working_dir + " " + job_id + " " + sys.argv[10] + " " + sys.argv[11])
    running_procs = Popen("python " + script_path + "hpc_monitor.py " + env_path + " " + working_dir + " " + job_id + " " + sys.argv[10] + " " + sys.argv[11], shell=True)

    print("Copy Database")
    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email + " " + input_pds + " " + sys.argv[2])
    os.system("python " + script_path + "hpc_copy_database.py " + env_path + " " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email + " " + input_pds + " " + sys.argv[2] + " " + parameters)

    folder_base_dir = os.getcwd() + "/FolderBase/"
#    parameters = env_path + "/AllFolderBase/parameters_final_noThreadCrawler.json"

    parameters = folder_base_dir + "parameters_final_noThreadCrawler.json"

    for file in os.listdir(folder_base_dir):
        if file.endswith(".dat"):
            print("dat file")
            print(file)
            print("dat file")
            os.rename(folder_base_dir + file, parameters)

    if sys.argv[11] == "standard_2_1":
        print "standard 2.1"
        if sys.argv[15] == "False":
            print "standard 2.1 + false"
            if includes_params_file:
                print "standard 2.1 + false + includes file"
                set_parameters_path = "/projects/b1035/shared/scripts/set_fragmentation_method.py"
                print("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "UVPD")
                os.system("python " + set_parameters_path + " " + parameters + " " + "FdrCutoff" + " " + "1000000")

    if sys.argv[3] != "None":
        if includes_params_file:
            set_parameters_path = "/projects/b1035/shared/scripts/set_fragmentation_method.py"
            print("python " + set_parameters_path + " " + parameters + " " + "fixed_modifications" + " " + sys.argv[3])
            os.system("python " + set_parameters_path + " " + parameters + " " + "fixed_modifications" + " " + sys.argv[3])

    print("sys.argv-13")
    print(sys.argv[13])
    print("sys.argv-13")

    if sys.argv[13] != "auto":
#        sys.exit(sys.argv[13])
        if includes_params_file:
            set_parameters_path = "/projects/b1035/shared/scripts/set_fragmentation_method.py"
            print("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + sys.argv[13])
            os.system("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + sys.argv[13])

#            if sys.argv[13] == "hi_res_uvpd_default_search_tree.pds":
#                print("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "UVPD")
#                os.system("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "UVPD")
#            elif sys.argv[13] == "hi_res_ethcd_default_search_tree.pds":
#                print("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "EThcD")
#                os.system("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "EThcD")
#            else:
#                print("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + sys.argv[13])
#                os.system("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + sys.argv[13])

    if sys.argv[12] != "hi_res":
        print "not hi res"
        print sys.argv[12]
        print "not hi res"
        if includes_params_file:
            set_parameters_path = "/projects/b1035/shared/scripts/set_fragmentation_method.py"
            print("python " + set_parameters_path + " " + parameters + " " + "BioMarker" + " " + "Delete")
            os.system("python " + set_parameters_path + " " + parameters + " " + "BioMarker" + " " + "Delete")
            os.system("python " + set_parameters_path + " " + parameters + " " + "IsLoPrecursor" + " " + "True")

    
#    sys.exit("end his res test")

    print("Prepare Files for Search")
#    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + sys.argv[1] + " " + working_dir + " " + job_id + " " + user_email)
    os.system("python " + script_path + "hpc_prepare.py")

    if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
        raise Exception('Error occurred preparing files for search')

    #time.sleep(50)

    print("Run Searches")
    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " 1 " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email)
    if includes_params_file:
        os.system("python " + script_path + "hpc_queue_array.py " + env_path + " 1 " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email + " " + parameters)
    else:
        os.system("python " + script_path + "hpc_queue_array.py " + env_path + " 1 " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email)

    print(os.system("python " + script_path + "hpc_error_check.py " + working_dir))

    if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
        raise Exception('Error occurred searching files')

    print("Generate TdReport")
    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " none " + sys.argv[5] + " " + working_dir + " " + job_id + " " + user_email)
    if includes_params_file:
        os.system("python " + script_path + "hpc_generate_reports.py " + env_path + " none  " + sys.argv[5] + " " + working_dir + " " + job_id + " " + user_email + " " + parameters)
    else:
        os.system("python " + script_path + "hpc_generate_reports.py " + env_path + " none  " + sys.argv[5] + " " + working_dir + " " + job_id + " " + user_email)

    print(os.system("python " + script_path + "hpc_error_check.py " + working_dir))


    if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
        raise Exception('Error occurred generating tdReport')
		
    print("Annotate PFR")
    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + sys.argv[5] + " " + working_dir + " " + job_id)
    os.system("python " + script_path + "hpc_annotate_pfr.py " + env_path + " " + sys.argv[5] + " " + working_dir + " " + job_id)

    if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
        raise Exception('Error occurred annotating PFR numbers')

    if sys.argv[4] == "True":
        print("Generate SAS Input")
        os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + regex + " " +  sys.argv[6] + " " + sys.argv[5] + " " + working_dir + " " + job_id + " " + user_email) 
        if includes_params_file:
            os.system("python " + script_path + "hpc_generate_sas.py " + env_path + " " + regex + " " +  sys.argv[6] + " " + sys.argv[5] + " " + working_dir + " " + job_id + " " + user_email + " " + parameters)
        else:
            os.system("python " + script_path + "hpc_generate_sas.py " + env_path + " " + regex + " " +  sys.argv[6] + " " + sys.argv[5] + " " + working_dir + " " + job_id + " " + user_email)

        if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
            raise Exception('Error occurred generating SAS input sheet')
		
if __name__ == "__main__":
    main()

