/**
 * revolution
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 0.0.1
 * Contact: api-support@metaswitch.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.3.1
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['../ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.Revolution) {
      root.Revolution = {};
    }
    root.Revolution.ChargePerc = factory(root.Revolution.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The ChargePerc model module.
   * @module model/ChargePerc
   * @version 0.0.1
   */

  /**
   * Constructs a new <code>ChargePerc</code>.
   * @alias module:model/ChargePerc
   * @class
   * @param percentage {String} The percentage of battery.
   */
  var exports = function(percentage) {
    var _this = this;

    _this['percentage'] = percentage;
  };

  /**
   * Constructs a <code>ChargePerc</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/ChargePerc} obj Optional instance to populate.
   * @return {module:model/ChargePerc} The populated <code>ChargePerc</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('percentage')) {
        obj['percentage'] = ApiClient.convertToType(data['percentage'], 'String');
      }
    }
    return obj;
  }

  /**
   * The percentage of battery.
   * @member {String} percentage
   */
  exports.prototype['percentage'] = undefined;



  return exports;
}));


