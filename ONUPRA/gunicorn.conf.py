bind = '127.0.0.1:8000'
workers = 4
user = 'john'
group = 'gunicorn-group'
timeout = 120
errorlog_file = '/var/log/gunicorn/error.log'
accesslog_file = '/var/log/gunicorn/access.log'