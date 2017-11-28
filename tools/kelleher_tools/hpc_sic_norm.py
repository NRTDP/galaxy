import sys, shutil, os.path, subprocess, zipfile
import time
from shutil import copyfile

def main():

    print  sys.argv[1:]
    script_path = "/share/PCEitAdmin/Galaxy/code_sets/standard_3_0/scripts/";

    base_dir = os.path.dirname(os.getcwd())
    inputs_dir = base_dir + "/inputs/"
    print("inputs")
    print(inputs_dir)
    results_folder = ""

    if "FTP" in sys.argv[5]:
        if "old" in sys.argv[5]:
            dataset_folder = "/share/PCEitAdmin/Galaxy/external_users/" + sys.argv[5].split()[1] + "/" + sys.argv[6]
            for file in sys.argv[7].split(','):
                copyfile(dataset_folder + "/" + file, inputs_dir + "/" + file)
                print(dataset_folder + "/" + file)
        if "new" in sys.argv[5]:
            dataset_folder = "/share/NU-PCEDATA/external_users/" + sys.argv[5].split()[1] + "/" + sys.argv[6]
            for file in sys.argv[7].split(','):
                copyfile(dataset_folder + "/" + file, inputs_dir + "/" + file)
                print(dataset_folder + "/" + file)
    else:
        dataset_folder = "/share/krgData/Projects/" + sys.argv[5] + "/" +  sys.argv[6] + "/Samples"
        results_folder = '"/share/krgData/Projects/' + sys.argv[5] + '/' +  sys.argv[6] + '/Results"'
        for file in sys.argv[7].split(','):
            copyfile(dataset_folder + "/" + file, inputs_dir + "/" + file)
    print("results_folder")
    print(results_folder)
    print("results_folder")
    os.system("python " + script_path + "hpc_sic_prepare.py")

    os.system("python " + script_path + "hpc_sic_queue_array.py" + " " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " " + "'" + results_folder + "'") 

if __name__ == "__main__":
    main()

