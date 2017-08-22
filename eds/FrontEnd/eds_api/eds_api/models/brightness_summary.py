# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class BrightnessSummary(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, nm: str=None, u: str=None, v: float=None, t: datetime=None, n: str=None, lbl: str=None):
        """
        BrightnessSummary - a model defined in Swagger

        :param nm: The nm of this BrightnessSummary.
        :type nm: str
        :param u: The u of this BrightnessSummary.
        :type u: str
        :param v: The v of this BrightnessSummary.
        :type v: float
        :param t: The t of this BrightnessSummary.
        :type t: datetime
        :param n: The n of this BrightnessSummary.
        :type n: str
        :param lbl: The lbl of this BrightnessSummary.
        :type lbl: str
        """
        self.swagger_types = {
            'nm': str,
            'u': str,
            'v': float,
            't': datetime,
            'n': str,
            'lbl': str
        }

        self.attribute_map = {
            'nm': 'nm',
            'u': 'u',
            'v': 'v',
            't': 't',
            'n': 'n',
            'lbl': 'lbl'
        }

        self._nm = nm
        self._u = u
        self._v = v
        self._t = t
        self._n = n
        self._lbl = lbl

    @classmethod
    def from_dict(cls, dikt) -> 'BrightnessSummary':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BrightnessSummary of this BrightnessSummary.
        :rtype: BrightnessSummary
        """
        return deserialize_model(dikt, cls)

    @property
    def nm(self) -> str:
        """
        Gets the nm of this BrightnessSummary.

        :return: The nm of this BrightnessSummary.
        :rtype: str
        """
        return self._nm

    @nm.setter
    def nm(self, nm: str):
        """
        Sets the nm of this BrightnessSummary.

        :param nm: The nm of this BrightnessSummary.
        :type nm: str
        """

        self._nm = nm

    @property
    def u(self) -> str:
        """
        Gets the u of this BrightnessSummary.

        :return: The u of this BrightnessSummary.
        :rtype: str
        """
        return self._u

    @u.setter
    def u(self, u: str):
        """
        Sets the u of this BrightnessSummary.

        :param u: The u of this BrightnessSummary.
        :type u: str
        """

        self._u = u

    @property
    def v(self) -> float:
        """
        Gets the v of this BrightnessSummary.

        :return: The v of this BrightnessSummary.
        :rtype: float
        """
        return self._v

    @v.setter
    def v(self, v: float):
        """
        Sets the v of this BrightnessSummary.

        :param v: The v of this BrightnessSummary.
        :type v: float
        """

        self._v = v

    @property
    def t(self) -> datetime:
        """
        Gets the t of this BrightnessSummary.
        the timestamp when the brightness was measured

        :return: The t of this BrightnessSummary.
        :rtype: datetime
        """
        return self._t

    @t.setter
    def t(self, t: datetime):
        """
        Sets the t of this BrightnessSummary.
        the timestamp when the brightness was measured

        :param t: The t of this BrightnessSummary.
        :type t: datetime
        """

        self._t = t

    @property
    def n(self) -> str:
        """
        Gets the n of this BrightnessSummary.

        :return: The n of this BrightnessSummary.
        :rtype: str
        """
        return self._n

    @n.setter
    def n(self, n: str):
        """
        Sets the n of this BrightnessSummary.

        :param n: The n of this BrightnessSummary.
        :type n: str
        """

        self._n = n

    @property
    def lbl(self) -> str:
        """
        Gets the lbl of this BrightnessSummary.

        :return: The lbl of this BrightnessSummary.
        :rtype: str
        """
        return self._lbl

    @lbl.setter
    def lbl(self, lbl: str):
        """
        Sets the lbl of this BrightnessSummary.

        :param lbl: The lbl of this BrightnessSummary.
        :type lbl: str
        """

        self._lbl = lbl

