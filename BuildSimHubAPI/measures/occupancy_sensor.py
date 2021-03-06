from .model_action import ModelAction


class OccupancySensor(ModelAction):
    def __init__(self):
        ModelAction.__init__(self, 'occupancy_sensor')
        self._default_list = [1, 0]

    def get_num_value(self):
        return ModelAction.num_of_value(self)

    def set_datalist(self, datalist):
        # this is just a on off option
        ModelAction.set_datalist(self, self._default_list)

