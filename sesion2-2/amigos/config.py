# Configuraciones para distintas formas de lanzar la aplicación

class Config:
    "Clase base de la que derivarán las demás"
    # Pueden ponerse valores comunes a todos los entornos de ejecución
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://amigosuser:amigospass@172.18.0.2/amigosdb"
    
class DevelopmentConfig(Config):
    "Configuración de desarrollo"
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    "Configuración de producción"
    DEBUG = False


# Diccionario que asocia un nombre con una configuración
app_config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig
        }