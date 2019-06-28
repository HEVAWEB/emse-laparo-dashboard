<?php
namespace Deployer;

require 'recipe/common.php';

$project_name = isset($_ENV['CI_PROJECT_NAME']) ? $_ENV['CI_PROJECT_NAME'] : 'dashboard-template';
$project_namespace = isset($_ENV['CI_PROJECT_NAMESPACE']) ? $_ENV['CI_PROJECT_NAMESPACE'] : 'web';
$project_path = "/var/www/$project_name";

$supervisor = <<<EOL
"[program:$project_name]
command                 = $project_path/shared/venv/bin/gunicorn --chdir $project_path/current -b unix://$project_path/gunicorn.sock index:app.server
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

// Hosts
host('production')
    ->hostname('172.16.11.59')
    ->user('hevadev')
    ->set('deploy_path', $project_path)
    ->set('branch', 'master');

task('python_env', function() {
    within('{{release_path}}', function () {
        run('python3 -m venv ./venv');
        run('source ./venv/bin/activate && pip install gunicorn && deactivate');
        run("./venv/bin/python -m pip install --no-cache-dir -r requirements.txt");
    });
});

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

task('protect_access', function() {
    if (file_exists('identifiants.csv')) {
        $rows = array_map(function($file_content) {
            return str_getcsv($file_content, ';');
        }, file('identifiants.csv'));
        if (sizeof($rows) > 1) {
            $contents = "";
            foreach ($rows as $key => $row) {
                if (sizeof($row) <> 2) {
                    throw new \Exception("Le fichier identifiant.csv ne respecte pas le format 'login;password'");
                }
                if ($key > 0) {
                    $login = $row[0];
                    $password = $row[1];
                    $hash = base64_encode(sha1($password, true));
                    $contents .=  "$login:{SHA}$hash" . PHP_EOL;
                }
            }
            run("echo \"$contents\" > {{release_path}}/.htpasswd");
        } else {
            writeln('Aucun identifiants trouvés dans le ficher "identifants.csv" !');
        }
    } else {
        writeln('Aucun fichier "identifants.csv" trouvé !');
    }
});

desc('Deploying ' . $project_name);
task('deploy', [
    'deploy:info',
    'deploy:prepare',
    'deploy:lock',
    'deploy:release',
    'deploy:update_code',
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
