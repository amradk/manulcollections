#!/bin/bash
set -e

# This script will install all necessary dependencies to run kronos-backend
# - install python3 and pip
# - install mysql-server if not present
# - install python modules
# - restore kronos_db from dump
# !!! ATTENTION this script still can't create separate user kronos-backend !!!
# !!! ATTENTION if mysql-server is not present script will install it and ask you some questions !!!

function check_prerequisites() {

    # update package list
    sudo apt update -y

    local CH_PYTHON_STUFF=$(check_python)
    local CH_MYSQL_STUFF=$(check_mysql)
    local INSTALL_STR=""

    if [ ${CH_PYTHON_STUFF} -eq 0 ]
    then
        echo 'Looks like Python stuff is in place.'
    elif [ ${CH_PYTHON_STUFF} -eq 1 ]
    then
        echo 'We are need to install python3 package'
        INSTALL_STR="${INSTALL_STR} python3"
    elif [ ${CH_PYTHON_STUFF} -eq 2 ]
    then
        echo "We are need to install pip for python."
        INSTALL_STR="${INSTALL_STR} python3-pip"
    elif [ ${CH_PYTHON_STUFF} -eq 3 ]
    then
        echo 'We are need to install python3 and pip for python3'
        INSTALL_STR="${INSTALL_STR} python3 python3-pip"
    fi

    # install python stuff
    if [ "x${INSTALL_STR}" != "x" ]
    then
        sudo apt install --no-install-recommends -y ${INSTALL_STR}
    fi

    if [ ${CH_MYSQL_STUFF} -eq 0 ]
    then
        echo 'Looks like mysql-server is in place.'
    elif [ ${CH_MYSQL_STUFF} -eq 1 ]
    then
        echo 'We are need to install mysql-server.'
        echo 'Install MySQL repo'
        install_mysql_repo
        install_mysql_server ${DB_PASS}
    fi
    #continue to check MySQL
    install_python_modules
    check_mysql_conection ${DB_USER} ${DB_PASS} ${DB_SRV}

}

function install_mysql_repo() {
    local CUR_DIR=$(pwd)
    cd /tmp
    wget https://dev.mysql.com/get/mysql-apt-config_0.8.14-1_all.deb
    sudo dpkg -i mysql-apt-config*
    sudo apt update
    cd ${CUR_DIR}
}

function install_mysql_server () {
    local ROOT_PASS=$1
    export DEBIAN_FRONTEND="noninteractive"

    sudo debconf-set-selections <<EOF
mysql-apt-config mysql-apt-config/select-server select mysql-5.7
mysql-community-server mysql-community-server/root-pass password $DEFAULTPASS
mysql-community-server mysql-community-server/re-root-pass password $DEFAULTPASS
EOF

    sudo apt install -y mysql-server
    sudo mysql_secure_installation
} 

# pass mysql user as first argument
# pass mysql user password as second argument
# pass mysql host as third argument
function check_mysql_arguments() {
    local RES=0
    local MYSQL_USER=$1
    local MYSQL_PASS=$2
    local MYSQL_HOST=$3

    if [ "x${MYSQL_USER}" == "x" ]
    then
        RES=1
    fi
    if [ "x${MYSQL_PASS}" == "x" ]
    then
        RES=2
    fi
    if [ "x${MYSQL_HOST}" == "x" ]
    then
        RES=3
    fi

    if [ ${RES} -eq 1 ]
    then
        echo "MySQL user is not present! Can't continue, aborting!"
        exit 1
    elif [ ${RES} -eq 2 ]
    then
        echo "Password for MySQL user is not present! Can't continue, aborting!"
        exit 1
    elif [ ${RES} -eq 3 ]
    then
        echo "Host for MySQL is not present! Can't continue, aborting!"
        exit 1
    fi
}

# pass mysql user as first argument
# pass mysql user password as second argument
# pass mysql host as third argument
function check_mysql_conection() {
    local MYSQL_USER=$1
    local MYSQL_PASS=$2
    local MYSQL_HOST=$3

    check_mysql_arguments ${MYSQL_USER} ${MYSQL_PASS} ${MYSQL_HOST}

    mysql -u ${MYSQL_USER} -h ${MYSQL_HOST} -p${MYSQL_PASS} -Ns -e "SELECT 1"
    if [ $? -ne 0 ]
    then
        echo "Can't connect to MySQL server! Aborting!"
        exit 1
    fi
}

function check_python() {
    local RES=0
    local CH_PYTHON=$(dpkg -l | awk '{print $2}' | grep "^python3-min*")
    local CH_PIP=$(dpkg -l | awk '{print $2}' | grep "^python3-pip")

    if [ "x${CH_PYTHON}" == "x" ]
    then
        #There is no python3 on host
        RES=1
    fi

    if [ "x${CH_PIP}" == "x" ]
    then
        #There is no pip for python3 on host
        RES=2
    fi

    if [ "x${CH_PYTHON}" == "x" ] && [ "x${CH_PIP}" == "x" ]
    then
        #There is no python3 and no pip for python3 on host
        RES=3
    fi

    echo ${RES}
}

function install_python_modules() {
    local REQUIREMENTS_TXT='requirements.txt'

    pip3 install -r ./${REQUIREMENTS_TXT}
}

function check_mysql() {
    local RES=0
    local CH_MYSQL_SERVER=$(dpkg -l | awk '{print $2}' | grep "^mysql-server")

    if [ "x${CH_MYSQL_SERVER}" == "x" ]
    then
        #There is no mysql server on host
        RES=1
    fi

    echo ${RES}
}

function usage() {
   
    echo "usage: $programname <-h> [-P] <-u> <-p>"
    echo "  -h      MySQL host to connect"
    echo "  -P      MySQL port"
    echo "  -u      MySQL user wirh read permissions"
    echo "  -p      MySQL user password"
    echo "Example: bootstrap.sh -h localhost -u itest -p password"
    exit 1

}

if [[ $# -eq 0 ]]
then
  usage
fi

while [[ $# -gt 0 ]]
do
    key="${1}"
    case ${key} in
    -h| --host)
      #Server where backups is stored
      DB_SRV="${2}"
      if [ "x${DB_SRV}" == "x" ]
      then
        DB_SRV='127.0.0.1'
        shift
      else
        shift
        shift
      fi 
    ;;
    -P|--port)
      #MySQL port to restore backup
      PORT="${2}"
      if [ "x${PORT}"  == "x" ]
      then
        PORT="3306"
        shift
      else
        shift
        shift 
      fi 
    ;;
    -u|--user)
      #MySQL user to restore backup
      DB_USER="${2}"
      if [ "x${DB_USER}" == "x" ]
      then
        DB_USER="root"
        shift
      else
        shift
        shift
      fi
    ;;
    -p|--password)
      #MySQL password to restore backup
      DB_PASS="${2}"
      if [ "x${DB_PASS}" == "x" ]
      then
        DB_PASS='password'
      	shift
      else
        shift
        shift
      fi
    ;;
    --help)
      usage
    ;;
    *)
        echo "Unknown option passed"
        usage  # unknown option
        shift # past argument
    ;;
    esac
    #shift
done

check_prerequisites