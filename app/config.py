class Config(object):
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIN_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['admin1@fitfriendster.com', 'admin2@fitfriendster.com']


    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')