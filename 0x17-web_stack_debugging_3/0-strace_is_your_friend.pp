# A puppet code that fixes a word press server

exec {
    'fix-wordpress-server-issue':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php'
    path    => ['usr/bin/sed'],
}
