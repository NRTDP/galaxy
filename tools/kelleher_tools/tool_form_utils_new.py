import os, sys, imp, re



def get_project_folders():
    folders = []
    projects = os.listdir("/share/krgData2/Projects/")
#    projects = os.listdir("/share/projects/")
    for i, field_component in enumerate( projects ):
        folders.append( ( field_component, field_component, i == 0 ) )
    return folders

def get_raw_file_folders(project_folder):
    raw_file_folders = []
    project_datasets = os.listdir("/share/krgData2/Projects/" + project_folder)
#    project_datasets = os.listdir("/share/projects/" + project_folder)
    for i, field_component in enumerate( project_datasets ):
        raw_file_folders.append( ( field_component, field_component, i == 0 ) )
    return raw_file_folders

def get_ftp_folders(trans, user_email):
    email_parts = user_email.split('@')
    cleaned_username = re.sub(r'\W+', '', email_parts[0])
    email_type = email_parts[1].split('.')[0]

    raw_file_folders = []
    ftp_datasets = os.listdir("/share/PCEitAdmin/Galaxy/external_users")
    for i, field_component in enumerate( ftp_datasets ):
        if field_component == cleaned_username:
            raw_file_folders.append( ( "(SFTP_old) " + field_component, "(SFTP_old) " + field_component, i == 0 ) )

    nu_pcedata_ftp_datasets = os.listdir("/share/NU-PCEDATA/external_users")
    for i, field_component in enumerate( nu_pcedata_ftp_datasets ):
        if field_component == cleaned_username:
            raw_file_folders.append( ( "(SFTP_new) " + field_component, "(SFTP_new) " + field_component, i == 0 ) )

    if "northwestern" in email_parts[1]:
        projects = os.listdir("/share/krgData2/Projects/")
        for i, field_component in enumerate( projects ):
            raw_file_folders.append( ( field_component, field_component, i == 0 ) )

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
    print("THERE")
    print(project_folder)
    print("THERE")

    email_parts = user_email.split('@')
    print(email_parts[0])
    print("I AM HERE")
    cleaned_username = re.sub(r'\W+', '', email_parts[0])
    print("cleaned")
    print(cleaned_username)



    raw_file_folders = []




    if "FTP" in project_folder:
        if "old" in project_folder:
            project_datasets = os.listdir("/share/PCEitAdmin/Galaxy/external_users/" + project_folder.split()[1])
            for i, field_component in enumerate( project_datasets ):
                raw_file_folders.append( ( field_component, field_component, i == 0 ) )
        if "new" in project_folder:
            project_datasets2 = os.listdir("/share/NU-PCEDATA/external_users/" + project_folder.split()[1])
            for i, field_component in enumerate( project_datasets2 ):
                raw_file_folders.append( ( field_component, field_component, i == 0 ) )
    else:    
        project_datasets = os.listdir("/share/krgData2/Projects/" + project_folder)
        for i, field_component in enumerate( project_datasets ):
            raw_file_folders.append( ( field_component, field_component, i == 0 ) )

    return raw_file_folders

def get_field_components_options( dataset, field_name ):
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

