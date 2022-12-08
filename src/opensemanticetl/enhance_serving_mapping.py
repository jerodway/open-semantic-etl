

class enhance_serving_mapping(object):

    def process(self, parameters=None, data=None):
        if parameters is None:
            parameters = {}
        if data is None:
            data = {}

        if 'serve_mappings' in parameters:
            data['serve_id_s'] = serving_mapping(
                value=parameters['filename'], mappings=parameters['serve_mappings'])

        return parameters, data


# Change value with best/deepest mapping
def serving_mapping(value, mappings=None):
    if mappings is None:
        mappings = {}

    max_match_len = -1

    # check all mappings for matching and use the best
    for map_from, map_to in mappings.items():

        # map from matching value?
        if value.startswith(map_from):

            # if from string longer (deeper path), this is the better matching
            match_len = len(map_from)

            if match_len > max_match_len:
                max_match_len = match_len
                best_match_map_from = map_from
                best_match_map_to = map_to

    # if there is a match, replace first occurance of value with mapping
    if max_match_len >= 0:
        value = value.replace(best_match_map_from, best_match_map_to, 1)

    return value