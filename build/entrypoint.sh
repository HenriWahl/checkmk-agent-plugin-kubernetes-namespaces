#!/usr/bin/env bash
# ©2024 henri.wahl@ukdd.de
# CLI steps done like described in https://docs.checkmk.com/latest/en/mkps.html

set -e

SOURCE=/source
MKP_DIR=${SOURCE}/mkp
CMK=/omd/sites/cmk

EXTENSION=kubernetes_namespaces

# root of site
cd ${CMK}/local

# copy lib stuff for bakery
cp -Rv ${MKP_DIR}/lib/* ./lib/

# go to other files
cd share/check_mk

# copy non-lib
cp -Rv ${MKP_DIR}/agents .
cp -Rv ${MKP_DIR}/web .

# needed for package config file creation
# has to be done by site user
su - cmk -c "/omd/sites/cmk/bin/mkp template ${EXTENSION}"

# otherwise /source is not accepted
git config --global --add safe.directory ${SOURCE}

# modify extension config file with correct version number, author etc.
/modify-extension.py ${SOURCE} ${CMK}/tmp/check_mk/${EXTENSION}.manifest.temp

# avoid errors like:
# Error removing file /omd/sites/cmk/local/lib/python3/cmk/base/cee/plugins/bakery/kubernetes_namespaces.py: [Errno 13] Permission denied: '/omd/sites/cmk/local/lib/python3/cmk/base/cee/plugins/bakery/yum.py'
chmod go+rw ${CMK}/local/lib/python3/cmk/base/cee/plugins/bakery

# also to be done by site user is packaging the mkp file
su - cmk -c "/omd/sites/cmk/bin/mkp package ${CMK}/tmp/check_mk/${EXTENSION}.manifest.temp"

# copy created extension package back into volume
cp ${CMK}/var/check_mk/packages_local/*.mkp ${SOURCE}

# let runner user access the created mkp file which is owned by root now
chmod go+r ${SOURCE}/*.mkp