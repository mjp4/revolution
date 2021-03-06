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
    define(['../ApiClient', '../model/ChargePerc'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('../model/ChargePerc'));
  } else {
    // Browser globals (root is window)
    if (!root.Revolution) {
      root.Revolution = {};
    }
    root.Revolution.StatusApi = factory(root.Revolution.ApiClient, root.Revolution.ChargePerc);
  }
}(this, function(ApiClient, ChargePerc) {
  'use strict';

  /**
   * Status service.
   * @module api/StatusApi
   * @version 0.0.1
   */

  /**
   * Constructs a new StatusApi. 
   * @alias module:api/StatusApi
   * @class
   * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
   * default to {@link module:ApiClient#instance} if unspecified.
   */
  var exports = function(apiClient) {
    this.apiClient = apiClient || ApiClient.instance;


    /**
     * Callback function to receive the result of the getChargePerc operation.
     * @callback module:api/StatusApi~getChargePercCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ChargePerc} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the charge percentage
     * @param {String} username Username for logging in 
     * @param {String} password Users password
     * @param {module:api/StatusApi~getChargePercCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ChargePerc}
     */
    this.getChargePerc = function(username, password, callback) {
      var postBody = null;

      // verify the required parameter 'username' is set
      if (username === undefined || username === null) {
        throw new Error("Missing the required parameter 'username' when calling getChargePerc");
      }

      // verify the required parameter 'password' is set
      if (password === undefined || password === null) {
        throw new Error("Missing the required parameter 'password' when calling getChargePerc");
      }


      var pathParams = {
        'username': username,
        'password': password
      };
      var queryParams = {
      };
      var collectionQueryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = [];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = ChargePerc;

      return this.apiClient.callApi(
        '/charge_perc/nissan/{username}/{password}', 'GET',
        pathParams, queryParams, collectionQueryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
  };

  return exports;
}));
