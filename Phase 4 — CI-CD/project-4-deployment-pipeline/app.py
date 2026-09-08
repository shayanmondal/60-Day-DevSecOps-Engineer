import sys

VERSION = "1.0.0"

def main():
    print(f"Deploying Application Version: {VERSION}")
    # Simulate a health check failure if version is corrupted
    if VERSION == "broken":
        print("HEALTH CHECK FAILED: Crashing deployment!")
        sys.exit(1)
    print("HEALTH CHECK PASSED: Deployment successful!")

if __name__ == "__main__":
    main()
