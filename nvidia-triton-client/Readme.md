# Command to start inference server
docker run -d -p 8000:8000 -p 8001:8001 -p 8002:8002 -v /Users/vsatpathy/Desktop/off_POCs/test/server-main/docs/examples/model_repository:/models nvcr.io/nvidia/tritonserver:20.06-py3 tritonserver --model-repository=/models --model-control-mode=poll --repository-poll-secs=5

# To run Prometheus metrics server
docker run -d -p 9090:9090 -v /Users/vsatpathy/Desktop/off_POCs/test/nvidia-triton-client/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus