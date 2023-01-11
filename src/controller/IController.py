import abc

from src.view.IView import IView


class IController(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_view(self, view: IView):
        """Set the view"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_view(self) -> IView:
        """Get the view"""
        raise NotImplementedError