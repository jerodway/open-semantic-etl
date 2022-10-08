#
# Write filename to Celery queue for batching and parallel processing
#

from tasks import index_file


class export_queue_files(object):

    def __init__(self, config=None):
        if config is None:
            config = {'verbose': False}
        self.config = config

    def process(self, parameters=None, data=None):
        if parameters is None:
            parameters = {}
        if data is None:
            data = {}

        # add file to ETL queue with standard prioritization
        # but don't if only plugins not ran that should run later (which will be added to queue in step below)
        if not 'only_additional_plugins_later' in parameters:
            index_file.apply_async(
                kwargs={'filename': parameters['filename']}, queue='open_semantic_etl_tasks', priority=5)

        # add file to (lower prioritized) ETL queue with additional plugins or options which should run later after all files tasks of standard prioritized queue done
        # to run ETL of the file later again with additional plugins like OCR which need much time/resources while meantime all files are searchable by other plugins which need fewer resources
        if 'additional_plugins_later' in parameters or 'additional_plugins_later_config' in parameters:

            additional_plugins_later = parameters.get('additional_plugins_later', [])

            additional_plugins_later_config = parameters.get('additional_plugins_later_config', {})

            if len(additional_plugins_later) > 0 or len(additional_plugins_later_config) > 0:

                index_file.apply_async(kwargs={
                                       'filename': parameters['filename'], 'additional_plugins': additional_plugins_later, 'config': additional_plugins_later_config}, queue='open_semantic_etl_tasks', priority=1)

        return parameters, data
