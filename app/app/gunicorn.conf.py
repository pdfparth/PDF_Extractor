accesslog = "/var/log/langchain_fast_api.access.log"
bind = "0.0.0.0:8082"
#capture_output = True
errorlog = "/var/log/langchain_fast_api.error.log"
loglevel = "info"
workers = 1
worker_class = "uvicorn.workers.UvicornWorker"