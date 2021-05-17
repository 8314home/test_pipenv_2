import subprocess
import os
import sys
from pathlib import Path
import logging
from datetime import datetime, timedelta
from configparser import ConfigParser


def create_dates_list(log, input_start_date, input_end_date, input_interval):
    lod = list()
    tmp_date = datetime.strptime(input_start_date, '%Y-%m-%d')
    end_dt = datetime.strptime(input_end_date, '%Y-%m-%d')
    while tmp_date + timedelta(days=int(input_interval)) < end_dt:
        prev_date = tmp_date
        tmp_date = tmp_date + timedelta(days=int(input_interval))
        lod.append((prev_date.strftime('%Y-%m-%d'), tmp_date.strftime('%Y-%m-%d')))
    # append remaining date period
    lod.append((tmp_date.strftime('%Y-%m-%d'), end_dt.strftime('%Y-%m-%d')))
    return lod


def get_date_period_to_process(logger, app_name, input_path):
    # check if history_config file is present
    if os.path.exists(input_path):
        logger.warning(f"\n HISTORY LOAD")
        logger.warning(f"\nHistory load config file exists - {input_path}")
        # if present take start date , end date , interval from history_load_config file
        parser = ConfigParser()
        parser.read(input_path)
        start_date = parser.get('default', 'start_date')
        end_date = parser.get('default', 'end_date')
        interval = parser.get('default', 'interval')
        logger.warning(f"\nHISTORY load start_date - {start_date}  end_date - {end_date} interval= {interval}")
        list_of_dates = create_dates_list(logger, start_date, end_date, interval)

    else:
        # else take default start date as 10 days ago and end date = today
        start_date = (datetime.utcnow().date() - timedelta(days=10)).strftime('%Y-%m-%d')
        end_date = datetime.utcnow().date().strftime('%Y-%m-%d')
        logger.warning(f"\n Daily load start_date - {start_date}  end_date - {end_date}")
        list_of_dates = [(start_date, end_date)]
    logger.warning(f"list_of_dates - {list_of_dates}")
    assert len(list_of_dates) > 0, "list_of_dates is empty, processing error"
    return list_of_dates


if __name__ == "__main__":
    # check if history_config file is present
    # if present take start date , end date , interval from history_load_config
    # else take default start date as 10 days ago and end date = today utc date

    # application_name = 'history_data_load'
    # input_load_config_path = '/tmp/history_load_config.ini'
    # script_to_be_executed = ["sleep", "10"]
    application_name = sys.argv[1]
    input_load_config_path = sys.argv[2]
    script_to_be_executed = list(str(sys.argv[3]).split(' '))

    custom_logger = logging.getLogger(application_name)
    custom_logger.setLevel(logging.WARNING)
    custom_logger.warning(f"application_name = {application_name}")
    custom_logger.warning(f"input_load_config_path = {input_load_config_path}")

    try:
        date_segments = get_date_period_to_process(custom_logger, application_name, input_load_config_path)
        custom_logger.warning(f"\nScript execution will be done for dates - {date_segments}\n")
    except AssertionError as e:
        custom_logger.error(e)
        sys.exit(2)

    # Shell script call to process data for period using date_segments (list_of_dates)
    datetime.
    tmp_list = script_to_be_executed.copy()
    for (s_dt, e_dt) in date_segments:
        try:
            script_to_be_executed = tmp_list.copy()
            script_to_be_executed.append(s_dt)
            script_to_be_executed.append(e_dt)
            custom_logger.warning(f"script_to_be_executed = {script_to_be_executed}")
            command_return_code = subprocess.check_call(script_to_be_executed, timeout=60*45)
        except subprocess.CalledProcessError as se:
            custom_logger.error(f"\nError in executing script for date period between {s_dt} and {e_dt}\n")
            custom_logger.error(se.output)
        else:
            custom_logger.warning(f"\nScript execution completed for dates between {s_dt} and {e_dt}\n")
