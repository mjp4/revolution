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
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.Revolution) {
      root.Revolution = {};
    }
    root.Revolution.AllInfoCar = factory(root.Revolution.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The AllInfoCar model module.
   * @module model/AllInfoCar
   * @version 0.0.1
   */

  /**
   * Constructs a new <code>AllInfoCar</code>.
   * @alias module:model/AllInfoCar
   * @class
   */
  var exports = function() {
    var _this = this;




  };

  /**
   * Constructs a <code>AllInfoCar</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/AllInfoCar} obj Optional instance to populate.
   * @return {module:model/AllInfoCar} The populated <code>AllInfoCar</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('lat')) {
        obj['lat'] = ApiClient.convertToType(data['lat'], 'String');
      }
      if (data.hasOwnProperty('long')) {
        obj['long'] = ApiClient.convertToType(data['long'], 'String');
      }
      if (data.hasOwnProperty('charge')) {
        obj['charge'] = ApiClient.convertToType(data['charge'], 'String');
      }
    }
    return obj;
  }

  /**
   * @member {String} lat
   */
  exports.prototype['lat'] = undefined;
  /**
   * @member {String} long
   */
  exports.prototype['long'] = undefined;
  /**
   * The charge in watt hour
   * @member {String} charge
   */
  exports.prototype['charge'] = undefined;



  return exports;
}));

