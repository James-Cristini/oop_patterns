from __future__ import print_function
import time


class Platform(object):

    def stop_systems(self):
        raise NotImplementedError("Stop Systems method not yet implemented")

    def start_systems(self):
        raise NotImplementedError("Start Systems method not yet implemented")

    def health_check_systems(self):
        raise NotImplementedError("Health Check Systems method not yet implemented")


class WebServer(Platform):

    __nodes = ['web_node_a', 'web_node_b', 'web_node_c']

    def stop_systems(self):
        for system in self.__nodes:
            print("Stopping WebServer system: {0}".format(system))
            time.sleep(0.1)

    def start_systems(self):
        for system in self.__nodes:
            print("Starting WebServer system: {0}".format(system))
            time.sleep(0.1)

    def health_check_systems(self):
        for system in self.__nodes:
            print("Checking WebServer system: {0}".format(system))
            time.sleep(0.1)


class Firewall(Platform):

    __nodes = ['fw_node_a', 'fw_node_b', 'fw_node_c']

    def stop_systems(self):
        for system in self.__nodes:
            print("Stopping Firewall system: {0}".format(system))
            time.sleep(0.1)

    def start_systems(self):
        for system in self.__nodes:
            print("Starting Firewall system: {0}".format(system))
            time.sleep(0.1)

    def health_check_systems(self):
        for system in self.__nodes:
            print("Checking Firewall system: {0}".format(system))
            time.sleep(0.1)


class AppServer(Platform):

    __nodes = ['app_node_a', 'app_node_b', 'app_node_c']

    def stop_systems(self):
        for system in self.__nodes:
            print("Stopping AppServer system: {0}".format(system))
            time.sleep(0.1)

    def start_systems(self):
        for system in self.__nodes:
            print("Starting AppServer system: {0}".format(system))
            time.sleep(0.1)

    def health_check_systems(self):
        for system in self.__nodes:
            print("Checking AppServer system: {0}".format(system))
            time.sleep(0.1)


class PatchingFactory(object):
    def stop_all(self, platform_object):
        return eval(platform_object)().stop_systems()

    def start_all(self, platform_object):
        return eval(platform_object)().start_systems()

    def health_check_all(self, platform_object):
        return eval(platform_object)().health_check_systems()

    def make_magic_happen(self, platform_object):
        self.health_check_all(platform_object)
        self.stop_all(platform_object)
        self.start_all(platform_object)
        self.health_check_all(platform_object)


def main():
    PF = PatchingFactory()

    # Good opportunity to test leveraging async here
    for platform in ['WebServer', 'Firewall', 'AppServer']:
        PF.make_magic_happen(platform)


if __name__ == '__main__':
    main()