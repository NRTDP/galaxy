import sys, os
from bioblend import galaxy

print("HEREHEHRHE")

project_datasets = os.listdir("/share/krgData2/Projects/" + sys.argv[1])
project_datasets.sort()
for i, field_component in enumerate( project_datasets ):
    print field_component

print(sys.argv[1:])

gi = galaxy.GalaxyInstance(url='http://galaxy.kelleher.northwestern.edu:8081', key='e3354d108c2ed425b2d5d7c3f2e9e52d')

#create library with full permissions for admin user and load linked files
#lib = gi.libraries.create_library("one" ,sys.argv[4] , sys.argv[5])
lib = gi.libraries.create_library(sys.argv[1] + ':' + sys.argv[2] ,sys.argv[4] , sys.argv[5])
lib_id = lib.get('id')
#print(lib_id)

roles = gi.roles.get_roles()
admin_role_id = ""
for n, i in enumerate(roles):
    if i.get('name') == sys.argv[8].replace("__at__" , "@"):
        admin_role_id = i.get('id')

print(admin_role_id)

print(admin_role_id)

per = gi.libraries.set_library_permissions( lib['id'], access_in=[admin_role_id], modify_in=[admin_role_id], add_in=[admin_role_id], manage_in=[admin_role_id] )

print(sys.argv[1] + '/' + sys.argv[2])

#gi.libraries.upload_file_from_server( lib['id'], '"' + sys.argv[1].replace("__at__" , "@") + '/' + sys.argv[2] + '/Samples' + '"', None, 'auto', '?', 'link-to-files')
gi.libraries.upload_file_from_server( lib['id'], sys.argv[1].replace("__at__" , "@") + '/' + sys.argv[2] + '/Samples', None, 'auto', '?', 'link-to-files')
#gi.libraries.upload_from_galaxy_filesystem( lib['id'], '/share/krgData2/Projects/' +  sys.argv[1].replace("__at__" , "@") + '/' + sys.argv[2] + '/Samples', None, 'auto', '?', 'link-to-files')

print('/share/krgData2/Projects/' +  sys.argv[1].replace("__at__" , "@") + '/' + sys.argv[2] + '/Samples')

