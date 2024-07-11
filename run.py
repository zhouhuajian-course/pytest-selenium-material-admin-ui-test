import pytest
import time
import os
import util

if __name__ == '__main__':
    util.login("...", "...")
    root_dir = os.path.dirname(__file__)
    report_file_path = f"{root_dir}/report/report_{time.strftime('%Y%m%d_%H%M%S')}.html"
    pytest.main([f'--html={report_file_path}', '--self-contained-html', root_dir])
