#!/usr/bin/env python3
# -*- coding: utf-8 -:-

from chardet.universaldetector import UniversalDetector


class GetEncoding:
    def __init__(self, unknown_file_path, convert=False,
                 known_encoding=None, known_file_path=None):
        """
        Helper Class to dynamically determine enconding of an unknown file.
        If convert is True, the class will also convert the file to the provided
        encoding and save it to the specified location.
        :param unknown_file_path: Realpath of file with unknown encoding
        :param convert: Boolean, if true, will attempt to convert file
        :param known_encoding: Encoding Codec value, e.g., 'utf-8'
        :param known_file_path: Realpath of where file should be saved
        """
        self.unknown_file_path = unknown_file_path
        self.convert = convert
        self.known_encoding = known_encoding
        self.known_file_path = known_file_path

    def unknown_codec(self):
        detector = UniversalDetector()
        # Read in file with unknown_encoding
        try:
            with open(self.unknown_file_path, 'rb') as file:
                for line in file.readlines():
                    detector.feed(line)
                    if detector.done():
                        detector.close()
            return detector.result

        except Exception as e:
            print(e)
            return None

    def write_known(self):
        unknown_codec = self.unknown_codec()
        if unknown_codec is not None and self.convert:
            print('The file was saved with the following encoding: {}'.format(unknown_codec))
            try:
                with open(self.unknown_file_path, 'r',
                          encoding=unknown_codec) as src, open(self.known_file_path, 'w',
                                                               encoding=self.known_encoding) as trg:
                    for line in src.readlines():
                        trg.write(line)

                return True

            except (UnicodeDecodeError, UnicodeEncodeError, Exception) as e:
                print(e)
                return None

