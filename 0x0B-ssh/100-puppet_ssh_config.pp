#!/usr/bin/env bash
# set up your client SSH configuration file so that you can connect to a server without typing a password.

file { '/etc/ssh/ssh_config':
        ensure => file,
content =>"

        #SSH client configuration
        host*
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
        ",
}