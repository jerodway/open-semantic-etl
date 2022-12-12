class enhance_orig_filepath(object):

    def process(self, parameters=None, data=None):
        if parameters is None:
            parameters = {}
        if data is None:
            data = {}

        if 'filename' in parameters:
            data['orig_filepath_s'] = parameters['filename']

        return parameters, data