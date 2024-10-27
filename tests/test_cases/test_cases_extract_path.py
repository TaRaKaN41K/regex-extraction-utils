test_cases = [
    ('--path.settings C:\\Users\\Administrator\\ELK\\logstash-8.11.1\\config --another.key qweqweqwe',
     'C:\\Users\\Administrator\\ELK\\logstash-8.11.1\\config'),
    ('--path.settings "C:\\Program Files\\Elastic" --another.key qweqweqwe',
     'C:\\Program Files\\Elastic'),
    ('--path.settings C:\\Program Files\\Elastic --another.key qweqweqwe',
     'C:\\Program Files\\Elastic'),

    ('--path.settings "/home/user/test_cases/config" --another.key example',
     '/home/user/test_cases/config'),
    ('--path.settings /opt/software/bin --another.key somevalue',
     '/opt/software/bin'),
    ('--path.settings eeeeeeen --another.key qweqweqwe',
     None),
    ('--another.key "/path/without/path.settings"',
     None),
    ('',
     None),
    ('--path.settings C:\\Users\\Administrator\\Documents\\example-file --another.key value',
     'C:\\Users\\Administrator\\Documents\\example-file'),
    ('--path.settings C:\\Users\\Administrator\\Documents\\example-file --another.key --another.value',
     'C:\\Users\\Administrator\\Documents\\example-file'),
    ('--path.settings "C:\\Users\\Administrator\\Documents\\" --another.key qweqweqwe',
     'C:\\Users\\Administrator\\Documents\\'),
    ('--path.settings C:\\Users\\Admin@strator\\test_cases#123 --another.key value',
     'C:\\Users\\Admin@strator\\test_cases#123'),
    ('--path.settings "C:\\Users\\Administrator\\some\\path\\" --another.key value',
     'C:\\Users\\Administrator\\some\\path\\'),
    ('--path.settings   C:\\Program Files\\SomeApp --another.key value',
     'C:\\Program Files\\SomeApp'),
    ('--path.settings "/home/user/test_cases/!@#$%^&*()" --another.key value',
     '/home/user/test_cases/!@#$%^&*()'),
    ('--path.settings C:\\Some\\Path --another.key value --path.settings /another/path --extra.key value',
     'C:\\Some\\Path'),
    ('--path.settings --another.key value',
     None),
]