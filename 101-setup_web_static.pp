# Puppet manifest to configure web server

exec{'update':
    command => '/usr/bin/apt-get -y update',
}

package{'nginx':
    ensure  => 'installed',
    require => Exec['update'],
}

file{['/data',
      '/data/web_static',
      '/data/web_static/releases',
      '/data/web_static/shared',
      '/data/web_static/releases/test',]:
    ensure  => 'directory',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    recurse => true,
}

file{'/data/web_static/releases/test/index.html':
    content => "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>",
    require => File['/data'],
}

file{'/data/web_static/current':
    ensure  => 'link',
    target  => '/data/web_static/releases/test',
    require => File['/data'],
}

file_line{'hbnb_static':
    ensure   => 'present',
    path     => '/etc/nginx/sites-available/default',
    after    => 'server_name localhost;',
    multiple => false,
    line     => '	location /hbnb_static {
    	     alias /data/web_static/current/;
	     }',
    require  => Package['nginx']
}

service{'nginx':
    ensure  => running,
    require => Package['nginx'],
}