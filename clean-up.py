import sys, os, shutil, subprocess

# Delete directories in /var/lib/jenkins/workspaces that Jenkins fails to remove during project delete/rename.
# WARNING! For testing comment out the delete(rmtree) command or set (preview_mode = "true")

preview_mode = "false"
build_dir = "/var/lib/jenkins/builds/"
workspace_dir = "/var/lib/jenkins/workspaces/"
exclude = ['.snapshot']

for arg in sys.argv:
    if arg == "-p":
        preview_mode = "true"
    if arg == "workspace":
        workspace_dir = "/var/lib/jenkins/workspace/"

if preview_mode == "false":
    print("\nNOT PREVIEW MODE!!!\n")
else:
    print("\nPREVIEW MODE!\n")

# Use subprocess to run shell command to get disk usage in human readable format.
def du(path):
    return subprocess.check_output(['du','-sh', path]).split()[0].decode('utf-8')

os.chdir(build_dir)
listBuildDir = filter(os.path.isdir, os.listdir(os.getcwd()))
# Convert list to set. Note: intersection command only possible on sets
set_build_dir = set(listBuildDir)
print(build_dir + " has", len(set_build_dir), "directories.\n")

os.chdir(workspace_dir)
list_workspace_dir = filter(os.path.isdir, os.listdir(os.getcwd()))
# Convert list to set. Note: intersection command only possible on sets
set_workspace_dir = set(list_workspace_dir)
print(workspace_dir + " has", len(set_workspace_dir), "directories.\n")

# Delete directories in 'exclude' from 'set_workspace_dir'
for i in exclude:
    if i in set_workspace_dir:
        print("  ****  Remove " + i + " from delete list.  ****")
        set_workspace_dir.remove(i)

# To reduce search time get common directories in 'builds' and 'workspaces' to search through.
common_dirs = set_build_dir.intersection(set_workspace_dir)
for i in common_dirs:
    if i in set_workspace_dir:
        # Delete NPM_TMP and NPM_CACHE directories from 'set_workspace_dir'
        npmCache = i + "_LOCAL_NPM_CACHE"
        npmTmp = i + "_LOCAL_NPM_TMP"
        if npmCache in set_workspace_dir:
            print("  ****  Remove " + npmCache + " from delete list.  ****")
            set_workspace_dir.remove(npmCache)
        if npmTmp in set_workspace_dir:
            print("  ****  Remove " + npmTmp + " from delete list.  ****")
            set_workspace_dir.remove(npmTmp)

print(workspace_dir + " has", len(set_workspace_dir), "directories that will be intersected.\n")

# If a directory is in 'workspaces' but not in 'builds' it should be removed
intersection = set_workspace_dir - set_build_dir
if preview_mode == "false":
    print("Deleting" , len(intersection) , "directories in " + workspace_dir + "\n")
else:
    print("PREVIEW Deleting" , len(intersection) , "directories in " + workspace_dir + "\n")

for i in intersection:
    print(workspace_dir + i + "     Size" , du(workspace_dir + i))
    if preview_mode == "false":
        shutil.rmtree(workspace_dir + i)

os.chdir(workspace_dir)
list_workspace_dir = filter(os.path.isdir, os.listdir(os.getcwd()))
set_workspace_dir = set(list_workspace_dir)
print("\n", len(set_workspace_dir), "directories remaining in: " + workspace_dir)
print("clean-up SUCCESS!\n")
