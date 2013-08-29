
mkdir /home/web/inasafe-docs
sudo cp scripts/inasafe-docs.conf.templ /etc/apache2/sites-available/inasafe-docs.conf
sudo rpl "inasafe-docs.linfiniti.com" "inasafe-docs.localhost" /etc/apache2/sites-available/inasafe-docs.conf
sudo a2ensite inasafe-docs.conf
sudo a2enmod rewrite
sudo service apache2 reload

if not contains('/etc/hosts', 'inasafe-docs.localhost')
    append('/etc/hosts', 127.0.0.1 inasafe-docs.localhost)

chmod +x scripts/post_translate.sh
scripts/post_translate.sh
cp -r docs/output/html/* /home/web/inasafe-docs
cp -r docs/output/pdf /home/web/inasafe-docs/
cp scripts/.htaccess /home/web/inasafe-docs

cp scripts/directory-listing-*.html /home/web/inasafe-docs/en/_static/

