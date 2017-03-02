import os, sys, imp, re

email = "mshort@chem.wisc.edu"
email_parts = email.split('@')
cleaned_username = re.sub(r'\W+', '', email_parts[0])
email_type = email_parts[1].split('.')[0]

raw_file_folders = []
ftp_datasets = os.listdir("/share/PCEitAdmin/Galaxy/external_users")
for i, field_component in enumerate( ftp_datasets ):
    if field_component == cleaned_username:
        print(i)
        print(field_component)
        raw_file_folders.append( ( "(SFTP) " + field_component, "(SFTP) " + field_component, i == 0 ) )

nu_pcedata_ftp_datasets = os.listdir("/share/NU-PCEDATA/external_users")
print("nu_pcedata_ftp_datasets")
print(nu_pcedata_ftp_datasets)
print("nu_pcedata_ftp_datasets")
for i, field_component in enumerate( nu_pcedata_ftp_datasets ):
    if field_component == cleaned_username:
        print(i)
        print(field_component)
        raw_file_folders.append( ( "(SFTP) " + field_component, "(SFTP) " + field_component, i == -1 ) )
print("raw_file_folders")
print(raw_file_folders)
print("raw_file_folders")
