from .core import PipelineInterface


class BasicExamplePipeline(PipelineInterface):
    """
    This pipeline just dispatch the message to a Service.

    Also you can customize your constructor and the other methods

    >>> pipeline = BasicExamplePipeline(
            config=SendgridConfig(),
            backend_klass=SendgridBackendV3,
            repo_klass=SendgridRepository
            service_klass=Service
            db_repo=PostgresDBRepo()
            connection=False
        )
    >>> res = pipeline.run(message)
    """

    def __init__(self, config, backend_klass, repo_klass, service_klass, db_repo, connection=None):
        self.config = config
        self.backend_klass = backend_klass
        self.repo = repo_klass(config=self.config, backend_klass=self.backend_klass, connection=connection)
        self.service = service_klass(sendgrid_repo)
        self.db_repo = db_repo

    def send(self, message):
        try:
            response = self.service.send(message)
            return response

        except Exception:
            raise

    def flow_response(self, response):
        pass
        # if response and response.status_code == 200:
            # response_translated = self.translate_response(res)
            # self.db_repo.update(res)
            # self.db_repo.update_status({ content: 'some content', status='delivered' })
            # return True

        # elif response and response.status_code != 200:
            # response_translated = self.translate_response(res)
            # self.db_repo.update(res)
            # self.db_repo.update_status({ content: 'some content', status='error' })
            # return False

        raise Exception('Response is none')


    def translate_response(self, response):
        """
        Customize the response of each provider
        """
        pass

    def run(self, message):
        res = None
        # U can create methods to customize your pipeline
        # Ex. save message on database with custom fields
        # self.db_repo.create_record_on_database({ content: 'some content', status='created' })

        # after your customizations send the message to provider/backend
        try:
            res = self.send(message)

        except Exception:
            # self.flow_response(res)
            # self.db_repo.update_status({ content: 'some content', status='exception' })
            raise

        try:
            return self.flow_response(res)

        except Exception:
            raise

