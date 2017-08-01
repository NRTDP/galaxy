import os, sys


def get_project_folders():
    folders = []
    projects = os.listdir("/share/krgData2/Projects/")
    projects.sort(reverse=True)
    for i, field_component in enumerate( projects ):
        folders.append( ( field_component, field_component, i == 0 ) )
    return folders

def get_raw_file_folders(project_folder):
    print(project_folder + "-1")
    raw_file_folders = []
    print(project_folder + "-2")
    project_datasets = os.listdir("/share/krgData2/Projects/" + project_folder)
    print(project_folder + "-3")
    project_datasets.sort()
    print(project_folder + "-4")
    for i, field_component in enumerate( project_datasets ):
        print(project_folder + "-5")
        print field_component
        raw_file_folders.append( ( field_component, field_component, i == 0 ) )
        print(project_folder + "-6")
    print(project_folder + "-7")
    return raw_file_folders

#def get_ftp_folders(user_email):
#    raw_file_folders = []
#    ftp_datasets = os.listdir("/share/PCEitAdmin/Galaxy/files/" + user_email)
#    ftp_datasets.sort(reverse=True)
##    ftp_datasets = os.listdir("/share/galaxy/files/" + user_email)
#    for i, field_component in enumerate( ftp_datasets ):
#        raw_file_folders.append( ( field_component, field_component, i == 0 ) )
#    return raw_file_folders

#def get_ftp_raw_file_folders(user_email, project_folder):
#    raw_file_folders = []
#    project_datasets = os.listdir("/share/PCEitAdmin/Galaxy/files/" + user_email + "/" + project_folder)
#    project_datasets.sort()
##    project_datasets = os.listdir("/share/projects/" + project_folder)
#    for i, field_component in enumerate( project_datasets ):
#        raw_file_folders.append( ( field_component, field_component, i == 0 ) )
#    return raw_file_folders

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

