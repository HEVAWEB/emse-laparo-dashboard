<?php
namespace Deployer;

require 'recipe/common.php';
require 'recipe/heva.php';

$project_name = isset($_ENV['CI_PROJECT_NAME']) ? slug($_ENV['CI_PROJECT_NAME']) : 'dashboard-template';
$project_namespace = isset($_ENV['CI_PROJECT_NAMESPACE']) ? $_ENV['CI_PROJECT_NAMESPACE'] : 'web';
$project_path = "/var/www/$project_name";

$supervisor = <<<EOL
"[program:$project_name]
command                 = $project_path/current/venv/bin/gunicorn --chdir $project_path/current -b unix://$project_path/gunicorn.sock index:app.server
numprocs                = 1
autostart               = true
autorestart             = true
user                    = hevadev
stdout_logfile          = $project_path/shared/logs/supervisor.log
stdout_logfile_maxbytes = 1MB
stderr_logfile          = $project_path/shared/logs/supervisor-error.log
stderr_logfile_maxbytes = 1MB
stopasgroup=true
stopsignal=QUIT"
EOL;

// Project name
set('application', $project_name);
set('repository', "git@gitlab.hevaweb.com:$project_namespace/$project_name.git");

// Shared files/dirs between deploys
set('shared_files', ['']);
set('shared_dirs', ['logs']);
set('writable_dirs', ['logs']);
set('allow_anonymous_stats', false);
set('keep_releases', 1);

// Hosts
host('production')
    ->hostname('172.16.11.55')
    ->user('hevadev')
    ->set('deploy_path', $project_path)
    ->set('branch', 'master');

task('supervisor', function() use ($supervisor, $project_name) {
    $supervisor_conf_path = "/home/hevadev/.supervisor/$project_name.conf";
    if (run("cat $supervisor_conf_path; true") == "") {
        run("echo $supervisor > $supervisor_conf_path");
        run("supervisorctl reload");
        run("supervisorctl update");
    } else {
        run("supervisorctl restart $project_name");
    }
});

task('upload', function () {
    $env_path = __DIR__ . DIRECTORY_SEPARATOR . '.env';
    $style_path = __DIR__ . DIRECTORY_SEPARATOR . 'assets' . DIRECTORY_SEPARATOR . 'style.css';
    if (file_exists($env_path)) {
        upload($env_path, '{{release_path}}');
    }
    upload($style_path, '{{release_path}}' . DIRECTORY_SEPARATOR . 'assets' . DIRECTORY_SEPARATOR);
});


desc('Deploying ' . $project_name);
task('deploy', [
    'deploy:info',
    'deploy:prepare',
    'deploy:lock',
    'deploy:release',
    'deploy:update_code',
    'upload',
    'python_env',
    'deploy:shared',
    'deploy:writable',
    'deploy:clear_paths',
    'deploy:symlink',
    'protect_access',
    'supervisor',
    'deploy:unlock',
    'cleanup',
    'success'
]);

after('deploy:failed', 'deploy:unlock');
