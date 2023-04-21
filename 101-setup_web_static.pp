# puppet version of our setup of nginx for web static
package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  content => template('yourmodule/nginx/default.erb'),
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/var/www/html/custom_404.html':
  content => 'Ceci n\'est pas une page',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

file { '/data/web_static/releases/test/index.html':
  content => 'simple content, to test your Nginx configuration',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  require => [
    File['/data/web_static/releases/test/'],
    File['/data/web_static/shared/'],
  ],
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  notify => Service['nginx'],
}

file { '/etc/nginx/sites-available/default':
  content => template('yourmodule/nginx/default.erb'),
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  hasstatus  => true,
}

exec { 'set ownership of /data':
  command => '/bin/chown -R ubuntu:ubuntu /data/',
  onlyif  => '/usr/bin/test "$(stat -c %U:%G /data/)" = "ubuntu:ubuntu"',
}
