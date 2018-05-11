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
    define(['ApiClient', 'model/AllInfoCar', 'model/Charger'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./AllInfoCar'), require('./Charger'));
  } else {
    // Browser globals (root is window)
    if (!root.Revolution) {
      root.Revolution = {};
    }
    root.Revolution.AllInfo = factory(root.Revolution.ApiClient, root.Revolution.AllInfoCar, root.Revolution.Charger);
  }
}(this, function(ApiClient, AllInfoCar, Charger) {
  'use strict';




  /**
   * The AllInfo model module.
   * @module model/AllInfo
   * @version 0.0.1
   */

  /**
   * Constructs a new <code>AllInfo</code>.
   * @alias module:model/AllInfo
   * @class
   */
  var exports = function() {
    var _this = this;



  };

  /**
   * Constructs a <code>AllInfo</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/AllInfo} obj Optional instance to populate.
   * @return {module:model/AllInfo} The populated <code>AllInfo</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('car')) {
        obj['car'] = AllInfoCar.constructFromObject(data['car']);
      }
      if (data.hasOwnProperty('chargers')) {
        obj['chargers'] = ApiClient.convertToType(data['chargers'], [Charger]);
      }
    }
    return obj;
  }

  /**
   * @member {module:model/AllInfoCar} car
   */
  exports.prototype['car'] = undefined;
  /**
   * @member {Array.<module:model/Charger>} chargers
   */
  exports.prototype['chargers'] = undefined;



  return exports;
}));


