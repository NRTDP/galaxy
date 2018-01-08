import xml.etree.ElementTree as ET, sys, subprocess, os, socket, getpass, time, os.path, time, re
from subprocess import Popen, PIPE
from shutil import copyfile

def main():
#    workflow_id_new = sys.argv[5].split('/')[5]
#    print(workflow_id_new)
#    print("Start Monitor")
#    sys.exit(workflow_id_new)


    shared_code_set_path = "/projects/b1035/shared/" + sys.argv[10];
    print(shared_code_set_path)

    database_base_path = "/share/PCEitAdmin/Galaxy/databases/";
    code_set_path = "/share/PCEitAdmin/Galaxy/code_sets/" + sys.argv[10];
    script_path = code_set_path + "/scripts/";

#    print(working_dir)
#    print(folderbase_path)
#    print(working_dir_code_set_path)
#    print(working_dir_script_path)
#    sys.exit("after building paths")


    print(sys.argv[1:])
    print("19")
    print(sys.argv[19])
    print("20")
    print(sys.argv[20])
    print("21")
    print(sys.argv[21])
    if sys.argv[21] == "None":
        sys.exit("Please include files to search")

    base_dir = os.path.dirname(os.getcwd())
    inputs_dir = base_dir + "/inputs/"
    print("inputs")
    print(inputs_dir)

    if "FTP" in sys.argv[19]:
        if "old" in sys.argv[19]:
            dataset_folder = "/share/PCEitAdmin/Galaxy/external_users/" + sys.argv[19].split()[1] + "/" + sys.argv[20]
            for file in sys.argv[21].split(','):
                copyfile(dataset_folder + "/" + file, inputs_dir + "/" + file)
                print(dataset_folder + "/" + file)
        if "new" in sys.argv[19]:          
            dataset_folder = "/share/NU-PCEDATA/external_users/" + sys.argv[19].split()[1] + "/" + sys.argv[20]
            for file in sys.argv[21].split(','):
                copyfile(dataset_folder + "/" + file, inputs_dir + "/" + file)
                print(dataset_folder + "/" + file)
    else:
        dataset_folder = "/share/krgData/Projects/" + sys.argv[19] + "/" +  sys.argv[20] + "/Samples"
        for file in sys.argv[21].split(','):
            copyfile(dataset_folder + "/" + file, inputs_dir + "/" + file)
            print(dataset_folder + "/" + file)


    time.sleep(10)
#    sys.exit("after print arguments")


    print("2")


    print(sys.argv[3])
    print("4")

    print(sys.argv[4])
    print("5")

    print(sys.argv[5])
    print("6")

    print(sys.argv[6])
    print("7")
    print(sys.argv[7])
    print("17")
    print(sys.argv[17])
    print("18")
    print(sys.argv[18])
    print("19")
    print(sys.argv[19])


    


    regex = '"' + sys.argv[3] + '"'
    regex = sys.argv[3]
	
    if not sys.argv[3]:
        regex = "none"
	
    parent = os.path.dirname(sys.argv[4])
			
    grandparent = os.path.dirname(parent)
		
    job_id = os.path.basename(os.path.normpath(grandparent))
		
    working_dir = sys.argv[6]
    base_dir = os.path.dirname(working_dir)
    stdout_path = base_dir + "/stdout"	
    stderr_path = base_dir + "/stderr"	
    user_email = sys.argv[8]
	
    includes_params_file = True

	
    input_pds = "search.pds"

    if sys.argv[13] == "None":
        if sys.argv[17] == "False":
            parameters = code_set_path + "/AllFolderBase/default_parameters.json"
        else:
            parameters = code_set_path + "/AllFolderBase/error_tolerant_parameters.json"
    else:
        parameters = sys.argv[13]    

#    set_parameters_path = "/projects/b1035/shared/scripts/set_fragmentation_method.py"
#    print("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "TEST MOD")
#    os.system("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "TEST MOD")

#    sys.exit(sys.argv[19])


#    print(parameters)
#    sys.exit(sys.argv[1])


    if sys.argv[3] == "True" and sys.argv[14] == "False":
        sys.exit("Cannot perform Quant without FDR. Please check input parameters.")


#    if sys.argv[11] == "standard_3_0":
#        if os.system("python " + script_path + "hpc_validate.py " + code_set_path + " " + parameters + " " + sys.argv[4]) != 0:
#            raise Exception('Error occurred preparing files for search')
#            sys.exit("21.")
#        stdout_open = open(stdout_path, "r")
#        for line in stdout_open:
#            if line.startswith('Error:'):
#                sys.exit(line)

    print("Create Metadata")
#    os.system("python " + script_path + "hpc_echo_sysargv.py " + code_set_path + " " + working_dir + " " + sys.argv[10] + " " + user_email)
    os.system("python " + script_path + "hpc_create_metadata.py " + code_set_path + " " + working_dir + " " + sys.argv[9] + " " + user_email)
    
#    print("Start Monitor")
#    os.system("python " + script_path + "hpc_echo_sysargv.py " + code_set_path + " " + working_dir + " " + job_id + " " + sys.argv[10] + " " + sys.argv[11])
#    running_procs = Popen("python " + script_path + "hpc_monitor.py " + code_set_path + " " + working_dir + " " + job_id + " " + sys.argv[10] + " " + sys.argv[11], shell=True)

#    sys.exit("after monitor")


#    if sys.argv[16] == "True":
#        print("I AM 17 AND I AM TRUE")
#        os.system("python " + script_path + "hpc_create_fasta.py " + code_set_path + " " + sys.argv[1])


#    sys.exit(sys.argv[19])

    print("Copy Database")
    print("Copy Database")
    print("Copy Database")
    os.system("python " + script_path + "hpc_echo_sysargv.py " + code_set_path + " " + database_base_path + sys.argv[1] + " " + working_dir + " " + job_id + " " + user_email + " " + input_pds + " " + sys.argv[1])
#    os.system("python " + script_path + "hpc_copy_database.py " + env_path + " " + sys.argv[2] + " " + working_dir + " " + job_id + " " + user_email + " " + input_pds + " " + sys.argv[2] + " " + parameters)
    os.system("python " + script_path + "hpc_copy_database.py " + code_set_path + " " + sys.argv[1] + " " + working_dir + " " + job_id + " " + user_email + " " + input_pds + " " + sys.argv[1] + " " + parameters)
    print("Copy Database")
    print("Copy Database")
    print("Copy Database")


#    time.sleep(60)
#    sys.exit("after create fasta test")


#    sys.exit("after copy database")

#
#    sys.exit("after building paths")


    folder_base_dir = os.getcwd() + "/FolderBase/"
#    parameters = env_path + "/AllFolderBase/parameters_final_noThreadCrawler.json"
    base=os.path.basename(parameters)
    print(base)
    print(base)
    print(base)
    print(base)
    print(base)
    parameters = folder_base_dir + base   
    print("parameters")
    print(parameters)
    print(parameters)
    print(parameters)
    print(parameters)
    print("parameters")

    if sys.argv[10] == "standard_2_1":
        print "standard 2.1"
        if sys.argv[14] == "False":
            print "standard 2.1 + false"
            if includes_params_file:
                print "standard 2.1 + false + includes file"
                set_parameters_path = "/projects/b1035/shared/scripts/set_fragmentation_method.py"
                print("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "UVPD")
                os.system("python " + set_parameters_path + " " + parameters + " " + "FdrCutoff" + " " + "1000000")

    if sys.argv[2] != "None":
        if includes_params_file:
            set_parameters_path = "/projects/b1035/shared/scripts/set_fragmentation_method.py"
            print("python " + set_parameters_path + " " + parameters + " " + "fixed_modifications" + " " + sys.argv[2])
            os.system("python " + set_parameters_path + " " + parameters + " " + "fixed_modifications" + " " + sys.argv[2])

    if sys.argv[12] != "auto":
        if includes_params_file:
            set_parameters_path = "/projects/b1035/shared/scripts/set_fragmentation_method.py"
            print("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + sys.argv[12])
            os.system("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + sys.argv[12])

            if sys.argv[12] == "hi_res_uvpd_default_search_tree.pds":
                print("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "UVPD")
                os.system("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "UVPD")
            elif sys.argv[12] == "hi_res_ethcd_default_search_tree.pds":
                print("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "EThcD")
                os.system("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + "EThcD")
            else:
                print("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + sys.argv[12])
                os.system("python " + set_parameters_path + " " + parameters + " " + "FragmentationMethodIdOverride" + " " + sys.argv[12])


    if sys.argv[11] != "hi_res":
        print "not hi res"
        print sys.argv[11]
        print "not hi res"
        if includes_params_file:
            set_parameters_path = "/projects/b1035/shared/scripts/set_fragmentation_method.py"
            print("python " + set_parameters_path + " " + parameters + " " + "BioMarker" + " " + "Delete")
            os.system("python " + set_parameters_path + " " + parameters + " " + "BioMarker" + " " + "Delete")
            os.system("python " + set_parameters_path + " " + parameters + " " + "IsLoPrecursor" + " " + "True")

    if sys.argv[18] == "False":
        if includes_params_file:
            set_parameters_path = "/projects/b1035/shared/scripts/set_fragmentation_method.py"
            print("python " + set_parameters_path + " " + parameters + " " + "CScoreCharacterizationCutoff" + " " + "0")
            os.system("python " + set_parameters_path + " " + parameters + " " + "CScoreCharacterizationCutoff" + " " + "0")


#    set_parameters_path = "/projects/b1035/shared/scripts/set_fragmentation_method.py"
#    print("python " + set_parameters_path + " " + parameters + " " + "ValidationFolderPath" + " " + "/projects/b1035/shared/standard_3_0/GoldenValidation")
#    os.system("python " + set_parameters_path + " " + parameters + " " + "ValidationFolderPath" + " " + "/projects/b1035/shared/standard_3_0/GoldenValidation")

    print("Prepare Files for Search")
#    os.system("python " + script_path + "hpc_echo_sysargv.py " + env_path + " " + sys.argv[1] + " " + working_dir + " " + job_id + " " + user_email)
#    os.system("python " + script_path + "hpc_prepare.py")
    os.system("python " + script_path + "hpc_mspathfinder_prepare.py")

    if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
        raise Exception('Error occurred preparing files for search')
#    sys.exit("after prepare")

#    time.sleep(50)
#    sys.exit("end prepare test")

    working_dir = sys.argv[6] + "/";
    folderbase_path = working_dir + "FolderBase/";
    working_code_set_path = folderbase_path + sys.argv[10] + "/";
    working_script_path = working_code_set_path + "scripts/";

    workflow_id_new = sys.argv[5].split('/')[5]
    print(workflow_id_new)
    print("Start Monitor")
#    sys.exit(workflow_id_new)
 

#    os.system("python " + working_script_path + "hpc_echo_sysargv.py " + working_code_set_path + " " + working_dir + " " + job_id + " " + sys.argv[9] + " " + sys.argv[10])
#    running_procs = Popen("python " + working_script_path + "hpc_monitor.py " + shared_code_set_path + " " + working_dir + " " + job_id + " " + sys.argv[9] + " " + sys.argv[10], shell=True)
    print("Start Monitor")

    print("python " + working_script_path + "hpc_echo_sysargv.py " + working_code_set_path + " " + working_dir + " " + job_id + " " + workflow_id_new + " " + sys.argv[10])
    print("Start Monitor")

    os.system("python " + working_script_path + "hpc_echo_sysargv.py " + working_code_set_path + " " + working_dir + " " + job_id + " " + workflow_id_new + " " + sys.argv[10])
    running_procs = Popen("python " + working_script_path + "hpc_monitor.py " + shared_code_set_path + " " + working_dir + " " + job_id + " " + workflow_id_new + " " + sys.argv[10], shell=True)

#    sys.exit(sys.argv[19])

    print("Run Searches")
    #os.system("python " + script_path + "hpc_echo_sysargv.py " + code_set_path + " 1 " + sys.argv[1] + " " + working_dir + " " + job_id + " " + user_email)
    os.system("python " + working_script_path + "hpc_echo_sysargv.py " + working_code_set_path + " 1 " + sys.argv[1] + " " + working_dir + " " + job_id + " " + user_email + " " + sys.argv[16]  + " " + sys.argv[19] + " " + sys.argv[20])
    print("python " + working_script_path + "hpc_echo_sysargv.py " + working_code_set_path + " 1 " + sys.argv[1] + " " + working_dir + " " + job_id + " " + user_email + " " + sys.argv[16]  + " " + sys.argv[19].replace(" ", "") + " " + sys.argv[20].replace(" ", ""))

#    time.sleep(50)
#    sys.exit("after print run database")

    if includes_params_file:
        os.system("python " + working_script_path + "hpc_queue_multiple_array.py " + working_code_set_path + " 1 " + sys.argv[1] + " " + working_dir + " " + job_id + " " + user_email + " " + parameters + " " + sys.argv[16] + " " + sys.argv[19].replace(" ", "") + " " + sys.argv[20].replace(" ", ""))
    else:
        os.system("python " + working_script_path + "hpc_queue_multiple_array.py " + working_code_set_path + " 1 " + sys.argv[1] + " " + working_dir + " " + job_id + " " + user_email + " " + sys.argv[16] + " " + sys.argv[19].replace(" ", "") + " " + sys.argv[20].replace(" ", ""))

    print(os.system("python " + script_path + "hpc_error_check.py " + working_dir))

    if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
        raise Exception('Error occurred searching files')

#    time.sleep(50)
#    sys.exit("AFTER QUEUE ARRAY")

    print("Generate TdReport")
    os.system("python " + script_path + "hpc_echo_sysargv.py " + working_code_set_path + " none " + sys.argv[4] + " " + working_dir + " " + job_id + " " + user_email)
    if includes_params_file:
        os.system("python " + script_path + "hpc_queue_generate_reports.py " + working_code_set_path + " none  " + sys.argv[4] + " " + working_dir + " " + job_id + " " + user_email + " " + parameters)
#        os.system("python " + script_path + "hpc_generate_reports.py " + working_code_set_path + " none  " + sys.argv[4] + " " + working_dir + " " + job_id + " " + user_email + " " + parameters)
    else:
        os.system("python " + script_path + "hpc_queue_generate_reports.py " + working_code_set_path + " none  " + sys.argv[4] + " " + working_dir + " " + job_id + " " + user_email)
#        os.system("python " + script_path + "hpc_generate_reports.py " + working_code_set_path + " none  " + sys.argv[4] + " " + working_dir + " " + job_id + " " + user_email)

    print(os.system("python " + script_path + "hpc_error_check.py " + working_dir))


    if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
        raise Exception('Error occurred generating tdReport')
		
    print("Annotate PFR")
    os.system("python " + script_path + "hpc_echo_sysargv.py " + code_set_path + " " + sys.argv[4] + " " + working_dir + " " + job_id)
    os.system("python " + script_path + "hpc_annotate_pfr.py " + code_set_path + " " + sys.argv[4] + " " + working_dir + " " + job_id)

    if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
        raise Exception('Error occurred annotating PFR numbers')

    if sys.argv[3] == "True":
        print("Generate SAS Input")
        os.system("python " + script_path + "hpc_echo_sysargv.py " + code_set_path + " " + regex + " " +  sys.argv[5] + " " + sys.argv[4] + " " + working_dir + " " + job_id + " " + user_email) 
        if includes_params_file:
            os.system("python " + script_path + "hpc_generate_sas.py " + code_set_path + " " + regex + " " +  sys.argv[5] + " " + sys.argv[4] + " " + working_dir + " " + job_id + " " + user_email + " " + parameters)
        else:
            os.system("python " + script_path + "hpc_generate_sas.py " + code_set_path + " " + regex + " " +  sys.argv[5] + " " + sys.argv[4] + " " + working_dir + " " + job_id + " " + user_email)

        if os.system("python " + script_path + "hpc_error_check.py " + working_dir) != 0:
            raise Exception('Error occurred generating SAS input sheet')
		
if __name__ == "__main__":
    main()

#    time.sleep(50)
#    sys.exit("after copy database")
