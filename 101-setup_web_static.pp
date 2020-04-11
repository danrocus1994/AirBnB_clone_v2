# configure server using puppet
exec {'install_nginx':
  path    => ['/usr/bin', '/bin'],
  command => 'sudo apt-get -y update; sudo apt-get -y install nginx',
}
-> exec {'create_data_dir':
  path    => ['/usr/bin', '/bin'],
  command => 'sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared',
}
-> exec {'create_symlink':
  path    => ['/usr/bin', '/bin'],
  command => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current'
}
-> exec {'create_fake_index':
  path    => ['/usr/bin', '/bin'],
  command => 'echo "This has been harder than i thought" | sudo tee /data/web_static/releases/test/index.html'
}
-> exec {'give_owner_and_group':
  path    => ['/usr/bin', '/bin'],
  command => 'chwon -R ubuntu:ubuntu /data/'
}
-> exec {'give_owner_and_group':
  path    => ['/usr/bin', '/bin'],
  command => 'sudo sed -i \'43i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\
  \n\t\t autoindex on;\n\t}\n\' /etc/nginx/sites-available/default',
}

-> exec { 'cmd_7':
  require => Exec['cmd_6'],
  path    => '/usr/bin:/bin',
  command => 'sudo service nginx restart',
}