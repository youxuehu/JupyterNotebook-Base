# -*- coding:utf-8 -*-
import unittest


class TestNotebookExecUtils(unittest.TestCase):
    def test_exec_code(self):
        import requests

        file_name = "test.ipynb"
        import codecs

        with codecs.open("static/code.txt", "r+", encoding="utf-8") as fout:
            code = fout.read()
        response = requests.get(
            "http://0.0.0.0:8888/exec/code?nb_file_name={file_name}&code={code}".format(file_name=file_name, code=code)
        )
        print(response.text)


if __name__ == "__main__":
    unittest.main()
