var assert = require('assert');
var getUrlProtocol = require('../src/dojo').getUrlProtocol;
var getUrlDomain = require('../src/dojo').getUrlDomain;

describe('Test True', function () {
    it('should return http', function () {
        assert.equal(getUrlProtocol("http://globo.com"), "http");
    });
    it('should return ftp', function () {
        assert.equal(getUrlProtocol("ftp://globo.com"), "ftp");
    });
    it('should return https', function () {
        assert.equal(getUrlProtocol("https://globo.com"), "https");
    });
    it('should return globo.com', function () {
        assert.equal(getUrlDomain("https://g1.globo.com"), "globo.com");
    });
    it('should return facebook.com', function () {
        assert.equal(getUrlDomain("ftp://facebook.com"), "facebook.com");
    });
    it('should return google.com', function () {
        assert.equal(getUrlDomain("https://google.com"), "google.com");
    });
});