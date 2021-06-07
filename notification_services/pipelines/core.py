import abc


class PipelineInterface:
    __metaclass__ = abc.ABCMeta

    @classmethod
    def __subclasshook__(cls, subclass):
        return
            (
                hasattr(subclass, "send") and callable(subclass.send)
                and hasattr(subclass, "flow_response") and callable(subclass.flow_response)
                and hasattr(subclass, "translate_response") and callable(subclass.translate_response)
                and hasattr(subclass, "run") and callable(subclass.run)
            ) or NotImplemented

    @abc.abstractmethod
    def send(self):
        raise NotImplementedError

    @abc.abstractmethod
    def flow_response(self, response):
        raise NotImplementedError

    @abc.abstractmethod
    def translate_response(self, response):
        raise NotImplementedError

    @abc.abstractmethod
    def run(self)
        raise NotImplementedError
