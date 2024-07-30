class Config:
    CELERY_BROKER_URL = 'redis://localhost:6379/0'  #  gerenciamento de tarefas
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # Backend de resultados
    PARCELVOY_API_KEY = 'coloca_uma_chave'