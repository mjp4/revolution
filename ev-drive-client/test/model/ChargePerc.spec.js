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
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.Revolution);
  }
}(this, function(expect, Revolution) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Revolution.ChargePerc();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('ChargePerc', function() {
    it('should create an instance of ChargePerc', function() {
      // uncomment below and update the code to test ChargePerc
      //var instane = new Revolution.ChargePerc();
      //expect(instance).to.be.a(Revolution.ChargePerc);
    });

    it('should have the property percentage (base name: "percentage")', function() {
      // uncomment below and update the code to test the property percentage
      //var instane = new Revolution.ChargePerc();
      //expect(instance).to.be();
    });

  });

}));