import unittest


suite = unittest.TestSuite()
loader = unittest.TestLoader()
runner = unittest.TextTestRunner()

suite.addTests(loader.discover(start_dir='.', pattern='test_*.py'))


if __name__ == '__main__':
    runner.run(suite)
