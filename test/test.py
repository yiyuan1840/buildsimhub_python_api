"""
8.9 test
"""
import BuildSimHubAPI as bshapi
import BuildSimHubAPI.postprocess as pp
import time

bsh = bshapi.BuildSimHubAPIClient()
project_key = ""
# model_key = "39ed84d0-062b-470d-96e6-b03abff9c31c"

# 1. define the absolute directory of your energy model
file_dir = '/Users/weilixu/Desktop/data/schedule/5ZoneTDV.idf'

# file_dir = "/Users/weilixu/Desktop/data/jsontest/5ZoneAirCooled.idf"

wea_dir = "/Users/weilixu/Desktop/data/jsontest/in.epw"

new_sj = bsh.new_simulation_job(project_key)
results = new_sj.run(file_dir=file_dir, epw_dir=wea_dir, add_files='/Users/weilixu/Desktop/data/schedule/csv', track=True)

if results:
    load_data = results.zone_load()
    print(load_data)
    zl = pp.ZoneLoad(load_data)
    print(zl.get_df())

    # results.bldg_geo()
# if results:
#    print(str(results.not_met_hour_cooling()) + " " + results.last_parameter_unit)
#    load_data = results.zone_load()
#    load = bshapi.postprocess.ZoneLoad(load_data)
#    print(load.get_df())
