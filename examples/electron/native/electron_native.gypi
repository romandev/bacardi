# Copyright (c) 2017 The Bacardi Authors.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

{
  'variables': {
    'examples_electron_native_cpp_files': [
      'electron_native.cc',
      'electron_native.h',
      '<(module_root_dir)/third_party/simrank/simrank.hpp',
    ],

    'examples_electron_native_idl_files': [
      '<(module_root_dir)/examples/electron/native/electron_native.idl',
    ],

    'examples_electron_native_idl_output_files': [
      '<(SHARED_INTERMEDIATE_DIR)/examples/electron/native/electron_native_bridge.cc',
      '<(SHARED_INTERMEDIATE_DIR)/examples/electron/native/electron_native_bridge.h',
    ],
  },
}
