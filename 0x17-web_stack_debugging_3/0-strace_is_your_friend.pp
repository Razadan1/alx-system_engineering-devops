# A puppet code that fixes 

exec {
    'fix-wordpress-server-issue':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php'
}