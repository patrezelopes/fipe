from app.services.worker import app

if __name__ == "__main__":
    argv = ['worker', '-l', 'info', '-B', "-s", "/tmp/celerybeat-schedule"]
    app.worker_main(argv)

