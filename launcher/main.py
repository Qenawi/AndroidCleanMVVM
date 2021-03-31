import yaml
import os


def main():
    m = MainI()
    m.init()
    m.build_test_demo()


class MainI:
    # MARK : Constants
    package_name_key = "packgeName"
    pattern_name_key = "pattern"

    # MARK : itesm
    package_name = ""
    pattern_name = ""
    owner_name = ""
    company_name = ""
    signature_name = ""

    def read_yaml(self):
        with open(r'build_rules.yaml') as file:
            fruits_list = yaml.load(file, Loader=yaml.FullLoader)
        self.package_name = fruits_list[self.package_name_key]
        self.package_name = fruits_list[self.pattern_name_key]

    def init(self):
        self.read_yaml()

    def build_dir(self, pathx):
        path = os.getcwd()
        print(path)
        try:
            os.mkdir(path + "/output/" + pathx)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)

    def build_test_demo(self):
        dic = ["viewmodel", "view", "model", "router", "protocol"]
        for i in dic:
            self.build_dir(pathx=i)


if __name__ == "__main__":
    main()
