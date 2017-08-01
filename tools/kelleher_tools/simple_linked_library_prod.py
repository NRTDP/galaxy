import sys, re
from bioblend import galaxy

print("sadkljflksdjflkdsflkdflkff")

print(sys.argv[1:])
print("sadkljflksdjflkdsflkdflkff")

gi = galaxy.GalaxyInstance(url='http://galaxy.kelleher.northwestern.edu:8081', key='3d52eee6f6d19fd68ba91d5de040fbce')

#create library with full permissions for admin user and load linked files
#lib = gi.libraries.create_library("one" ,sys.argv[5] , sys.argv[6])
lib = gi.libraries.create_library(sys.argv[2] + ':' + sys.argv[3] ,sys.argv[5] , sys.argv[6])
lib_id = lib.get('id')
#print(lib_id)

roles = gi.roles.get_roles()
admin_role_id = ""
for n, i in enumerate(roles):
    if i.get('name') == sys.argv[9].replace("__at__" , "@"):
        admin_role_id = i.get('id')

print("sadkljflksdjflkdsflkdflkff")
groups = gi.groups.get_groups()
for n, i in enumerate(groups):
    print("n")
print("sadkljflksdjflkdsflkdflkff")



print(admin_role_id)

print(admin_role_id)

per = gi.libraries.set_library_permissions( lib['id'], access_in=[admin_role_id], modify_in=[admin_role_id], add_in=[admin_role_id], manage_in=[admin_role_id] )

print(sys.argv[1] + '/' + sys.argv[2] + '/' + sys.argv[3])

#gi.libraries.upload_file_from_server( lib['id'], '"' + sys.argv[1].replace("__at__" , "@") + '/' + sys.argv[2] + '/Samples' + '"', None, 'auto', '?', 'link-to-files')

#gi.libraries.upload_file_from_server( lib['id'], sys.argv[1].replace("__at__" , "@") + '/' + sys.argv[2] + '/Samples', None, 'auto', '?', 'link-to-files')


if "SFTP" in sys.argv[2]: 
#    print("FTP")
#    print(sys.argv[2].split()[1].replace("__at__" , "@"))
#    gi.libraries.upload_from_galaxy_filesystem( lib['id'], '/share/PCEitAdmin/Galaxy/external_users' + '/' + sys.argv[1].replace("__at__" , "@") + '/' +  sys.argv[2].split()[1].replace("__at__" , "@") + '/' + sys.argv[3] + '/Samples', None, 'auto', '?', 'link-to-files')
    print("SFTP")
    print(sys.argv[2].split()[1].replace("__at__" , "@"))
    email_parts = sys.argv[1].split('@')
    print(email_parts[0])
    cleaned_username = re.sub(r'\W+', '', email_parts[0])
#    gi.libraries.upload_from_galaxy_filesystem( lib['id'], '/home/jbg669/external_users' + '/' + cleaned_username + '/' +  sys.argv[2].split()[1].replace("__at__" , "@") + '/' + sys.argv[3] + '/Samples', None, 'auto', '?', 'link-to-files')
#    gi.libraries.upload_from_galaxy_filesystem( lib['id'], '/share/PCEitAdmin/Galaxy/external_users' + '/' + cleaned_username + '/' +  sys.argv[2].split()[1].replace("__at__" , "@") + '/' + sys.argv[3] + '/Samples', None, 'auto', '?', 'link-to-files')
    if "_old" in sys.argv[2]:
        gi.libraries.upload_from_galaxy_filesystem( lib['id'], '/share/PCEitAdmin/Galaxy/external_users' + '/' + cleaned_username + '/' + sys.argv[3] , None, 'auto', '?', 'link-to-files')
    if "_new" in sys.argv[2]:
        gi.libraries.upload_from_galaxy_filesystem( lib['id'], '/share/NU-PCEDATA/external_users' + '/' + cleaned_username + '/' + sys.argv[3] , None, 'auto', '?', 'link-to-files')
else:
    print("NON-FTP") 
    gi.libraries.upload_file_from_server( lib['id'], sys.argv[2] + '/' + sys.argv[3] + '/Samples', None, 'auto', '?', 'link-to-files')
#    gi.libraries.upload_from_galaxy_filesystem( lib['id'], '/share/PCEitAdmin/Galaxy/external_users' + '/' + sys.argv[1].replace("__at__" , "@") + '/' +  sys.argv[2].replace("__at__" , "@") + '/' + sys.argv[3] + '/Samples', None, 'auto', '?', 'link-to-files')

#print('/share/krgData2/Projects/' +  sys.argv[1].replace("__at__" , "@") + '/' + sys.argv[2] + '/Samples')

