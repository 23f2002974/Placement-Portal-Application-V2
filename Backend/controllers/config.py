class Config:

    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///placement_portal.db'
    SECURITY_PASSWORD_SALT = 'your-password-salt'
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'