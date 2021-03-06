/*
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for
 * license information.
 *
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

'use strict';

/**
 * @class
 * Initializes a new instance of the StorageAccountRegenerateKeyParameters class.
 * @constructor
 * @member {string} [keyName] Possible values include: 'key1', 'key2'
 *
 */
function StorageAccountRegenerateKeyParameters() {
}

/**
 * Defines the metadata of StorageAccountRegenerateKeyParameters
 *
 * @returns {object} metadata of StorageAccountRegenerateKeyParameters
 *
 */
StorageAccountRegenerateKeyParameters.prototype.mapper = function () {
  return {
    required: false,
    serializedName: 'StorageAccountRegenerateKeyParameters',
    type: {
      name: 'Composite',
      className: 'StorageAccountRegenerateKeyParameters',
      modelProperties: {
        keyName: {
          required: false,
          serializedName: 'keyName',
          type: {
            name: 'Enum',
            allowedValues: [ 'key1', 'key2' ]
          }
        }
      }
    }
  };
};

module.exports = StorageAccountRegenerateKeyParameters;
