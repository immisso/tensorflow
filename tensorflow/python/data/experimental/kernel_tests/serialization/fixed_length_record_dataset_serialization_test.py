# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Tests for checkpointing the FixedLengthRecordDataset."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import parameterized

from tensorflow.python.data.experimental.kernel_tests import reader_dataset_ops_test_base
from tensorflow.python.data.kernel_tests import checkpoint_test_base
from tensorflow.python.data.kernel_tests import test_base
from tensorflow.python.data.ops import readers as core_readers
from tensorflow.python.framework import combinations
from tensorflow.python.platform import test


class FixedLengthRecordDatasetCheckpointTest(
    reader_dataset_ops_test_base.FixedLengthRecordDatasetTestBase,
    checkpoint_test_base.CheckpointTestBase, parameterized.TestCase):

  def _build_iterator_graph(self, num_epochs, compression_type=None):
    filenames = self._createFiles()
    return core_readers.FixedLengthRecordDataset(
        filenames, self._record_bytes, self._header_bytes,
        self._footer_bytes).repeat(num_epochs)

  @combinations.generate(test_base.default_test_combinations())
  def testFixedLengthRecordCore(self):
    num_epochs = 5
    num_outputs = num_epochs * self._num_files * self._num_records
    self.run_core_tests(lambda: self._build_iterator_graph(num_epochs),
                        num_outputs)


if __name__ == "__main__":
  test.main()
