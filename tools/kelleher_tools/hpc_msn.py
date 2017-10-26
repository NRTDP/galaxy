import xml.etree.ElementTree as ET, sys, subprocess, os, socket, getpass, time, os.path, time, shutil
from subprocess import Popen, PIPE


def main():
#    print  sys.argv[1:]

#    sys.exit("after history path")

    script_path = "/share/PCEitAdmin/Galaxy/code_sets/standard_3_0/scripts/";


    os.system("python " + script_path + "hpc_msn_prepare.py")

    #outputs in working
    output_dir = os.getcwd() + "/Output/"

    #raw files in working
    raw_files_dir = os.getcwd() + "/RawFiles/"

    parameters_file = os.getcwd() + "/MSN/parameters.json"

    set_parameter_path = "/share/PCEitAdmin/Galaxy/scripts/set_parameter.py"
    os.system("python " + set_parameter_path + " " + parameters_file + " " + "ScoreThreshold" + " " + sys.argv[2])
    os.system("python " + set_parameter_path + " " + parameters_file + " " + "MaxSubnetworkSize" + " " + sys.argv[3])
    os.system("python " + set_parameter_path + " " + parameters_file + " " + "SpectralCountThreshold" + " " + sys.argv[4])
    os.system("python " + set_parameter_path + " " + parameters_file + " " + "kMaxDifference" + " " + sys.argv[5])
    os.system("python " + set_parameter_path + " " + parameters_file + " " + "kMaxRelativeDifference" + " " + sys.argv[6])
    os.system("python " + set_parameter_path + " " + parameters_file + " " + "SameMassCosineCutoff" + " " + sys.argv[7])
    os.system("python " + set_parameter_path + " " + parameters_file + " " + "kRTmin" + " " + sys.argv[8])
    os.system("python " + set_parameter_path + " " + parameters_file + " " + "kRTmax" + " " + sys.argv[9])
    os.system("python " + set_parameter_path + " " + parameters_file + " " + "HalfIsolationWidth" + " " + sys.argv[10])
    os.system("python " + set_parameter_path + " " + parameters_file + " " + "kMassOfAProton" + " " + sys.argv[11])
    os.system("python " + set_parameter_path + " " + parameters_file + " " + "precursorIntensityCutoff" + " " + sys.argv[12])
    os.system("python " + set_parameter_path + " " + parameters_file + " " + "MaxPercentBasePeak" + " " + sys.argv[13])
    os.system("python " + set_parameter_path + " " + parameters_file + " " + "kMS2Tolerance" + " " + sys.argv[14])

    print("BEFORE")
    os.system("python " + script_path + "hpc_echo_sysargv.py"  + " " + sys.argv[15] + " " + sys.argv[16])
    os.system("python " + script_path + "hpc_msn_queue_array.py" + " " + sys.argv[15] + " " + sys.argv[16])
    print("AFTER")

#sys.argv[2]

#"$input_raw_files" "$score_threshold" "$max_subnetwork_size" "$spectral_count_threshold" "$k_max_difference" "$k_max_relative_difference" "$same_mass_cosine_cutoff" "$k_rt_min" "$k_rt_max" "$half_isolation_width" 
#"$kMass_of_a_roton" "$precursor_intensity_cutoff" "$max_percent_base_peak" "$k_ms2_tolerance" "$annotation_database"</command>




    #copy code set to working
   
    #update parameters file in code set 

    #queue up job
    #input directory = input directory , output = working , parameters = parameters in code set , cores = 8 , annotation db path = annotation file in inputs 

if __name__ == "__main__":
    main()

