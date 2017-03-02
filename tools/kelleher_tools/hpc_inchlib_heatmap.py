import xml.etree.ElementTree as ET, sys, subprocess, os, socket, getpass, time, os.path, time, shutil
from subprocess import Popen, PIPE


def main():
#   print  sys.argv[1:]

    env_path = "/projects/b1035/shared/" + sys.argv[6];

    script_path = env_path + "/GalaxyHPCSearch/";

    json_path = sys.argv[7] + "/output.json"
 
    print("Generate JSON")
    create_json_command = "python " + script_path + "hpc_create_json.py " + sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[5] + " " + json_path
    print(create_json_command)

    os.system(create_json_command)

    print("Generate HTML")
    create_html_command = "python " + script_path + "hpc_create_html.py " + sys.argv[4] + " " + json_path + " " + sys.argv[8]
    print(create_html_command)

    os.system(create_html_command)

#    shutil.copyfile("/projects/b1035/shared/PGAFF_columns_added.html", sys.argv[8])
		
if __name__ == "__main__":
    main()



##metadata_path = sys.srgv[1]
##data_path = sys.srgv[2]
##custer_algo = sys.srgv[3]
##working_path = sys.srgv[4]

#metadata_path = "path to metadata csv"
#data_path = "path to data csv"
#custer_algo = "both"
#working_path = "path to working"
#output_json_path = working_path + "output.json"


#inchlid_cluster_command = "python " + path to inchlib.py + "-dd -md"
#print(inchlib_cluster_command)

#os.system(create_json_command)
