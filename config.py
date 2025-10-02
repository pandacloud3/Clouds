from my import db_password, db_host

class Config:
    # JWT_TOKEN_LOCATION = ["headers"]
    # JWT_HEADER_NAME = "Authorization"
    # JWT_HEADER_TYPE = "Bearer"
    # JWT_SECRET_KEY = jwt_secret_key

    DB_USER = "admin"
    DB_PASSWORD = db_password
    DB_HOST = db_host
    DB_PORT = 3306
    DB_NAME = "database-1"
    # SQLALCHEMY_D# SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_DATABASE_URI = "mysql://root:VladPanda777@localhost:3306/SQL server"