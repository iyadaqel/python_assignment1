from configparser import ConfigParser

def createConfig():
    """
    Create a config file
    """
    config = ConfigParser()
    config.add_section("database")
    config.set("database", "url", "../pos.db")


    config.add_section("firsttime")
    config.set("firsttime" , "db-installed" , "0")


    with open("settings.ini", "w") as config_file:
        config.write(config_file)

