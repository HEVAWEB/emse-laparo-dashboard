<?php
namespace Deployer;

require 'recipe/common.php';
require 'recipe/heva.php';

set('application', slug($_ENV['CI_PROJECT_NAME']));
set('repository', "git@gitlab.hevaweb.com:" . $_ENV['CI_PROJECT_NAMESPACE'] . "/" . get('application') .".git");
set('shared_files', ['']);
set('shared_dirs', ['logs']);
set('writable_dirs', ['logs']);
set('allow_anonymous_stats', false);
set('keep_releases', 1);
set('domain', 'hevaweb.com');
set('ovh_target', '91.134.26.25');

host('production')
    ->hostname('172.16.11.55')
    ->user('hevadev')
    ->set('deploy_path', "/var/www/" . get('application'))
    ->set('branch', 'master');

task('deploy', [
    'dashboard:deploy'
]);

after('deploy:failed', 'deploy:unlock');
