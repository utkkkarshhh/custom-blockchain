from settings import Settings

def main():
    print(f"SECRET_KEY: {Settings.Secrets.SECRET_KEY}")
    print(f"DEBUG: {Settings.Secrets.DEBUG}")

if __name__ == '__main__':
    main()
