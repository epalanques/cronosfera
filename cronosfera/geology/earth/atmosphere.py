import subprocess as sp


class Atmosphere:
    def __init__(self):
        self.composition = ''
        self.info_file = ''

    def get_info(self):
        info_path = 'cronosfera/geology/concepts/atmosphere/%s.txt' % self.info_file
        sp.Popen(["open", info_path])
