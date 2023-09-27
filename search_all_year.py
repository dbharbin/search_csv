import subprocess
import search_string 

###
# Each of the following are run once at a time with results moved to excel file for charting
###
#download_file="dragonboard410c/qualcomm/android/\*/dragonboard410c_sdcard_install_android-118.zip"
#download_file="dragonboard410c/linaro/debian/\*/Image"
#download_file="dragonboard410c/qualcomm/android/"
#download_file="dragonboard410c/qualcomm/android/\*/boot.img.tar.xz"
#download_file="dragonboard410c/qualcomm/android/\*/source-manifest.xml"
#download_file="dragonboard410c/linaro/openembedded/\*/rpb/rpb-\*-image-dragonboard-410c-\*.rootfs.manifest"
#download_file="dragonboard820c/qualcomm/firmware/linux-board-support-package\*"
#download_file="/dragonboard820c/qualcomm/firmware"
#download_file="dragonboard845c/linaro/debian/\*/boot-linaro\*.img.gz"
#download_file="dragonboard845c/linaro/openembedded/\*/source-manifest.xml"

## This one captures both /rpb and /rpb-wayland subdirectories
download_file="rb5/linaro/openembedded/\*/boot-\*rb5\*.img"


subprocess.call("python3 search_string.py /Users/donharbin/Downloads/dragonboard_or_rb_downloads.csv 2020- {}".format(download_file),shell=True)
subprocess.call("python3 search_string.py /Users/donharbin/Downloads/dragonboard_or_rb_downloads.csv 2021- {}".format(download_file),shell=True)
subprocess.call("python3 search_string.py /Users/donharbin/Downloads/dragonboard_or_rb_downloads.csv 2022- {}".format(download_file),shell=True)
subprocess.call("python3 search_string.py /Users/donharbin/Downloads/dragonboard_or_rb_downloads.csv 2023- {}".format(download_file),shell=True)
