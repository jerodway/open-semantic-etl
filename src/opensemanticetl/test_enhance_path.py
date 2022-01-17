#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

import enhance_path

class Test_enhance_path(unittest.TestCase):

    def test(self):

        enhancer = enhance_path.enhance_path()


        docid = '/home/user/test.pdf'
        parameters, data = enhancer.process(parameters={'id': docid})

        self.assertEqual(data['path0_s'], 'home')
        self.assertEqual(data['path1_s'], 'user')
        self.assertEqual(data['path_basename_s'], 'test.pdf')
        self.assertEqual(data['filename_extension_s'], 'pdf')


        docid = '/home/user/test_without_filename_extension'
        parameters, data = enhancer.process(parameters={'id': docid})

        self.assertFalse('filename_extension_s' in data)


        docid = '/home/user/test.PDF'
        parameters, data = enhancer.process(parameters={'id': docid})

        self.assertEqual(data['filename_extension_s'], 'pdf')


if __name__ == '__main__':
    unittest.main()
