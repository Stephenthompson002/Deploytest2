import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def deploy_application():
    logging.info("Starting deployment process...")
    try:
        subprocess.run(["git", "pull", "origin", "main"], check=True)
        subprocess.run(["docker-compose", "down"], check=True)
        subprocess.run(["docker-compose", "up", "-d"], check=True)
        logging.info("Deployment completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Deployment failed: {e}")

if __name__ == "__main__":
    deploy_application()
