import webbrowser
from .httpurllib import request_get
from .httpurllib import make_url
# This is a class that contains all the model information for user
# to read


# potentially in the future, to write

class ParametricModel(object):
    # every call will connect to this base URL
    BASE_URL = 'https://my.buildsim.io/'

    def __init__(self, project_key, track_token, base_url=None):
        """
        Construct parametric result object

        :param project_key: required
        :param track_token: required
        :param base_url: optional
        :type project_key: str
        :type track_token: str
        :type base_url: str

        """
        self._project_key = project_key
        self._last_parameter_unit = ""
        self._track_token = track_token
        self._base_url = ParametricModel.BASE_URL
        if base_url is not None:
            self._base_url = base_url

    @property
    def last_parameter_unit(self):
        return self._last_parameter_unit

    def bldg_geo(self):
        """Open the online geometric viewer in browser"""
        url = self._base_url + 'IDF3DViewerSocket.html'
        track = 'model_api_key'
        test = self._track_token.split('-')
        if len(test) is 3:
            track = 'tracking'

        payload = {
            'project_api_key': self._project_key,
            track: self._track_token,
        }

        r = make_url(url, payload)
        webbrowser.open(r)

    # Below are the methods use for retrieving results
    def net_site_eui(self):
        return self.__call_api('NetSiteEUI')

    def total_site_eui(self):
        return self.__call_api('TotalSiteEUI')

    def not_met_hour_cooling(self):
        return self.__call_api('NotMetHoursCooling')

    def not_met_hour_heating(self):
        return self.__call_api('NotMetHoursHeating')

    def not_met_hour_total(self):
        return self.__call_api('NotMetHoursTotal')

    def total_end_use_electricity(self):
        return self.__call_api('TotalEndUseElectricity')

    def total_end_use_naturalgas(self):
        return self.__call_api('TotalEndUseNaturalGas')

    def cooling_electricity(self):
        return self.__call_api('CoolingElectricity')

    def cooling_naturalgas(self):
        return self.__call_api('CoolingNaturalGas')

    def domestic_hotwater_electricity(self):
        return self.__call_api('DomesticHotWaterElectricity')

    def domestic_hotwater_naturalgas(self):
        return self.__call_api('DomesticHotWaterNaturalGas')

    def exterior_equipment_electricity(self):
        return self.__call_api('ExteriorEquipmentElectricity')

    def exterior_equipment_naturalgas(self):
        return self.__call_api('ExteriorEquipmentElectricity')

    def exterior_lighting_electricity(self):
        return self.__call_api('ExteriorLightingElectricity')

    def exterior_lighting_naturalgas(self):
        return self.__call_api('ExteriorLightingNaturalGas')

    def fan_electricity(self):
        return self.__call_api('FanElectricity')

    def fan_naturalgas(self):
        return self.__call_api('FansNaturalGas')

    def heating_electricity(self):
        return self.__call_api('HeatingElectricity')

    def heating_naturalgas(self):
        return self.__call_api('HeatingNaturalGas')

    def heat_rejection_electricity(self):
        return self.__call_api('HeatRejectionElectricity')

    def heat_rejection_naturalgas(self):
        return self.__call_api('HeatRejectionNaturalGas')

    def interior_equipment_electricity(self):
        return self.__call_api('InteiorEquipmentElectricity')

    def interior_equipment_naturalgas(self):
        return self.__call_api('InteirorEquipmentNaturalGas')

    def interior_lighting_electricity(self):
        return self.__call_api('InteriorLightingElectricity')

    def interior_lighting_naturalgas(self):
        return self.__call_api('InteriorLightingNaturalGas')

    def pumps_electricity(self):
        return self.__call_api('PumpsElectricity')

    def pumps_naturalgas(self):
        return self.__call_api('PumpsNaturalGas')

    def bldg_lpd(self):
        return self.__call_api('BuildingLPD')

    def bldg_epd(self):
        return self.__call_api('BuildingEPD')

    def bldg_ppl(self):
        return self.__call_api('BuildingPPL')

    def wall_rvalue(self):
        return self.__call_api('WallRValue')

    def roof_rvalue(self):
        return self.__call_api('RoofRValue')

    def window_uvalue(self):
        return self.__call_api('WindowUValue')

    def window_shgc(self):
        return self.__call_api('WindowSHGC')

    def roof_absorption(self):
        return self.__call_api('RoofAbsorption')

    def bldg_infiltration(self):
        return self.__call_api('Infiltration')

    def bldg_water_heater_efficiency(self):
        return self.__call_api('WaterHeaterEfficiency')

    def bldg_dx_cooling_efficiency(self):
        return self.__call_api('DXCoolingCoilEfficiency')

    def bldg_chiller_efficiency(self):
        return self.__call_api('ChillerEfficiency')

    def bldg_electric_boiler_efficiency(self):
        return self.__call_api('ElectricBoilerEfficiency')

    def bldg_fuel_boiler_efficiency(self):
        return self.__call_api('FuelBoilerEfficiency')

    def bldg_dx_heating_efficiency(self):
        return self.__call_api('ElectricHeatingDXCoils')

    def __call_api(self, request_data):
        url = self._base_url + 'ParametricResults_API'
        payload = {
            'project_api_key': self._project_key,
            'folder_api_key': self._track_token,
            'request_data': request_data
        }

        r = request_get(url, params=payload)
        resp_json = r.json()
        if r.status_code > 200:
            print('Code: ' + str(r.status_code) + ' message: ' + resp_json['error_msg'])
            return False

        value = list()
        model = list()
        model_plot = list()
        counter = 1
        if resp_json['status'] == 'success':
            datalist = resp_json['data']
            for i in range(len(datalist)):
                value.append(datalist[i]['value'])
                model.append(datalist[i]['model'])
                model_plot.append('case' + str(counter))
                counter += 1
                if 'unit' in datalist[i]:
                    self._last_parameter_unit = datalist[i]['unit']
            result = dict()
            result['value'] = value
            result['model'] = model
            result['model_plot'] = model_plot
            return result
        else:
            return resp_json['error_msg']
