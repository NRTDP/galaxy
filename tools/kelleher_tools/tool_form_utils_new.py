import os, sys, imp, re



def get_project_folders():
    print("one_a")
    folders = []
    projects = os.listdir("/share/krgData2/Projects/")
#    projects = os.listdir("/share/projects/")
    for i, field_component in enumerate( projects ):
        folders.append( ( field_component, field_component, i == 0 ) )
    return folders

def get_raw_file_folders(project_folder):
    print("two_a")
    raw_file_folders = []
    project_datasets = os.listdir("/share/krgData2/Projects/" + project_folder)
#    project_datasets = os.listdir("/share/projects/" + project_folder)
    for i, field_component in enumerate( project_datasets ):
        raw_file_folders.append( ( field_component, field_component, i == 0 ) )
    return raw_file_folders

def get_ftp_folders(trans, user_email):
    print("three_a")
    email_parts = user_email.split('@')
    print("three_b")
    cleaned_username = re.sub(r'\W+', '', email_parts[0])
    print("three_c")
    email_type = email_parts[1].split('.')[0]
    print("three_d")

    raw_file_folders = []
    ftp_datasets = os.listdir("/share/PCEitAdmin/Galaxy/external_users")
    print("three_e")
    for i, field_component in enumerate( ftp_datasets ):
        print("three_f")
        if field_component == cleaned_username:
            print("three_g")
            raw_file_folders.append( ( "(SFTP_old) " + field_component, "(SFTP_old) " + field_component, i == 0 ) )

    print("three_h")
    nu_pcedata_ftp_datasets = os.listdir("/share/NU-PCEDATA/external_users")
    print("three_i")
    for i, field_component in enumerate( nu_pcedata_ftp_datasets ):
        print("three_j")
        if field_component == cleaned_username:
            print("three_k")
            raw_file_folders.append( ( "(SFTP_new) " + field_component, "(SFTP_new) " + field_component, i == 0 ) )

    print("three_l")
    if "northwestern" in email_parts[1]:
        print("three_m")
        projects = os.listdir("/share/krgData2/Projects/")
        print("three_n")
        for i, field_component in enumerate( projects ):
            print("three_o")
            raw_file_folders.append( ( field_component, field_component, i == 0 ) )

    print("three_p")
    return raw_file_folders


#def get_ftp_folders(trans, user_email):
#    print("user_email2")
#    print(user_email)
#    print("user_email")
#
#    isHoganBool = False
##    decoded_group_id = trans.security.decode_id('f2db41e1fa331b3e')
##    group = trans.sa_session.query( trans.app.model.Group ).get(decoded_group_id)
##    for uga in group.users:
##        if uga.user.email == user_email:
##            print(uga.user.email)
##            print("match found")   
##            isHoganBool = True
#
#    raw_file_folders = []
#    ftp_datasets = os.listdir("/share/PCEitAdmin/Galaxy/external_users/" + user_email)
#    for i, field_component in enumerate( ftp_datasets ):
#        print("ftp project found")
#        raw_file_folders.append( ( "(FTP) " + field_component, "(FTP) " + field_component, i == 0 ) )
#
#    if isHoganBool:
#        projects = os.listdir("/share/krgData2/Projects/")
#        for i, field_component in enumerate( projects ):
#            print("hogan project found")
#            raw_file_folders.append( ( field_component, field_component, i == 0 ) )
#
#    return raw_file_folders

def get_ftp_raw_file_folders(user_email, project_folder):
    print("THERE77777777777777777777777777777777777777777777777777777777777777777777777777777")
    print(project_folder)
    print("THERE")

    email_parts = user_email.split('@')
    print(email_parts[0])
    print("I AM HERE")
    cleaned_username = re.sub(r'\W+', '', email_parts[0])
    print("cleaned")
    print(cleaned_username)



    raw_file_folders = []



    print("three_a1")

    if "FTP" in project_folder:
        print("three_b1")
        if "old" in project_folder:
            print("three_c1")
            project_datasets = os.listdir("/share/PCEitAdmin/Galaxy/external_users/" + project_folder.split()[1])
            for i, field_component in enumerate( project_datasets ):
                print("three_d1")
                raw_file_folders.append( ( field_component, field_component, i == 0 ) )
                print("three_e1")
        if "new" in project_folder:
            print("three_f1")
            project_datasets2 = os.listdir("/share/NU-PCEDATA/external_users/" + project_folder.split()[1])
            print("three_g1")
            for i, field_component in enumerate( project_datasets2 ):
                print("three_h1")
                raw_file_folders.append( ( field_component, field_component, i == 0 ) )
    else:    
        print("three_i1")
        project_datasets = os.listdir("/share/krgData2/Projects/" + project_folder)
        print("three_j1")
        for i, field_component in enumerate( project_datasets ):
            print("three_k1")
            raw_file_folders.append( ( field_component, field_component, i == 0 ) )
            print("three_l1")

    print("three_m1")

    return raw_file_folders

def get_field_components_options( dataset, field_name ):
    print("four_a")
    options = []
    if dataset.metadata is None:
        return options
    if not hasattr( dataset.metadata, 'field_names' ):
        return options
    if dataset.metadata.field_names is None:
        return options
    if field_name is None:
        # The expression validator that helps populate the select list of input
        # datsets in the icqsol_color_surface_field tool does not filter out
        # datasets with no field field_names, so we need this check.
        if len( dataset.metadata.field_names ) == 0:
            return options
        field_name = dataset.metadata.field_names[0]
    flds2 = os.listdir("/share/projects/")
#    field_components = dataset.metadata.field_components.get( field_name, [] )
    for i, field_component in enumerate( flds2 ):
        options.append( ( field_component, field_component, i == 0 ) )
    return options

