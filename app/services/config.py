import orjson
import os
import utils


class Config:
    def __init__(self):
        super().__init__()
        print(os.path.join(utils.CONFIG_DIR + "config.json"))
        # Try to read the config file, if there is none copy the dummy one
        try:
            with open(os.path.join(utils.CONFIG_DIR + "config.json"), "rb") as file:
                self.configuration = orjson.loads(file.read())
                print("Loaded configuration")
        except:
            print("can't find file")

    def getGitlabURL(self):
        return self.configuration["gitlab_url"]

    def getPrivateToken(self):
        return self.configuration["private_token"]

    def getCert(self):
        return self.configuration["cert_name"]
