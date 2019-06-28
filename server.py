import config

connexion_app = config.connexion_app

connexion_app.add_api(config.swagger_path)

if __name__ == "__main__":
    connexion_app.run(debug=True)

