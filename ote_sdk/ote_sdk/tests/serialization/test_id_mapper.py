#
# INTEL CONFIDENTIAL
#
# Copyright (C) 2021 Intel Corporation
#
# This software and the related documents are Intel copyrighted materials, and
# your use of them is governed by the express license under which they were provided to
# you ("License"). Unless the License provides otherwise, you may not use, modify, copy,
# publish, distribute, disclose or transmit this software or the related documents
# without Intel's prior written permission.
#
# This software and the related documents are provided as is,
# with no express or implied warranties, other than those that are expressly stated
# in the License.
#

""" This module contains tests for the mapper for ID entities """

import pytest

from ote_sdk.entities.id import ID
from ote_sdk.serialization.id_mapper import IDMapper
from ote_sdk.tests.constants.ote_sdk_components import OteSdkComponent
from ote_sdk.tests.constants.requirements import Requirements


@pytest.mark.components(OteSdkComponent.OTE_SDK)
class TestIDMapper:
    @pytest.mark.priority_medium
    @pytest.mark.component
    @pytest.mark.reqids(Requirements.REQ_1)
    def test_serialized_representiaton(self):
        """
        This test serializes ID and checks serialized representation.
        """

        id = ID("21434231456")
        serialized_id = IDMapper.forward(id)
        assert serialized_id == "21434231456"

    @pytest.mark.priority_medium
    @pytest.mark.component
    @pytest.mark.reqids(Requirements.REQ_1)
    def test_serialization_deserialization(self):
        """
        This test serializes ID, deserializes serialized ID and compare with original.
        """

        id = ID("21434231456")
        serialized_id = IDMapper.forward(id)
        deserialized_id = IDMapper.backward(serialized_id)
        assert id == deserialized_id
