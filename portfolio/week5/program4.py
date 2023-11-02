if __name__ == "__main__":
    import sys
    import requests

    def check_link(sys.argv):
        response = requests.get(sys.argv)
        if response.status_code == 200:
            print("The website is working.")
        else:
            print("The website is not working.")