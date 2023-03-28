import logging
import os
import sys
from pythonjsonlogger import jsonlogger


def init_logger():
    log_level = os.getenv('LOGLEVEL', 'info').upper()
    formatter = jsonlogger.JsonFormatter(
        '%(asctime)s %(name)s[%(process)d]: %(levelname)s - %(message)s')
    log = logging.getLogger('IMT-fleet-status')
    if not log.hasHandlers():
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        log.addHandler(console_handler)
        log.setLevel(log_level)
    return log


log = init_logger()


def print_logs():
    log.info("fixbot_sitetracker_job_process_begins")
    log.error("fixbot_sitetracker_job_process_begins")
    log.warning("fixbot_sitetracker_job_process_begins")


print_logs()